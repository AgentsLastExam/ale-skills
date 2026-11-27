# Biology: immunology

This file adds content specific to immunology to `references/disciplines/biology.md`, whose provisions still apply.

Scope: innate immunity and inflammation (pattern recognition and interferon, inflammasomes and pyroptosis, myeloid cell states and trained immunity); lymphocyte development and the receptor repertoire (V(D)J recombination and repertoire sequencing, T-cell differentiation and exhaustion, germinal centers and affinity maturation); antigen recognition and structural immunology (MHC presentation and epitope prediction, antibody structure and broad neutralization); mucosal and tissue immunity (tissue-resident memory); mechanisms of immunotherapy (response and resistance to checkpoint blockade, engineered T cells and CAR design). For variation and spread on the pathogen side see `microbiology-virology.md`; for signaling pathways and cell-state control inside immune cells see `cell-biology.md`; for structural computation on antibodies and TCRs see `molecular-biophysics.md`; for the processing pipelines of repertoire and single-cell data see `genomics-omics.md`; for clinical outcomes of immunotherapy and patient cohorts see `references/disciplines/medicine.md`.

## Screening criteria

- Build with priority: questions in antigen presentation and epitope prediction that come down to a metric on a held-out set, for example predicting from mass-spectrometry eluted-ligand data whether a peptide is presented by a given HLA molecule. The IEDB has run an automated benchmark of MHC class I binding prediction since 2014, using newly curated data as a blind test over peptides of length 8–11; the field judges methods by AUC, AUC0.1 and PPV and uses %rank as a common scale across alleles, so the workflow is mature and several methods exist to compare against.
- Build with priority: deconvolving the binding motifs of individual HLA molecules from multi-allelic immunopeptidome data. Mono-allelic cell-line data provide the true values, GibbsCluster, MixMHCp and NNAlign_MA form baselines, and a simulated mixture gives the true assignment of every peptide.
- Defer: generalization to unseen epitopes in TCR–epitope specificity prediction. In the IMMREP23 challenge 53 teams sent in 398 submissions, most methods were close to random on the subset of unseen epitopes, and the construction of the negative examples itself introduced bias. Discuss with the expert a formulation that fixes the epitope set and asks only for the ranking within seen epitopes, or that requires the submitter to state and ablate the construction of the negatives.
- Defer: conclusions that can be confirmed only by a new cell experiment, for example the effect of a change in CAR architecture on T-cell killing, or a new ligand for a pattern-recognition receptor. Such checks involve cell culture and a functional readout and cannot be completed within six hours (physical-world observation level 3).
- Defer: tasks whose purpose is to raise the immune escape of a pathogen; these touch biosafety-sensitive content. Immunology tasks are restricted to surveillance, diagnosis, prediction and basic mechanism, for example monitoring antigenic drift of already circulating strains from public sequences.

## Matters to confirm in conversation

- The nomenclature and resolution of the HLA or MHC alleles, and the version of the allele sequences used.
- The type of data: binding affinity, mass-spectrometry eluted ligands and T-cell recognition measure different steps and cannot be mixed; whether the negatives are experimental negatives or randomly generated.
- The range of peptide lengths and how the length distribution is handled; for class II, also how the core is aligned and the flanks treated.
- Metrics and thresholds: the definitions of AUC, AUC0.1 and PPV, and the %rank conventions (0.5% and 2% for class I, 2% and 10% for class II).
- The split: by epitope, by allele, by donor or by time; how homologous peptides and receptors with near-identical CDR3s are grouped.
- The identification pipeline for immunopeptidome data, its false discovery rate, and the fraction of contaminant peptides.
- How large an effect has to be to matter immunologically, for example the fraction of top-ranked peptides actually recognized by T cells.
- The data use agreement and ethics approval for human samples, and whether controlled data may be placed in the task package.

## Checking templates

The templates below add to the general templates in `references/disciplines/biology.md`.

| Template | Criterion | Scope |
|---|---|---|
| Presentation prediction on a held-out set of eluted ligands | AUC, AUC0.1 and PPV computed on eluted ligands curated after the cutoff date; PPV takes the top N predictions, with N the number of ligands times 0.95, to allow for mass-spectrometry contaminants | Uses existing data, scientific discovery level 2 |
| Motif deconvolution against true values | The position weight matrix of each recovered cluster is compared with the reference motif from mono-allelic data; on a simulated mixture, the fraction of peptides assigned to the right source is counted | Uses existing data |
| Consistency of the %rank scale | Submitted scores are converted to %rank against the same background of random natural peptides before positive rates are compared across alleles; raw scores are never compared across alleles | Must pass |
| Depth correction of repertoire metrics | Conclusions about diversity or clonal expansion still hold after resampling to the same sequencing depth; the clonotype definition and the V/J annotation version are the same across samples | Uses existing data, must pass |
| Ablation of the negative set | Metrics are recomputed after changing how the negatives are built (random natural peptides, receptors from other epitopes, peptides matched on source-protein abundance), and the direction of the conclusion is unchanged | Uses existing data, counts for part of the score |
| Comparison with structures in immunology | A predicted pMHC or antibody–antigen complex is compared with an experimental structure released only after the cutoff date, on the set of interface contact residues | Uses existing data, scientific discovery level 2–3 |

## Sources of existing data

- Epitopes and presentation: IEDB, public, holding binding, eluted-ligand and T-cell recognition records, and running the automated benchmark of MHC class I binding prediction; the MHC Motif Atlas collects 1,013,733 ligands covering 135 class I and 88 class II molecules, with ligand lists, molecule sequences and links to structures available for download.
- Immunopeptidome mass spectrometry: the mono-allelic data of Sarkizova and colleagues, over 185,000 peptides eluted from 95 mono-allelic cell lines, some of them carried over from earlier work, so the exact composition must be checked against the paper; the HLA Ligand Atlas holds 227 benign tissue samples from 29 tissues. Raw spectra are released through the ProteomeXchange repositories PRIDE and MassIVE, and what to report follows MIAIPE.
- Repertoires and structures: VDJdb and McPAS-TCR hold manually curated TCR–epitope pairs; Observed Antibody Space holds over a billion antibody sequences under CC-BY 4.0; SAbDab holds antibody structures. Repertoire data are reported under the AIRR Community's MiAIRR standard and can be queried through the AIRR Data Commons interface.
- Functional and clinical immunology: ImmPort holds data from NIAID-funded studies; it requires registration and acceptance of a data use agreement that forbids re-identifying individuals.
- When the "reference motif" or "reference score" is itself computed by a model, the task is pure computation, not existing data.

## Preventing answer leakage

- The labels of public benchmarks can be downloaded. The IEDB automated benchmark uses newly curated data as a blind test; when an already published dataset is used, split it by curation date and keep entries after the cutoff as the held-out set.
- Peptide and receptor sequences are highly similar to one another. Peptides from the same epitope, clonotypes from the same donor, and receptors whose CDR3s differ by one or two amino acids cannot be split between the discovery set and the held-out set; cluster by sequence similarity first, then split by cluster.
- The output of existing prediction tools is directly available. If "is it presented" is the only basis for scoring, calling a public tool is enough to pass; score the deconvolution result, the motif itself, or quantities the tools do not give (allele assignment, which alleles cannot be separated) instead.
- The task statement contains no IEDB IDs, no PRIDE or MassIVE dataset IDs, no cell-line names and no HLA typing of the sample; each of these leads back to the source data and the published conclusions.
- Labels of the held-out set and the mono-allelic reference motifs stay in the agent judge material and never enter the solving agent's environment.

## Tools and compute

- Presentation prediction: NetMHCpan and NetMHCIIpan (free for academic use, downloaded separately, no redistribution, with a separate license for commercial use); MHCflurry is open source under Apache 2.0; MixMHCpred is free of charge but for-profit use needs a separate license.
- Motif deconvolution: GibbsCluster handles peptides of unequal length and has a trash cluster, but does not assign alleles by itself, so the assignment is made by comparison with known motifs; MixMHCp handles only peptides of equal length and deconvolves on a 9-residue core by default; NNAlign_MA clusters, assigns alleles and trains a prediction model in one step.
- Mass-spectrometry identification and repertoire processing: Comet, MaxQuant and Percolator for peptide identification; IgBLAST and Immcantation for receptor annotation and clonotype assignment; MiXCR requires a license request for academic use.
- Structure and single cell: AlphaFold and ColabFold for pMHC and antibody complexes, ANARCI for antibody numbering; immune cell-state analysis uses Scanpy and Seurat as elsewhere.
- Compute: prediction and deconvolution at the peptide level take minutes to hours on a single workstation; re-searching raw mass-spectrometry data and predicting structures need GPUs and large storage, so give the identified peptide lists rather than raw spectra whenever possible. The recomputation during review covers only metrics and a small amount of deconvolution and is far smaller than solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Mixing binding-affinity data, eluted-ligand data and T-cell recognition data. Binding is not presentation, and presentation is not recognition.
- Using randomly generated peptides as negatives without matching the length distribution and source-protein abundance, so the model wins on features unrelated to presentation and the metric is inflated.
- Comparing raw scores directly across alleles. The score scale differs between alleles, so scores must be converted to %rank first.
- Leaving contaminants and false identifications in the immunopeptidome data, so a recovered cluster corresponds to a contaminant source rather than to an allele.
- Forcing a split between alleles with similar motifs. Such alleles cannot be separated from the data, and the result must be reported as one merged motif rather than as a false split.
- Comparing repertoire diversity metrics across samples of different sequencing depth without resampling to a common depth first.
- A clonotype definition that differs between datasets (whether V/J genes are included, nucleotide or amino acid level), so conclusions about "shared clonotypes" do not hold.
- Running statistical tests with the cell as the unit in single-cell data, ignoring the variation between donors, so p values are too small.

## Example: deconvolving HLA binding motifs from multi-allelic immunopeptidome data

The class I HLA molecules on a cell or tissue sample are encoded by at most six alleles (two each of HLA-A, -B and -C), so the eluted peptides are a mixture of what these molecules present, and mass spectrometry gives only the peptide sequences, not which molecule presented each one. Separating the mixture by source molecule and giving the binding motif of each is a basic step of immunopeptidomics, and GibbsCluster, MixMHCp and NNAlign_MA were all built for it. The true values come from mono-allelic cell lines: Sarkizova and colleagues eluted over 185,000 peptides from 95 mono-allelic cell lines, and on data of this kind the MHC Motif Atlas has collected 1,013,733 ligands and the motifs of 135 class I molecules. The task asks the solving agent to recover, from a multi-allelic peptide list whose typing is withheld, the separable motifs, the assignment of each peptide, and which alleles cannot be separated.

The following is illustrated for the Inversion class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives a peptide list from a multi-allelic sample (lengths 8–11) and a simulated sample mixed in given proportions from known mono-allelic peptides; it gives no HLA typing of the sample, no number of motifs and no dataset ID. The deliverables are the assignment of every peptide (including an "unassigned" category), the position weight matrix of each group with its 9-residue core alignment, the allele assignment with its basis, and a list of allele combinations that cannot be separated. The format of the assignment table and the position weight matrices is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Number of motifs and peptide assignment: determine how many motifs are separable in the sample and give the assignment of every peptide and the fraction of contaminants.
  2. Characterizing the motifs and assigning alleles: give the amino acid preferences at the anchor positions (P2 and the last position) and the length distribution of each group, and assign the corresponding alleles.
  3. Identifiability: state which alleles cannot be separated in this sample (similar motifs, or too few peptides presented), and give the merged motif and the uncertainty of the assignment.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the observed data the sub-question concerns. The deliverable is the reconstructed part, as computation (the probability of generating the peptides from the recovered motifs and mixing proportions, with residuals against the observed frequencies at noise level, and recovery of the known mono-allelic motifs on the simulated mixture) and as text (the amino acid frequencies at each position in the peptide list and the length distribution that the motifs rest on; a report of non-separability when motifs are close or a group is too small). The constraints (each column of a position weight matrix sums to one, no more than six motifs) are checked by the agent judge.
- **Checks.** On the simulated mixture the agent judge computes the fraction of correct assignments, with the true source given by the mixing; it compares the position weight matrix of each group with the mono-allelic reference motif, scores correctly assigned alleles and scores nothing for wrong assignments. For the real sample, the agent judge regenerates the amino acid frequencies at each position from the submitted motifs and proportions, and the residuals must be at the noise level estimated by bootstrap resampling. The tolerance is set from the spread observed when the deconvolution is run repeatedly on the same sample and from the sampling error of the mono-allelic reference data itself.
- **Tiers and scoring.** The number of motifs and the assignment on the simulated sample form the first tier, the anchor preferences and allele assignment the second, and the identifiability argument the third; completing only the first tier earns the corresponding score. The weights are set by the expert.
- **Calibration cases.** The empty submission (score 0); tracing the peptide list back to the original dataset and its published typing and copying the motifs (a shortcut, which the simulated sample and the residual check must detect); recovering only the two or three most abundant motifs (partially correct); motifs assembled directly from the mono-allelic reference data using the true typing (a known result).
- **Other tasks of the same structure.** Switch to a class II immunopeptidome, where the core position is not fixed and the alignment must be determined at the same time, or to a peptide list from a tissue sample rather than a cell line.
