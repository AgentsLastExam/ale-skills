# Chemistry: theory and computational methods

This file adds content specific to theory and computational methods to `references/disciplines/chemistry.md`, whose provisions still apply.

Scope: the development and benchmarking of electronic-structure methods (density functionals, wavefunction methods, strong-correlation methods), the construction and testing of force fields and machine-learned potentials, enhanced sampling and free-energy methods, cheminformatics and property-prediction models, and chemistry algorithms for quantum computers. Tasks that use these methods to answer a specific chemical question belong to the corresponding applied direction: for reaction mechanisms and selectivity see `mechanism-properties.md`, for rates and spectra see `structure-dynamics.md`, for protein–ligand binding free energies see `life-processes.md`, for retrosynthesis and reaction-prediction models see `synthesis.md`; for universal potentials aimed at crystals and materials properties see `references/disciplines/materials.md`.

## Screening criteria

- Build with priority: the accuracy and extrapolation of machine-learned potentials, for example training a potential for a flexible organic molecule on a few hundred first-principles configurations and then testing its error at higher temperature and on unseen configurations. Training and testing both fit on one GPU, the agent judge can recompute the energy and force errors directly, and published results on benchmarks such as 3BPA and rMD17 serve as baselines.
- Build with priority: more accurate density functionals and strong-correlation methods, for example lowering the error for one class of properties (barrier heights, non-covalent interactions) on a public benchmark set. The benchmark sets are public and the error can be quantified directly; for small strongly correlated systems (the hydrogen chain, the full configuration interaction energy of benzene) there are reference values on which several high-accuracy methods agree.
- Build with priority: the efficiency of enhanced sampling and free-energy methods, for example reproducing the free-energy surface of a model system such as alanine dipeptide with less sampling under a fixed force field. The reference comes from long sampling, and both the metric and the constraints can be recomputed.
- Defer: chemistry algorithms for quantum computers, for example circuit design for the variational quantum eigensolver. Such algorithms can be verified only for small systems on classical simulators, and an advantage on large systems cannot be judged. The question can be recast by fixing the molecule, basis set and number of qubits in advance, taking exact diagonalization as the reference, and asking for the energy error at a given circuit depth or number of measurements.
- Defer: questions whose goal is "a universal functional or universal potential better than existing models across the board". The conclusion depends on the choice of benchmarks, overlap between training data and test sets is hard to exclude, and the compute needed for training is far beyond the size of one task. The question can be recast as a sub-problem with the training set, test set and compute budget fixed in advance.

## Matters to confirm in conversation

- The definition of the metric: MAE or RMSE; energies per molecule or per atom, forces per component or by magnitude; units; how several subsets are weighted.
- The level and source of the reference data: whether reference values are high-accuracy computations or experimental values; whether the training and test sets come from the same settings (functional, basis set, convergence thresholds).
- The boundary of the training data: whether additional labels are allowed and how many first-principles calculations; whether pretrained models are allowed, and whether their training data covers the target system.
- The distribution of the tests: the composition of the in-distribution test set, and the direction of the extrapolation tests (higher temperature, unseen dihedral angles, bond breaking, larger systems).
- The current best result and the baseline: where they come from, whether the training conditions are comparable, and the variation between repeated training runs.
- The constraints to be kept: energy conservation (forces as derivatives of the energy), symmetry, inference time and model size, and the original accuracy.
- The criteria at the level of simulation: the definition of stability (duration, temperature, threshold on bond-length deviation), and the observables to be reproduced with their tolerances.

## Checking templates

The templates below add to the general templates in `references/disciplines/chemistry.md`.

| Template | Criterion | Scope |
|---|---|---|
| Re-evaluation on held-out configurations | The agent judge loads the submitted model and recomputes the energy and force errors on test configurations that are not public; the metrics the submitter reports are not used | Pure computation, must pass |
| Extrapolation tests | Errors are recomputed on test sets outside the training distribution (configurations at higher temperature, dihedral scans, bond stretching), and the potential-energy curves are checked to be smooth and free of unphysical minima | Pure computation, scientific discovery level 2–3 |
| Simulation stability and conservation | The agent judge runs molecular dynamics of a given length with the submitted model: the total energy does not drift in the microcanonical ensemble; no unphysical events occur, such as a bond length deviating from its equilibrium value by more than a threshold; observables such as radial distribution functions and vibrational spectra agree with the reference trajectory | Pure computation, counts for part of the score |
| Recomputation on a benchmark set | For electronic-structure method tasks: the agent judge reruns the submitted implementation on a sampled part of the benchmark set, checks the per-subset errors the submitter reports, then aggregates the weighted error and compares it with the baseline | Pure computation, scientific discovery level 2–3 |
| Exact limits and constraints | The new method agrees with full configuration interaction on small systems that can be solved exactly; it satisfies the properties to be kept, such as size consistency and rotational and permutational invariance | Pure computation, must pass |
| Generalization to held-out systems | Re-evaluated on molecules or chemical space not used in development (split by scaffold or by time), the improvement still holds | Pure computation, or uses existing data |
| Rerun of the ablation | The agent judge reruns the version with one improvement removed and checks that the contribution of that improvement to the metric agrees with the submitted attribution | Pure computation, counts for part of the score |

## Sources of existing data

- Benchmarks for machine-learned potentials: rMD17 (ten small organic molecules); the 3BPA and acetylacetone datasets (trained at 300 K, tested at higher temperature and on dihedral scans); SPICE (drug-like small molecules, dipeptides and related systems; version 2.0 holds more than 2 million conformations with energies and forces, and its data are released under CC0).
- Electronic-structure benchmarks: GMTKN55 (55 subsets), BH9, QUESTDB (excitation energies); for strong correlation, the multi-method comparison on the hydrogen chain and the blind test on the ground-state energy of benzene.
- Free energies and property prediction: FreeSolv (experimental and calculated hydration free energies, CC-BY 4.0); the inputs and results of the SAMPL series of blind challenges; the property datasets collected in MoleculeNet and Therapeutics Data Commons.
- The reference values of the potential and electronic-structure benchmarks above are computed, so they count as pure computation, not existing data; FreeSolv, SAMPL and the property-prediction datasets contain experimental values and count as existing data.

## Preventing answer leakage

- The test configurations and labels of public benchmarks can be downloaded, so training or tuning on the test set lowers the error. The test configurations used in review are generated separately by the expert with the same settings and are not public; the public test set is for the solving agent's development only.
- The published errors of models on public benchmarks are not a basis for scoring; the agent judge loads the submitted model and recomputes.
- The training data of a pretrained model may already cover the target molecule or benchmark subsets. The task statement says whether pretrained models are allowed; if they are, switch to a molecule absent from their training sets, or list the pretrained model separately as a baseline.
- For functional and method development tasks: parameters fitted on a benchmark set and errors then reported on the same set constitute leakage. Hold out several subsets from the fitting.
- Property-prediction tasks are split by scaffold or by time, with duplicate and near-duplicate structures removed between the training and test sets.

## Tools and compute

- Machine-learned potentials: MACE and NequIP (equivariant graph neural networks, MIT license), DeePMD-kit; the molecular dynamics interfaces are ASE, LAMMPS and OpenMM.
- Labeling and electronic structure: PySCF and Psi4 (open source), xtb; the functional library Libxc; for strong correlation, Block2 (DMRG) and the full configuration interaction module of PySCF.
- Enhanced sampling and free energies: PLUMED (open source; input files can be deposited in PLUMED-NEST for reproduction), OpenMM, GROMACS.
- Cheminformatics: RDKit, scikit-learn, Chemprop, DeepChem.
- Classical simulation of quantum algorithms: Qiskit, PennyLane, OpenFermion.
- Compute: training an equivariant potential for a single molecule on a few hundred configurations takes hours to a day on one GPU; during review, recomputing the errors takes minutes and the molecular dynamics of the stability test tens of minutes to hours; evaluating a functional on a complete benchmark set takes thousands of single-point calculations. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Test and training sets taken from neighboring frames of the same trajectory; the samples are correlated and the in-distribution error is underestimated.
- Force errors used in place of checks at the level of simulation. Benchmark studies have shown that models with similar force MAE can differ severalfold in how long they stay stable, and that the model with the lowest force error may become unstable within tens of picoseconds.
- A model that predicts forces directly instead of differentiating the energy does not guarantee energy conservation, and the energy drifts in microcanonical simulation.
- The original MD17 used. Its energies contain numerical noise, and the field has moved to rMD17, recomputed with tighter settings.
- Inconsistent units and normalization (kcal/mol and meV, per molecule and per atom, MAE and RMSE), so that a comparison with published values is off by a factor of several without being noticed.
- A potential trained on DFT data tested against experimental values. Whether the deviation comes from the reference method or from the fit cannot be told; the two must be tested separately.
- The result of a single training run compared with the baseline. The variation from random seeds can be as large as the improvement; train several times and state the spread.
- Errors of a functional reported on the benchmark used to fit its parameters; or the deviation from an incomplete basis set counted as method error while the reference values are at the complete basis set limit.
- Property-prediction datasets containing invalid structures, duplicate entries with contradictory labels and undefined stereocenters; a random split puts the same scaffold in both the training and the test set.

## Example: training a machine-learned potential and testing its extrapolation

The 3BPA benchmark tests the extrapolation of potentials on the flexible drug-like molecule 3-(benzyloxy)pyridin-2-amine (27 atoms, 3 rotatable bonds): the training set is 500 configurations taken from a molecular dynamics trajectory at 300 K, and the test sets come from trajectories at 300 K, 600 K and 1200 K and from dihedral scans. In published results the force RMSE fell from 27.1 meV/Å for linear ACE to 8.8 meV/Å for MACE on the 300 K test set, and from 187.0 meV/Å to 62.0 meV/Å on the 1200 K test set; for one and the same model the force error grows about sevenfold from 300 K to 1200 K. Benchmark studies have also shown that force error and simulation stability do not go together. The task asks the solving agent, with the training data fixed, to bring the error of the potential on the extrapolation tests below the best published result and to keep long simulations stable.

The following is illustrated for the Development class; the class is assigned by the expert. Scientific discovery level 3, physical-world observation level 0.

- **Task statement and deliverables.** The task statement gives the 500 training configurations with their energies and forces, the settings of the reference computation, a public test set for development and the training script of the baseline model; it states that no first-principles labels may be added and no pretrained model may be used, and it gives an upper limit on inference time. The test configurations used in review are generated separately by the expert with the same settings and are kept only in `tests/`. The deliverables are the model file, a uniform interface for calling energies and forces, the training script and logs, the ablation results and a short report. The calling interface is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Model architecture: the effect of the treatment of symmetry (equivariant features), the body order and the cutoff radius on the in-distribution and extrapolation errors.
  2. Training procedure: the effect of the loss weights on energies and forces, data augmentation and regularization on the error for high-temperature configurations.
  3. Physical priors and stability: the effect of short-range repulsion, a smooth cutoff and energy conservation on the dihedral potential-energy curves and on long simulations.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the part of the existing method the sub-question concerns, with the metric and the constraints to be maintained. The deliverable is the improvement and its contribution to the metric, as text (why the improvement lowers the extrapolation error, and why the constraints to be kept still hold) and as computation (the improved model and its metric; the metric obtained by retraining with the improvement removed, which is the ablation). The agent judge recomputes the metric and checks the constraints.
- **Checks.** The agent judge loads the submitted model, recomputes the energy and force RMSE on the non-public configurations at 300 K, 600 K and 1200 K and on the dihedral scans, checks that the forces are derivatives of the energy, then runs molecular dynamics of a given length at a given temperature and records the time at which a bond length first deviates from its equilibrium value by more than 0.5 Å and the energy drift in the microcanonical ensemble. The main metric is the force RMSE on the 1200 K configurations; the values for the baseline and for the current best model are obtained by the agent judge on the same test configurations, and an improvement counts only when it exceeds the spread of three independent training runs. One ablated version is drawn and retrained as a check.
- **Tiers and scoring.** The mapping to a score is set by the expert; for illustration: the baseline model corresponds to a low score, reaching the current best result to a middle score, and the margin beyond it enters the rest of the score through a continuous function; a submission that violates a constraint (added labels, a pretrained model, inference time over the limit, non-conservative forces) earns no score for improvement.
- **Calibration cases.** The empty submission (score 0); the baseline model (a baseline); the current best model trained with the published settings (a known result); a model trained on the public test set, with a very low error there and no improvement on the held-out configurations (a shortcut); a model that predicts forces directly, with a lower error but no energy conservation (a higher metric that violates a constraint); a model whose in-distribution error is lower while its 1200 K error and stable duration show no improvement (partially correct).
- **What passing does not show.** The checks above form a proxy verifier and are only a set of necessary conditions: a lower error on the held-out configurations and a simulation that stays stable for the given duration show that the potential is closer to the reference computation within the tested range of configurations of this molecule; they do not show that it is equally reliable for free-energy surfaces, rare events or other molecules, nor that the reference computation itself agrees with experiment. Whether the improvement is significant as a method and whether it generalizes are for the expert to judge.
- **Other tasks of the same structure.** Change the system (hydrogen transfer in acetylacetone, liquid water) or the metric (inference speed at fixed accuracy); the workflow and the checks stay the same.
