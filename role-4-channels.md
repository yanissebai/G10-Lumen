# Role 4 — Germany launch-channel recommendation

## Decision

Start Germany with a controlled two-channel launch: **Gym & Office partnerships plus DTC Online**, at the team’s proposed €2.19 test price. Use Retail/Grocery as a measured second-wave channel after the first launch produces evidence on repeat purchase, contribution after fulfilment, and acquisition payback.

This is a deliberate trade-off: Gym & Office and DTC Online provide stronger unit economics and better control over learning, while Retail/Grocery provides the widest reach but lower contribution per unit.

## Evidence

| Channel | German survey preference | €2.19 net price to LUMEN | €2.19 unit contribution | Source |
|---|---:|---:|---:|---|
| Retail/Grocery | 46.4% (195/420) | €1.25 | €0.63 | `data/customer_survey.csv`; `data/channel_economics.csv` |
| DTC Online | 28.3% (119/420) | €1.78 | €1.16 | `data/customer_survey.csv`; `data/channel_economics.csv` |
| Gym & Office | 25.2% (106/420) | €1.75 | €1.13 | `data/customer_survey.csv`; `data/channel_economics.csv` |

At €2.19, Gym & Office contributes €0.50 more per unit than Retail/Grocery, an approximately 79% uplift relative to Retail/Grocery’s €0.63 contribution (`data/channel_economics.csv`). DTC Online contributes €0.03 more per unit than Gym & Office, but its €0.35 fulfilment cost and payment-processing charge must remain in the model (`data/channel_economics.csv`).

The channel recommendation should not be read as a volume forecast: the price-test results are reported by channel and do not provide a pre-built German channel mix (`data/price_test_results.csv`; `LUMEN_Case_Brief.md`). Retail/Grocery remains strategically important because it is the most-preferred purchase channel in the survey (`data/customer_survey.csv`), but broad rollout would expose LUMEN to lower contribution before German demand and repeat behavior are validated.

## Proposed launch sequence

1. **Pilot:** Gym & Office partnerships and DTC Online in selected urban wellness/fitness audiences; instrument channel-level orders, repeat rate, fulfilment-adjusted contribution, CAC, and payback.
2. **Learn:** Compare the two launch channels against the same €2.19 test-price baseline; do not blend results across channels.
3. **Expand:** Add a limited Retail/Grocery test once the pilot demonstrates repeat purchase and acceptable payback; scale only if its reach compensates for its lower per-unit contribution.

## Assumptions and limitations

- The 420-response German survey is directional evidence, not observed sales; percentages are calculated from the channel-preference counts in `data/customer_survey.csv`.
- The €2.19 economics are illustrative per-unit estimates, not a full channel P&L; marketing CAC, returns, taxes, logistics, and repeat-purchase timing require separate validation (`data/channel_economics.csv`; `data/marketing_funnel_monthly.csv`).
- Germany has no historical LUMEN sales, so the recommendation combines German survey evidence with channel economics and must be validated through a pilot (`data/README_data.md`; `LUMEN_Case_Brief.md`).
- Customer names and email addresses were not accessed or used; only aggregated channel-preference counts were used from `data/customer_survey.csv`.
- The recommendation prioritizes controllable economics and learning speed over immediate maximum German reach; this is the explicit choice made against the CMO/CFO trade-off described in `LUMEN_Case_Brief.md`.