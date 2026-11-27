# Chemistry: chemistry of life processes

This file adds content specific to the chemistry of life processes to `references/disciplines/chemistry.md`, whose provisions still apply.

Scope: chemical biology and chemical probes, enzyme catalysis and enzyme engineering, protein–ligand interactions, the binding and selectivity of drug molecules, and the metalloenzymes and metallodrugs of bioinorganic chemistry. For questions whose object is protein structure, function or cellular processes themselves, see `references/disciplines/biology.md`; for dosing, pharmacokinetics and clinical use of drugs see `references/disciplines/medicine.md`; for the development and benchmarking of free-energy methods, force fields and enhanced sampling themselves see `theory-computation.md`; for catalysis in non-biological systems see `catalysis.md`; for synthetic routes to ligands see `synthesis.md`.

## Screening criteria

- Build with priority: relative binding free energies between a congeneric ligand series and a protein, for example the potency ordering of a set of kinase inhibitors against one target. The free-energy perturbation workflow is mature, public benchmarks cover more than twenty targets, experimental affinities exist to compare against, and one perturbation edge fits on a single GPU.
- Build with priority: the conclusion is a relative quantity or an ordering within one series, for example the selectivity of one ligand between two related kinases, expressed as the difference between two sets of relative binding free energies. A relative quantity cancels part of the systematic error of system preparation and of the force field, and is less affected by errors in absolute values than an absolute binding free energy.
- Defer: mechanisms of enzyme catalysis, for example identifying the rate-determining step of a metalloenzyme catalytic cycle. The combined quantum mechanics and molecular mechanics workflow is feasible, but building the system is involved and the conclusion is sensitive to how the active site is cut out, to protonation states and to the starting conformation. Discuss with the expert fixing the QM region, the protonation states and the starting structure in advance and asking only for barriers within that model, or switching to a comparison of the relative barriers of two candidate mechanisms.
- Defer: de novo design of proteins and enzymes, for example designing an enzyme that catalyzes a given reaction. Designs can be generated, but whether the function holds requires expression, purification and an activity assay, which cannot be done within six hours. Switch to a design task judged by a scoring program fixed in advance (structural self-consistency, geometric validity, recomputation of the binding free energy), and state that passing the scoring does not establish the function.
- Defer: design and optimization tasks whose goal is to increase the activity of a toxin or a controlled substance; these touch biosafety-sensitive and controlled content.

## Matters to confirm in conversation

- The source and resolution of the starting structure, how missing loops and side chains are completed, and how cofactors, metal ions and crystal waters are kept.
- The protonation states, tautomers and stereochemistry of the ligands, and how a change of net charge across a perturbation is handled.
- Where the binding pose comes from: a co-crystal structure, homology superposition or docking, and the uncertainty this brings.
- The force-field combination: protein force field, ligand force field, water model and ion parameters, and whether the field accepts this combination.
- How the experimental values were measured (ITC, SPR, Kᵢ, IC₅₀), under what conditions, and whether one series comes from a single laboratory; the conditions under which IC₅₀ converts to a binding free energy.
- The number of ligands and the dynamic range of the experimental values. Accepted benchmark sets require at least 16 ligands and a dynamic range above 3 kcal/mol, with 25 ligands and 5 kcal/mol considered better.
- The form of the conclusion: an absolute binding free energy, a relative value within the series, or an ordering; what the tolerance rests on (experimental repeatability, method error, spread between repeat runs).
- For enzyme mechanism tasks: how the QM region is chosen, the quantum chemistry method and basis set, the embedding scheme, and how conformations are sampled.

## Checking templates

The templates below add to the general templates in `references/disciplines/chemistry.md`.

| Template | Criterion | Scope |
|---|---|---|
| Recomputation of the free-energy network | From the submitted relative binding free energy of each edge, the agent judge solves the network again to obtain a binding free energy per ligand, then compares with experiment by mean unsigned error and rank correlation; the summary values the submitter reports are not used | Uses existing data, scientific discovery level 1–2 |
| Cycle closure | In the perturbation network, the deviation from zero of the sum of relative binding free energies around every closed cycle stays within a threshold fixed in advance, set from the repeat runs of step 2; cycle closure reflects only whether the sampling is self-consistent and does not by itself show agreement with experiment | Pure computation, must pass |
| Spread between repeat runs | The same edge is repeated several times with different random seeds, and the standard deviation agrees with the uncertainty stated in the submission | Pure computation, counts for part of the score |
| Validity of system preparation | The agent judge checks the submitted topologies and coordinates: net charges, protonation states and stereochemistry agree with the task statement, the atom mapping does not change bonding, and the protein has no missing residues or overlapping atoms | Pure computation, must pass |
| Held-out ligands | The experimental values of some ligands do not appear in the task statement; the agent judge computes the mean unsigned error and Kendall τ on them and gives confidence intervals by bootstrapping | Uses existing data, scientific discovery level 2–3 |
| Recomputation of an enzyme-mechanism barrier | With the QM region and method fixed in the task statement, the agent judge recomputes single-point energies on the submitted reactant, transition-state and product structures; the transition state has exactly one imaginary frequency, and the barrier agrees within tolerance with the value converted from the experimental rate constant | Pure computation, scientific discovery level 2–3 |
| Binding pose | The predicted binding pose is compared with a held-out co-crystal structure by heavy-atom RMSD, and bond lengths, angles and atom overlaps are checked for validity | Uses existing data |

## Sources of existing data

- Structures and activities: the PDB (complex structures); BindingDB (the part curated by its own staff is CC BY 3.0, the part imported from ChEMBL is CC BY-SA 3.0); ChEMBL.
- Free-energy benchmarks: the Open Force Field protein-ligand-benchmark, holding protein and ligand structures, experimental affinities and perturbation edges for 21 targets and about 560 ligands, with the code under MIT and the data under CC BY 4.0. Its experimental affinities count as existing data, while the predicted values of the various methods on this set are computed and count as pure computation.
- Blind-challenge data: the datasets of the successive Drug Design Data Resource challenges, for example BACE1 in the fourth round (154 compounds for affinity prediction, 34 of them for free-energy calculation) and cathepsin S (459 compounds, 39 of them for free-energy calculation); registration and the requested citation are required.
- Enzymes and mechanisms: M-CSA (1003 hand-curated entries, 734 of them with a detailed mechanism, CC BY 4.0); BRENDA (enzyme kinetic parameters, CC BY 4.0); UniProt.
- Complex collections and splits: PLINDER (more than 400,000 protein–ligand systems, with splits built by interaction similarity to reduce leakage).

## Preventing answer leakage

- The experimental values of the public benchmark sets and the predictions of the various methods are all published, and are often part of the training data of models. Switch to a congeneric series outside the benchmark sets, or use ligands published after a split in time.
- Make the per-edge values, the input files and the trajectories the object of scoring, not the errors and correlation coefficients the submitter reports.
- The task statement contains no PDB IDs, ChEMBL IDs, compound names or challenge round names; structures are supplied as coordinate files with identifiers removed.
- The experimental values of the held-out ligands are kept only in the agent judge's materials and never placed in the solving environment.
- The training sets of structure-prediction and affinity-prediction models may already contain the target complex; check release dates before using one as a baseline.

## Tools and compute

- System preparation and molecule handling: PDBFixer, the modeling tools of OpenMM, ParmEd, RDKit, Open Babel.
- Molecular dynamics and free energy: OpenMM, GROMACS (open source); AmberTools is open source, while pmemd carries a separate license, is free for non-commercial use and may not be redistributed.
- Free-energy workflows and analysis: openfe from Open Free Energy (MIT license, with the Lomap and Kartograf atom mappers), pAPRika (attach-pull-release workflow, BSD license), cinnabar (formerly arsenic, which reports the statistics of relative free-energy results on a common basis).
- Enzyme mechanisms: CP2K and the QM/MM interfaces between quantum chemistry programs and molecular dynamics programs; conformers can first be screened with xtb and CREST.
- Structure and design: the AlphaFold source code is under Apache 2.0, the AlphaFold 2 model parameters are under CC BY 4.0, and the AlphaFold 3 parameters must be obtained directly from Google and may not be redistributed; the code and weights of Boltz are both under MIT; RFdiffusion is under BSD; Rosetta is free for non-commercial use and needs a separate paid agreement for commercial use, under a license that is not open source. The geometric validity of generated poses can be checked with PoseBusters.
- Compute: one perturbation edge (tens of thousands of atoms, a dozen or more λ windows) takes on the order of hours on a single GPU, and a network of a dozen or more ligands and twenty or more edges is on the order of hundreds of GPU-hours; the review can recompute a few edges and solve the network again, far less than solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- A protonation state, tautomer or stereocenter chosen wrongly, which shifts the whole series systematically.
- The net charge of the ligand changes across the perturbation and no finite-size correction is applied.
- An atom mapping that changes bonding, making the simulation unstable and the error very large; such failures do occur in large-scale assessments and must be excluded by the system-preparation check.
- A perturbation network too sparse, with no closed cycles, so that the sampling error cannot be estimated; or the cycle-closure error used in place of the error against experiment.
- The experimental values of one series pieced together from different laboratories or different assays, so that neither the dynamic range nor the error is reliable.
- Too few ligands or too narrow a dynamic range, so that the confidence intervals of correlation and ranking metrics are wide and cannot distinguish the quality of methods.
- Correlation coefficients applied to relative binding free energies: the sign of each edge can be flipped at will and the statistic changes with it, so error-type metrics are preferable, or the direction is fixed in advance.
- A tolerance tighter than the experimental repeatability. The difference between assays for the same compound is on the order of 0.4–0.7 kcal/mol, and 0.64 kcal/mol is a commonly used empirical estimate.
- When the binding pose comes from docking rather than a co-crystal structure, the error comes mainly from the pose and not from the free-energy method itself.

## Example: relative binding free energies of a congeneric ligand series to a kinase

Relative binding free energies between congeneric ligands are the routine basis on which medicinal chemistry decides which compound to make next. A large public retrospective assessment ran free-energy perturbation on eight targets (BACE, CDK2, JNK1, MCL1, p38, PTP1B, thrombin and TYK2), 199 ligands and 330 perturbations: the RMSE per target was 0.93–1.41 kcal/mol, the errors of the 330 perturbations followed approximately a normal distribution of standard deviation 1.1 kcal/mol, 63% of the perturbations were within 1.0 kcal/mol, and only 9 of the 199 ligands differed from experiment by more than 2 kcal/mol. The TYK2 series within it holds 16 ligands and 24 perturbations, with experimental binding free energies spanning 4.3 kcal/mol. The task asks the solving agent to carry out this calculation independently on a congeneric series whose experimental values are not given.

The following is illustrated for the Prediction class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives the protein structure, the two-dimensional structures and stereochemistry of the ligands, the force field and water model, the temperature and the ion concentration, and the required accuracy; it gives no experimental values, no perturbation network and no published predictions. The deliverables are the relative binding free energy of each edge with its uncertainty, the binding free energy of each ligand obtained by solving the network, all input files and trajectory summaries, the comparison results on the sensitivity to settings, and a short report. The format of the numerical files is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Changes of substituents in the hydrophobic pocket: the change in binding free energy on enlarging a ring or replacing a substituent.
  2. Substitutions involving hydrogen bonds and charges: the introduction and removal of polar groups, and the protonation-state questions that come with them.
  3. Substitutions that displace an active-site water: the change in binding free energy when a substituent reaches into a pocket occupied by water.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the target quantity as defined in the task statement; the true value is not provided to the solving agent. The deliverable is the prediction with its uncertainty, as text (the choice of force field and water model with an argument that they apply to this class of substitution, where needed compared with a higher-level method on a small system) and as computation (the relative binding free energy of each edge, convergence in the number of λ windows, simulation length and number of repeats, sensitivity analysis on protonation states, water model and network topology, which is the ablation of the Prediction class, and an uncertainty estimate). The comparison with the held-out experimental values is made by the agent judge.
- **Checks.** The agent judge first checks the validity of system preparation and the cycle closure, then solves the network again from the submitted per-edge values, computes the mean unsigned error and Kendall τ on the held-out ligands and gives confidence intervals by bootstrapping; a few edges are rerun and compared with the values the submitter reports. The tolerance is set from the experimental repeatability (on the order of 0.4–0.7 kcal/mol) and the error of the method itself (RMSE per target 0.93–1.41 kcal/mol), and may not be tighter than the larger of the two.
- **Tiers and scoring.** Building the network and converging each edge form the first tier, the error and ordering on the held-out ligands the second, and the sensitivity analysis on settings the third; completing only the first tier earns the corresponding score. The weights are set by the expert; for illustration: system preparation and topology validity 15, convergence and cycle closure of the edges 25, error on the held-out ligands 25, ordering 15, sensitivity analysis 10, report 10.
- **Calibration cases.** The empty submission (score 0); published predictions or experimental values copied without input files and per-edge values (a shortcut; the corresponding values score 0); an ordering from docking scores or MM-GBSA (a baseline); a submission that completes only some edges or whose cycle-closure error exceeds the threshold (partially correct); the reference computation itself (a known result).
- **Other tasks of the same structure.** Change the target family (proteases, nuclear receptors), or switch to the selectivity of one ligand between two related targets expressed as the difference between two sets of relative binding free energies; the workflow and the checks stay the same.
