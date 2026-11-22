# Chemistry

## Screening criteria

- Build with priority: the target is a quantity that can be computed or looked up (a reaction energy, a barrier, a pKa, a spectral peak position, a selectivity, a structure), and there is an experimental value or a high-accuracy computed value to compare against.
- Build with priority: for computational chemistry tasks, the system is small enough for high-accuracy methods, or an experimental benchmark exists.
- Defer: tasks that need a new synthesis or new characterization taking more than six hours to be judged (physical-world observation level 3); experimental values reported in a single paper and never repeated; using a quantity as sensitive to experimental conditions as yield as the only basis for scoring.

## Matters to confirm in conversation

- What the target property is, and under what conditions (gas phase or solvent, temperature, pH).
- What accuracy is required, and whether 1 kcal/mol on energy differences is enough.
- Whether the reference value comes from experiment or computation. If computation, which method and basis set, and whether the field accepts it.
- How conformers, protonation states, tautomers and spin states are fixed.
- How a molecule must be represented to count as the same answer (SMILES canonicalization, stereochemistry, salts and solvates).
- Which database and version the experimental data comes from, and whether the license allows redistribution.

## Checking templates

Most templates below are implemented as numerical-check scripts that the agent judge calls; where the conclusion can be written as a Lean statement in advance, the agent judge checks it with the Lean tool; derivations, explanations and arguments are reviewed by the agent judge directly against the rubric. See `references/agent-judge.md`.

| Template | Criterion | Scope |
|---|---|---|
| High-accuracy quantum chemistry reference value | The submitted energy or barrier agrees within tolerance with a reference at the level of CCSD(T) at the complete basis set limit | Pure computation, scientific discovery level 1–2 |
| Recomputation on the submitted structure | The agent judge runs single-point and frequency calculations on the submitted structure: a minimum has no imaginary frequency, a transition state has exactly one and connects along the reaction path to the correct reactants and products | Pure computation, scientific discovery level 2–3 |
| Structure equivalence check | Comparison of canonicalized SMILES or InChI, including stereochemistry; a synthesis route is checked step by step for atom conservation and valid valences | Pure computation, or uses existing data |
| Comparison with an experimental database | Predicted properties are compared with held-out experimental values (thermochemistry, spectra, solubility, pKa) | Uses existing data |
| Held-out reactions or spectra | Reaction prediction or spectrum interpretation is judged on reaction outcomes or spectra held out by a split in time | Uses existing data, scientific discovery level 2–3 |
| Optimization metric | Design a molecule or catalyst; it is scored by a scoring program fixed in advance and not changed afterwards (docking, DFT descriptors), which the agent judge recomputes itself; the score follows the margin above the baseline | Scientific discovery level 3 |

## Sources of existing data

- Thermochemistry and benchmarks: NIST Chemistry WebBook, CCCBDB, the ATcT thermochemical tables. The reference values of benchmark sets such as GMTKN55 are computed, so they count as pure computation, not existing data.
- Structures: the Cambridge Structural Database, CSD (needs a license), and the Crystallography Open Database.
- Compounds and activity: PubChem, ChEMBL.
- Reactions: the Open Reaction Database and the USPTO patent reaction set. Reaxys and SciFinder are commercial and cannot be redistributed.
- Spectra: SDBS, MassBank.

## Preventing answer leakage

- The properties of common compounds turn up with one PubChem search. Use compounds or reactions that entered the database after a split in time.
- Or switch to derivatives that are not in the databases, with reference values from high-accuracy computation.
- For spectrum interpretation tasks, use spectra that have not been published.
- The task statement contains no identifier that could be used to look up the answer (CAS numbers, InChIKeys, database IDs).

## Tools and compute

- Molecule handling: RDKit, Open Babel.
- Semi-empirical methods and conformer search: xtb, CREST.
- Quantum chemistry: Psi4, PySCF (open source); ORCA is free for academic use but may not be redistributed; Gaussian needs a commercial license.
- Molecular dynamics and docking: OpenMM, GROMACS, AutoDock Vina.
- Compute: DFT on a medium-sized molecule takes a few to a few tens of CPU core-hours; CCSD(T) reaches only small molecules; machine-learned potentials need GPUs.

## Common pitfalls

- Incomplete conformer search, leaving energies off by several kcal/mol.
- Inconsistent solvent models and standard-state conversions.
- If the reference value is DFT, the agent judge only judges "agrees with a certain functional", not right or wrong.
- Experimental values from different sources contradict each other.
- Stereochemistry and tautomerism make string comparison mark correct answers wrong.
- Yield data in the literature is biased toward high yields; failed reactions are rarely recorded.
