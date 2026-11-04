---
name: gig-builder
description: Build a complete Fiverr gig or productized service listing (title, 3 packages, description, FAQ, requirements, tags, image/video brief). Use when the user wants to create or rewrite a gig or fixed-price service on Fiverr, PeoplePerHour, Contra, Upwork Project Catalog or similar.
---

# Gig builder

Read `playbooks/01-fiverr.md` and `cheatsheets/fiverr.md` first. Limits marked (verify) must be checked in the Fiverr gig editor before submitting.

## Steps
1. Confirm the offer from `/niche` output (promise, buyer, tiers). If none exists, run `niche-validator` first.
2. **Keyword research**: run `listing-seo` to get 1 primary and 4 supporting keywords from live Fiverr search suggestions and top-gig titles.
3. **Title**: starts with "I will", contains primary keyword early, outcome-focused, within the limit (80 chars, verify). Give 5 options, recommend 1.
4. **Packages** (Basic / Standard / Premium): same deliverable ladder, price ratio about 1 : 2.5 : 5, clear delivery days, revisions, and extras. Basic must be profitable at your real hourly rate (`cheatsheets/pricing-formulas.md`).
5. **Description** (max ~1200 chars, verify): hook line -> who it is for -> what you get (bullets) -> process -> why you -> CTA to message first. Plain language, no keyword stuffing.
6. **Gig extras**: fast delivery, extra revision, source files, commercial use. Price each by real effort.
7. **Requirements questions** (so work starts without back-and-forth): 4-6 specific questions, see `templates/client-intake-questionnaire.md`.
8. **FAQ**: 4-6 objections answered (revisions, timeline, tools, refunds, custom orders).
9. **Tags**: 5 tags (verify) from the keyword set; no brand names you do not own.
10. **Media brief**: 3 image concepts (before/after, process, proof), 1 short video script (30-75 s, face + screen), PDF sample if allowed.
11. **AI disclosure**: state honestly where AI assists, as Fiverr policy requires (verify).
12. Save `products/gig-<slug>.md` using `templates/fiverr-gig.md`; add row to `tracker/gigs.csv` (status: draft).

## Quality gate
No guarantees you cannot keep, no off-platform contact info, no copyrighted images, no claims of "Top Rated" unless true, every price covers effort + fees (20% commission, verify).
