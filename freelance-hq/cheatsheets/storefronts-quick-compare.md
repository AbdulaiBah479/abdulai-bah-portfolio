# Storefronts quick compare: where to sell digital products (verify details)

| Platform | Best for | Fee shape (2026 sources, verify) | Pros | Watch out |
|---|---|---|---|---|
| Gumroad | First product, creators | ~10% per sale (some sources add $0.50) | Very quick setup, discovery, widgets | Weekly payouts, fee on small items |
| Payhip | Digital downloads, courses, memberships | Free plan ~5% + payment fees; paid plans lower | Simple, instant payouts | Check current plan prices |
| Lemon Squeezy | Global sales tax handled for you | ~5% + $0.50 (merchant of record) | Tax/VAT handled | Stripe is migrating merchants over time; read notices |
| Ko-fi | Tips + small shop | Free tier with shop fees; Gold reduces | Friendly for small creators | Less buyer search traffic |
| Etsy | Printables, templates, planners | $0.20 listing + 6.5% transaction + ~3% + $0.25 processing (US) | Huge search traffic | Fixed fees hurt $2-5 items; AI/creator rules |
| Creative Market / Envato | Design assets, themes, code | Revenue share | Quality audience | Application/review process |
| Notion / Canva / Figma / Framer / Webflow marketplaces | Platform-specific templates | Revenue share | Built-in buyers | Platform rules and review |
| Teachers Pay Teachers | Education resources | Revenue share | Niche demand | Education focus |
| itch.io / Unity Asset Store | Game assets | Revenue share | Game audience | Niche |
| Own site (Astro + Stripe/Payhip embed) | Brand, margin, data | Payment fees only | Own your customers | Needs traffic |

## Choosing in 30 seconds
- **Brand new, one product:** Gumroad or Payhip.
- **Printable/template with search demand:** add Etsy.
- **Selling to many countries and don't want to handle tax:** Lemon Squeezy (merchant of record) or similar.
- **Developers:** GitHub + Gumroad/Lemon Squeezy; free sample repo as marketing.
- **Designers:** Creative Market/Envato after a small portfolio, plus Gumroad.

## Net-fee check
Use `python3 scripts/price_calc.py product --price 19 --fee 0.10 --processing 0.029 --fixed 0.30` to see what you keep.

## Listing basics
Cover image, 5-7 previews, clear licence, support email, refund policy, versioning, welcome email with download link and a "how to start" PDF.
