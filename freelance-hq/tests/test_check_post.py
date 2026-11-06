"""Tests for scripts/check_post.py. Run: python3 -m unittest discover -s tests -v"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_post  # noqa: E402

GOOD = (Path(__file__).resolve().parent.parent / "templates" / "newsletter-post-template.md").read_text(encoding="utf-8")


def levels(text, **kw):
    issues, _ = check_post.check_text(text, **kw)
    return [(lvl, msg) for lvl, _, msg in issues]


class CheckPostTests(unittest.TestCase):
    def test_template_has_no_failures(self):
        self.assertFalse([m for l, m in levels(GOOD) if l == "FAIL"])

    def test_missing_front_matter_fails(self):
        self.assertTrue(any(l == "FAIL" and "front matter" in m for l, m in levels("# Hi\n\nSome text.")))

    def test_missing_alt_text_fails(self):
        text = GOOD.replace("![Owner updating opening hours on a phone]", "![]")
        self.assertTrue(any(l == "FAIL" and "alt text" in m for l, m in levels(text)))

    def test_placeholder_and_bad_links_fail(self):
        text = GOOD + "\nSee [here](https://example.com) and [broken](#) TODO fix.\n"
        msgs = [m for l, m in levels(text) if l == "FAIL"]
        self.assertTrue(any("Placeholder or local URL" in m for m in msgs))
        self.assertTrue(any("Empty or placeholder link" in m for m in msgs))
        self.assertTrue(any("Placeholder text" in m for m in msgs))

    def test_vague_link_text_and_http_warn(self):
        text = GOOD + "\nRead [here](http://news.example.org/a).\n"
        warns = [m for l, m in levels(text) if l == "WARN"]
        self.assertTrue(any("Vague link text" in m for m in warns))
        self.assertTrue(any("not secure" in m for m in warns))

    def test_repeated_word_and_heading_jump(self):
        text = GOOD + "\nThis is is wrong.\n\n#### Deep heading\n"
        warns = [m for l, m in levels(text) if l == "WARN"]
        self.assertTrue(any("Repeated word" in m for m in warns))
        self.assertTrue(any("Heading jumps" in m for m in warns))

    def test_code_blocks_are_ignored(self):
        text = GOOD + "\n```\n![](bad) TODO [x](#)\n```\n"
        self.assertFalse([m for l, m in levels(text) if l == "FAIL"])

    def test_metadata_limits(self):
        text = GOOD.replace("slug: five-quick-wins-get-found-online", "slug: Bad Slug").replace(
            "date: 2026-11-30", "date: 30/11/2026")
        warns = [m for l, m in levels(text) if l == "WARN"]
        self.assertTrue(any("Slug" in m for m in warns))
        self.assertTrue(any("Date" in m for m in warns))

    def test_utm_option(self):
        warns = [m for l, m in levels(GOOD, utm=True) if l == "WARN"]
        self.assertTrue(any("utm_source" in m for m in warns))


if __name__ == "__main__":
    unittest.main()
