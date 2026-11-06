#!/usr/bin/env python3
"""Pre-publish checker for newsletter / blog posts written in Markdown.

Catches the mistakes a publishing assistant must never let through:
missing metadata, bad links, images without alt text, placeholder text,
heading problems, repeated words and more.

Usage
  python3 scripts/check_post.py post.md [more.md ...]
  python3 scripts/check_post.py post.md --online        # also test that links open
  python3 scripts/check_post.py post.md --utm           # warn if external links lack utm_source
  python3 scripts/check_post.py post.md --require title,description,slug,tags,category,date

Exit code: 0 = no FAIL (warnings allowed), 1 = at least one FAIL, 2 = usage error.

Post format: optional front matter between '---' lines, then Markdown. See
templates/newsletter-post-template.md. No third-party packages needed.
"""
import argparse
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|FIXME|XXX)\b|lorem ipsum|\[(?:INSERT|ADD|LINK|NAME)[^\]]*\]|\{\{|\}\}", re.I)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]*)(?:\s+\"[^\"]*\")?\)")
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]*)(?:\s+\"[^\"]*\")?\)")
REPEAT_RE = re.compile(r"\b([A-Za-z]{2,})\s+\1\b", re.I)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
BAD_LINK_TEXT = {"here", "click here", "link", "this", "read more", "more"}
BAD_URL_PARTS = ("example.com", "localhost", "127.0.0.1", "yourwebsite", "your-site")
DEFAULT_REQUIRED = ["title", "description", "slug", "tags", "category"]


def split_front_matter(text):
    """Return (meta dict, body, number of lines used by front matter)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text, 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            meta, key = {}, None
            for raw in lines[1:i]:
                if re.match(r"^\s*-\s+", raw) and key:
                    meta[key] = (meta.get(key, "") + "," + re.sub(r"^\s*-\s+", "", raw).strip()).strip(",")
                    continue
                m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", raw)
                if m:
                    key = m.group(1).lower()
                    meta[key] = m.group(2).strip().strip("\"'")
            return meta, "\n".join(lines[i + 1:]), i + 1
    return {}, text, 0


def check_text(text, required=None, utm=False):
    """Return a list of (level, line_number, message). level in FAIL/WARN/INFO."""
    issues = []
    required = DEFAULT_REQUIRED if required is None else required
    meta, body, offset = split_front_matter(text)

    # ---- metadata ----
    if not meta:
        issues.append(("FAIL", 1, "No front matter found (title, description, slug, tags, category...)."))
    for key in required:
        if not meta.get(key, "").strip():
            issues.append(("FAIL", 1, f"Missing metadata: '{key}'."))
    title = meta.get("title", "")
    if title and len(title) > 70:
        issues.append(("WARN", 1, f"Title is {len(title)} characters; aim for 60 or less so it is not cut off."))
    if title and len(title) < 15:
        issues.append(("WARN", 1, "Title is very short; check it is clear and specific."))
    desc = meta.get("description", "")
    if desc and not 70 <= len(desc) <= 160:
        issues.append(("WARN", 1, f"Meta description is {len(desc)} characters; aim for 70-160."))
    slug = meta.get("slug", "")
    if slug and not SLUG_RE.match(slug):
        issues.append(("WARN", 1, f"Slug '{slug}' should use lowercase letters, numbers and hyphens only."))
    date = meta.get("date", "")
    if date and not DATE_RE.match(date):
        issues.append(("WARN", 1, f"Date '{date}' should look like 2026-11-30."))
    tags = [t.strip() for t in re.split(r"[,\[\]]", meta.get("tags", "")) if t.strip()]
    if tags and len(tags) != len(set(t.lower() for t in tags)):
        issues.append(("WARN", 1, "Duplicate tags."))

    # ---- body ----
    in_code = False
    last_level = 0
    h1_count = 0
    link_urls = []
    words = 0
    for n, line in enumerate(body.split("\n"), start=offset + 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            if level == 1:
                h1_count += 1
            if last_level and level > last_level + 1:
                issues.append(("WARN", n, f"Heading jumps from H{last_level} to H{level}."))
            last_level = level
        for alt, url in IMAGE_RE.findall(line):
            if not alt.strip():
                issues.append(("FAIL", n, f"Image has no alt text: {url or '(no url)'}"))
            elif re.search(r"\.(jpe?g|png|gif|webp)$", alt.strip(), re.I) or len(alt) > 125:
                issues.append(("WARN", n, f"Alt text should describe the image in under 125 characters: '{alt[:40]}'"))
            if not url:
                issues.append(("FAIL", n, "Image has an empty source."))
        for text_, url in LINK_RE.findall(line):
            if not url or url == "#":
                issues.append(("FAIL", n, f"Empty or placeholder link on '{text_[:30]}'."))
                continue
            low = url.lower()
            if any(p in low for p in BAD_URL_PARTS):
                issues.append(("FAIL", n, f"Placeholder or local URL: {url}"))
            if low.startswith("http://"):
                issues.append(("WARN", n, f"Link is not secure (http): {url}"))
            if text_.strip().lower() in BAD_LINK_TEXT:
                issues.append(("WARN", n, f"Vague link text '{text_.strip()}'; describe where it goes."))
            if low.startswith(("http://", "https://")):
                link_urls.append((n, url))
                if utm and "utm_source=" not in low:
                    issues.append(("WARN", n, f"External link has no utm_source: {url}"))
            elif not low.startswith(("mailto:", "tel:", "#", "/")):
                issues.append(("WARN", n, f"Link may be missing https://: {url}"))
        if PLACEHOLDER_RE.search(line):
            issues.append(("FAIL", n, f"Placeholder text left in: '{PLACEHOLDER_RE.search(line).group(0)}'"))
        plain = IMAGE_RE.sub("", line)
        plain = LINK_RE.sub(lambda mm: mm.group(1), plain)
        r = REPEAT_RE.search(plain)
        if r:
            issues.append(("WARN", n, f"Repeated word: '{r.group(0)}'"))
        if re.search(r"\S  +\S", plain):
            issues.append(("WARN", n, "Double space."))
        words += len(re.findall(r"\b\w+\b", plain))

    if h1_count > 1:
        issues.append(("WARN", 1, f"{h1_count} H1 headings; use one (the post title) and H2/H3 for sections."))
    counts = Counter(u for _, u in link_urls)
    for url, c in counts.items():
        if c > 2:
            issues.append(("WARN", 1, f"Same link used {c} times: {url}"))
    if words < 50:
        issues.append(("WARN", 1, f"Very short post ({words} words)."))
    issues.append(("INFO", 1, f"{words} words, about {max(1, round(words / 200))} min read, {len(link_urls)} external links."))
    return issues, link_urls


def check_online(urls, timeout=8):
    """Optionally test external links. Returns (level, line, message) list."""
    out = []
    seen = {}
    for n, url in urls:
        if url in seen:
            continue
        seen[url] = True
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (post-checker)"}, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                if resp.status >= 400:
                    out.append(("FAIL", n, f"Link returned {resp.status}: {url}"))
        except urllib.error.HTTPError as e:
            level = "WARN" if e.code in (401, 403, 429) else "FAIL"  # some sites block bots
            out.append((level, n, f"Link returned {e.code}: {url}"))
        except Exception as e:  # network error, timeout, TLS
            out.append(("WARN", n, f"Could not open ({type(e).__name__}): {url}"))
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description="Pre-publish checker for Markdown newsletter/blog posts.")
    p.add_argument("files", nargs="+")
    p.add_argument("--online", action="store_true", help="also test that external links open")
    p.add_argument("--utm", action="store_true", help="warn when external links have no utm_source")
    p.add_argument("--require", default=",".join(DEFAULT_REQUIRED), help="comma list of required metadata keys")
    a = p.parse_args(argv)
    required = [k.strip().lower() for k in a.require.split(",") if k.strip()]
    failed = False
    for f in a.files:
        path = Path(f)
        if not path.is_file():
            print(f"{f}: file not found")
            return 2
        issues, urls = check_text(path.read_text(encoding="utf-8"), required, a.utm)
        if a.online:
            issues += check_online(urls)
        order = {"FAIL": 0, "WARN": 1, "INFO": 2}
        issues.sort(key=lambda x: (order[x[0]], x[1]))
        fails = sum(1 for i in issues if i[0] == "FAIL")
        warns = sum(1 for i in issues if i[0] == "WARN")
        print(f"\n== {path.name}: {'FAIL' if fails else 'PASS'} ({fails} fail, {warns} warn)")
        for level, line, msg in issues:
            print(f"  [{level}] line {line}: {msg}")
        failed = failed or bool(fails)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
