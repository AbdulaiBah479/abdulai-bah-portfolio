# 07. Ebooks playbook

Rules and royalty numbers marked `(verify)` change; check each platform's help pages before publishing.

## Ebook types and goals
| Type | Length | Price | Goal |
|---|---|---|---|
| Lead magnet | 10-25 pp | Free | Email list, authority |
| Practical guide | 30-80 pp | $4.99-$14.99 | Direct sales + credibility |
| Workbook/toolkit | 40-120 pp | $9-$39 | Higher price, sold direct |
| Full book | 100-250 pp | $2.99-$9.99 retail | Marketplace discovery |
| Bundle (guide + templates) | varies | $19-$79 | Best margin, sell direct |

Great fits for these skills: "AI automation for small business owners", "Build your first chatbot without code", "Freelancing in [country] guide", "Prompt library for [profession]", "n8n recipes", "Canva social templates handbook".

## Workflow (matches `skills/ebook-pipeline`)
1. **Reader + promise** -> 2. **Validate** (category ranks, comparable titles, reviews) -> 3. **Outline** -> 4. **Interview yourself** (real stories, mistakes, steps) -> 5. **Draft** (Markdown chapters) -> 6. **Edit x3** -> 7. **Format** (Pandoc: EPUB + PDF) -> 8. **Cover** -> 9. **Metadata + keywords** -> 10. **Publish** -> 11. **Launch and market** -> 12. **Improve with reviews**.

## Using AI responsibly
AI can outline, brainstorm, edit and summarise. You must contribute real experience, verify facts, rewrite in your voice and never fabricate quotes, studies or case results. Disclose per platform policy (Amazon KDP asks you to indicate AI-generated content when publishing; AI-assisted editing differs from AI-generated text, verify definitions). Low-effort, repetitive AI books get rejected, reviewed poorly, and risk account bans.

## Formatting stack (free)
- Write: Markdown in VS Code / Obsidian / Typora alternatives.
- Convert: **Pandoc** (EPUB, PDF via LaTeX/Typst, DOCX). `scripts/build_ebook.sh` does it.
- Edit/inspect EPUB: **Calibre**, **Sigil**; validate with EPUBCheck; preview with Kindle Previewer (free from Amazon).
- Proof: Vale/LanguageTool for style and grammar, read aloud with text-to-speech.
- PDF layout alternative: **Typst** or **Marp** (slide-style guides).
- Covers: Canva, Figma, GIMP, Inkscape; licensed or self-made images only.

## Cover rules
Genre-appropriate, one focal image, title readable at thumbnail size, subtitle small, no clutter, high contrast. KDP ebook cover recommended 1600 x 2560 px (verify). Test it next to 10 bestselling covers in your category.

## Amazon KDP essentials (verify all)
- Ebook royalty options: 70% for list prices in a set band (about $2.99-$9.99) in supported stores, otherwise 35%. A delivery fee per MB applies under 70%.
- KDP Select: 90-day exclusivity, unlocks Kindle Unlimited page-read income and promos. Skip it if you want wide distribution.
- Paperback/hardcover: print-on-demand, royalty ~60% minus print cost, need interior PDF with margins, bleed settings for covers.
- Publishing limits and AI-disclosure questions exist (verify).
- Keywords: 7 phrases; categories: choose the most specific; description with HTML formatting is allowed in limited tags.

## Going wide
Draft2Digital (single upload to many stores), Kobo Writing Life, Apple Books (needs Apple account / Mac tools in some cases), Google Play Books, Barnes & Noble Press, IngramSpark (print distribution), Payhip/Gumroad (direct), Leanpub (iterative publishing), Substack/Beehiiv/Ghost (serialised or paid newsletters). Wide = more reach, KDP Select = Kindle Unlimited income. Choose per book.

## Pricing and promos
Lead magnet free; guide at $4.99-$9.99; direct-sale bundle higher. Free promo days (if KDP Select), countdown deals, newsletter swaps with other authors, BookBub Featured Deals are curated and selective (verify).

## Marketing
Email list first; excerpts as social posts; Pinterest/YouTube for how-to topics; guest posts; podcasts; LinkedIn for professional topics; Reddit/forums with value; a free chapter or checklist as the funnel. Ask genuine readers for honest reviews; never buy or swap reviews.

## Rights and legal
Own your text; license images/fonts; avoid trademarks in titles where they imply endorsement; include copyright page; ISBN is optional on KDP ebooks but needed for some retailers (free ISBN via KDP is retailer-locked, buy your own if you want publisher control) (verify); public-domain republishing is low-value and often rejected.

## Series strategy
One reader -> three connected short books -> bundle -> print omnibus -> course. Cross-promote inside back matter.

## Metrics
Page reads/sales, conversion from sample, review count and rating, list growth, revenue per book. Track in `tracker/products.csv`.
