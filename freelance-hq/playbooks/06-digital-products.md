# 06. Digital products playbook

Digital products = build once, sell many times. Fees and rules marked `(verify)` change.

## What sells (validate each with `/niche`)
| Type | Examples | Where |
|---|---|---|
| Templates | Notion, Canva, Figma, Google Sheets, Excel trackers, Airtable bases | Gumroad, Payhip, Etsy, Creative Market, Notion/Canva marketplaces (verify) |
| Automation packs | n8n/Make workflows with setup guide | Gumroad, Payhip, own site (check n8n licence terms for redistribution of workflows, not hosted n8n) |
| Code | Starter kits, UI components, boilerplates, scripts | Gumroad, Lemon Squeezy, GitHub Sponsors, own site |
| Prompt packs / custom GPT & Claude Project kits | Role-specific prompt libraries + guide | Gumroad, Payhip, Etsy |
| Design assets | Icons, mockups, social templates, fonts (own licence), LUTs, presets | Creative Market, Etsy, Envato (author), Gumroad |
| Printables | Planners, checklists, worksheets | Etsy, Teachers Pay Teachers (education), Payhip |
| Courses / mini-courses | Video or text with exercises | Gumroad, Payhip, Udemy, Skillshare, Teachable, Kajabi, Whop (verify) |
| Data / lists | Curated, legally compiled datasets | Gumroad, Payhip |
| Memberships | Templates and community monthly | Ko-fi, Patreon, Buy Me a Coffee, Whop, Circle (paid) |
| Stock | Photos, video, audio you created | Shutterstock/Adobe Stock/Pond5 etc. (contributor terms) |
| Game assets | Sprites, sounds, models | itch.io, Unity Asset Store |

## Idea sources
Your own repeated client tasks, FAQ from clients, forum threads ("anyone have a template for..."), competitor reviews (1-3 star complaints), seasonal events, tools people adopt but struggle to set up.

## The validation test (before building)
- Does a similar product have visible sales/reviews? (proves demand)
- Can you do it better in a specific way (niche, completeness, quality, support)?
- Can you describe the result in one sentence?
- Pre-sell or collect waitlist emails with a mock cover and 3-bullet promise.

## Build standard
Solve one job well; usable in 15 minutes; includes quick-start guide; licence; support email; changelog. Test on a fresh account. Remove personal/client data. See `agents/product-builder`.

## Pricing
Value-based: price relative to time/money saved. Typical bands (guideline only): checklist/template $5-19, premium template/kit $19-79, workflow pack/code starter $29-199, course $49-299. Bundle low-priced items for a higher AOV. Launch price for 7 days, then raise. Test pay-what-you-want with a minimum on Gumroad/Ko-fi for lead magnets.

## Choosing a storefront (details in `cheatsheets/platform-fees-comparison.md`)
- **Gumroad / Payhip / Ko-fi**: fastest setup, own audience, email capture.
- **Lemon Squeezy, Paddle, Polar, Creem and similar merchant-of-record platforms** (verify availability per country): they handle global sales tax/VAT as the seller of record.
- **Etsy**: huge search traffic, strong for templates/printables; listing + transaction fees; strict AI/creator rules (verify).
- **Creative Market / Envato**: curated; quality bar and review time; revenue share.
- **Own site**: best margins and data; needs traffic. Self-host options: see `resources/github-repos.md` (e.g. Medusa, Payload CMS, Ghost for paid newsletters).
Start on ONE platform; expand once you have 10+ sales.

## Listing essentials
Cover with one clear benefit, 5-7 images (what's inside, mockups, before/after, use cases, licence, FAQ), benefit-led title, description (problem -> solution -> inside -> who for -> how it works -> licence -> FAQ), tags via `listing-seo`, preview/demo, refund policy, support contact.

## Launch plan (14 days)
Day -7: waitlist + teasers. Day -3: build proof (screens, mini-case-study). Day 0: email list + 2 communities (rules!) + social + Product Hunt/Indie Hackers only if relevant. Day 1-7: answer every comment, post a use-case daily, collect testimonials. Day 7: launch discount ends. Day 14: review data, ship v1.1, bundle.

## Traffic engines
SEO (blog/YouTube/Pinterest for printables), marketplace search, email list, partnerships/affiliates (offer 20-40% to creators, verify platform support), communities, templates distributed free in lite versions (lead magnet).

## Legal basics
Licences for fonts/images/icons/code; trademark-free naming; clear licence for buyers (personal/commercial/extended); privacy policy for email lists; consumer refund rules by region; AI-content disclosure where required; do not sell resale-rights bundles you can't back. Not legal advice.

## Metrics
Visitors -> product-page views -> add-to-cart -> sale; conversion rate (aim to find ~1-5% as a rough working range for storefront traffic, varies widely); refund rate; revenue per visitor; email signups. Log in `tracker/products.csv`.
