---
name: digital-product-launch
description: Plan, build, price and launch a digital product (templates, Notion/Canva kits, prompt packs, code starters, n8n workflow bundles, design assets, mini-courses, checklists) on Gumroad, Payhip, Etsy, Lemon Squeezy, Ko-fi, Creative Market and similar. Use for any "sell a product" request.
---

# Digital product launch

Read `playbooks/06-digital-products.md`, `cheatsheets/digital-product-launch.md`, `cheatsheets/platform-fees-comparison.md`.

## Steps
1. **Validate** with `niche-validator` (a product with zero search/pain evidence is a hobby).
2. **Choose the format** that matches the buyer's job-to-be-done: template, swipe file, toolkit, workflow pack, mini-course, dataset, plugin, asset pack. Prefer products built from your real client work (de-identified).
3. **Define the MVP**: one painful problem, one clear result, delivered in a form usable in 15 minutes. Write the promise and the "what is inside" list before building.
4. **Build** in `products/<slug>/`: source files, README/usage guide, licence file (personal vs commercial), changelog. Use `agents/product-builder`.
5. **Quality check**: open on a clean machine/account, follow your own guide, fix friction, check fonts/images/icons/code licences, remove client data, scan for secrets.
6. **Pricing**: anchor on value saved, price ladder (starter $9-19 / pro $29-79 / bundle), launch discount with an end date. Details in `playbooks/09-pricing-and-money.md`.
7. **Listing**: title + benefit subtitle, 5-7 preview images (cover, contents, use-case mockups, before/after), description (problem -> solution -> inside -> who for -> FAQ -> licence), tags via `listing-seo`.
8. **Platform choice**: start with ONE storefront (Gumroad/Payhip for simplicity, Etsy for search traffic, Lemon Squeezy for merchant-of-record tax handling, verify fees). Add marketplaces after the first sales.
9. **Launch**: `/launch-checklist`, 3-email sequence (`templates/launch-email-sequence.md`), 5 posts via `content-repurposer`, post in 2-3 relevant communities **within their self-promotion rules**.
10. **After launch**: collect feedback, ship v1.1, add to bundle, track in `tracker/products.csv` (views, conversion, revenue, refunds).

## Compliance
Disclose AI assistance if the platform requires it, do not sell content you do not have rights to, include correct licence terms, handle refunds per platform policy, mind data-protection rules for buyer emails.
