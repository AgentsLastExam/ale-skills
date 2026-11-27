# Biology: molecular and cell biology

This file adds content specific to molecular and cell biology to `references/disciplines/biology.md`, whose provisions still apply.

Scope: control of gene expression (transcription factors and enhancers, stochastic expression and transcriptional bursting, translational control and ribosome profiling), trafficking and organelles (the secretory and endolysosomal pathways, organelle contact sites, biomolecular condensates), cytoskeleton and cell mechanics (motors and filament dynamics, adhesion and mechanotransduction, migration and polarity), cell cycle, cell death and quality control (checkpoints and mitotic control, regulated cell death, proteostasis and autophagy), and signal transduction (kinase cascades and phosphoproteomics, GPCRs and second messengers, signaling dynamics and single-cell response). For structures at the molecular level and in vitro biophysics see `molecular-biophysics.md`; for genome-wide measurement and its data processing see `genomics-omics.md`; for statistical and machine learning methods on single-cell data see `computational-biology.md`; for cell behavior in tissue and embryo context see `developmental-biology.md`; for mechanisms at the organ and disease level see `physiology.md`; for neurons and synapses see `cellular-neuroscience.md`; for engineering reporters and perturbation tools see `bioengineering.md`.

## Screening criteria

- Build with priority: inferring transcriptional burst kinetics from single-cell count distributions. The two-state model is the forward model the field accepts, allele-resolved public data exists, and recovery on synthetic data and profile-likelihood intervals are established practice.
- Build with priority: explaining the temporal behavior of a signaling pathway with a kinetic model, for example the pulsatile response of ERK or NF-κB. Public live-cell imaging data, reproducible SBML models and ablation by removing one feedback are all available.
- Defer: conclusions that invoke phase separation as the mechanism, for example the function inside cells of condensates formed by a given protein. How phase separation in cells is established is still disputed in the field, and artifacts from 1,6-hexanediol treatment and from overexpression are common. Discuss with the expert a formulation that fixes the assay in advance and asks only for an in vitro phase diagram or a ranking between candidates.
- Defer: conclusions that depend on a newly made knock-in cell line or on a perturbation experiment lasting days (physical-world observation level 3), for example the effect of a gene knockout on cell cycle duration. Such a task can be reformulated as a prediction on existing perturbation data, or as a live-cell readout obtainable within six hours (physical-world observation level 2).

## Matters to confirm in conversation

- The cell system and its state: the source and authentication of the cell line, passage number, mycoplasma testing, medium and confluence, and whether cells are synchronized.
- The measurement modality and its calibration: smFISH, a live-cell reporter or single-cell sequencing; and whether the maturation time and half-life of the reporter are shorter than the process being studied.
- How counts or fluorescence intensities are converted into molecule numbers: capture efficiency, detection threshold, spot-detection parameters, and whether nascent signal at the transcription site is counted.
- The form and units of the kinetic model: which rate sets the unit of time (degradation of mRNA or of protein), and where the degradation rate comes from.
- The levels of replication: how independent experiments, wells and cells relate, and which level the statistical test uses as its unit.
- How extrinsic noise is handled: corrections for cell size, cell cycle stage and total counts; and whether allele resolution is used to control extrinsic noise.
- The specificity of the perturbation and its controls: off-target effects, compensation, and the difference between acute and chronic perturbation.
- The form of the conclusion and the tolerance: a parameter value, a ratio of parameters or a direction of change; whether the tolerance comes from the spread between replicate experiments, from the recovery bias on synthetic data, or from the sampling noise of the counts.

## Checking templates

The templates below add to the general templates in `references/disciplines/biology.md`.

| Template | Criterion | Scope |
|---|---|---|
| Rerunning the inference | The agent judge reruns the submitted code on the same count data and checks that the parameters the submitter reports are at the likelihood optimum and that the profile-likelihood intervals can be reproduced | Pure computation, must pass |
| Recovery on synthetic data | Synthetic data is generated from known parameters at the cell number and capture efficiency of the measured data, and the bias of the point estimates and the coverage of the intervals must meet thresholds set in advance | Pure computation, must pass |
| Forward simulation and comparison of distributions | Count distributions are simulated forward from the submitted parameters, and their difference from the measured distributions is at the level of sampling noise, with the test statistic compared against a noise envelope | Uses existing data |
| Flagging of identifiability | Parameter combinations that are not identifiable are flagged, with a statement of what further data would separate them; anything flagged as not identifiable scores nothing as if it had been identified | Counts for part of the score |
| Recomputation of image quantification | With fixed segmentation and spot-detection software and parameters, per-cell counts or intensities are recomputed from the raw images and agree with the values the submitter reports; statistical tests use independent experiments, not cells, as the unit | Uses existing data, must pass |
| Short live-cell readout | A response-curve prediction submitted in advance (amplitude, time to peak, degree of adaptation) is compared with a time series obtained within six hours by live-cell imaging or on a plate reader, with the criterion and threshold written out beforehand | Needs a new observation (physical-world observation level 2) |

## Sources of existing data

- Single-cell counts: allele-resolved Smart-seq2 datasets are held in ArrayExpress/ENA; for single-cell data in general see the sources in the general file.
- Imaging: the Image Data Resource, the BioImage Archive (which follows the REMBI metadata guidelines), EMPIAR, and large image collections such as Cell Painting. Raw images often run to several TB, so a task package holds only a subset or derived quantifications.
- Perturbation and modification: the perturbation expression data of LINCS, proteomics and phosphoproteomics data in PRIDE, modification site annotation in PhosphoSitePlus, and the dependency data of DepMap.
- Models: cell cycle and signaling models stored as SBML in BioModels. Their output is computed, so it counts as pure computation, not existing data.
- Cell line information: the cell line identities and misidentification records collected in Cellosaurus, used to check whether the cell line in use is reliable.

## Preventing answer leakage

- Published tables of burst parameters and model parameters are released with the papers and can be found by searching. Use genes the paper filtered out, another dataset or another species, and anonymize the gene IDs.
- A dataset can be identified from gene names plus cell type. The task statement contains no dataset accessions, gene names or paper information.
- Public segmentation and spot-detection models may already have been trained on the same public images, which inflates the metrics. Use a newly deposited image set, or a subset whose labels are not public.
- Cells from the same donor, the same batch or the same well must not appear in both the fitting data and the held-out data.
- The held-out perturbation data and the reference values used for scoring are kept only in `tests/`.

## Tools and compute

- Image processing and segmentation: Fiji/ImageJ, CellProfiler, Cellpose, StarDist, ilastik, napari; tracking uses TrackMate.
- Spot detection and smFISH quantification: tools such as FISH-quant; images are stored as OME-TIFF or OME-Zarr.
- Stochastic models and inference: SSIT (finite state projection and maximum likelihood, in MATLAB) and stochastic simulators such as GillesPy2; profile likelihood and Bayesian inference use general numerical and sampling libraries.
- Deterministic kinetic models: described in SBML and solved with COPASI, Tellurium or PySB.
- Pathway and localization annotation: Reactome, SIGNOR, and the subcellular localization data of the Human Protein Atlas.
- Compute: inference runs independently per gene, so a few thousand genes take on the order of hours on a multicore CPU; the state space of the finite state projection grows with the count cutoff, so highly expressed genes need a truncation with a convergence check; image segmentation needs a GPU; raw images run to TB, so derived count matrices are preferable. Review mainly reruns the inference on the held-out part and is far smaller than solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Statistical tests that treat cells as independent replicates when the independent unit is the experimental batch, which raises false positives sharply.
- Absolute rates reported, without stating the unit of time used, when steady-state distributions can only fix ratios of parameters.
- Capture efficiency not accounted for, so burst size is systematically underestimated.
- Nascent transcription signal at the transcription site counted together with mature mRNA spots.
- Counts for a lowly expressed gene too few to separate the two-state model from a Poisson distribution, yet narrow intervals are reported.
- Extrinsic noise from cell size and cell cycle stage left uncorrected and taken for variation caused by bursting.
- A reporter whose maturation time or half-life is longer than the process being studied, so the measured kinetics are those of the reporter itself.
- An overexpressed fusion protein that changes the process being studied; off-target effects of treatments such as 1,6-hexanediol taken as evidence of a mechanism.
- A misidentified cell line or mycoplasma contamination, so results cannot be reproduced.

## Example: inferring transcriptional burst kinetics from single-cell count distributions

Transcription occurs in bursts, and the two-state model is the standard forward model: the promoter switches between an on and an off state at rates kon and koff, mRNA is synthesized at ksyn in the on state, and mRNA decays at its degradation rate. In one allele-resolved Smart-seq2 study, burst frequency and burst size were inferred for 7,186 genes from 224 primary mouse fibroblasts (a CAST/EiJ × C57BL/6J cross). Steady-state count distributions can only fix the ratios of the rates to the mRNA degradation rate, so burst frequency is reported in units of that degradation rate and burst size is taken as ksyn/koff; the individual rates are not identifiable over large regions of parameter space. Parameters were estimated by maximum likelihood with confidence intervals from the profile likelihood at a cutoff of 1.92, and fitting molecule counts worked better than fitting RPKM. The conclusion was that enhancers mainly change burst frequency while TATA elements in the core promoter raise burst size: deleting one enhancer lowered burst frequency significantly on that allele with no significant change in burst size. The task asks the solving agent to infer burst parameters independently from the count distributions of held-out genes and to argue identifiability.

The following is illustrated for the Inversion class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives the allele-resolved molecule count matrix, the number of cells, how capture efficiency is estimated and the convention for units; it gives no published parameter table, and all gene IDs are anonymized. The deliverables are inference code that can be rerun, a parameter table per gene and allele (`estimates.csv`: gene ID, allele, burst frequency, burst size, interval, identifiable or not), the results of recovery on synthetic data, and a short report. The format of that file is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Recovery of the burst parameters: point estimates and profile-likelihood intervals for the held-out genes.
  2. Identifiability and the limits of the data: which combinations steady-state distributions can fix, how the number of cells and the capture efficiency set the interval width, and what further data would separate kon from koff.
  3. Perturbation prediction: which parameter changes, and in which direction, when a specified regulatory element is deleted, tested on held-out allele-level data.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the observed data the sub-question concerns. The deliverable is the reconstructed part, as computation (counts simulated forward from the inferred parameters through the same capture and detection model, with residuals at the level of sampling noise, and correct recovery on synthetic data whose truth is generated by simulation) and as text (the distribution features invoked, such as the mean, the Fano factor and the fraction of zero counts, which the agent judge confirms are present in the count data; the interval widths, and the flagging of genes that are not identifiable). The physical constraints (non-negativity and the convention for units) are checked by the agent judge.
- **Checks.** The agent judge reruns the inference and checks that the reported parameters are at the likelihood optimum; it checks bias and interval coverage on synthetic data generated from known parameters at the same cell number and capture efficiency as the measured data; it simulates distributions forward from the submitted parameters and compares their difference from the measured distributions against a sampling-noise envelope; it scores the perturbation prediction on the held-out allele-level data with a statistical test fixed in advance; and genes flagged as not identifiable score nothing as if they had been identified. The tolerance is set from the spread of repeated inference on synthetic data and from the sampling noise of the counts.
- **Calibration cases.** The empty submission (score 0); a published parameter table copied over (a shortcut; the gene IDs are anonymized, the genes used are those the paper filtered out together with another dataset, and the agent judge reruns the code separately); point estimates from the method of moments with no intervals and no identifiability statement (partially correct); the published maximum-likelihood tool run as it stands (a known result).
- **Other tasks of the same structure.** Inferring the kinetic parameters of a pathway from live-cell signaling traces, or the promoter switching kinetics at transcription sites from smFISH counts; the workflow and the checks stay the same.
