# Pricing formulas

## Minimum hourly rate
```
rate = ((target_take_home + business_costs) / (1 - tax_rate)) / (billable_hours_per_week * working_weeks)
```
Example: ((12000 + 1200) / 0.8) / (20 * 46) = 17.93

## Fixed-price quote
```
price = (hours_estimate * rate) * (1 + buffer 20-30%) + third_party_costs
platform_gross_up = price / (1 - platform_fee)    # so you still net the price
```
Fiverr at 20%: to net $80 charge $100.

## Effective hourly rate
`net_income / total_hours (including marketing, admin, revisions)`. Track weekly.

## Productized tier ratios
Basic : Standard : Premium = 1 : 2.5 : 5; Premium adds speed, extras, support.

## Retainer price
`monthly = hours_included * rate * 0.9` (small discount for commitment) + rollover rules. Add a minimum 3-month term for stability.

## Rush fee
+25% for under half the normal timeline, +50% for under a quarter.

## Digital product ceiling
`price <= (hours_saved * buyer_hourly_value) * 0.1` as a sanity check; bundle for AOV.

## Break-even for a product
`units = build_hours*rate / (price * (1 - fee))`. If units > realistic first-year sales, shrink the scope or raise price.

## Discount rules
Time-boxed (7 days), never permanent; give discounts for scope reduction or prepayment, not for nothing.

## Proposal price presentation
3 options; recommended in the middle; mention what's included and what's not; keep the number plain, not in a long paragraph.
