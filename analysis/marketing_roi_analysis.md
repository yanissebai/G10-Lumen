# LUMEN Marketing ROI Analysis — Role 5

## Business summary

LUMEN's historical acquisition data supports a launch plan led by Referral / Subscription and supported by Influencer / Content, with Paid Social used selectively for measurable testing. Referral / Subscription has the lowest CAC (€28.14) and highest LTV:CAC (2.92x); Influencer / Content is the next-lowest-CAC channel (€37.53). Retail Sampling acquires the most customers (12,080) and has the highest LTV (€172.30), but its €60.13 CAC makes it the least efficient acquisition channel by cost. The evidence supports prioritising efficient, trackable acquisition first and using sampling as a controlled awareness/activation test rather than the default budget anchor.

## Scope and data quality

Sources used: data/marketing_funnel_monthly.csv, data/channel_economics.csv, data/cost_breakdown.csv, and data/price_test_results.csv.

- marketing_funnel_monthly.csv has 72 rows: 18 months × 4 channels, with no duplicate month/channel keys.
- No required funnel field is missing or negative.
- Reported CAC was validated as spend ÷ acquired customers: weighted totals reconcile to €44.01.
- Weighted total LTV is €126.32, calculated as the customer-acquisition-weighted mean of row-level LTV estimates.
- The funnel covers LUMEN's existing markets, not Germany. These are directional benchmarks, not German outcomes.
- No names or email addresses from customer_survey.csv were accessed or used.

## Main findings

All channel figures below are weighted across the 18 monthly observations unless stated otherwise.

| Channel | Spend | Acquired customers | CAC | LTV | LTV:CAC | Conversion / reach | Conversion / engagement | Spend share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Referral / Subscription | €322,241.25 | 11,452 | €28.14 | €82.17 | 2.92x | 1.732% | 34.822% | 27.4% |
| Influencer / Content | €84,732.86 | 2,258 | €37.53 | €103.02 | 2.75x | 0.355% | 11.768% | 7.2% |
| Paid Social | €43,588.69 | 952 | €45.79 | €129.19 | 2.82x | 0.108% | 8.776% | 3.7% |
| Retail Sampling | €726,327.24 | 12,080 | €60.13 | €172.30 | 2.87x | 2.152% | 22.823% | 61.7% |
| **Total** | **€1,176,890.04** | **26,742** | **€44.01** | **€126.32** | **2.87x** | **0.976%** | **19.288%** | **100.0%** |

The brief's blended CAC headline is approximately €44, and the computed €44.01 validates it (data/marketing_funnel_monthly.csv). All channels are below the brief's assumed 3:1 LTV:CAC target: Referral / Subscription is closest at 2.92x. The data does not support claiming that any channel currently meets the target.

Referral / Subscription leads acquisition efficiency: it converts 34.822% of engagements and acquires a customer for €28.14. Retail Sampling converts most efficiently from reach (2.152%) but consumes 61.7% of spend and has the highest CAC, showing that volume and efficiency are different objectives.

## Contribution and payback

marketing_funnel_monthly.csv provides CAC and estimated LTV, but no revenue-recognition schedule, repeat-purchase interval, or monthly gross-profit curve. A months-to-payback figure cannot be calculated without inventing timing assumptions. The defensible payback proxy is CAC ÷ LTV: 0.342 for Referral / Subscription, 0.349 for Retail Sampling, 0.354 for Paid Social, and 0.364 for Influencer / Content; this is a share of estimated lifetime value, not months.

At the brief's €2.19 candidate price, unit contribution is €1.16 for DTC Online, €0.63 for Retail/Grocery, and €1.13 for Gym & Office (data/price_test_results.csv). The €0.62 COGS in data/cost_breakdown.csv is consistent with these contribution levels after channel deductions. A €44.01 acquisition cost would require approximately 38 DTC units, 70 Retail/Grocery units, or 39 Gym & Office units to recover CAC on unit contribution alone; this is break-even volume, not a forecast of purchase frequency or time.

## Recommendation

Allocate the first German test budget primarily to Referral / Subscription and Influencer / Content, with Paid Social as a tightly capped experiment for audience and creative validation. Reserve Retail Sampling for targeted gyms, offices, and launch events with pre-defined CAC and repeat-purchase gates; do not scale it merely because it generated the largest historical customer count.

For the initial learning phase, use 45% Referral / Subscription, 30% Influencer / Content, 15% Paid Social, and 10% Retail Sampling. This allocation is a recommendation, not an observed fact; it shifts spend away from the historical 61.7% sampling share while preserving a small offline test. Reallocate only when Germany-specific CAC, repeat rate, contribution, and cohort payback are measured consistently by channel.

## Assumptions, limitations, and risks

- Historical channel performance is assumed directionally transferable to Germany; this is unverified because LUMEN has no German sales data.
- LTV is an estimate in the funnel export, not observed realised customer lifetime value.
- Attribution rules and cross-channel double counting are undocumented.
- CAC reconciliation validates arithmetic, not causal incrementality. Referral and sampling may capture customers who would have converted organically.
- The 3:1 target is an assumption from the brief; no channel reaches it on the supplied estimates.
- Payback in months is unavailable without timing and gross-profit cash-flow data.
- Price-test acceptance is survey-based and reported per channel, not a Germany launch forecast. At €2.19 acceptance is 51.7%, with contribution ranging from €0.63 to €1.16 across channels (data/price_test_results.csv).
- Scaling the lowest-CAC channel may reduce efficiency; the recommendation requires spend-response tests and cohort tracking.

## Implications for the final LUMEN recommendation

Marketing efficiency supports a €2.19 launch test because it is the brief's balanced acceptance/margin option, but marketing alone cannot justify a final price or channel mix. The final recommendation should pair the premium positioning decision with a measurable acquisition plan led by referral/subscription and content, while treating sampling as an awareness investment with strict gates. The team should explicitly state that the chosen strategy prioritises faster, more observable payback and learning over maximum offline reach and immediate sampling-driven volume.
