# ROLE 3 — Germany Pricing Analysis

## Concise business summary

Launch LUMEN in Germany at a **€2.19 shelf price**. It is the strongest of the three tested candidates because it keeps estimated acceptance above half of the test sample (**51.7%**) while generating the highest calculated contribution per 100 exposed customers in **every tested channel**. It also occupies defensible “accessible premium” space: below VoltFit's current single-can price in all three observed channels, but above Mate Libre where the two overlap.

This is a deliberate compromise. Compared with €1.79, LUMEN gives up **10.0 percentage points of acceptance** in exchange for materially better unit economics. Compared with €2.59, it gives up **€0.23–€0.38 contribution per accepted unit** and a more overtly premium price signal, but avoids a **25.0-point acceptance decline**. The choice therefore does not maximise reach or margin per buyer; it maximises the tested balance between the two.

## Scope and data quality

Only the four files assigned to the pricing role were used. `customer_survey.csv` was not opened or used, so no customer names or email addresses were processed or exposed.

| Source | Rows checked | Result |
|---|---:|---|
| `data/competitor_prices_by_channel.csv` | 27 | No missing cells, exact duplicate rows, or duplicate competitor-channel-format keys. Competitor coverage is uneven: Mate Libre has no DTC observations and Root & Rise has no Gym & Office observations, so comparisons use like-for-like single cans within observed channels. |
| `data/competitor_price_history.csv` | 48 | Complete 12-month series for each of four competitors; no missing cells, exact duplicate rows, or duplicate competitor-month keys. |
| `data/price_sensitivity_survey.csv` | 300 | Unique respondent IDs, no missing cells or exact duplicate rows, and all four thresholds are logically ordered for every respondent. |
| `data/price_test_results.csv` | 9 | Complete 3-price × 3-channel grid, with no missing cells or duplicate price-channel keys. Net price less contribution equals €0.62 in all nine rows, indicating a consistent implied unit cost within the test. |

These checks support using the records as supplied. Uneven competitor coverage and survey-based rather than observed German sales results remain limitations, not cleaning errors.

## Main findings

### 1. Competitor positioning leaves room for an accessible-premium price

Current single-can prices are:

| Competitor and stated positioning | DTC Online | Retail/Grocery | Gym & Office |
|---|---:|---:|---:|
| PulsUp — mass market | €1.15 | €1.07 | €1.28 |
| Mate Libre — heritage / loyal niche | Not observed | €1.59 | €1.83 |
| VoltFit — premium performance | €2.49 | €2.37 | €2.72 |
| Root & Rise — boutique adaptogenic | €3.11 | €2.98 | Not observed |

Observed facts from `data/competitor_prices_by_channel.csv`:

- **€1.79** is a reach-oriented price. It is only €0.04 below Mate Libre in Gym & Office and €0.20 above Mate Libre in Retail/Grocery, while remaining 24.5%–34.2% below VoltFit across the three channels. This would weaken a premium-performance comparison.
- **€2.19** creates a clear step above Mate Libre: +€0.60 in Retail/Grocery and +€0.36 in Gym & Office. It remains below VoltFit by €0.30 in DTC, €0.18 in Retail/Grocery, and €0.53 in Gym & Office (12.0%, 7.6%, and 19.5%, respectively). It signals premium value without matching the premium leader's price.
- **€2.59** is the overt premium option. It is 4.0% above VoltFit in DTC and 9.3% above VoltFit in Retail/Grocery, although still 4.8% below VoltFit in Gym & Office. Where Root & Rise is observed, €2.59 remains 13.1%–16.7% below it.

Historical prices reinforce those anchors. Over September 2025–August 2026, mean list prices were **€1.0917 PulsUp, €1.5817 Mate Libre, €2.3883 VoltFit, and €2.9500 Root & Rise**. Start-to-end list-price changes were only **−€0.03, +€0.02, −€0.03, and €0.00**, respectively. Promotions occurred in 2 of 12 months for PulsUp and 1 of 12 months for each other brand. The minimum observed promotional shelf prices were €0.87, €1.26, €2.16, and €2.50, respectively (`data/competitor_price_history.csv`).

Implication: competitor list prices were stable, so LUMEN should not assume rivals will move their regular anchors immediately. However, VoltFit's one observed 10% promotion brought its shelf price to **€2.16**, €0.03 below a €2.19 LUMEN launch, temporarily removing LUMEN's price advantage.

### 2. Customer thresholds support premium targeting but warn against €2.59

The 300 price-sensitivity responses produced these aggregate thresholds:

| Threshold | Median | Middle 50% of responses |
|---|---:|---:|
| Too cheap | €0.91 | €0.75–€1.11 |
| Cheap / good value | €1.45 | €1.15–€1.69 |
| Expensive but considered | €2.21 | €1.81–€2.60 |
| Too expensive | €2.82 | €2.32–€3.25 |

Calculated from `data/price_sensitivity_survey.csv`. At the three candidates:

| Candidate | At or above respondent's “expensive” threshold | At or above respondent's “too expensive” threshold | Inside respondent's non-rejection range |
|---|---:|---:|---:|
| €1.79 | 23.0% | 0.7% | 99.3% |
| €2.19 | 48.3% | 15.7% | 84.3% |
| €2.59 | 74.7% | 38.0% | 62.0% |

Thresholds differ sharply by segment. Median “expensive / too expensive” points are **€1.71 / €2.21** for Students & Budget-Conscious (n=99), **€2.08 / €2.71** for On-the-go Commuters (n=64), **€2.52 / €3.09** for Fitness & Gym-Goers (n=63), and **€2.79 / €3.50** for Urban Wellness Professionals (n=74). At €2.19, the price is at or above the “expensive” threshold for **97.0% of students** and **65.6% of commuters**, versus **9.5% of fitness consumers** and **1.4% of urban wellness professionals**.

A standard empirical Van Westendorp check gives a **marginal cheapness point of about €1.39** and a **marginal expensiveness point of about €1.97**. The data do not yield a unique optimal price point: both “too cheap” and “too expensive” curves are zero from €1.52 through €1.77 because the maximum “too cheap” response is €1.51 and the minimum “too expensive” response is €1.78. Therefore, no single point from that plateau should be presented as a precise optimum. €2.19 sits above the aggregate marginal-expensiveness point, reinforcing that it requires premium targeting and value communication.

These threshold results measure price perception, not purchase probability. The acceptance results below are kept separate and carry more weight in the launch-price recommendation.

### 3. €2.19 wins the tested acceptance-versus-margin trade-off

Observed results from `data/price_test_results.csv`:

| Candidate | Estimated acceptance | DTC contribution / margin | Retail contribution / margin | Gym & Office contribution / margin |
|---|---:|---:|---:|---:|
| €1.79 | 61.7% | €0.77 / 55.3% | €0.40 / 39.2% | €0.81 / 56.7% |
| €2.19 | 51.7% | €1.16 / 65.1% | €0.63 / 50.3% | €1.13 / 64.6% |
| €2.59 | 26.7% | €1.54 / 71.4% | €0.86 / 58.0% | €1.45 / 70.1% |

To compare the trade-off on a common basis, acceptance was multiplied by contribution per accepted unit. This calculated proxy assumes 100 equally qualified exposures, one unit per accepting person, and no differences in repeat purchase, acquisition cost, or channel mix:

| Candidate | DTC contribution per 100 exposed | Retail contribution per 100 exposed | Gym & Office contribution per 100 exposed |
|---|---:|---:|---:|
| €1.79 | €47.51 | €24.68 | €49.98 |
| **€2.19** | **€59.97** | **€32.57** | **€58.42** |
| €2.59 | €41.12 | €22.96 | €38.71 |

Calculated from `data/price_test_results.csv`. The €2.19 candidate ranks first in every channel on this proxy, so its advantage does not depend on inventing a Germany channel mix.

- Moving from **€1.79 to €2.19** reduces acceptance by 10.0 points (−16.2% relative), but raises unit contribution by €0.39 DTC, €0.23 Retail, and €0.32 Gym & Office. Contribution per 100 exposed increases by **26.2%, 32.0%, and 16.9%**, respectively.
- Moving from **€2.19 to €2.59** adds €0.38, €0.23, and €0.32 contribution per accepted unit, but acceptance falls by 25.0 points (−48.4% relative). Contribution per 100 exposed declines by **31.4%, 29.5%, and 33.7%**, respectively.

## Recommendation

Set the German launch shelf price at **€2.19 per unit**, using the single-can competitor set as the positioning benchmark, and position it as **accessible premium** rather than mass market or boutique luxury.

This recommendation is strongest because it:

1. Preserves majority estimated acceptance at 51.7%.
2. Delivers the best acceptance-weighted contribution in all three tested channels.
3. Prices above the heritage/niche competitor while retaining a regular-price discount to VoltFit.
4. Produces contribution margins of 50.3%–65.1%, materially above the €1.79 candidate's 39.2%–56.7% range.

What LUMEN deliberately gives up:

- **Versus €1.79:** 10.0 points of acceptance and greater accessibility for students and price-sensitive commuters. LUMEN should not expect to win on mass reach or value leadership.
- **Versus €2.59:** €0.23–€0.38 of contribution per accepted unit, the highest percentage margins, and closer price parity with VoltFit/Root & Rise. LUMEN should not claim to maximise premium signalling or margin per buyer.

## Assumptions, limitations, and risks

- **No observed German LUMEN sales:** acceptance and contribution are test estimates, not realised volume or profit. Germany should be treated as a validation market, consistent with `data/README_data.md`.
- **Acceptance proxy:** contribution per 100 exposed is a calculated comparison, not a forecast. It assumes equal traffic quality and one unit per accepter and excludes acquisition cost, repeat purchase, fixed costs, VAT effects beyond the supplied net prices, and channel mix.
- **Survey interpretation:** the threshold file contains 300 unweighted responses; no population weights are supplied, and Students & Budget-Conscious is the largest observed segment (99 responses). Thresholds describe perceptions, not guaranteed purchase.
- **Price-test consistency:** acceptance is identical across channels at a given price in `data/price_test_results.csv`. Actual shoppers may respond differently by context; this needs live validation.
- **Cost risk:** the price test embeds an invariant €0.62 unit cost. Cost inflation, launch inefficiency, or promotional funding would reduce contribution.
- **Competitor comparability:** current competitor coverage is incomplete by channel and format. Historical prices lack channel and format fields, so they are used only to assess anchor stability and promotional risk, not as exact same-channel matches.
- **Promotion risk:** a VoltFit promotion has already produced a €2.16 shelf price. A €2.19 launch must earn its three-cent premium during similar events through product claims, trial, or controlled temporary promotion rather than automatic permanent discounting.
- **Price architecture:** the recommendation applies to the tested single-can shelf price. Multipack and subscription discounts require separate economics and should not be inferred from competitor pack rows.

## Implications for the final LUMEN recommendation

- Use **€2.19 as the base price assumption** in the final Germany business case and scenario model.
- Align positioning and communications to **Urban Wellness Professionals and Fitness & Gym-Goers**, whose price thresholds are more compatible with €2.19. Treat broad student reach as a conscious non-objective at launch.
- Do not infer a launch-channel decision from this role alone. At €2.19, absolute unit contribution is €1.16 DTC, €1.13 Gym & Office, and €0.63 Retail/Grocery, but the final channel choice must also incorporate reach, CAC, repeat behavior, operational feasibility, and the analyses assigned to other roles.
- Validate €2.19 with live German sell-through and repeat-purchase data before scaling. The first review should explicitly compare realised acceptance and unit contribution with the supplied test estimates and reassess if the €0.62 cost assumption does not hold.

## Calculation notes

- Percent differences use the observed current single-can price in the same channel as the denominator.
- “Contribution per 100 exposed” = estimated acceptance percentage × unit contribution in euros.
- Threshold shares compare each candidate with each respondent's four recorded Van Westendorp thresholds. Intersections use empirical cumulative/reverse-cumulative curves at €0.01 increments.
- All displayed calculations use unrounded source values where available and are rounded only for presentation.
