# Medicine: precision medicine and clinical genomics

This file adds content specific to precision medicine and clinical genomics to `references/disciplines/medicine.md`, whose provisions still apply.

Scope: clinical variant interpretation (classification frameworks and evidence codes, functional assays for variants of uncertain significance, periodic reanalysis and reclassification), diagnostic sequencing (exome and genome diagnosis in rare disease, transcriptome-assisted diagnosis), pharmacogenomics and genotype-guided prescribing, the construction and portability of polygenic risk scores, population genomic screening, and cancer genomics and targeted therapy (tumor profiling and actionability, acquired resistance and clonal evolution). For basic genomics, the molecular mechanism of variants and population-genetic methods see `references/disciplines/biology.md`; for pharmacokinetics, dosing regimens and the evaluation of drug efficacy see `therapeutics-pharmacology.md`.

## Screening criteria

- Build with priority: variant classification questions judged against a public framework and an authoritative classification held out by time. An example is classifying missense variants in a gene for which a ClinGen expert panel has published gene-specific specifications: the ACMG/AMP framework, the points-based scoring and the calibrated thresholds for computational evidence are all public, and ClinVar releases on the first Thursday of each month with all past releases retained, so the data can be split at a cutoff date.
- Build with priority: conclusions that come down to a metric defined in advance that can be recomputed independently. An example is the portability of a polygenic risk score across ancestries: GWAS summary statistics, the scoring files of the PGS Catalog and the 1000 Genomes reference panel are all public, and the criterion is the R² or AUROC in each population and how it changes with genetic distance; one study across 84 traits reports a correlation of −0.95 between genetic distance and score accuracy.
- Build with priority: genotype calling judged against consensus reference samples. An example is calling star alleles and metabolizer phenotypes in pharmacogenomics: GeT-RM gives consensus genotypes for 28 pharmacogenes in 137 samples, tools such as PharmCAT are open source, and the criterion is the agreement rate reported per gene.
- Defer: tasks that rest only on controlled-access individual-level genotype data, such as training and validating a score on UK Biobank or All of Us individual data. Such data may not be redistributed with a task package. For such questions, discuss with the expert a reformulation built on public summary statistics and public reference panels, or one in which the expert does the computation locally and the task scores only a derived quantity that may be published.
- Defer: tasks scored only on a patient's actual diagnosis or treatment response, for example whether an actionability call from tumor profiling improves outcomes. That judgement requires following up a new patient cohort, far longer than six hours.

## Matters to confirm in conversation

- Whether the gene-disease relationship holds and which version of the validity assessment is used, and which phenotype and inheritance pattern the classification applies to.
- The classification framework used, the version of the gene-specific specifications, and the strength adjustments applied to each evidence code in that gene.
- The prediction tool, version and calibrated thresholds used for computational evidence; whether the tool is fixed in advance and whether only one is used per gene.
- The source and version of the population frequency data, which populations are used, and the threshold on the filtering allele frequency.
- The source and strength of functional evidence: whether the assay was calibrated against control variants, and how the strength was derived.
- The source and timing of the truth: an expert panel classification, family co-segregation, a functional assay or follow-up outcome; when it was published relative to the task's cutoff date.
- The form of the conclusion: a five-tier classification, a point total, an actionability tier or a risk stratum; what the tolerance rests on (disagreement between laboratories, variation between repeat reviews).
- Whether the data use agreement allows putting genotype data into a task package, and in what form controlled data may serve as a reference without being redistributed.

## Checking templates

The templates below add to the general templates in `references/disciplines/medicine.md`.

| Template | Criterion | Scope |
|---|---|---|
| Classification re-derived from the evidence codes | From the submitted list of evidence codes, the agent judge recomputes the point total and the tier under the scoring rule fixed in advance: the tier must follow directly from the set of codes and must agree with the tier the submitter reports | Pure computation, must pass |
| Recomputation of frequency codes | With the population frequency database version fixed in the task statement, the agent judge recomputes the filtering allele frequency and checks how the frequency codes were applied | Pure computation, must pass |
| Comparison with an authoritative classification held out by time | Compared with the expert panel classifications published after the cutoff date: the agreement rate, the fraction left as uncertain significance, and the number of opposite calls between pathogenic and benign | Uses existing data, scientific discovery level 2 |
| Comparison with consensus reference samples | Star allele and metabolizer phenotype calls compared with the consensus genotypes of the reference samples, with the agreement rate reported per gene | Uses existing data, scientific discovery level 1 |
| Recomputation of a score in a held-out population | With the submitted weight file, the agent judge recomputes the score in held-out reference individuals and checks its distribution, its relation to ancestry components and its discrimination | Uses existing data |
| Comparison with a variant-calling benchmark | Compared with the Genome in a Bottle benchmark set and its confidence regions: recall, precision and F1, reported separately for difficult-to-map regions | Uses existing data, scientific discovery level 1 |
| Sensitivity analysis | After the thresholds, the population frequency version or the reference panel are changed, the conclusion moves no more than the submitter declared | Pure computation, counts for part of the score |

## Sources of existing data

- Variant classification: ClinVar, public, released monthly with all past releases retained, so it can be split by date; the gene-disease validity assessments of ClinGen and the gene-specific specifications of its expert panels.
- Population frequency: gnomAD, publicly downloadable; its v4 contains 730,947 exomes and 76,215 genomes.
- Functional assays: MaveDB collects data from multiplexed assays of variant effect, and its 2024 version holds over seven million variant effect measurements; when used as evidence, the strength must be calibrated against control variants (OddsPath).
- Benchmarks and challenges: the reference samples and benchmark sets of Genome in a Bottle; the precisionFDA Truth Challenge; the blinded competitions of CAGI, one challenge of whose sixth round used 219 experimentally assayed missense variants of uncertain significance as the held-out set.
- Pharmacogenomics: PharmVar (star allele definitions), CPIC and PharmGKB (genotype to phenotype and prescribing recommendations), and the consensus genotypes of GeT-RM.
- Oncology and polygenic scores: AACR Project GENIE requires registration and acceptance of terms of access and may not be redistributed without written permission; OncoKB is free for academic research, while commercial and clinical use requires a license; the PGS Catalog and the GWAS Catalog are public, and some scores carry their own license terms.

## Preventing answer leakage

- ClinVar, expert panel classifications and published reclassifications can be downloaded directly. Split at a cutoff date: the held-out set contains only variants that first received an authoritative classification, or were reclassified, after the cutoff, and the task statement and solving environment contain only a database snapshot dated before it.
- Literature and database entries cited in a submission must predate the cutoff date. The agent judge checks the submission and the solving trajectory for evidence dated after it.
- Several prediction tools were trained on historical ClinVar classifications, so a held-out variant may already be in their training set. The task statement fixes the tool and version and asks for that tool's performance on the held-out set, not only for the final classification.
- Variants in the same gene, the same family and the same functional assay are highly correlated. Split by gene or by assay so that held-out variants and visible variants do not come from the same source.
- Controlled-access individual-level genotypes may not be put into a task package. Use public summary statistics, public reference panels and simulated genotypes instead, or have the expert compute locally and supply only a derived quantity that may be published.
- The task statement contains no database entry IDs for variants, no sample IDs and no study names.

## Tools and compute

- Variant annotation and interpretation: VEP, ANNOVAR, SnpEff; Exomiser and the HPO for phenotype-driven ranking of candidate genes.
- Variant calling and benchmark comparison: GATK, DeepVariant, bcftools; hap.py and RTG vcfeval for comparison with a benchmark set.
- Pharmacogenomics: PharmCAT is open source; genes with structural variation such as CYP2D6 need dedicated star allele callers.
- Polygenic scores: PLINK, PRS-CS, LDpred2, and pgsc_calc, the pipeline of the PGS Catalog.
- Compute: variant interpretation and score computation run mainly on CPUs, on the order of minutes to hours for the variant set of one gene; calling variants again from sequencing reads needs tens of GB of reference data and hours of computation, so review should take VCFs as input. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Evidence codes that are not independent, so evidence from one source is counted twice, for example as both a population frequency code and a computational evidence code.
- Uncalibrated prediction scores used, or several prediction tools mixed in one task with the most favorable one chosen.
- Frequency codes applied without distinguishing populations and without the filtering allele frequency, so a variant that is rare overall but common in one population is misjudged.
- The strength of a functional assay counted as strong evidence without calibration against control variants.
- The current ClinVar classification taken as the truth, when that classification may itself come from the pipeline under evaluation or postdate the cutoff.
- A polygenic score used across ancestries without recalibration. Its absolute values and thresholds drift with ancestry components, so the ranking may survive while the absolute risk does not.
- Within-sample quantiles of a score used in place of discrimination in an independent cohort.
- Germline and somatic evidence mixed in a tumor variant call. The classification framework for germline variants and the actionability tiers for somatic variants are not the same standard.
- A tolerance set tighter than the disagreement in the reference call itself. Laboratories are known to classify the same variant differently.

## Example: classification of missense variants held out by time

A large share of the missense variants reported by clinical sequencing are of uncertain significance. The ACMG/AMP framework of 2015 divides the evidence into codes and gives rules for combining them; the scoring proposed by Tavtigian and colleagues converts the strengths into points (very strong +8, strong +4, moderate +2, supporting +1, with benign evidence taking negative values), with pathogenic at 10 points or more, likely pathogenic at 6–9, uncertain significance at 0–5, likely benign at −1 to −6 and benign at −7 or below. On top of this, the ClinGen variant curation expert panels publish gene-specific specifications, the PTEN panel and the hearing loss panel being early examples, and their classifications enter ClinVar with three-star status. The strength of computational evidence has since been calibrated, and several tools reach more than supporting strength at given thresholds. ClinVar releases on the first Thursday of each month and retains all past releases, so the data can be split by date: variants that were still of uncertain significance at a chosen cutoff and later received an expert panel classification form the held-out set. The task asks the solving agent to classify these variants, with evidence codes, using only data and literature dated before the cutoff.

The following is illustrated for the Prediction class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement fixes the gene and phenotype, the version of the framework and of the gene-specific specifications, the single computational evidence tool and its threshold table, the version of the population frequency database, and the cutoff date; it provides a database snapshot dated before the cutoff and a variant list, with no classification labels. The deliverables are, for each variant, the list of evidence codes, the point total, the tier and the reasoning, collected in a `results.json` with a short report. That format is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Population frequency evidence: compute the filtering allele frequency with the fixed version of the frequency database and decide whether the benign frequency codes apply.
  2. Computational and functional evidence: give the strength of the computational evidence with the fixed tool and thresholds; for variants with data from a multiplexed assay of variant effect, enter functional evidence at the strength derived from calibration against control variants.
  3. Classification and uncertainty: derive the tier under the scoring rule, state which variants are left as uncertain significance for lack of evidence, and give the change in the conclusion when the strength of some codes is varied.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the target quantity as defined in the task statement; the true value is not provided to the solving agent. The deliverable is the prediction with its uncertainty, as text (the argument that the chosen codes, tool and thresholds apply to this gene) and as computation (the point total; the change in the conclusion when thresholds, the frequency database version and the strength of functional evidence vary, which is the sensitivity analysis of the Prediction class; the confidence stated for each variant). The comparison with the expert panel classifications published after the cutoff is made by the agent judge.
- **Checks.** The agent judge first re-derives the tier from the submitted set of codes under the fixed scoring rule; a variant whose tier disagrees with the one the submitter reports scores nothing. It then recomputes the frequency codes with the fixed version of the frequency database and the computational evidence with the fixed tool. It then compares with the held-out expert panel classifications, reporting the agreement rate, the fraction left as uncertain significance, and the number of opposite calls; a variant with an opposite call (submitted as pathogenic where the panel called it benign, or the reverse) scores 0. The tolerance is set from the known spread in how laboratories classify the same variant and from the panels' own record of reclassification.
- **Tiers and scoring.** Applying the frequency and computational evidence forms the first tier, calibrating and entering functional evidence the second, and the overall classification with its uncertainty the third; completing only the first tier earns the corresponding score. The weights are set by the expert; for illustration: reproducibility of code application 25, agreement with the held-out classifications 35, penalty for opposite calls 15, uncertainty and sensitivity analysis 15, report 10.
- **Calibration cases.** The empty submission (score 0); looking up the current ClinVar classification (a shortcut, caught by the cutoff date and the check on the dates of the evidence; those variants score nothing); calling every variant uncertain significance (partially correct, no opposite calls but a low agreement rate); the evidence codes published by the expert panel (a known result); the dichotomous call from a single prediction tool thresholded directly (a baseline).
