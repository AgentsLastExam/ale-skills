# Medicine: global and environmental health

This file adds content specific to global and environmental health to `references/disciplines/medicine.md`, whose provisions still apply.

Scope: burden of disease (burden estimation and life tables, verbal autopsy and vital registration), environmental and occupational exposure (air pollution and exposure modeling, climate and heat-related health, occupational hazard and injury), nutrition and lifestyle (dietary assessment and intake modeling, physical activity measurement), health behavior and intervention (cluster-randomized field trials), and maternal and child health programs in low-resource settings. For infectious disease transmission models, outbreak surveillance and causal inference in observational studies see `epidemiology.md`; for death certification and cause-of-death coding see `pathology.md`; for the cost-effectiveness of interventions see `health-policy-economics.md`; for the processing of wearable device signals see `clinical-assessment.md`; for atmospheric and climate processes themselves see `references/disciplines/earth.md`.

## Screening criteria

- Build with priority: questions that estimate, from public daily series, the exposure–response relationship between temperature or air pollution and mortality, and the attributable burden. An example is the time-series analysis of daily deaths and temperature in one city: the workflow of distributed lag non-linear models is mature, and simulated series with a planted known relationship and held-out years exist to compare against.
- Build with priority: questions that rebuild life tables and burden measures from public vital registration data, for example computing life expectancy from deaths and population by age, decomposing the change in life expectancy between two periods by age and cause, or computing years of life lost. The algorithms are fixed, and the results can be recomputed exactly.
- Build with priority: questions that evaluate cause-of-death assignment methods on public gold-standard data, for example comparing algorithms on the PHMRC verbal autopsy dataset. The field has accepted metrics (chance-corrected concordance, CSMF accuracy) and a prescribed way of constructing test sets.
- Defer: questions in which the health effect of long-term exposure or a future burden can be judged only after decades of follow-up, for example the cohort association between long-term PM2.5 exposure and mortality (the Six Cities study followed 8,111 adults for 14 to 16 years, and its individual data is not public), or heat-related deaths by the middle of this century under climate change scenarios. Discuss with the expert fixing the exposure–response function, the population and the baseline mortality in advance and asking only for the attributable deaths that can be recomputed under the given function; the conclusion of this sub-problem is conditional on the chosen function and does not show whether the function itself is right.
- Defer: questions in which the effect of an intervention can be judged only by a new field trial, for example the effect of water, sanitation and handwashing interventions or of nutritional supplementation on child growth (physical-world observation level 3). These can become a reanalysis, under the pre-analysis plan, of a cluster-randomized trial whose data is public (for example WASH Benefits).

## Matters to confirm in conversation

- The definition and coding of the outcome (all-cause or cause-specific, the ICD version, whether external causes are excluded), and the population, region and period.
- The measure and source of exposure: monitoring stations, reanalysis or satellite retrievals, the daily mean or daily maximum, the spatial aggregation, and how exposure measurement error is considered.
- In time-series analysis, how season and long-term trend are controlled and with how many degrees of freedom, the length of the lag period, the form of the exposure–response function, and whether humidity, pollutants and influenza are adjusted for.
- How the reference level of the attributable burden (the minimum mortality temperature or the theoretical minimum risk exposure level) is determined, the cut-offs between cold and heat and between extreme and moderate, and how the confidence interval is computed.
- For life tables and burden measures, the age groups, the treatment of the open-ended age group, the standard population and the reference life table, and whether discounting and age weighting are used.
- For verbal autopsy, the questionnaire version, the cause list and the diagnostic basis of the gold standard, and how the cause composition of the test sets is set.
- For survey and field trial data, the sampling design, weights and clustering, and whether the analysis follows a pre-registered plan.
- The nature of the comparison values: direct observations, gold-standard diagnoses, or model estimates (for example the GBD estimates); what the tolerance rests on (sampling variation, the spread between reasonable model specifications).

## Checking templates

The templates below add to the general templates in `references/disciplines/medicine.md`.

| Template | Criterion | Scope |
|---|---|---|
| Recovery of the exposure–response relationship on simulated series | The agent judge runs the submitted code on simulated series with a planted known exposure–lag–response relationship: the cumulative relative risk curve, the percentile of the minimum mortality temperature and the attributable fraction agree with the planted values within tolerance | Pure computation, scientific discovery level 1–2 |
| Prediction of held-out years | The submitted model predicts daily deaths in the held-out years with a deviance lower than that of a baseline model containing only season and trend terms, and the residuals show no marked autocorrelation | Uses existing data, scientific discovery level 2 |
| Sensitivity to model specification | After refitting with changed degrees of freedom for season, lag length and spline knots, the submitted conclusion still holds within its stated uncertainty | Uses existing data, must pass |
| Recomputation of the attributable burden | Given the exposure distribution, the exposure–response function and the baseline mortality, the population attributable fraction and the attributable deaths are recomputed; the cold and heat components sum to the total | Pure computation |
| Recomputation of life tables | Probabilities of death, life expectancy and years of life lost are recomputed from deaths and population by age; in a decomposition, the contributions of the ages and causes sum to the difference in life expectancy | Uses existing data, scientific discovery level 1 |
| Evaluation of verbal autopsy methods | On many test sets whose cause composition is resampled from a Dirichlet distribution, chance-corrected concordance at the individual level and chance-corrected CSMF accuracy at the population level are computed | Uses existing data, scientific discovery level 2–3 |
| Reanalysis of a cluster trial | The difference between arms is re-estimated under the pre-analysis plan, with standard errors that account for clustering, and agrees with the reference analysis within tolerance | Uses existing data, scientific discovery level 1–2 |

## Sources of existing data

- Deaths and population: the WHO Mortality Database and the United Nations World Population Prospects (public); the Human Mortality Database requires registration; CDC WONDER in the United States can be queried publicly, with small counts suppressed.
- Daily health series: the daily mortality, weather and pollution data for Chicago, 1987–2000, shipped with the R package dlnm; the daily mortality and temperature series for London, 1993–2006, and the series for 10 regions of England and Wales, 1990–2012, released with methodological tutorials. The full data of the multi-country study was not released with the paper.
- Exposure: the ERA5 reanalysis (Copernicus, registration required); the AQS monitoring data of the US EPA (public); gridded PM2.5 products from satellite retrievals.
- Burden estimates: the GBD results are obtained through GHDx, for non-commercial use only. These values are model estimates, so comparing against them counts as pure computation, not existing data.
- Verbal autopsy: the PHMRC gold-standard dataset (6 sites in 4 countries, 12,542 verbal autopsies, of which 7,836 adults), downloadable from GHDx under the same non-commercial terms.
- Surveys and trials: DHS requires registration and a research project request per country, and once downloaded the datasets may not be passed on without written consent; NHANES is public and includes dietary recalls and accelerometer data; the primary analysis materials of the WASH Benefits Bangladesh trial are public on OSF.

## Preventing answer leakage

- Analysis results for the public series appear in software documentation and tutorials, for example the fitted results for the Chicago and London series. Make the submitted code the object of scoring, rerun by the agent judge on simulated series and on held-out years.
- The simulated series are generated from a real temperature series plus a planted exposure–response relationship, and the planted parameters are kept only in `tests/`.
- Published attributable fractions, life expectancies and GBD estimates can be found by searching. Switch to regions, years or age groups the papers did not report, or change the reference level and the cut-offs, and score the recomputed quantities.
- The cause labels of the verbal autopsy gold-standard data are public. The agent judge resamples the test sets to a new cause composition, or a whole site is held out; the task statement does not name the dataset.
- The name of the city and the years can be used to look the series up. The task statement hides the place name; when dates are shifted, the day-of-week and seasonal structure is kept.

## Tools and compute

- Time series and exposure–response: in R, dlnm, mixmeta (pooling across locations), gnm (conditional Poisson regression) and splines.
- Demography and burden: in R, demography and HMDHFDplus; for attributable burden, BenMAP-CE of the EPA (open source) and AirQ+ of the WHO.
- Verbal autopsy: openVA (InterVA, InSilicoVA and other algorithms); SmartVA-Analyze (the Tariff method).
- Survey and trial analysis: in R, survey (complex sampling), lme4 and geepack (clustered data); GGIR for processing accelerometer data.
- Compute: fitting a daily series of ten to twenty years for one city takes seconds to minutes on one core; Monte Carlo sampling for empirical confidence intervals and repeated evaluation on hundreds of test sets take minutes to hours; attributable burden on a global grid is limited mainly by data volume. The rerun during review is of the same order as solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Too little control for season and long-term trend, so that the influence of other winter factors is counted as an effect of cold; too much control absorbs the real effect of exposure. The choice of degrees of freedom needs a sensitivity analysis.
- A lag period that is too short. The effect of cold can last two to three weeks, so a lag of a few days underestimates it; deaths brought forward after heat (harvesting) also need a long enough lag period to be netted out.
- The minimum mortality temperature lies where the curve is flat, and its uncertainty is large. A tight tolerance set on the temperature value leads to wrong verdicts; the attributable fraction is more stable.
- The attributable burden changes with the reference level and with the exposure–response function. For global deaths attributable to PM2.5, GEMM estimated 8.9 million for 2015 while the function used by GBD gave 4.0 million, a difference of more than a factor of two; the task statement must fix the function.
- The mean of a monitoring station or a city taken as individual exposure, and a group-level association stated as individual risk.
- Model estimates (GBD, gridded exposure products) treated as observed truth. When the two share inputs, a comparison shows only that the workflows agree.
- The open-ended age group, the average survival time of infants and the random fluctuation of small populations handled wrongly in a life table; ill-defined cause-of-death codes left unhandled in a decomposition by cause.
- CSMF accuracy not corrected for chance. Random allocation of causes already has an expected value of about 0.63; when the test sets keep the cause composition of the training set, the metric is inflated.
- A cluster trial analyzed by individual without accounting for clustering; a complex sample survey analyzed without the weights and design variables.

## Example: the exposure–response relationship between daily temperature and mortality, and the attributable fraction

The 2015 multi-country study by Gasparrini and colleagues analyzed 74,225,200 deaths in 384 locations of 13 countries between 1985 and 2012 and estimated that 7.71% (95% empirical confidence interval 7.43–7.91) of mortality was attributable to non-optimum temperature: 7.29% to cold and 0.42% to heat, with extreme cold and heat together responsible for only 0.86%; the minimum mortality temperature lay at about the 60th percentile in tropical areas and at about the 80th–90th percentile in temperate regions. How this burden will evolve under climate change is a north-star problem that needs decades of observation and depends on demographic change and adaptation; it cannot be judged here. What can be built is the sub-problem at its base: recover the exposure–lag–response relationship from the public daily series of one city, and compute the attributable fraction. This sub-problem does not show the future burden, and it does not rule out unmeasured confounding.

The following is illustrated for the Inversion class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement provides, for one city, more than ten years of daily all-cause deaths, daily mean temperature, date and day of week (for example the public series for London, 1993–2006, with the place name hidden), with the deaths of the last few years held out; it also states that the submitted code will be run on series that are not provided. The deliverables are analysis code that can be rerun, a `results.json` (the minimum mortality temperature and its percentile, the cumulative relative risk at the 1st and 99th temperature percentiles against the minimum mortality temperature, and the attributable fractions for cold and heat with their intervals), and a table of relative risks by temperature grid and lag day. The format of `results.json` and of the relative risk table is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Overall exposure–response curve: the cumulative relative risk over 21 days as a function of temperature, and the minimum mortality temperature.
  2. Lag structure: the effect of heat concentrated in the first few days, the effect of cold lasting two to three weeks, and the extent to which deaths are brought forward.
  3. Attributable burden: the attributable fractions for cold and for heat, with their empirical confidence intervals.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the observed data the sub-question concerns. The deliverable is the reconstructed part, as computation (expected daily deaths computed from the fitted model, with residuals against the observations at the noise level of an overdispersed Poisson distribution; correct recovery also on simulated series with a planted known relationship) and as text (the observed features it rests on, for example the peaks in deaths after hot summer days and the excess deaths in winter; an argument that the seasonal term and the temperature term can be separated, with the results under different degrees of freedom, lag periods and spline knots). The constraints (the relative risk is 1 at the minimum mortality temperature, and the cold and heat components sum to the total attributable fraction) are checked by the agent judge.
- **Checks.** The agent judge runs the submitted code on the simulated series and compares with the planted values: the logarithm of the cumulative relative risk at the 1st and 99th temperature percentiles, the attributable fractions for cold and heat, and the percentile of the minimum mortality temperature each deviate by no more than the half-width of the 95% interval that the reference analysis obtains over repeated simulations, and the intervals stated in the submission cover the planted values; on the held-out years of the real series, the predictive deviance is lower than that of the baseline model containing only season and trend terms. The other source of the tolerance is the model specification: step 2 records how the results of the reference analysis differ between 6 and 10 degrees of freedom per year and between lag periods of 21 and 28 days, and the tolerance may not be smaller than this difference.
- **Calibration cases.** The empty submission (score 0); the 7.71% of the multi-country study or the values of a software example copied without runnable code (a shortcut; nothing can be recomputed on the simulated series, and the corresponding values score 0); a model with no control for season and long-term trend (it gives a biased cold effect on the simulated series); a model with a lag of only 3 days or with a linear threshold form (partially correct); the reference analysis of step 2 (a known result).
- **Other tasks of the same structure.** Change the exposure (PM10 or ozone and daily deaths) or the outcome (cardiovascular or respiratory deaths), or move to a two-stage analysis of several locations (the public series for 10 regions of England and Wales); the workflow and the checks stay the same.
