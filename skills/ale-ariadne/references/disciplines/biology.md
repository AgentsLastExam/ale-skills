# Biology

## Subdomains

The directions of biology differ widely in their objects of study, types of data and ways of verification. This file gives what is common to all of them. Once the expert has described the research problem, pick the subdomain file from the table below and read it as well; the files are in `references/disciplines/biology/`. A subdomain file only adds what is specific to that direction (screening examples, checking templates, data sources, tools, pitfalls and a worked example); it does not alter the provisions of this file. When a problem spans two subdomains, read both files; when it is unclear where a problem belongs, ask the expert to say. Record the chosen subdomain under "Discipline" in the problem card.

| Subdomain | Scope | File |
|---|---|---|
| Molecular biophysics and structure | Protein folding and energy landscapes, experimental structure determination, molecular dynamics and free energy, protein engineering and de novo design, nucleic acid structure and dynamics | `molecular-biophysics.md` |
| Genomes and omics | Genome assembly and variant discovery, epigenome and chromatin state, transcriptome and splicing, proteome and post-translational state, metabolome and multi-omic integration | `genomics-omics.md` |
| Computational biology | Sequence alignment and search, phylogenetic inference, single-cell data analysis, networks and pathway modeling, machine learning models of biology | `computational-biology.md` |
| Bioengineering and synthetic biology | Genome editing tools, synthetic circuits and chassis, biomaterials and delivery, biosensors and imaging probes, directed evolution and screens | `bioengineering.md` |
| Microbiology and virology | Bacterial physiology and metabolism, resistance, phages and interbacterial conflict, virus replication and host interaction, microbiomes and communities, microbial genetics tools | `microbiology-virology.md` |
| Molecular and cell biology | Gene expression control, trafficking and organelles, cytoskeleton and cell mechanics, cell cycle, cell death and quality control, signal transduction | `cell-biology.md` |
| Immunology | Innate immunity and inflammation, lymphocyte development and repertoire, antigen recognition and structural immunology, mucosal and tissue immunity, mechanisms of immunotherapy | `immunology.md` |
| Cellular and circuit neuroscience | Synaptic transmission and plasticity, neuronal cell types and atlases, circuit recording and manipulation, neural development and wiring, glia and neuroimmune interaction | `cellular-neuroscience.md` |
| Development and tissue biology | Morphogenesis and patterning, stem cells and fate decisions, organoids and in vitro development, regeneration and repair, evolution of development | `developmental-biology.md` |
| Systems and behavioral neuroscience | Sensory coding, motor control, learning, memory and decision, whole-brain imaging and connectivity, computational models of brain function | `systems-neuroscience.md` |
| Physiology and disease mechanism | Organ system physiology, metabolism and energy balance, circadian rhythm and homeostasis, mechanisms of pharmacology and toxicology, animal and cellular disease models | `physiology.md` |
| Plant biology | Photosynthesis and carbon metabolism, plant development and hormones, plant immunity and stress response, crop genetics and improvement, roots, rhizosphere and symbiosis | `plant-biology.md` |
| Evolution and ecology | Population genetics and selection, phylogenomics and comparative genomics, species interaction and community ecology, behavior and cognitive ecology, paleobiology and deep time | `evolution-ecology.md` |

For problems whose object is patients, clinical data or care, see `references/disciplines/medicine.md`; for problems that are mainly the chemistry of small molecules, enzyme catalysis or drug molecules, see `references/disciplines/chemistry.md`.

## Screening criteria

- Build with priority: questions that can be answered with public data and verified with held-out data or an independent dataset (prediction, inference, reanalysis).
- Build with priority: conclusions that come down to a statistic or a prediction metric.
- Defer: conclusions that can only be confirmed by a new experiment taking more than six hours (physical-world observation level 3); findings that appear in a single dataset with no independent validation set; work that needs controlled-access human data without a compliant route to it; anything touching biosafety-sensitive content.

## Matters to confirm in conversation

- Whether the question is prediction, inference or mechanistic explanation, and which statistic expresses the conclusion.
- The accession and version of the dataset, and which version of the reference genome and annotation is used.
- Whether there is an independent cohort or a held-out part for validation, and how it relates to the data used for discovery (same batch, same lab, homologous sequences).
- Which batch effects and confounders exist, and what the standard way of handling them is.
- Which baseline methods and metrics the field accepts.
- How large an effect has to be to matter biologically, beyond statistical significance.
- Whether the data carries privacy or data use restrictions.

## Checking templates

Most templates below are implemented as numerical-check scripts that the agent judge calls; where the conclusion can be written as a Lean statement in advance, the agent judge checks it with the Lean tool; derivations, explanations and arguments are reviewed by the agent judge directly against the rubric. See `references/agent-judge.md`.

| Template | Criterion | Scope |
|---|---|---|
| Comparison with the result of a standard pipeline | Given the data and versions, the agreement or overlap of the result (variants, differentially expressed genes, clusters) with the reference pipeline | Uses existing data, scientific discovery level 1–2 |
| Prediction on held-out data | Metrics computed on a hidden held-out set (AUROC, correlation, RMSD, lDDT) | Uses existing data, scientific discovery level 2–3 |
| Replication in an independent cohort | A conclusion drawn on the discovery set (a gene set, an association, a marker) is re-tested on an independent dataset with a statistical test fixed in advance | Uses existing data, scientific discovery level 3 |
| Comparison with structures | A predicted structure or complex is compared with an experimental structure released only after the cutoff date | Uses existing data, scientific discovery level 2–3 |
| Statistical validity check | Multiple-testing correction was done; effect sizes and confidence intervals are reported; a negative control with shuffled labels is not significant | Must pass |
| Recovery of known answers | The analysis recovers known positive controls (known pathways, known binding sites) | Counts for part of the score |
| Model recomputation | Given a model (a kinetic model, molecular dynamics, a population genetics simulation), the agent judge reruns it and checks the submitted parameters or conclusions | Pure computation |
| Agent judge reviews against a rubric | Used when the result is an explanation or argument; every claim must point to an analysis result that can be recomputed | Scientific discovery level 3 |

## Sources of existing data

- Transcriptomics and sequencing: GEO, SRA/ENA, ArrayExpress, ENCODE, and the open tiers of GTEx and TCGA.
- Single cell: Human Cell Atlas, CELLxGENE.
- Proteins and structures: UniProt, PDB, AlphaFold DB, prediction targets from CASP and CAMEO, ProteinGym (mutation effects).
- Genetics and function: ClinVar, gnomAD, DepMap. UK Biobank is controlled-access and needs an application.
- Proteomics, metabolomics and models: PRIDE, MetaboLights, BioModels.

## Preventing answer leakage

- Sequences are homologous, so they cannot be split at random. Cluster by sequence similarity first, then split by cluster.
- Split by time: use PDB release dates, or newly deposited datasets.
- The conclusions and supplementary tables of the original paper can be found by searching. Hide the dataset accession, or ask for a quantity the original paper did not report.
- Samples from the same patient or donor cannot appear in both the discovery set and the held-out set.
- Labels of the held-out set stay in the agent judge only and never enter the solving agent's environment.

## Tools and compute

- Transcriptomics and single cell: DESeq2, edgeR, limma, Scanpy, Seurat.
- Sequencing data processing: STAR, salmon, samtools, bcftools, GATK.
- Sequence and structure: BLAST, MMseqs2, HMMER, AlphaFold, ColabFold, ESM.
- Simulation and genetics: GROMACS, OpenMM, PLINK.
- Workflow management: Snakemake, Nextflow.
- Compute: raw sequencing data runs to tens or hundreds of GB for a single dataset, and alignment is heavy on memory and storage, so give processed count matrices instead of raw data whenever possible; structure prediction and protein language models need GPUs; the sequence databases used for structure prediction are very large and must be placed in the environment offline.

## Common pitfalls

- Batch effects mistaken for biological signal.
- No multiple-testing correction, or switching analysis methods repeatedly until something is significant.
- Data leakage from homologous sequences or a shared donor, inflating prediction metrics.
- Mismatched versions of the reference genome or annotation, so results do not line up.
- The standard pipeline is itself not unique; "agrees with the reference pipeline" is not the same as correct.
- A held-out set that is too small, so the metric is noisy and cannot separate good from bad.
