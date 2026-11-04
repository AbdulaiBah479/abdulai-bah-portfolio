---
name: ebook-pipeline
description: End-to-end ebook workflow: topic validation, outline, drafting, editing, formatting to EPUB/PDF with Pandoc, cover brief, metadata, and publishing to Amazon KDP, Kobo, Apple Books, Draft2Digital, Gumroad/Payhip. Use for any ebook, guide, lead magnet or short book.
---

# Ebook pipeline

Read `playbooks/07-ebooks.md` and `cheatsheets/kdp-ebook.md`.

## Steps
1. **Topic and reader**: one reader, one transformation. Validate with `niche-validator` (category bestseller ranks, comp titles, review complaints = your angle).
2. **Type**: lead magnet (10-25 pages, free, builds email list), paid guide (30-80 pages, $4.99-$14.99), practical workbook/templates (higher price), or full book. Short, specific, actionable beats long and vague.
3. **Outline** from `templates/ebook-outline.md`: promise, chapters with one takeaway each, exercises/checklists, resources, CTA to next product.
4. **Draft** in `ebooks/<slug>/manuscript/NN-chapter.md` (Markdown). Use `agents/ebook-author`. AI drafts must be rewritten with the owner's real experience, examples and voice, then fact-checked. Never include invented statistics or fake citations.
5. **Edit in 3 passes**: structure, line edit (clarity, voice), proof (spelling, consistency, links). Read aloud once.
6. **Front/back matter**: title page, copyright page (licence/ISBN/AI-disclosure line if relevant), table of contents, about the author, call-to-action, other works.
7. **Build files**: `bash scripts/build_ebook.sh ebooks/<slug>` -> EPUB (Pandoc) + PDF. Validate the EPUB with EPUBCheck / Kindle Previewer; test on a real e-reader or app.
8. **Cover**: brief the 3 concepts (genre-correct, readable at thumbnail size). Make in Canva/Figma/GIMP using properly licensed assets. KDP ebook cover ideal 1600x2560 px (verify).
9. **Metadata**: title + subtitle with search keywords, description (hook, bullets, who it is for), 7 keyword phrases, 2-3 categories, price, series info. Use `listing-seo`.
10. **Publish** (verify each platform's current rules): KDP (declare AI-generated content as required, KDP Select = 90-day exclusivity trade-off), Kobo Writing Life, Apple Books, Draft2Digital for wide distribution, plus direct sale on Payhip/Gumroad (keeps the customer list).
11. **Launch and market**: `content-repurposer` (excerpt posts, email, podcasts/guest posts), request honest reviews only from genuine readers (never buy or swap reviews).
12. Track in `tracker/products.csv`.
