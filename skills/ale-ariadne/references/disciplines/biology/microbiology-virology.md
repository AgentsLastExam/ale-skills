# Biology: microbiology and virology

This file adds content specific to microbiology and virology to `references/disciplines/biology.md`, whose provisions still apply.

Scope: bacterial physiology and metabolism (growth laws and resource allocation, stress response and persistence), resistance and phages (evolution of antimicrobial resistance, phage biology and defense systems, secretion systems and interbacterial conflict), virus replication and host interaction (entry and receptors, viral evolution, antagonism of innate immunity), microbiomes and communities (community composition and metagenomics, host-microbiome interaction, community assembly and cross-feeding), and microbial genetic tools (transposon and fitness screens). For the host immune response see `immunology.md`; for diagnosis and treatment of infection at the patient level see `references/disciplines/medicine.md`; for sequence assembly and variant calling pipelines see `genomics-omics.md`; for phylogenetic inference and inference of selection see `evolution-ecology.md`; for strain engineering and chassis work see `bioengineering.md`.

## Screening criteria

- Build with priority: questions in bacterial physiology that come down to a set of quantitative relations which can be refitted, for example the growth laws and proteome resource allocation. Coarse-grained models and published compilations of growth rate and RNA/protein ratio are both mature, and growth rates themselves can be measured again within six hours (physical-world observation level 2).
- Build with priority: predicting resistance phenotype from a genome and comparing with phenotypic susceptibility data, for example resistance prediction in Mycobacterium tuberculosis. Whole genomes and MICs for 13 drugs are published for 12,289 clinical isolates, per-drug sensitivity, specificity and the share of resistant isolates called susceptible are established metrics in the field, and mutation catalogues provide a baseline.
- Build with priority: forecasting on surveillance data, for example predicting the frequency of a variant over the following weeks from public sequences and testing data. The scoring rules, naive baselines and splitting by time are all established, and the data used is limited to surveillance, diagnosis and basic mechanism.
- Defer: questions whose conclusion needs long culture, animal colonization or serial passage, for example the assembly of a synthetic community in the mouse gut after several weeks (physical-world observation level 3). Discuss with the expert whether to predict the outcome of pairwise coculture or short-term growth under a fixed model instead, or to ask for a ranking.
- Defer: tasks that touch biosafety-sensitive content. These are not built, and no technical detail about them appears in the task statement, the research log or the conversation.

## Matters to confirm in conversation

- Strain and culture conditions: the source and collection number of the strain, the medium recipe, temperature and aeration, and the difference between a microplate and a shake flask.
- The definition of growth rate and how it is fitted: from OD, CFU or dry mass; the time window and density range used for fitting; how blanks, evaporation and path length are handled.
- Which proxy is used for ribosome content, and the factor converting the RNA/protein ratio into a ribosomal protein fraction and where it comes from.
- The susceptibility testing system and version: EUCAST or CLSI, the version of the breakpoints, the two-fold dilution grid of MICs and the spread between replicate measurements.
- The population structure of the genome data: the distribution of lineages, clones and outbreak clusters, and whether the held-out part is split by phylogeny.
- The databases and versions used in metagenomic analysis, and the contamination controls for low-biomass samples.
- The source of viral sequences and surveillance data, their redistribution license, the date of the data snapshot and the reporting delay.
- The form of the conclusion and the tolerance: an absolute rate, a ranking or a forecast score; whether the tolerance comes from the spread between replicate cultures, from measurement error or from sampling noise.

## Checking templates

The templates below add to the general templates in `references/disciplines/biology.md`.

| Template | Criterion | Scope |
|---|---|---|
| Refitting of growth curves | With a fixed density range, time window and blank subtraction, the agent judge refits growth rates from the raw OD time series, they agree with the values the submitter reports, and the spread between replicate wells is reported | Needs a new observation (physical-world observation level 2) |
| Recomputation of the resource allocation model | The agent judge solves the coarse-grained model again with the submitted parameters and checks that the slopes and intercepts of both growth laws fall within a tolerance set by the spread of the data | Pure computation |
| Resistance prediction split by lineage | On a held-out set split by phylogeny, sensitivity and specificity are computed per drug, with the share of resistant isolates called susceptible reported separately; an MIC prediction counts as agreeing if it is within one two-fold dilution | Uses existing data, scientific discovery level 2 |
| Recomputation of a metagenomic pipeline | The classification or binning pipeline is rerun on benchmark data of known composition, precision and recall are computed per taxonomic rank, and the completeness and contamination of reconstructed genomes are reported | Uses existing data, must pass |
| Scoring of a forecast made in advance | A forecast submitted before the cutoff date is scored with a rule fixed in advance on surveillance data released after the cutoff, and compared with a fixed naive baseline | Uses existing data, scientific discovery level 2–3 |
| Negative control | After labels are shuffled or shifted in time, the same pipeline has no predictive power; on a subset without the target signal it returns nothing significant | Must pass |

## Sources of existing data

- Resistance: the public Mycobacterium tuberculosis dataset (12,289 clinical isolates with whole genomes, MICs for 13 drugs and binary resistance calls); genome and phenotype records in NCBI Pathogen Detection and BV-BRC; the resistance gene databases CARD, ResFinder and AMRFinderPlus, whose versions must be recorded. Breakpoint tables are published by EUCAST and CLSI and revised yearly.
- Genomes and metagenomes: ENA/SRA, GTDB, MGnify, and cohorts such as the Human Microbiome Project. The ground truth of benchmark sets such as CAMI is generated by simulation, so it counts as pure computation, not existing data.
- Physiology: published compilations of E. coli growth rates and RNA/protein ratios, condition-dependent quantitative proteomics datasets, phenotype data from single-gene deletion collections, and values collected in BioNumbers together with their primary sources.
- Viruses: sequences in GenBank and NCBI Virus can be redistributed freely; GISAID requires registration and an agreement, does not allow redistribution, and its sequences must not be placed in a task package.
- Surveillance: case, testing and sequencing time series published by public health agencies. Such data is revised retrospectively, so the snapshot date must be recorded.

## Preventing answer leakage

- Catalogues of resistance mutations are public, so a phenotype can be looked up from a genotype. Ask instead for predictions on drugs, lineages or rare variants the catalogue does not cover, or for effect sizes to be re-estimated.
- Isolates cluster by clone and outbreak, so a random split puts the same clone on both sides and inflates the metrics. Split by phylogeny, by sampling site or by sampling time.
- The slopes and model parameters of the growth laws are published. Use a strain or medium the paper did not use, or ask for a quantity the paper did not report, such as the predicted curve under a given antibiotic titration.
- Forecasting tasks must freeze the data snapshot and the cutoff date, and the data used for scoring is released only after the cutoff.
- The task statement contains no sample accessions, strain collection numbers, dataset names or paper information; the labels of the held-out part are kept only in `tests/`.

## Tools and compute

- Assembly and annotation: SPAdes, Flye, Prokka, Bakta.
- Classification, binning and quality assessment: Kraken2 with Bracken, MetaPhlAn, GTDB-Tk, CheckM2.
- Resistance and phylogeny: AMRFinderPlus, ResFinder, Mykrobe, TB-Profiler; Snippy, IQ-TREE.
- Growth and metabolism: growth curves can be fitted with tools such as growthcurver; genome-scale metabolic models are handled with COBRApy, with models taken from BiGG Models or built with CarveMe.
- Defense systems and viruses: DefenseFinder, PADLOC; typing and phylogenetics of viral sequences use the public Nextclade and Nextstrain workflows.
- Compute: assembling and annotating one bacterial genome takes minutes to an hour on an ordinary computer, while pipelines over thousands of genomes and phylogenetic inference need a cluster; the databases for metagenomic classification run to tens or hundreds of GB and must be placed in the environment offline; solving a coarse-grained growth model takes seconds, and refitting during review is far smaller than solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- OD is not proportional to biomass at high density, and the path length of a plate reader differs from that of a spectrophotometer, so values cannot be compared directly.
- A growth rate taken from the maximum slope or a fixed time window that includes part of the lag phase or the entry into stationary phase.
- Poor aeration in a microplate gives a lower growth rate than a shake flask, so values in the same medium are not interchangeable.
- A medium of the same name has different recipes in different labs; different K-12 strains grow at different rates in the same medium, so growth-law parameters belong to a strain.
- Using the RNA/protein ratio for ribosome content assumes that the share of rRNA in total RNA is constant.
- MICs sit on a two-fold dilution grid and replicate measurements often differ by one dilution, yet they are treated as exact continuous values when computing errors.
- Breakpoints are revised over the years, so re-calling old data with new breakpoints changes the phenotype labels and the results are not comparable.
- Classification results change with the database version; reagent contamination in low-biomass samples is taken for real species.
- Sequencing intensity changes over time, so the denominator of a variant frequency changes with it; reporting delays truncate recent data, and fitting it directly overestimates the growth rate.

## Example: bacterial growth laws and proteome resource allocation

In E. coli, when growth rate is changed through the nutrient quality of the medium, the mass fraction of ribosomal proteins in total protein, φR, rises linearly with growth rate λ as φR = φR,min + λ/γ; when growth is slowed with a sub-lethal concentration of a translation-inhibiting antibiotic such as chloramphenicol, φR remains linear in λ but with a negative slope, φR = φR,max − λ/ν. The literature takes φR,min ≈ 0.07, φR,max ≈ 0.55 and a maximal translational efficiency of about 5.9 h⁻¹. Both lines can be derived from a three-way partition of the proteome (a growth-rate-independent fraction, a ribosome-affiliated fraction and a metabolic fraction) together with amino acid flux balance. The elongation rate is not strictly constant: as the doubling time lengthens from 20 minutes to 20 hours, the peptide elongation rate per ribosome falls from about 16 amino acids per second to about 9, so the assumption of constant γ in the first growth law has a limited range. The task asks the solving agent to explain both growth laws with one coarse-grained model and to predict conditions that were not used for fitting.

The following is illustrated for the Explanation class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 2.

- **Task statement and deliverables.** The task statement gives growth rates and RNA/protein ratios for one strain across several media and several antibiotic concentrations, the factor converting the ratio into φR, and the list of held-out conditions, but not the measurements for those conditions and not the form of the model. The deliverables are model code that can be rerun, a parameter table with uncertainties, the two predicted growth-law lines, an ablation table, and predictions for the held-out conditions (`predictions.csv`: condition ID, predicted growth rate, interval). The format of that file is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. The growth law under nutrient quality: where the positive slope comes from, and what γ and φR,min mean.
  2. The growth law under translation inhibition: where the negative slope comes from, and why the lines for different media meet at a common point.
  3. Range of validity: when the elongation rate falls with slower growth and a fraction of ribosomes is inactive, which of the two growth laws fails first.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the phenomenon (the corresponding data points, slopes and measurement spread). The deliverable is the mechanism, as computation (solving and refitting the model, with ablation performed by removing the fixed proteome fraction and by making the elongation rate depend on amino acid concentration, and observing whether each line disappears or changes slope) and as mathematics (deriving both expressions from flux balance and the proteome partition constraint, and stating the correspondence between model parameters and measurable quantities).
- **Checks.** The agent judge refits the submitted code on the same data and checks that the slopes and intercepts fall within a tolerance set by the spread of the measurements; it reruns each ablation and confirms that the effect of each element matches the submitted classification; it then checks the predictions for the held-out conditions. Those conditions need a new observation: the check writes out the instrument and procedure — OD₆₀₀ time series on a plate reader, at least three replicate wells per condition, growth rate fitted over a fixed density range, with the strain and medium withheld from the solving agent — and the criterion applied once the data exist, namely that the prediction intervals must cover at least a share of the conditions fixed in advance. Following "Tasks at physical-world observation level 2" in `references/2-research.md`, this part cannot be run on the expert's machine: the check is written out as usual, the parts that need no experiment are actually run, and the research log, the verifier decision and the problem card state plainly that this part was not run and needs an experiment; in steps 4 and 5 its score is likewise recorded as not run, and no experimental data is fabricated to make it pass.
- **Calibration cases.** The empty submission (score 0); fitting a straight line to each of the two datasets without a model (a shortcut; it reproduces both growth laws but fails the ablation and the held-out prediction); a model that explains the first growth law but gets the sign of the second slope wrong (partially correct); the published coarse-grained model with its published parameters (a known result).
- **Other tasks of the same structure.** The transition in growth rate after a nutrient shift up or down, the burden of heterologous protein expression, or the same relations in another microbe; the workflow and the checks stay the same.
