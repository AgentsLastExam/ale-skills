# Biology: genomes and omics

This file adds content specific to genomes and omics to `references/disciplines/biology.md`, whose provisions still apply.

Scope: genome assembly and variant discovery (long-read assembly, pangenomes, structural variants and repeat regions, population-scale genome resources), the epigenome and chromatin state (methylation, accessibility, three-dimensional organization), the transcriptome and alternative splicing, the proteome and post-translational modifications, and the metabolome and multi-omic integration. For the development and benchmarking of analysis methods and models themselves see `computational-biology.md`; for molecular structure, simulation and design see `molecular-biophysics.md`; for questions particular to microbial and viral genomes see `microbiology-virology.md`; for the clinical interpretation of human cohort data see `references/disciplines/medicine.md`.

## Screening criteria

- Build with priority: detection problems with a public truth set and an accepted benchmarking standard, for example calling small variants in difficult regions. The GIAB benchmarks, the GA4GH comparison tools and the stratification region files form a mature evaluation workflow, with metrics reported by region stratum and not only as a genome-wide average.
- Build with priority: reanalyses whose conclusion can be re-tested on an independent dataset, for example a set of differentially expressed genes or differentially methylated regions under a treatment, re-tested on data from another batch and another platform with a statistical test fixed in advance.
- Defer: site maps that rest on a single antibody-based experiment, for example RNA modification sites from an immunoprecipitation assay, which cannot serve as true values without confirmation by a method based on a different principle. Such questions can be restated to use only sites supported by both methods, or to ask for a ranking of sites.
- Defer: work that needs controlled-access human data without a compliant route to it, or data whose use agreement does not allow it to be placed in a task package.
- Defer: anything touching biosafety-sensitive content.

## Matters to confirm in conversation

- Whether the raw data (read files, raw mass spectrometry files) can be distributed with the task package, and in what processed form the controlled-access part is replaced.
- The measurement platform, read length, depth, library type (single-end or paired-end, strandedness, whether UMIs are present) and how duplicates are removed.
- The composition of the reference sequence: whether alt contigs, decoys and masked regions are included, and the source of the annotation for non-human species such as Arabidopsis and mouse.
- The source and coverage of the true values: how the benchmark regions are drawn, how calls outside them are handled, and the version of the stratification region files.
- The kind of replicates in the experimental design (biological or technical), the batches and covariates, and the standard treatment of confounding in this area.
- The normalization and units of quantification (counts, TPM, LFQ, peak area), and whether a log transform is applied.
- The confidence standards for identification and quantification: filtering thresholds for variants, FDR for peptides and proteins, MSI confidence levels for metabolites.
- The form of the conclusion and the tolerance: an absolute metric, an improvement over a baseline, or stratified metrics; where the tolerance comes from.

## Checking templates

The templates below add to the general templates in `references/disciplines/biology.md`.

| Template | Criterion | Scope |
|---|---|---|
| Standard-conforming comparison with the truth set | The submitted variants are first normalized (left-aligned, multiallelic sites decomposed), then compared with the truth set by haplotype, restricted to the benchmark regions, with precision, recall and F1 given separately for each region stratum | Uses existing data, scientific discovery level 1–2 |
| Read-level support | The agent judge returns to the alignment file and checks each claimed site: allele depth, strand balance and mapping quality; a site with no read support scores nothing | Uses existing data, must pass |
| Pedigree consistency | For trio data: the Mendelian inconsistency rate and the number of de novo variants are of the usual order for data of this kind, and the phasing is compatible with the parental haplotypes | Must pass |
| Reanalysis for confounding and batch | The agent judge refits the model with batch and the known covariates included, and the reported effect keeps its direction and magnitude; when batch is completely confounded with the treatment condition, the conclusion scores nothing | Uses existing data, must pass |
| Agreement between orthogonal methods | The conclusion is supported jointly by methods based on different principles: long reads and short reads, DIA and DDA, a metabolite identified at MSI level 1 against an authentic standard | Uses existing data, counts for part of the score |
| Reproducibility of the workflow | The submitted workflow is rerun from the given data to the reported tables, with the software versions, reference sequence and annotation version all pinned, and the values reproduce | Uses existing data, must pass |

## Sources of existing data

- Benchmarks and true values: the GIAB small-variant benchmarks (v4.2.1 for HG002 covers about 92% of the GRCh38 autosomes), the benchmark covering 273 challenging medically relevant genes, and the newer benchmark built on a complete assembly; the GA4GH stratification region files and comparison tools; precisionFDA provides a public evaluation platform.
- Population variation and annotation: gnomAD, the 1000 Genomes Project, dbSNP, ClinVar.
- Functional genomics: ENCODE, Roadmap Epigenomics, 4D Nucleome, and the open tiers of GTEx and TCGA; the controlled tiers need an application through dbGaP or EGA and, once granted, still cannot be distributed with a task package.
- Proteomics and metabolomics: PRIDE and MassIVE (deposited through ProteomeXchange), MetaboLights and Metabolomics Workbench; raw mass spectrometry files are large, so usually only processed matrices are provided.
- When the output of a pipeline (for example the calls of one calling pipeline) serves as the reference values, those values are themselves computed, so the task counts as pure computation and pipeline reproduction, not as using existing data.

## Preventing answer leakage

- The truth files and region files of the public benchmarks can be downloaded directly: the solving environment has no network access, and the sample ID, the read groups and any identifiers in file names are removed.
- Hold out the regions newly added in the latest version of a benchmark, or use a sample whose true values are not yet public.
- Some checks do not depend on the truth set: read-level support, pedigree consistency and agreement between orthogonal methods cannot be passed by searching.
- The task statement contains no GEO, SRA or dbGaP accessions and no paper titles; it can ask for quantities the original paper did not report, such as stratified metrics and the fraction of sites that cannot be decided.
- Controlled-access data must not be placed in a task package; where needed, switch to public samples, or provide only summary statistics from which no individual can be recovered.

## Tools and compute

- Alignment, assembly and variant calling: BWA-MEM, minimap2, DeepVariant, hifiasm, Flye, verkko, bedtools.
- Benchmarking: hap.py and vcfeval (comparison by haplotype), truvari (structural variants), the GA4GH stratification region files.
- Epigenome and three-dimensional genome: MACS, deepTools, Bismark (methylation), cooler and HiCExplorer (contact matrices).
- Proteomics and metabolomics: MaxQuant (free but closed source), FragPipe and MSFragger (free for academic use, with a separate license for commercial use), Skyline, OpenMS, XCMS, MZmine.
- Compute: one set of 30× whole-genome reads is tens of GB, and one complete run from reads to variants takes on the order of hours on a multi-core machine; tasks usually restrict the data to a few chromosomes or regions to keep the volume under control. Running the comparison tool during review takes only minutes, whereas rerunning the whole workflow is on the same scale as solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Submitted variants not normalized, so that one variant is counted in the comparison as both a false positive and a false negative.
- A genome-wide average F1 hiding the performance in difficult regions: metrics in homopolymers, short tandem repeats and segmental duplications are far below the average.
- A truth set covering only part of the genome, so that calls outside the regions count neither as right nor as wrong; a change of benchmark version changes the coverage and with it the metrics.
- Duplicate reads, index hopping and amplification bias left untreated, distorting the evidence for low-frequency alleles.
- Ambient RNA and doublets not removed from single-cell data, so that a supposed rare cell type is in fact a mixed signal.
- Sequencing depth or sample quality confounded with the groups, so that the difference between groups comes from the libraries and not from biology.
- Sites from an antibody-based experiment, which depend on the specificity of the antibody, taken as true values without confirmation by an orthogonal method.
- After controlling the FDR at 1% by target-decoy in mass spectrometry, proteins supported by a single peptide still treated as reliable identifications; metabolites treated as established compounds with no MSI confidence level stated.

## Example: calling diploid small variants in difficult regions

Variant calling in the homopolymers, short tandem repeats and segmental duplications of the human genome is still unreliable. The GIAB small-variant benchmark v4.2.1 for HG002 covers about 92% of the GRCh38 autosomes, and the part it does not cover consists of exactly these regions; a separate benchmark covers 273 medically relevant genes that earlier benchmarks covered poorly. The GA4GH benchmarking standard requires the submitted variants to be normalized and compared by haplotype (hap.py and vcfeval), and the metrics to be reported separately for each region stratum, because agreement inside and outside the high-confidence regions differs greatly. The task provides de-identified alignment data and asks for diploid genotypes in specified difficult regions.

The following is illustrated for the Inversion class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives alignment files with the sample identifiers removed (restricted to a few chromosomes and regions to keep the volume under control), the versions of the reference sequence and annotation, and the file of regions to be answered; it gives no truth files and no benchmark version, and the solving environment has no network access. The deliverables are a normalized variant file (with genotypes, allele depths and quality values), a list of sites explicitly marked as undecidable, and a short report. The format of the variant file and of the list is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Insertions and deletions in homopolymers and short tandem repeats: give the genotype and length, with the read evidence they rest on.
  2. Substitutions in segmental duplications and paralogous regions: distinguish real variants from mismatches caused by paralogous sequence.
  3. Local phasing and pedigree relations: give the local haplotypes, and state whether the result is compatible with the Mendelian relations of the trio.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the observed data the sub-question concerns. The deliverable is the reconstructed part, as computation (reads regenerated from the proposed diploid haplotypes and aligned, compared with the observed pileup, with residuals at the level of sequencing noise; correct reconstruction also on a phantom generated by simulating reads from known haplotypes) and as text (the features relied on in the read pileup of the region, allele depths, strand balance and the distribution of mapping quality; an argument for which sites cannot be determined uniquely at the given read length and depth, with these marked as undecidable and not guessed). The physical constraints (the diploid constraint and consistent phasing, the Mendelian relations) are checked by the agent judge.
- **Checks.** The agent judge first checks that the submitted variants are normalized, then compares them with the truth set by haplotype, restricted to the benchmark regions, with precision, recall and F1 given separately for each region stratum; it returns to the alignment file for each claimed variant and checks the read support, and a variant with no support scores nothing; it checks whether the Mendelian inconsistency rate and the number of de novo variants are of the usual order; recall on the phantom data must reach a floor set in advance. The floor for the metrics of each region stratum is set from measurements on the baseline pipeline in step 2, and the genome-wide average is not used.
- **Tiers and scoring.** Homopolymers and short tandem repeats form the first tier, segmental duplications the second, and phasing and pedigree consistency the third; correct marking of undecidable sites is scored separately, so that answering "undecidable" is better than guessing. The weights are set by the expert; for illustration: normalization and read support 10, first tier 30, second tier 25, third tier 20, marking of undecidable sites 10, report 5.
- **Calibration cases.** The empty submission (score 0); the truth file of the public benchmark submitted directly (a shortcut, prevented by the absence of network access and of identifiers, and scoring nothing if it occurs); a submission marking every site as undecidable (zero recall, score 0); a submission correct only in easy regions and level with the baseline in difficult regions (partially correct); the calls of the baseline pipeline (a baseline).
