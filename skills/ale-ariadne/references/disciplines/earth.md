# Earth science

## Screening criteria

- Build with priority: the target is a quantity that can be tested against public observations or reanalysis data (forecast skill, an inversion result, a trend, earthquake source parameters, a land-surface classification), and there is a held-out period or an independent observation (another set of stations, another satellite) to compare against.
- Build with priority: the evaluation metric and the baseline to beat have an accepted practice in the field.
- Defer: tasks that need new field observations, drilling or a cruise to be judged (physical-world observation level 3); long-term projections that can only be verified many years from now; reference values that exist only as the output of a single model; a reference computation that needs a global high-resolution model and exceeds the budget in one run.

## Matters to confirm in conversation

- What the target quantity is, and its spatial extent, time span and resolution.
- Whether the reference data is direct observation, reanalysis or model output. Reanalysis contains a model component and is not the same as observation.
- Which coordinate system, datum, projection, time standard and units are used.
- Which metric is used for evaluation, and which baseline it is compared with (climatology, a persistence forecast, an operational model).
- How held-out data is split (by time, by region), and how autocorrelation in time and space is handled.
- How large the observation error is, and how the representativeness difference between a station observation and a grid value is accounted for.
- How missing values and quality-control flags are handled.
- Whether the data license allows redistribution.

## Checking templates

Most templates below are implemented as numerical-check scripts that the agent judge calls; where the conclusion can be written as a Lean statement in advance, the agent judge checks it with the Lean tool; derivations, explanations and arguments are reviewed by the agent judge directly against the rubric. See `references/agent-judge.md`.

| Template | Criterion | Scope |
|---|---|---|
| Forecast or reconstruction test on a held-out period | RMSE, anomaly correlation coefficient and CRPS computed on the held-out period, plus skill scores relative to climatology or a persistence forecast | Uses existing data, scientific discovery level 2–3 |
| Comparison with independent observations | Model or inversion results are compared with stations, soundings or another satellite not used in building the method, with the observation error included | Uses existing data |
| Comparison with the result of a standard pipeline | Given raw data (seismic waveforms, remote sensing imagery, GNSS records), the agreement of the result (phase arrival times, locations, a classification map, a displacement field) with a reference catalog or reference product | Uses existing data, scientific discovery level 1–2 |
| Budget and physical consistency checks | Mass, energy and water budgets close; dimensions are correct; values lie in a physically reasonable range | Must pass, or counts for part of the score |
| Synthetic recovery test | Run the inversion or assimilation on synthetic data with a known truth and check whether the truth is recovered | Pure computation, scientific discovery level 2–3 |
| Model recomputation | The agent judge reruns the submitted parameters or scheme with a fixed model configuration (a simplified model, a single column, a small regional case) | Pure computation |
| Skill relative to a baseline | On a fixed evaluation set, the score follows the margin above an operational model or a baseline from the literature | Scientific discovery level 3 |

## Sources of existing data

- Reanalysis: ERA5, MERRA-2. Reanalysis is produced by assimilating observations into a model; say so when it is used as ground truth.
- Weather and ocean observations: NOAA's GHCN and ISD station data, IGRA soundings, Argo floats, GPCP precipitation, and the archives of NOAA NCEI.
- Satellites: NASA Earthdata (MODIS, GPM, GRACE), the Copernicus Sentinel series, Landsat.
- Seismology: waveform data from EarthScope (formerly IRIS), the USGS ComCat catalog, the ISC catalog.
- Geodesy and hydrology: GNSS time series from the Nevada Geodetic Laboratory, USGS NWIS streamflow, the CAMELS catchment dataset.
- Evaluation benchmark: WeatherBench 2.
- Climate model output: CMIP6. It counts as pure computation, not existing data.

## Preventing answer leakage

- Historical observations are all public, so a solving agent with network access can download the truth for the held-out period. Cut the environment off from the network or use an allowlist, and keep the truth for the held-out period in the agent judge only.
- The data is autocorrelated in time and space, so a random split leaks. Split by contiguous blocks of time or by region, and leave a gap between the two parts.
- A pretrained weather model has its own training period. The evaluation period must come after it.
- Results for famous events (a particular large earthquake, a particular typhoon) can be found by searching. Hide the event's name and date, or choose an event that is not well known.
- Reanalysis and observations are not independent of each other; the reanalysis assimilated the same observations. Keep this in mind when testing a method trained on reanalysis against observations.

## Tools and compute

- Gridded data: xarray, netCDF4, Dask, cfgrib, MetPy, CDO, NCO.
- Geospatial: GDAL, rasterio, pyproj, GeoPandas, PyGMT.
- Seismology: ObsPy, SeisBench, SPECFEM.
- Numerical models: WRF, MPAS, MITgcm; full Earth system models such as CESM are heavy.
- Compute: data volumes are large, the full ERA5 archive is at the petabyte scale, so a task gives only a cropped subset; global models are usually out of reach, and a small regional case takes tens to hundreds of CPU core-hours; data-driven weather models need GPUs.

## Common pitfalls

- Treating reanalysis as observed ground truth.
- Autocorrelation in time and space left unhandled, inflating skill scores.
- No comparison with climatology or a persistence forecast, so it cannot be told whether the method helps.
- Inconsistent longitude convention (0 to 360 or −180 to 180), projection or datum.
- Inconsistent time: time zone, calendar type, leap years.
- Inconsistent units: precipitation in mm/day or kg m⁻² s⁻¹, geopotential or geopotential height.
- Comparing station values directly with grid values without accounting for the representativeness difference.
- Trends that are sensitive to the start and end years.
- Missing values and quality-control flags included in the computation unhandled.
