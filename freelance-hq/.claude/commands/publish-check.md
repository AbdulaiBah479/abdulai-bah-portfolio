---
description: Check a newsletter or blog post before publishing (links, images, metadata, formatting)
argument-hint: [path to the post, e.g. products/post.md]
---
Use the `newsletter-publishing-qa` skill on: $ARGUMENTS

Run `python3 scripts/check_post.py` on the file with `--utm`, explain each problem in plain words, fix what is safe, list what needs a human decision, fill the publishing log row, and write a short hand-off note.
