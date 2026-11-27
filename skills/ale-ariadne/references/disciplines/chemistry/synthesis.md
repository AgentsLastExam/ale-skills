# Chemistry: synthesis

This file adds content specific to synthesis to `references/disciplines/chemistry.md`, whose provisions still apply.

Scope: organic, inorganic and organometallic synthetic methods, total synthesis, retrosynthetic route design, and the prediction and optimization of reaction conditions and yields. For reaction mechanisms and the origins of selectivity see `mechanism-properties.md`; for the study of catalyst active sites and catalytic cycles as such see `catalysis.md`; for enzyme catalysis and biosynthesis see `life-processes.md`; for polymer synthesis see `macromolecular-nano.md`; for solid-state synthesis and the preparation of inorganic materials see `references/disciplines/materials.md`.

## Screening criteria

- Build with priority: questions whose conclusion can be judged against a public high-throughput experimentation dataset from a single source, for example yield prediction for Pd-catalyzed C–N coupling. Thousands of reactions were measured on one platform by one protocol, so an additive, a substrate or a ligand can be held out as a whole to test how a model generalizes to reaction components it has not seen. Yield is sensitive to conditions and is comparable only within one dataset; the score takes the error and ranking over the whole held-out part, supported by control models, and does not rest on any single yield value.
- Build with priority: optimization of reaction conditions in which a fully enumerated high-throughput experimentation dataset stands in for the experiment, for example finding the combination of ligand, base and solvent with the highest yield within a limited number of experiments. Each "experiment" is a table lookup, so no new observation is needed, and random search and Bayesian optimization baselines exist to compare against.
- Defer: retrosynthetic route design for complex molecules. Routes can be generated, but whether a route works must be decided by experiment, which takes far more than six hours. Discuss with the expert a formulation that can be judged: each step is checked for atom conservation, valences and atom mapping, the starting materials are restricted to a list fixed in advance, and the route is compared with routes already realized in patents or the literature; passing then shows only that the route is formally sound.
- Defer: the discovery of entirely new reaction types, and tasks that use the measured yield or enantioselectivity of new substrates as the only basis for scoring. Computation can only propose hypotheses, and the verdict needs new synthesis and characterization (physical-world observation level 3). The computable quantities a hypothesis rests on (the barrier of a key step, a selectivity) can be set as a task of their own; see `mechanism-properties.md`.
- Defer: tasks involving synthesis routes or condition optimization for chemical weapons agents, explosives or controlled drugs and their precursors, however they are formulated.

## Matters to confirm in conversation

- The source of the data: high-throughput experimentation, electronic laboratory notebooks, or literature and patents; whether all reactions were measured on the same platform by the same protocol.
- How yield is defined and measured: isolated yield, or a chromatographic or mass-spectrometric yield calibrated against an internal standard; the repeatability of replicate experiments, and how reactions with no detected product are recorded.
- How the held-out part is formed: which reaction component (substrate, additive, ligand, base, solvent) is held out as a whole; how far the held-out components differ chemically from the training components; whether the test set contains components that deactivate the reaction.
- The form of the target: a yield value, a ranking, whether a threshold is exceeded, or the best conditions found within a limited budget; the tolerance is set from the spread of replicate experiments.
- What makes a route task decidable: the list of starting materials, the maximum number of steps, the reaction types allowed, and whether stereochemistry, protecting groups and regioselectivity are counted.
- What "correct" means: agreement with a reported route, or any formally valid route; how the score is assigned when several reasonable routes exist.
- How reactions are represented: how SMILES are canonicalized, where the atom mapping comes from, and whether reagents, solvents and catalysts are written into the reaction.
- Whether the target molecule, intermediates or reagents involve controlled substances or high-hazard processes.

## Checking templates

The templates below add to the general templates in `references/disciplines/chemistry.md`.

| Template | Criterion | Scope |
|---|---|---|
| Retraining and prediction on held-out components | The agent judge runs the submitted training and prediction code in an environment without the held-out labels, computes R² and RMSE for the additives, substrates or ligands held out as a whole, and compares them with the baseline and with the spread of replicate experiments; the values the submitter reports are not used | Uses existing data, must pass |
| Label scrambling and feature controls | The model is retrained after the training labels are randomly scrambled, or after the chemical descriptors are replaced by one-hot encodings or random-number features: R² should fall to about zero in the first case and become clearly worse on the held-out components in the second; otherwise the model is not using chemical information | Uses existing data, counts for part of the score |
| Condition optimization by table lookup | The submitted optimization program is run on a fully enumerated dataset, with each query counted as one experiment; the agent judge reruns it with several random seeds and compares the highest yield reached within the limited budget with the random search and Bayesian optimization baselines | Uses existing data, scientific discovery level 2–3 |
| Step-by-step validity of a route | Each step of the submitted route is checked for atom conservation, valid valences and a consistent atom mapping, and a forward reaction prediction model fixed in advance is used to check that the step can give the stated product; every terminal molecule is in the fixed list of starting materials | Pure computation, must pass |
| Comparison with realized routes | The submitted route is compared with patent or literature routes in starting materials, number of steps and distance between routes; a route that differs is not marked wrong outright but is judged by step-by-step validity and the rubric | Uses existing data, scientific discovery level 2 |
| Held-out reactions for single-step retrosynthesis | On reactions split by time, the fraction of cases in which the top k predictions contain the literature reactants, reported together with the round-trip accuracy (the predicted reactants lead back to the target product through a forward model) | Uses existing data, scientific discovery level 1–2 |

## Sources of existing data

- High-throughput experimentation: the Buchwald–Hartwig coupling dataset (Ahneman et al., three 1536-well plates, 4,608 reactions including controls) and the Suzuki–Miyaura coupling dataset (Perera et al., 5,760 reactions), published with the papers and also held in the Open Reaction Database (data under a CC-BY-SA license).
- Patent and literature reactions: the USPTO patent reaction set and its subset USPTO-50K (about 50,000 reactions in 10 classes, used for single-step retrosynthesis). Yields in patents vary with reaction scale and differ widely between similar reactions, so they should not be used directly as true yields. Reaxys, SciFinder and Pistachio are commercial databases and cannot be redistributed.
- Routes: PaRoutes (two sets of 10,000 synthesis routes each, taken from patents, with lists of starting materials and evaluation scripts).
- Reaction optimization benchmarks: Summit provides benchmarks in which a mechanistic or data-driven model simulates the reaction outcome. Such "experimental results" come from a model, so they count as pure computation, not existing data.

## Preventing answer leakage

- All the yields of a public dataset can be downloaded, the labels of the held-out part among them. Make the submitted code the object of scoring: the agent judge retrains and predicts in an environment with no network access and no held-out labels.
- Under a random split, every component of a test reaction has already appeared in the training set, so memorizing component labels is enough for a high score. Hold out whole components, and check that a held-out component does not appear in the training set under another notation.
- Where possible, use as the held-out part an experimental plate or additional components that the expert has not yet published.
- When the target molecule of a retrosynthesis task comes from a patent or the literature, the realized route can be found by searching. Use target molecules published after a split in time, or base the score on step-by-step validity instead of agreement with the literature route.
- Atom-map numbers and the order of atoms can leak the position of the reaction center; retrosynthesis models on USPTO data have overestimated their accuracy for this reason. Molecules given in the task statement must have their map numbers removed and be canonicalized again.
- The task statement contains no patent numbers, paper titles or reaction IDs from the datasets.

## Tools and compute

- Reaction and molecule handling: RDKit, RDChiral (extraction and application of reaction templates), RXNMapper (atom mapping).
- Retrosynthesis and forward prediction: AiZynthFinder, ASKCOS (open source). Commercial retrosynthesis software cannot be placed in the review environment, so its results cannot be rerun by the agent judge.
- Descriptors and models: xtb and Psi4 for molecular descriptors; scikit-learn and PyTorch for training models; public yield models such as Yield-BERT can serve as baselines.
- Experimental design and optimization: EDBO, Summit (Bayesian optimization and its benchmarks).
- Compute: for a dataset of a few thousand reactions, training a tree model is on the order of minutes, and fine-tuning a language model or graph neural network takes hours on one GPU; DFT descriptors for a few tens of reaction components are on the order of tens of CPU core-hours. The review has to retrain, so its compute is comparable to solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- R² under a random split taken as evidence of generalization. On the Ahneman dataset, replacing the chemical descriptors by random numbers or one-hot encodings leaves the performance under a 70/30 random split almost unchanged.
- Only one way of holding out reported. Of the 23 additives in that dataset, 4 deactivate the reaction severely; when all 4 fall into the test set and the training set has no additive of this kind, R² drops from about 0.8 to 0.19.
- Chromatographic or mass-spectrometric yields from high-throughput experimentation treated as isolated yields, or yields from different sources and different assays merged for training.
- A tolerance smaller than the spread of replicate experiments. Ahneman et al. themselves note that a substantial part of their test error is likely to come from experimental and analytical error.
- Single-step retrosynthesis scored by exact agreement with the literature reactants. One product often has several reasonable disconnections, so reasonable predictions are marked wrong.
- Route search scored by the fraction of targets for which a route is found. This metric depends on the list of starting materials and on the single-step model, and finding a route does not mean the route is feasible.
- Passing the step-by-step validity check stated as "the route can be realized". Regioselectivity, functional-group compatibility and protecting-group issues lie outside what that check examines.
- Reagents, solvents and by-products recorded incompletely in a dataset; the atom-conservation check must allow for unrecorded small molecules, or valid reactions are marked invalid.
- The conformers, charge states and ligand coordination modes on which the descriptor calculation depends left unspecified, so the same molecule yields different features.

## Example: generalization of a C–N coupling yield model to unseen additives

Ahneman et al. measured 4,608 reactions (including controls) of the Pd-catalyzed Buchwald–Hartwig coupling on three 1536-well plates: 4-methylaniline was coupled with 15 aryl and heteroaryl halides, in every combination of 4 ligands, 3 bases and 23 isoxazole additives. A random forest trained on 120 computed descriptors reached R² = 0.92 and RMSE = 7.8% under a 70/30 random split; trained on 15 additives and predicting the other 8, it gave R² = 0.83 and RMSE = 11.3%. Chuang and Keiser then pointed out that replacing the descriptors by random numbers or one-hot encodings leaves the performance under a random split almost unchanged; the original authors' reply showed that the difference appears when additives are held out and the test set contains additives that deactivate the reaction (over 14 test sets of this kind, R² was 0.63 ± 0.12 for the descriptor model and 0.36 ± 0.20 for one-hot encoding). The task asks the solving agent to develop a yield model that generalizes better to unseen additives and to show that the gain comes from chemical information.

The following is illustrated for the Development class; the class is assigned by the expert. Scientific discovery level 3, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives the reactions of the training part (the structures of the components and the yields), the structures of the held-out additives, the definition of the metric and the baseline procedure, and withholds the yields of the held-out part; the environment has no network access. The deliverables are the training and prediction code, a file `predictions.csv` with the predictions for the held-out reactions, and a short report. The format of `predictions.csv` (reaction ID and predicted yield) is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Representation of the additives: which description lets the model distinguish additives that deactivate the reaction from ordinary additives.
  2. Representation of the substrates: whether the model can extrapolate from aryl bromides to aryl chlorides and iodides.
  3. Sparse data: whether the improvement holds when only 5% of the data (about 230 reactions) is used for training.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the part of the existing method the sub-question concerns, with the metric and the constraints to be maintained. The deliverable is the improvement and its contribution to the metric, as text (why the representation carries chemical information related to deactivation, for example the electrophilicity of an additive and its tendency to undergo oxidative addition to Pd(0)) and as computation (the improved model and its metric; the ablation, in which the representation of that component is replaced by one-hot encodings or random-number features, or the training labels are scrambled, and the metric should fall accordingly). The agent judge retrains and recomputes the metric on the held-out part.
- **Checks.** The agent judge runs the submitted code in an isolated environment, retrains with several random seeds, and computes R² and RMSE on four held-out additive test sets constructed by activity ranking. The mean R² must exceed the baseline (0.69 ± 0.12 for descriptors with a random forest, 0.61 ± 0.11 for one-hot encoding) by a margin larger than the spread between seeds; after the training labels are scrambled, R² must fall to about zero; the values the submitter reports do not score. The thresholds are provisional and are set from the spread of repeated baseline runs and the error of replicate experiments.
- **Calibration cases.** The empty submission (score 0); reading the held-out yields directly from the public data, or reporting a high R² only under a random split (a shortcut, score 0); a one-hot encoding model (partially correct: good under a random split, no better than the baseline on held-out additives); the descriptors with a random forest of the original paper (the baseline).
- **What passing does not show.** The checks above form a proxy verifier: passing shows that, within the reaction space of this dataset, the model predicts unseen additives better than the baseline and that the gain depends on the chemical representation. Passing does not show that the model applies to other reaction types, other experimental platforms or new substrates in real synthesis; whether the gain is chemically meaningful remains for the expert to judge.
- **Other tasks of the same structure.** Change the dataset (the 5,760 reactions of the Suzuki–Miyaura coupling, held out by ligand or substrate), or turn the task into condition optimization by table lookup; the workflow and the checks stay the same.
