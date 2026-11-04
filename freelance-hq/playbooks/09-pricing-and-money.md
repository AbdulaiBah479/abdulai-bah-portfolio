# 09. Pricing and money

## Know your numbers
```
Target yearly take-home      = T
Taxes + retirement set-aside = ~20-35% (depends on country; ask an accountant)
Business costs               = C (tools, platform fees, internet, hardware)
Billable hours per week      = 15-25 realistic (rest is marketing/admin)
Weeks worked per year        = 46-48

Minimum hourly rate = (T + C) / (1 - tax rate) / (billable hours x weeks)
```
Example: T = $12,000, C = $1,200, tax 20%, 20 h x 46 wk = 920 h -> (13,200 / 0.8) / 920 ≈ **$17.9/h**. Never price below this unless it's a deliberate, time-boxed review-building move.

## Pricing models
| Model | Use when | Risk |
|---|---|---|
| Hourly | Unclear scope, ongoing support | Rewards slowness, caps income |
| Fixed project | Clear scope | Scope creep; protect with out-of-scope list |
| Value-based | Outcome has measurable money value | Needs strong proof |
| Retainer | Ongoing needs | Define hours/deliverables |
| Productized | Repeatable | Needs discipline |
| Tiered (Good/Better/Best) | Almost always | None; most buyers choose the middle |

## Marketplace price maths
Always compute net: `price - platform fee (Fiverr ~20%, Upwork ~10%, verify) - payment/withdrawal fees - your time`. Example Fiverr $100 order: $80 net before withdrawal cost.

## Raise prices when
Calendar > 80% full, you win > 40% of proposals, same job is repeatable in less time, or you earned 5+ great reviews. Raise 15-30% on new clients; give existing clients 30 days notice.

## Anchoring and packaging
Show 3 prices; the middle should be your target. Add paid extras (rush, source files, extra revisions). Use "starting at" carefully; avoid unclear ranges.

## Product pricing
Value saved x 10-20% as a ceiling; check competitor bands; use launch discounts with deadlines; bundles raise AOV; keep a free tier for list growth.

## Getting paid
- Marketplace escrow/milestones; withdraw via Payoneer, Wise, PayPal, bank, or local methods supported in your country (verify availability and fees).
- Direct clients: invoice with clear terms (deposit 30-50%, balance on delivery, late fees if legal), accept bank transfer, Wise, Stripe/PayPal links, or local mobile money where relevant.
- Never deliver final files before payment on direct work.

## Money system (tracker/)
Log every payment in `tracker/income.csv` (date, source, client, gross, fees, net, currency, type). Run `scripts/income_report.py` weekly. Use a separate business account/wallet. Move 20-30% to a tax bucket at once (adjust after advice).

## Cash-flow rules
Emergency buffer of 2-3 months of expenses; no income-based lifestyle jump until 3 months of stable income; diversify (no source > 50%); invoice within 24h of delivery; chase late invoices politely at day 1, 7, 14.

## Currency and country issues
Platforms and payment tools differ by country; check eligibility, withdrawal fees, exchange rates, and whether you need a business registration or tax ID. Ask a local accountant. This repo gives general information, not tax or legal advice.

See `cheatsheets/pricing-formulas.md`, `agents/finance-admin`.
