# Freelance HQ

A Claude Code project that runs a one-person freelance and digital-products business:
**Fiverr, Upwork and other marketplaces, direct clients, digital products, ebooks, and the audience that feeds them.**

> Honest note: this gives you the system, templates and AI workflows. It does not guarantee income.
> Results depend on your niche, proof, consistency and the market. Fees and rules marked `(verify)` change: check the platform's current help page.

## New to all this? Start here
1. Read `start-here/00-READ-ME-FIRST.md` (10 minutes, explains everything in plain language).
2. Follow `start-here/01-setup-windows.md`, then run `/start` in Claude.
3. Follow `start-here/04-first-14-days.md`. Look up any word in `start-here/02-glossary.md` or type `/explain <word>`.

## Start in 3 steps
```bash
cd freelance-hq
claude            # loads CLAUDE.md, 17 skills, 11 agents, 14 commands from .claude/
bash scripts/init_tracker.sh   # creates your PRIVATE tracker files (repo is public)
```
Then type: `/start` (Claude interviews you and writes your personal plan).

## What is inside
| Folder | What |
|---|---|
| `start-here/` | Beginner course: setup, glossary, how money works, first 14 days, account setup, mistakes, FAQ |
| `offers/` | 16 ready-to-test services (tiers, delivery steps, tools, risks) |
| `ideas/` | 110-idea bank, 20 outside-the-box strategies, one-asset-seven-ways, income streams map |
| `CLAUDE.md` | Rules and index Claude follows |
| `.claude/skills/` | niche-validator, platform-profile-optimizer, gig-builder, proposal-writer, client-onboarding, digital-product-launch, ebook-pipeline, listing-seo, content-repurposer, weekly-business-review, beginner-coach, local-business-audit, chatbot-project-delivery, n8n-workflow-productizer, course-builder, newsletter-and-lead-magnet, portfolio-case-study |
| `.claude/agents/` | market-researcher, gig-copywriter, proposal-specialist, product-builder, ebook-author, client-success-manager, finance-admin, growth-marketer, teacher-coach, automation-engineer, course-designer |
| `.claude/commands/` | `/start` `/explain` `/idea` `/niche` `/gig` `/proposal` `/audit` `/case-study` `/chatbot` `/product` `/course` `/ebook` `/weekly-review` `/launch-checklist` |
| `playbooks/` | 13 deep guides: strategy, Fiverr, Upwork, other platforms, direct outreach, productized services, digital products, ebooks, marketing, pricing, legal/tax, AI automation, delivery |
| `cheatsheets/` | 18 one-pagers: Fiverr, Upwork, fees, storefronts, pricing, proposals, KDP, product launch, red flags, prompts, scripts, routines, SEO tags, n8n, chatbots, design rules, terminal/Git basics, Claude Code |
| `resources/` | 299 verified GitHub repos + a pick-by-goal guide, free tools beyond GitHub, platform directory, MCP/connectors guide, learning list |
| `templates/` | Gig, proposal, intake, scope, contract-lite, invoice, testimonial, cold email, ebook outline, product listing, launch emails |
| `tracker/` | CSVs: leads, income, gigs, products, content calendar |
| `scripts/` | `income_report.py`, `price_calc.py`, `new_client.sh`, `build_ebook.sh` (Pandoc), `init_tracker.sh` |
| `ebooks/_starter/` | A buildable ebook skeleton |

## The 30-day plan
**Week 1: Foundation.** `/niche` -> choose ONE offer. Set up Fiverr + Upwork profiles (`platform-profile-optimizer`). Turn 3 portfolio projects into case studies. Set up payouts (check country eligibility).
**Week 2: Launch services.** `/gig` x2 on Fiverr. Send 5 proposals a day with `/proposal` (quality over volume). Start `tracker/leads.csv`.
**Week 3: Win and deliver.** Run `client-onboarding` for every order. Over-deliver on the first 3, ask for honest reviews. Outreach to 20 local/vertical prospects (audit-first, `playbooks/04`).
**Week 4: Add the asset layer.** Turn the most repeated client task into a product (`/product`) and a 15-page lead-magnet ebook (`/ebook`). Post 3x a week (`content-repurposer`). Run `/weekly-review`, decide: double down, fix or kill.

**Month 2-3:** raise prices, add a retainer, publish product #2 and ebook #1 on KDP + direct, start the email list.
**Month 4+:** bundle, course, affiliates, partner with agencies, productize the top service.

## Privacy note
This GitHub repo is public. Trackers, drafts, `my-plan.md` and `clients/` are git-ignored so your leads, income and unreleased products stay local. Keep backups somewhere private.

## Rules that protect your accounts and reputation
No fake reviews/portfolios/stats, one account per platform, keep payments on-platform, honest AI disclosure, licensed assets only, no income guarantees. Details in `CLAUDE.md` and `cheatsheets/client-red-flags.md`.

## Connectors (optional)
Copy `.mcp.example.json` to `.mcp.json` to enable filesystem/fetch MCP servers. Other helpful connectors if you have them: Google Drive, Gmail drafts, Notion/Airtable, Canva, Figma. Start read-only; approve writes deliberately.

## Related
`../bah-digital/` is the AI operating system / SaaS foundation; `../index.html` is the portfolio site that feeds your profiles. Update it with new case studies as you win work.

## Maintenance
Quarterly: refresh `resources/github-repos.md`, re-verify every `(verify)` item, prune unused tools. Weekly: `/weekly-review`.
