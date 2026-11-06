---
name: newsletter-publishing-qa
description: Check, format and prepare newsletter and blog posts for publication with zero avoidable errors: run the checker, review links/images/metadata, apply the style guide, fill the publishing log and write a short hand-off note to the Content and Analytics teams. Use for /publish-check, newsletter or blog publishing, content-assistant work, or pre-publish QA.
---

# Newsletter publishing QA

Read `playbooks/13-newsletter-publishing-assistant.md` and `templates/newsletter-publishing-checklist.md`.

## Steps
1. **Get the inputs:** final text (Markdown/Docs), images, style guide, template, schedule. If something is missing, ask; never guess facts, dates or links.
2. **Format** the post to the template: front matter (`templates/newsletter-post-template.md`), heading order, short paragraphs, consistent lists.
3. **Run the checker:** `python3 scripts/check_post.py <post.md> --utm` (add `--online` when internet is available). Explain every FAIL and WARN in plain language and fix what is safe; list what needs a human decision (e.g. changing the editor's wording).
4. **Manual checks the script cannot do:** names, numbers and dates match the source; images fit the text; links go where the text promises; tone matches the style guide; the preview looks right on a phone.
5. **Fill the log** (`tracker/publishing_log.csv`) and the checklist. Mark each check honestly (Y/N/NA).
6. **Hand-off note** (5 lines max): what is ready, what changed from the source, open questions, schedule, live URL placeholder.
7. **After publishing:** verify the live page, record the URL, and report any issue immediately.

## Rules
Do not change the author's meaning. Flag, don't silently rewrite. Never publish with a FAIL. Mark uncertain facts `TODO(owner)`. Keep a clear change log. Respect confidentiality of unpublished content.
