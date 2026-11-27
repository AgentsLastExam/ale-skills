# Biology: bioengineering and synthetic biology

This file adds content specific to bioengineering and synthetic biology to `references/disciplines/biology.md`, whose provisions still apply.

Scope: genome-editing tools (nuclease engineering and specificity, base and prime editing, editor delivery and in vivo editing), synthetic circuits and chassis (genetic logic and feedback controllers, cell-free expression systems), biomaterials and delivery vehicles, biosensors and imaging probes (engineered fluorescent reporters, optogenetic and chemogenetic actuators), directed evolution and large-scale screens (continuous and directed evolution, pooled CRISPR screens and MPRAs). For protein structure prediction and de novo design see `molecular-biophysics.md`; for statistical models of sequence to function and algorithms for screen data see `computational-biology.md`; for the cellular process being engineered see `cell-biology.md`; for the physiology of the chassis organism see `microbiology-virology.md`; for the developmental questions in tissue engineering see `developmental-biology.md`; for the chemistry of delivery materials see `references/disciplines/chemistry.md`.

## Screening criteria

- Build with priority: the conclusion comes down to a distribution or a metric recomputed on held-out target sites, with public measurements to compare against. An example is predicting the distribution of repair outcomes at a Cas9 cut from sequence: amplicon sequencing and its quantification pipeline are mature, synthetic target-site libraries already provide measurements for more than 40,000 sgRNA–target pairs, and published models serve as a baseline.
- Build with priority: fitness prediction on a public deep mutational scan, for example predicting the activity ranking of the remaining variants of one assay from a subset of its variants. The way the data is split, the rank correlation coefficient and the zero-shot baselines are all established practice in the field.
- Defer: tasks scored solely on in vivo delivery and editing efficiency, for example the editing rate of a lipid-nanoparticle-delivered editor in the liver of an animal. Such results take days to weeks to obtain (physical-world observation level 3). Discuss with the expert whether to predict a cell-based readout instead, or to rank formulations under a physicochemical model fixed in advance.
- Defer: tasks scored solely on the measured behavior of a genetic circuit in a new host or new culture condition, for example the oscillation period of a feedback controller. Transfer functions change with plasmid copy number, strain, medium and growth phase. Such a task can be reformulated by fixing the model in advance and asking only for conclusions within the model, or by using a cell-free expression readout obtainable within six hours (physical-world observation level 2).
- Defer: tasks that touch biosafety-sensitive content. These are not built, and no technical detail about them appears in the task statement, the research log or the conversation.

## Matters to confirm in conversation

- The editing tool and its configuration: the version of the nuclease or editor, the sgRNA scaffold, the delivery method and dose, the cell line and culture conditions.
- Quantification conventions: where the amplicon primers sit, the quantification window, whether the denominator is all reads or edited reads, and the rules for aligning and merging indels.
- How far repair outcomes or circuit behavior depend on cell type and chromatin context, and whether the conclusion is required to hold across cell lines.
- The design of the screen: library coverage, multiplicity of infection, number of rounds and time points, the composition of control sgRNAs, and how counts are normalized.
- The definition of the fitness or activity readout: enrichment ratio, survival or fluorescence intensity; and how selection strength and bottleneck size affect it.
- The definition of the performance metric for a circuit or protein: dynamic range, leakiness, response time, orthogonality; and the instrument and units (whether flow cytometry arbitrary units are converted with calibration beads).
- The form of the conclusion: an absolute value, a ranking, or the margin above a fixed baseline; and whether the tolerance comes from the spread between replicate measurements or from the sampling noise set by read counts.
- Whether feasibility is listed as a condition in design tasks: synthesis difficulty, vector capacity, burden on the host.

## Checking templates

The templates below add to the general templates in `references/disciplines/biology.md`.

| Template | Criterion | Scope |
|---|---|---|
| Distribution prediction on held-out target sites | The agent judge reruns the submitted code to generate distributions on the held-out sites and compares them with measured distributions recomputed from raw reads by the fixed pipeline: the median per-site correlation and the median total-variation distance must beat a fixed baseline | Uses existing data, scientific discovery level 2–3 |
| Recomputation of editing quantification | With the primers, quantification window, denominator convention and alignment parameters fixed in the task statement, indel frequencies are recomputed from raw reads and agree with the values the submitter reports | Uses existing data, must pass |
| Transfer across cell lines | A model fitted on one cell line is scored on endogenous sites in another cell line, and the drop in the metric is compared with a threshold set in advance | Uses existing data |
| Reanalysis of screen data | With a fixed count normalization and statistical method, the log fold changes of sgRNAs and the hit list are recomputed, positive controls such as essential genes are recovered, and control sgRNAs are not significant | Uses existing data, must pass |
| Recomputation of the circuit model | The agent judge solves the kinetic model again with the submitted parameters and checks the steady states, dynamic range and response time, and that the parameters lie in the range declared in the task statement | Pure computation, must pass |
| Cell-free expression readout | A dose-response prediction submitted in advance is compared with a curve measured within six hours in a cell-free expression system on a plate reader, with the criterion and threshold written out beforehand | Needs a new observation (physical-world observation level 2) |
| Independent recomputation of a design | A candidate sequence or circuit is recomputed by a scoring program fixed in advance, and the score follows the margin above the baseline; the metrics the submitter reports are not used | Scientific discovery level 3 |

## Sources of existing data

- Editing outcomes: measurements of Cas9 repair outcomes in synthetic target-site libraries and amplicon data from endogenous sites, mostly released with the papers, with raw reads in SRA/ENA and the labels in supplementary tables.
- Screens: the CRISPR knockout screens of DepMap, the screen results collected in BioGRID ORCS, and read count tables of individual screens in GEO.
- Variants and fitness: ProteinGym (about 217 substitution assays covering some 2.7 million variants, plus about 74 insertion-deletion assays), MaveDB, and the fixed splits of FLIP. The number of entries differs between versions, so the version must be recorded.
- Parts and circuits: plasmid sequences in Addgene, the iGEM registry of parts, SynBioHub entries described in SBOL, and circuit models stored as SBML in BioModels.
- Values produced by a published prediction model, and scores produced by a fixed scoring program, are computed, so they count as pure computation, not existing data. Data on in vivo delivery and clinical editing is mostly unpublished and is not used as a source for checks.

## Preventing answer leakage

- Published prediction models and their weights can be downloaded directly. Ask for quantities the published models do not output, score on a held-out subset whose labels are not public, and have the agent judge rerun the submitted code.
- Measurements from synthetic target-site libraries are released as supplementary tables. Use a library published after the time split, another cell line, or statistics the paper did not report.
- The same target site or highly similar flanking sequences may appear in both the training set and the held-out set. Cluster by sequence similarity first and split by cluster, and never let the same sgRNA cross the split.
- The task statement contains no dataset accessions, library names, plasmid IDs or paper information.
- The measurements for held-out sites and the reference values used by the scoring scripts are kept only in `tests/`.

## Tools and compute

- Quantification of editing outcomes: CRISPResso2; read processing and alignment use the standard sequencing tools.
- sgRNA design and off-target assessment: CRISPOR, Cas-OFFinder; experimental off-target maps come from methods such as GUIDE-seq and CHANGE-seq, and absolute numbers from different methods cannot be compared with each other.
- Screen analysis: MAGeCK, BAGEL2.
- Circuit modeling and cell-free systems: models described in SBML and solved with COPASI or Tellurium; cell-free expression uses the PURE system or a TXTL system, and the readout is usually a fluorescence time series on a plate reader.
- Sequence models: public weights such as ESM can be used for zero-shot scoring of variant effects; commercial software such as Benchling and Geneious needs a license, and its output must not be the only reference value.
- Compute: processing screen and amplicon data is on the order of tens of GB and a few CPU hours; training a sequence model on an editing-outcome library is usually a few hours on a single GPU; solving a circuit model takes seconds on an ordinary computer; review mainly reruns inference on the held-out sites and is far smaller than solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Editing efficiency (the share of reads that are edited) confused with the outcome distribution (the composition within edited reads); the denominators differ, so the numbers cannot be compared.
- A changed quantification window, alignment parameters or indel merging rule, so the same data yields different indel frequencies.
- Synthetic target sites integrated at a single locus lack endogenous chromatin context, so a model derived from them deviates more on endogenous sites.
- Repair outcomes change with cell line and with the state of the repair pathways, yet a model fitted in one cell type is applied directly to another.
- PCR chimeras in amplicons and misalignment in homopolymer tracts taken for real editing products.
- The copy-number effect ignored in screens: sgRNAs in amplified regions drop out from cutting toxicity and are called essential genes.
- Enrichment ratios change with selection strength and bottleneck size, yet fitness values from different batches are pooled directly.
- Flow cytometry fluorescence reported in arbitrary units without conversion by calibration beads, so values are not comparable across instruments or days.
- A circuit transfer function measured at one plasmid copy number, strain and medium applied directly to another context.

## Example: predicting the distribution of repair outcomes at a Cas9 cut from sequence

Repair of a Cas9 cut is not random: the same sgRNA gives a reproducible indel distribution in the same cell line, and the distribution is largely set by the sequence around the cut. In synthetic target-site libraries, microhomology-mediated deletions make up 39%–58% of all products and 62%–75% of deletions, and a single-base insertion is usually a duplication of the base next to the cut on the side away from the PAM. On 189 held-out sites, a published model reached a median Pearson correlation of 0.94 for genotype frequencies and 0.91 for indel-length distributions; on endogenous sites in HEK293 the median correlation for frameshift frequency was 0.81, against 0.37 for an earlier score based on microhomology alone. The same model predicted that 5%–11% of SpCas9 sgRNAs in the human genome give a single genotype in more than half of the major editing products. The distribution changes with cell line, so results for one sgRNA in different cells cannot stand in for each other. The task asks the solving agent to predict the full distribution of repair outcomes at held-out sites from sequence alone.

The following is illustrated for the Prediction class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives the raw amplicon reads for the training target sites, the fixed quantification pipeline (primer positions, quantification window, denominator convention, alignment and merging parameters) and the sequences of the held-out sites, but not their measurements. The deliverables are code that can be rerun, a probability distribution over a fixed genotype vocabulary for each held-out site (`predictions.csv`: site ID, genotype, probability, with probabilities summing to 1 per site), the frameshift frequency and the "single dominant genotype" call derived from the distribution, and a short report. The format of that file is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. The microhomology deletion spectrum: predict the relative frequency of each deletion genotype from microhomology length, GC content and deletion length.
  2. Single-base insertions and microhomology-less deletions: predict the identity of the inserted base and its share of all products.
  3. Transfer across cell lines: predict the distributions at endogenous sites in another cell line with the same model, stating the assumed composition of repair pathways.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the target quantity as defined in the task statement; the true value is not provided to the solving agent. The deliverable is the prediction with its uncertainty, as text (the model's assumptions, such as the competition between end resection and annealing, the duplicated base produced by fill-in at the cut, and classical non-homologous end joining, argued to apply to this cell line and this type of cut) and as computation (fitting and running the model, with a sensitivity analysis over the quantification window, the read-depth cutoff and the genotype vocabulary, which is the ablation of the Prediction class, and an uncertainty built from the sampling noise set by read counts and the spread between replicate experiments). The comparison with the held-out measurements is made by the agent judge.
- **Checks.** The agent judge does not use the values the submitter reports; it reruns the submitted code, regenerates the distributions on the held-out sites, and scores them with metrics fixed in advance: the median per-site Pearson correlation of the genotype frequency vector, the median total-variation distance, and the correlation of frameshift frequency; the result must beat two fixed baselines (the library-average distribution and a microhomology-only score). The agent judge also recomputes the measured distributions of the held-out sites from raw reads with the fixed pipeline, confirming that the reference values used for scoring can be reproduced. The tolerance is set from the spread between replicate measurements at the same site and from the sampling noise of the read counts.
- **Calibration cases.** The empty submission (score 0); predictions downloaded from a published model, or the measurement table hardcoded (a shortcut; the agent judge reruns the code and rescores on another, unpublished set of sites); a submission implementing only the microhomology model (partially correct, better than the library-average baseline but failing on single-base insertions); the published model retrained on the given training set (a baseline).
- **Other tasks of the same structure.** Predicting the product spectrum of base editing, the efficiency of prime editing, or the cleavage activity of an sgRNA; the workflow and the checks stay the same.
