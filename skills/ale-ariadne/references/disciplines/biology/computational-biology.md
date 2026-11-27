# Biology: computational biology

This file adds content specific to computational biology to `references/disciplines/biology.md`, whose provisions still apply.

Scope: sequence alignment and homology search, phylogenetic inference (maximum-likelihood and Bayesian trees, molecular clocks and divergence dating, phylodynamics of outbreaks), single-cell data analysis (dimensionality reduction and clustering, trajectory and RNA-velocity inference, batch correction and atlas integration), network and pathway modeling (gene regulatory network inference, constraint-based metabolic models, pathway enrichment), and machine learning models of biology. The object of this file is the methods and their benchmarking; for the generation of omics data and specific biological conclusions see `genomics-omics.md`; for molecular structure, simulation and design see `molecular-biophysics.md`; for specific conclusions in evolution and ecology see `evolution-ecology.md`; for the design of synthetic biology circuits see `bioengineering.md`.

## Screening criteria

- Build with priority: methodological questions with a fixed public benchmark, fixed metrics and clear baselines, for example single-cell atlas integration, gene regulatory network inference assessed against a curated gold standard, or zero-shot prediction by protein language models on deep mutational scanning data. The metrics of such questions can be recomputed by the agent judge and the baselines can be rerun.
- Build with priority: questions whose true values are given by simulation, for example simulating sequences under a known tree and substitution model, then checking whether phylogenetic inference recovers that tree and its divergence times. The generating process is the true value, and the task is pure computation that depends on no published conclusion.
- Defer: questions in which the gold standard shares its origin with the methods under assessment, for example network inference that takes transcription factor binding sites as the true regulatory relations: binding is not regulation, the incomplete network leaves the negatives unknowable, and the metric changes with the choice of gold standard. Such questions can be restated as an assessment on simulated data, or restricted to a curated subnetwork and expressed through early precision and ranking.
- Defer: tasks whose benchmark labels and leaderboard are entirely public, so that a score can be obtained by searching; these can be switched to datasets released after the cutoff date, or to a held-out split whose labels are not public.
- Defer: conclusions that must be confirmed by a new wet-lab experiment taking more than six hours (physical-world observation level 3).

## Matters to confirm in conversation

- The metric to be improved, the script that computes it, and the exact versions of the current best result and of each baseline.
- The versions of the evaluation datasets and how they are split, and which data take no part in development.
- How several datasets and several metrics are aggregated: normalization per dataset, weighting or averaging, and who sets the weights between metrics.
- How the hyperparameters are determined and over what range they are searched, and the random seeds and number of repeated runs.
- Where pretrained weights are used, the scope and cutoff time of the training data, and whether it overlaps the evaluation data.
- The generative model and parameters of the simulated data, and how they relate to the assumptions made by the method under assessment.
- How large an improvement has to be to mean something: compared with the fluctuation between random seeds and with the differences between datasets.
- The form of the conclusion: a leaderboard rank, an improvement in a metric, or a conclusion that "holds for a certain kind of data".

## Checking templates

The templates below add to the general templates in `references/disciplines/biology.md`.

| Template | Criterion | Scope |
|---|---|---|
| Recomputation in a fixed evaluation pipeline | The agent judge reruns the submitted method in the pipeline fixed in the task statement and recomputes every metric, and does not use the values the submitter reports; the metric implementation may not be altered by the submitter | Uses existing data, must pass |
| Generalization across datasets | The same improvement is rerun on datasets and tasks not used in development, where the gain must also hold and point in the same direction | Uses existing data, scientific discovery level 2–3 |
| Ablation item by item | Each claimed improvement is removed in turn and the metric recomputed, and the attribution of the gain agrees with the claimed mechanism | Uses existing data, scientific discovery level 2–3 |
| Recoverability on simulated data | On data generated from a known tree, network or generative model, the method recovers the true value, and the parameter estimates fall within an interval set in advance | Pure computation, must pass |
| Randomized controls | After shuffling the labels, permuting the samples or switching to a null-model network, the metric falls back to chance level; a method that still scores high on the null model scores nothing | Must pass |
| Margin over the baseline and its uncertainty | The gain exceeds the fluctuation between several random seeds and the bootstrap confidence interval; the baseline is obtained by the agent judge rerunning it in the same pipeline, and values reported in papers are not used | Scientific discovery level 3 |

## Sources of existing data

- Benchmark suites: Open Problems (data, methods and metrics for single-cell tasks, continuously updated), scIB (implementations of 13 atlas integration tasks and 14 metrics), BEELINE (gene regulatory network inference, with simulated data and curated gold standards), ProteinGym (about 217 deep mutational scanning datasets of amino acid substitutions, with Spearman correlation as the main metric).
- Alignment and phylogeny: the alignments and models of Pfam and Rfam, multiple sequence alignment benchmarks such as BAliBASE, and published phylogenetic data matrices.
- Networks and metabolic models: the constraint-based metabolic models collected in BiGG, with MEMOTE for checking the internal consistency of a model.
- Data simulated from a known tree, network or generative model: the true values come from the generating process, so such tasks count as pure computation, not as using existing data.

## Preventing answer leakage

- The labels and leaderboards of public benchmarks can be found by searching: keep the evaluation pipeline of the public benchmark, but switch to datasets whose labels are not public, or split by time and use data released after the cutoff date.
- Where a pretrained model is used, the scope and cutoff time of its training data must be declared; the agent judge re-checks on data that is later in time, to guard against inflation from overlap between training and evaluation data.
- Hyperparameters must be determined within the development data and fixed in advance, and the agent judge reruns with the fixed hyperparameters; a submission that repeatedly selects hyperparameters on the evaluation data is treated as a shortcut.
- The task statement gives the metric definitions and the evaluation script but not the scores of the baselines on the held-out data, so that the answer cannot be worked back from a target score.
- The generating parameters of simulated data are part of the answer; they are kept only in `tests/` and are not provided with the data.

## Tools and compute

- Single-cell methods and assessment: scvi-tools (scVI, scANVI), Harmony, Scanorama, scGen, BBKNN, LIGER; scIB and scib-metrics implement the evaluation metrics.
- Phylogenetics: IQ-TREE, RAxML-NG, MrBayes, BEAST2, ASTRAL, MAFFT; simulated data can be generated with AliSim and Seq-Gen.
- Networks and metabolism: GENIE3, GRNBoost2, SCENIC; COBRApy with BiGG models, where the linear programming solvers Gurobi and CPLEX need a license, Gurobi is free to academic institutions, and open-source solvers can replace them.
- Sequence and structure search: DIAMOND, Foldseek; the statistics and machine learning frameworks scikit-learn and PyTorch.
- Compute: one complete run of an atlas integration task takes on the order of hours on data of several hundred thousand cells, training needs a GPU, and computing the metrics (neighbor graphs, silhouette widths, LISI) can cost more than the training itself on large datasets; Bayesian phylogenetic inference is counted in CPU core-hours, and the size of simulated data can be adjusted. Review must rerun the method and the baselines, on the same scale as solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Hyperparameters selected, or the stopping point of training decided, on the evaluation data, so that the reported gain cannot be reproduced on new data.
- A gold standard that shares its origin with the methods under assessment, so that the assessment reflects only the assumptions the two have in common.
- Clustering and then testing for differences on the same data, which makes the p-values too small across the board; count splitting, data thinning or independent data must be used.
- A trade-off between batch removal and conservation of biology, in which reporting the metrics of only one side is enough for a high score.
- Metrics such as ARI and NMI that change with the number of clusters; methods compared without fixing the number of clusters or deriving the clusters by the same procedure.
- A generative model for the simulated data that matches the assumptions of the method under assessment, so that the result reflects only performance when that assumption holds.
- Bootstrap support taken for the probability that the topology is true; long-branch attraction and a misspecified substitution model give wrong topologies with high support.
- Training data of a pretrained model overlapping the benchmark data, inflating zero-shot metrics.
- A few datasets dominating the overall score of a multi-dataset benchmark, with no normalization per task and no per-dataset results reported.

## Example: improving a method for single-cell atlas integration

Integrating single-cell data from different laboratories, platforms and donors into one atlas requires a balance between removing batch effects and conserving biological differences. A systematic benchmark compared 68 combinations of method and preprocessing on 85 batches from 23 publications, more than 1.2 million cells, assessing them on 13 integration tasks with 14 metrics; the overall score weights conservation of biology by 0.6 and batch removal by 0.4, after min-max scaling of each metric within a task. In that benchmark scANVI, Scanorama, scVI and scGen did well on complex tasks. The Open Problems platform assesses the same task continuously with fixed data, methods and metrics. The task asks for an overall score above the current best method under a fixed evaluation pipeline, holding also on datasets not used in development.

The following is illustrated for the Development class; the class is assigned by the expert. Scientific discovery level 3, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives the development datasets, the metric implementation and aggregation, the list of baseline methods and how to run them, and the random seeds and number of repeats; it gives neither the held-out datasets nor the scores of the baselines on the held-out data. The deliverables are an implementation of the method that can be rerun, the embeddings and clusterings of each run, a `results.json` collecting the values (the score for every dataset and metric and the overall score), the implementations of each ablated version and a short report. The interface of the implementation and the format of `results.json` are the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Representing and removing batch effects: which kind of batch the improvement addresses (platform, donor, laboratory) and how it is represented.
  2. Conserving biological differences: conservation of rare cell types and continuous trajectories, and how the trade-off with batch removal is handled.
  3. Scale and stability: behavior as the numbers of cells and batches grow, and sensitivity to random seeds and hyperparameters.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the part of the existing method the sub-question concerns, with the metric and the constraints to be maintained. The deliverable is the improvement and its contribution to the metric, as text (the scientific basis of the improvement, explaining why it raises the overall score and why the constraints still hold: no reading of held-out labels, no change to the metric implementation, a resource ceiling for a single run) and as computation (the improved method and its metrics; the overall score with this improvement removed, which is the ablation and establishes its contribution to the overall gain). The agent judge reruns in the same pipeline and recomputes the metrics, and does not use the values the submitter reports.
- **Checks.** The agent judge recomputes every score with the fixed metric implementation and aggregation; it reruns on datasets not used in development, where the gain must also hold; it runs controls with shuffled batch labels and with shuffled cell-type labels, where the overall score must fall back to chance level; it compares the fluctuation between several random seeds, and the gain must exceed that fluctuation and the bootstrap confidence interval; it inspects the solving trajectory to confirm that the method did not read the labels of the held-out data. The baseline scores are obtained by the agent judge rerunning the baseline methods in the same pipeline.
- **Calibration cases.** The empty submission (score 0); a call to a baseline method with its output passed through unchanged (a baseline); a submission that reads or fits the labels of the held-out data (a shortcut, score 0); a submission whose overall score rises slightly but whose gain vanishes on the held-out datasets (partially correct); a submission whose overall score rises while the biology-conservation side falls, lifted only by the batch-removal side (violates a constraint, identified from the component metrics).
- **What passing does not show.** The checks form the proxy verifier proposed by the expert and show only that, for this set of data, this set of metrics and this way of aggregating them, the gain can be recomputed, can be attributed and holds on held-out data. The metrics are themselves a proxy for integration quality: min-max scaling makes the scores depend on the methods assessed together, the weights between metrics are set by convention of the benchmark, and the cell-type labels themselves carry noise. Whether the method really improves the biological usefulness of the atlas remains for the expert to judge.
