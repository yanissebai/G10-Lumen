# LUMEN Germany: market, city, and timing analysis

**Role:** Market, city, and timing analyst  
**Student ID:** E260249  
**Decision covered:** first German city/region and approximate launch timing

## 1. Business summary

LUMEN should enter **Berlin first**, with a controlled launch in **May 2027** (pilot distribution and awareness in late April; wider availability in May). Berlin is the best scale-adjusted first test: the market file assigns it the largest named-city share (18%), the German survey gives Berlin a high mean purchase intent (7.40/10; 44.4% rated intent at least 8/10), and its assumed regional growth rate is 9%. May begins the sustained demand upswing (seasonality index 118; 15°C) before the July peak (138; 19°C), while the observed competitor promotion calendar shows no May promotions.

Hamburg is the best challenger/second test: it has the highest observed city-level intent (7.52/10), the highest share of high-intent respondents (45.8%), and the highest purchase frequency among named cities (6.32/month), but its modeled market share is 10% versus Berlin's 18%. The recommendation therefore prioritizes Berlin's scale while using Hamburg as a validation cell rather than claiming Berlin is the highest-conversion city.

## 2. Main findings

### Market attractiveness and city choice

- `data/market_context.csv` reports a 2026 Germany **Energy / focus** market of **€2.548bn**. This is the closest available sub-category proxy for LUMEN; it is not LUMEN revenue and should not be read as a city sales forecast.
- Applying the file's illustrative 2026 city shares to €2.548bn gives modeled Energy / focus opportunity of: **Berlin €458.6m (18%)**, **Munich €382.2m (15%)**, **Hamburg €254.8m (10%)**, **Cologne €229.3m (9%)**, and **Frankfurt €203.8m (8%)**. These are calculated sizing metrics, not observed city sales.
- The same file assigns **9% regional CAGR** to Berlin and Munich versus **7%** to Hamburg, Cologne, Frankfurt, and Other Germany. The notes explicitly call these splits illustrative and say the faster growth is assumed from urban wellness concentration.
- `data/customer_survey.csv` contains **420** German respondents. After excluding `respondent_id`, `first_name`, `last_name`, and `email` from analysis, city results were: **Hamburg n=48, intent 7.52, high intent 45.8%, spend €20.27/month, frequency 6.32/month; Berlin n=81, 7.40, 44.4%, €19.98, 6.16; Munich n=57, 7.30, 35.1%, €19.89, 6.38; Frankfurt n=32, 7.18, 31.2%, €20.93, 5.95; Cologne n=45, 7.04, 44.4%, €18.10, 6.03**. “High intent” is a calculated metric defined as intent ≥8/10.
- The survey's preferred channel mix is **Retail/Grocery 46.4% (195/420)**, **DTC Online 28.3% (119/420)**, and **Gym & Office 25.2% (106/420)**. This supports a retail-led pilot with DTC measurement, but channel execution is outside this role's primary scope.

See the standalone [city comparison](city_comparison.md) for the full side-by-side table and decision interpretation.

#### Visual city comparison

The charts below are embedded in the main analysis so the market and city evidence is visible in one place.

```mermaid
%%{init: {'themeVariables': {'xyChart': {'plotColorPalette': ['#1f4e79']}}}}%%
xychart-beta
    title "Illustrative 2026 city opportunity (€m)"
    x-axis [Berlin, Munich, Hamburg, Cologne, Frankfurt]
    y-axis "€m" 0 --> 500
    bar [458.6, 382.2, 254.8, 229.3, 203.8]
```

```mermaid
%%{init: {'themeVariables': {'xyChart': {'plotColorPalette': ['#c55a11']}}}}%%
xychart-beta
    title "Mean LUMEN purchase intent by city (/10)"
    x-axis [Berlin, Munich, Hamburg, Cologne, Frankfurt]
    y-axis "Intent" 0 --> 10
    bar [7.40, 7.30, 7.52, 7.04, 7.18]
```

### Seasonality and weather

- `data/seasonality_and_weather.csv` shows demand below the annual baseline in winter: **January 78 at 2°C**, **February 80 at 3°C**, and **March 88 at 7°C**.
- Demand rises through spring: **April 98 at 11°C**, **May 118 at 15°C**, and **June 132 at 18°C**. It peaks in **July at 138 and 19°C**, then remains strong in **August at 128 and 19°C** before falling to **104 in September**.
- May is therefore a calculated timing compromise: **20 index points above April and 14.5% below the July peak**, while creating a meaningful pre-peak learning window. The 15°C average is a contextual weather signal, not causal proof.

#### Visual launch-timing signal

```mermaid
%%{init: {'themeVariables': {'xyChart': {'plotColorPalette': ['#1f4e79']}}}}%%
xychart-beta
    title "Monthly demand seasonality index"
    x-axis [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
    y-axis "Seasonality index" 0 --> 150
    line [78, 80, 88, 98, 118, 132, 138, 128, 104, 90, 82, 84]
```

### Competitor promotion patterns

- `data/competitor_price_history.csv` has **48 rows** (12 months × 4 competitors), with no duplicates or missing values. Across the history, there were **5 promotion-month observations**: PulsUp in **October 2025 and February 2026**, Root & Rise in **February 2026**, VoltFit in **June 2026**, and Mate Libre in **July 2026**.
- Promotion discounts averaged **15% for PulsUp**, **15% for Root & Rise**, **10% for VoltFit**, and **20% for Mate Libre**. Promotions are concentrated in **February, June, July, and October**; there is no observed May promotion in this 12-month sample.
- Average shelf prices in the file were **€1.06 PulsUp**, **€1.56 Mate Libre**, **€2.37 VoltFit**, and **€2.91 Root & Rise**. These are historical observations and do not establish future shelf prices.

## 3. Recommendation

1. **City:** Start in **Berlin**, focused on urban retail/grocery locations and a measurable DTC support layer. Use a geographically bounded pilot so repeat, rate of sale, and promotion response can be compared with Hamburg.
2. **Timing:** Target **May 2027** for the broad pilot; seed retail and awareness in late April. This captures the spring demand inflection before the July maximum and avoids the competitor promotion months observed in the supplied history. The year is a planning assumption because the seasonality file has months but no launch calendar.
3. **Test design before scaling:** Run Berlin as the primary cell and Hamburg as a matched challenger. Track weekly distribution, rate of sale per active store, repeat purchase, DTC conversion, CAC/payback, and net contribution after promotions. Hold out comparable locations or audiences where feasible.

## 4. Assumptions, limitations, and risks

- **Observed facts:** row counts, survey responses, reported market-context values, seasonality indices/temperatures, and competitor list/shelf prices and promotion flags.
- **Calculated metrics:** city euro sizing, survey percentages/means, and the May-versus-July index comparison. Calculations use the supplied values without names or email addresses.
- **Assumptions:** the Energy / focus sub-category is a reasonable proxy for LUMEN; the file's city shares can be used for directional prioritization; May 2027 is operationally feasible; and the historical promotion pattern is informative for planning.
- There is **no German LUMEN sales history**, so city attractiveness is triangulated from an illustrative market split and a synthetic German survey. Survey city samples are uneven, especially Frankfurt (n=32), and intent is not purchase behavior.
- The market-context regional splits and CAGRs are explicitly illustrative/assumed; they should be replaced or calibrated with retailer distribution, category sales, and local media-cost data before committing a national rollout.
- The competitor history covers only 12 months. One observed quiet May does not guarantee a promotion-free May. Monitor retailer leaflets and online prices in the weeks before launch.
- Weather is Germany-wide average temperature, not city-level weather, and the data is observational. It supports timing logic but does not prove temperature causes demand.
- Risks include Berlin's higher competition and launch cost, price/promotion pressure from PulsUp, and overestimating intent-to-repeat conversion. A May launch may also miss a retailer window or face an unobserved competitor event.

## 5. Implications for the final LUMEN recommendation

The final case recommendation should frame Berlin/May as a **learning-oriented, scale-first entry**, not as proof that Berlin will outperform every city. It should preserve Hamburg as the next test because Hamburg leads on survey intent and frequency. The final recommendation should also state that any premium positioning and price decision needs a city-by-channel pilot: market size and timing support where/when to learn, but they do not by themselves establish willingness to pay or marketing payback.
