# Medicine: infectious disease and host response

This file adds content specific to infectious disease and host response to `references/disciplines/medicine.md`, whose provisions still apply.

Scope: pathogen genomics and typing (sequence-based surveillance, lineage calling, detection and prediction of resistance genes), antimicrobial therapy and stewardship, vaccine immunogenicity and effectiveness (correlates of protection, real-world effectiveness, waning immunity and boosting schedules), treatment strategy and resistance in chronic infections such as HIV, and host response and markers of severity. For basic virology and microbiology see `references/disciplines/biology.md`; for transmission modeling and the design of surveillance systems see `epidemiology.md`; for the performance evaluation of diagnostic assays themselves see `laboratory-medicine.md`.

## Screening criteria

- Build with priority: questions that take public sequences as input and end in a typing or lineage call, where the workflow is mature and a reference call exists to compare against. An example is calling the Pango lineage of SARS-CoV-2 on genomes held out by time from a public database: the Nextclade and pangolin workflows are public, designated lineages can be compared against, and the UShER mode of pangolin is more accurate than the pangoLEARN mode on designated sequences.
- Build with priority: prediction of a resistance phenotype from a genotype, with matched phenotypic results to compare against. An example is predicting resistance in Mycobacterium tuberculosis from whole-genome sequence: the CRyPTIC dataset contains 12,289 isolates with both sequence data and quality-assessed phenotypic data across 13 antituberculosis drugs, the WHO mutation catalogue serves as a reference rule set, and the criterion is sensitivity, specificity and error rates reported per drug.
- Build with priority: re-testing a published host-response marker in an independent cohort. An example is transcriptomic signatures that separate bacterial from viral infection: several signatures have a clearly lower AUROC in external cohorts than in the derivation cohort, and the expression data needed for the re-test is mostly public.
- Defer: tasks scored only on an estimate of vaccine effectiveness for a new season or a new variant. A test-negative design estimate needs individual-level surveillance data, which usually may not be redistributed, and the estimate itself cannot be observed again within six hours. For such questions, discuss with the expert a reformulation as a reanalysis of public trial or cohort data under an analysis plan fixed in advance, or as a quantification of the bias from depletion of susceptibles and from differential healthcare seeking under a model fixed in advance.
- Defer: questions about increasing the transmissibility, virulence, host range or immune escape of a pathogen. These touch biosafety-sensitive content and are not built.

## Matters to confirm in conversation

- The pathogen and the unit of analysis: species, the typing scheme and its version (lineage nomenclature, sequence type, clonal complex), and whether that scheme was redefined during the period the task covers.
- Where the sequence data comes from and under what terms: an open database such as GenBank, or a registered-access database such as GISAID; the latter cannot be redistributed with a task package.
- What the reference call rests on: phenotypic susceptibility testing, a manually designated lineage, or the output of another tool; its own error, and the standard and version of the breakpoints used (EUCAST, CLSI).
- Quality thresholds for the sequence data: coverage depth, genome completeness, how mixed samples and contamination are handled, and the rule for excluding low-quality sequences.
- Sampling bias: how representative the surveillance sequences are across regions, time and populations, and how far the conclusion depends on that bias.
- The definition of the immunological quantities: the units and the standard used for antibody titers, the stimulation protocol for cellular readouts, and where the protective threshold comes from (a hemagglutination inhibition titer of 1:40 is generally taken to correspond to about 50% protection, a figure from volunteer challenge studies that does not hold for every strain and population).
- The design of vaccine tasks: the definition of the control group, the outcome and what triggers testing, the covariates adjusted for, and the difference between efficacy and real-world effectiveness.
- The form of the conclusion: a typing label, a resistant/susceptible dichotomy, a quantitative value (MIC, titer, coverage) or a mechanistic explanation; what the tolerance rests on.

## Checking templates

The templates below add to the general templates in `references/disciplines/medicine.md`.

| Template | Criterion | Scope |
|---|---|---|
| Lineage calls re-checked on a time-based held-out set | With the tool version and reference tree fixed in the task statement, the agent judge calls lineages again on genomes submitted to public databases after the cutoff date and compares with the submitted labels, reporting the agreement rate and the fraction left uncalled | Uses existing data, scientific discovery level 1–2 |
| Resistance phenotype from genotype | Compared with matched phenotypic susceptibility results: sensitivity, specificity and major error rate computed per drug | Uses existing data, scientific discovery level 2 |
| Re-application of a variant catalogue | With a mutation catalogue fixed in advance, the agent judge annotates the submitted variant list again and checks that the resistance call follows directly from that catalogue, rather than from the values the submitter reports | Pure computation, must pass |
| Recomputation of conservation and population coverage | With the sequence set, identity threshold and allele frequency table fixed, the agent judge recomputes the conservation of the epitope regions and the predicted population coverage and compares them with the submitted values | Pure computation |
| Re-test of a marker in an independent cohort | A marker set and thresholds fixed in advance are recomputed in another cohort for AUROC and calibration, and the drop is judged against the range declared in advance | Uses existing data, scientific discovery level 2–3 |
| Re-estimation of an epidemiological quantity | Given the data and an analysis plan specified in advance, the agent judge re-estimates the effectiveness, titer ratio or waning rate and compares point estimates and confidence intervals | Uses existing data |
| Ablation: recomputation after removing a component | A component the submission declares necessary is removed from the epitope set or the marker set, the coverage or discrimination is recomputed, and the drop must reach the amount the submitter declared | Pure computation, counts for part of the score |

## Sources of existing data

- Pathogen sequences: GenBank and NCBI Virus, ENA and the SRA, openly accessible with no restriction on redistribution; databases such as GISAID EpiCoV require registration and acceptance of terms of use, their data may not be distributed outside the registered community, and so it cannot be supplied with a task package, leaving only search criteria to be given in the task statement.
- Matched genotype and phenotype: the CRyPTIC Mycobacterium tuberculosis dataset (whole-genome sequences with MICs for 13 drugs); the genotype-phenotype and genotype-treatment datasets of the Stanford HIV Drug Resistance Database, both publicly downloadable; NCBI Pathogen Detection and BV-BRC.
- Resistance references: the WHO catalogue of mutations in Mycobacterium tuberculosis; the databases of CARD, ResFinder and AMRFinderPlus. Such a catalogue is itself the decision rule, so when its output is the reference call the task is pure computation, not existing data.
- Immunology: IEDB (epitopes, their hosts and MHC restriction) and its analysis tools; the Allele Frequency Net Database (HLA allele frequencies).
- Host response: expression data from public infection cohorts in GEO and ArrayExpress; clinical data on severity is mostly in controlled databases such as MIMIC-IV and needs a separate application.

## Preventing answer leakage

- Sequences in public databases mostly carry lineage labels and resistance annotations already, so a direct comparison of labels can be passed by downloading them. Make the recomputed call the object of scoring, and split by time: sequences submitted after the cutoff date have no label when the task is built.
- Typing tools and resistance catalogues change their calls between versions. The task statement fixes the tool and database versions; the reference call is produced with those versions and kept only in `tests/`.
- Isolates from the same outbreak have nearly identical sequences, so a random split makes the visible part and the held-out part near-duplicates. Split by outbreak, by sampling site or by time, and state what the split rests on.
- Effectiveness estimates, AUROCs and marker lists from published studies can be found by searching. The task statement contains no study names, registration numbers or database entry IDs, and asks for quantities the paper did not report (stratified estimates, recomputed calibration, the change after a component is removed).
- The training data of epitope prediction tools often includes the known epitopes in IEDB. When a prediction is used as evidence, the submission must show that the held-out set does not overlap that training data.

## Tools and compute

- Alignment and phylogenetics: MAFFT, IQ-TREE, TreeTime, Augur, and Nextclade and pangolin, all open source.
- Resistance and typing: AMRFinderPlus, ResFinder, the RGI of CARD, TB-Profiler, Mykrobe; hAMRonization collects the output of different tools into one format.
- Immunoinformatics: the IEDB analysis tools (epitope conservancy analysis, population coverage calculation); NetMHCpan and NetMHCIIpan offer downloads to academic users, other uses require contacting the developers; MHCflurry is open source.
- Statistics and epidemiology: R (survival, lme4) and Python (statsmodels, lifelines); test-negative design effectiveness estimates are implemented as logistic regression.
- Compute: sequence analysis and immunoinformatics run mainly on CPUs, aligning and building a tree from tens of thousands of genomes is on the order of hours, and a population coverage calculation takes minutes; the recomputation during review is usually far smaller than solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- A list of resistance genes from a tool taken directly as a resistance phenotype. Gene lists differ greatly between detection tools, with pairwise Jaccard overlap reported as low as 16%.
- Resistance called from the presence or absence of a gene, ignoring expression level, copy number and promoter variants, and ignoring the standard and version of the breakpoints used.
- Tools and modes for lineage calling mixed together. The UShER and pangoLEARN modes of pangolin give different results, and the reference dataset changes between versions, so a result without a stated version cannot be reproduced.
- The composition of surveillance sequences taken as the composition of the real epidemic. Which samples get sequenced depends on testing policy and on referral preferences.
- Predicted MHC binding equated with immunogenicity, or a computed population coverage written as a measured response rate in recipients.
- Isolates from the same outbreak or the same hospital used as external validation, where near-duplication inflates the metrics.
- Bias from depletion of susceptibles and from differential healthcare seeking left in a vaccine effectiveness estimate, and a declining estimate read directly as waning immunity.
- No limit placed on when the host-response sample was drawn. The discrimination of the same marker differs markedly with the time window after admission.
- A tolerance set tighter than the error of the reference call itself. Phenotypic susceptibility testing ordinarily allows a difference of one doubling dilution between repeat measurements.

## Example: a conserved T-cell epitope set for a pan-strain vaccine

The north-star problem is whether a single, non-personalized vaccine formulation can protect a population spanning all major HLA supertypes against future variants not included in the design. It counts as solved when, in a pre-registered human challenge trial or prospective efficacy study, more than 90% of recipients mount an immune response above the protective threshold and statistically significant protection is shown against strains excluded from the design. That judgement needs a new human trial, far longer than six hours, and cannot be made here. What can be built is the sub-problem upstream of it: the selection of conserved T-cell epitope regions and the computation of population coverage. A 2025 paper in Cell mapped conserved T-cell epitope regions of SARS-CoV-2 that make up 12% of the complete proteome, and showed that including regions outside the spike protein raises cross-reactivity across strains and HLA coverage. Population coverage can be computed in silico, whereas clinical protection against strains not yet seen remains unproven; that divide is the boundary of this task.

The following is illustrated for the Design class; the class is assigned by the expert. Scientific discovery level 3, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives the cutoff date, the search criteria for the sequence set (genomes in public databases dated before the cutoff), fixed versions of the conservancy analysis and population coverage tools, a fixed allele frequency table and HLA supertype grouping, and an upper bound on the total length of the epitope regions; it provides no published region list and no coverage values. The deliverables are the list of epitope regions (protein, start and end positions, sequence), a `results.json` with the result for each condition, the results of the ablation, and a short report. The format of the list and of `results.json` is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Conservation: on the sequence set dated before the cutoff, compute the conservation of each candidate region at the fixed identity threshold and give the selected regions.
  2. Coverage: with the fixed allele frequency table, compute the predicted population coverage of the set, the average number of hits and PC90, and give the coverage of each HLA supertype separately.
  3. Trade-offs under the length budget: within the upper bound on total length, state which regions are kept and which are dropped to reach the coverage.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the condition (the conservation threshold, the floor on coverage per supertype, the upper bound on total length). The deliverable is the candidate with its design rationale, as computation (the computed result for the candidate under the condition; the coverage recomputed after the group of regions that supplies it is removed, which is the ablation of the Design class) and as text (which group of regions supplies the coverage). The agent judge recomputes independently with the fixed tools and does not use the values the submitter reports. Whether the regions outside the spike protein are necessary is decided by that ablation.
- **Checks.** The agent judge recomputes conservation and population coverage and compares them with the submitted values; items that disagree score nothing. It then recomputes conservation on sequences submitted to public databases after the cutoff date, and the drop must not exceed the limit stated in the task statement. The coverage of every HLA supertype and PC90 must exceed their floors. In the ablation, removing a region declared necessary must reduce the coverage by the amount the submitter declared. A search of IEDB confirms that the set is not a copy of a published list. The tolerances are set from the numerical differences between tool versions and from the spread observed when the sequence set is resampled.
- **Calibration cases.** The empty submission (score 0); taking the whole proteome to maximize coverage (a shortcut, violating the upper bound on total length); copying a published list of conserved regions without recomputing (a known result, with the expected score set by the expert); taking only spike regions (a baseline, partially correct).
- **What passing does not show.** The checks show only that the selected regions are conserved in the sequences available and are predicted, from allele frequencies, to be presented across the HLA supertypes. Predicted MHC binding is not measured immunogenicity, and coverage computed from allele frequencies is not a measured response rate in recipients; neither shows clinical protection against a strain excluded from the design. That part has to be decided by a human challenge trial or a prospective efficacy study, and is judged by the expert.
