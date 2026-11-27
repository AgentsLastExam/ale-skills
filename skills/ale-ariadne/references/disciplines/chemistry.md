# Chemistry

## Subdomains

The directions of chemistry differ widely in their objects of study, tools and ways of verification. This file gives what is common to all of them. Once the expert has described the research problem, pick the subdomain file from the table below and read it as well; the files are in `references/disciplines/chemistry/`. A subdomain file only adds what is specific to that direction (screening examples, checking templates, data sources, tools, pitfalls and a worked example); it does not alter the provisions of this file. When a problem spans two subdomains, read both files; when it is unclear where a problem belongs, ask the expert to say. Record the chosen subdomain under "Discipline" in the problem card.

| Subdomain | Scope | File |
|---|---|---|
| Catalysis | Active sites, mechanisms, activity and selectivity in heterogeneous, homogeneous, electro- and photocatalysis | `catalysis.md` |
| Mechanism and properties | Physical organic and physical inorganic chemistry: distinguishing reaction mechanisms, origins of selectivity, structure–property relationships, mechanisms of excited-state and photoredox reactions | `mechanism-properties.md` |
| Structure and dynamics | Reaction kinetics in the gas and condensed phases, rate theory, kinetics of combustion and plasma chemistry, assignment of molecular spectra, ultrafast dynamics | `structure-dynamics.md` |
| Synthesis | Organic, inorganic and organometallic synthetic methods, total synthesis, retrosynthetic route design, prediction of reaction conditions and yields | `synthesis.md` |
| Measurement and imaging | Analytical chemistry: separation, mass spectrometry, spectroscopic analysis, surface and materials analysis, electroanalysis and sensing, chemometrics, and structure elucidation from spectra | `measurement-imaging.md` |
| Systems and solutions | Chemistry in complex systems: reactions in the atmosphere, water and soil, reactions at interfaces, transport and degradation of pollutants, thermodynamics of solutions and electrolytes | `systems-solutions.md` |
| Theory and computational methods | Development and benchmarking of electronic-structure methods, force fields and machine-learned potentials, enhanced sampling and free-energy methods, cheminformatics and property-prediction models | `theory-computation.md` |
| Chemistry of life processes | Chemical biology, enzyme catalysis and enzyme engineering, protein–ligand interactions, drug molecules, bioinorganic chemistry | `life-processes.md` |
| Macromolecular, supramolecular and nanochemistry | Polymer synthesis, polymer physics and characterization, host–guest chemistry and self-assembly, nanostructures | `macromolecular-nano.md` |

For solid-state chemistry, electrochemical energy storage, porous framework materials and functional inorganic materials, see `references/disciplines/materials.md`.

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

For computational tasks, the toolchain, the compute and the way of checking depend mainly on the computational workflow the solving agent actually carries out. Numerical-check scripts and the agent judge's materials can be reused within one type of workflow; a task may pass through two types in succession, for example periodic first-principles calculation followed by microkinetics.

| Computational workflow | What the solving agent does | Typical tools | Usual way of checking | Approximate size of one task |
|---|---|---|---|---|
| Molecular electronic structure | Computes energies, structures and transition states of molecules | PySCF, Psi4, ORCA, xtb | Comparison with experimental barriers, selectivities and spectra | Tens of atoms, tens to a hundred or more quantum chemistry calculations, about a day on a workstation |
| Periodic first-principles calculation | Computes energies and properties of surfaces and crystals | Quantum ESPRESSO, GPAW, ASE | Recomputation on the submitted structures, then comparison with the reference computation and with published adsorption energies, barriers and band gaps | A periodic model of twenty to thirty atoms, tens of structures and several transition states, days to one or two weeks on a CPU cluster |
| Molecular simulation | Molecular dynamics and Monte Carlo simulation | GROMACS, OpenMM, LAMMPS, RASPA | Comparison with experimental free energies and adsorption isotherms | Tens of thousands of atoms, hundreds of simulation segments, about a week on one GPU |
| Kinetics and multiscale modeling | Derives macroscopic rates or morphology from microscopic data | CatMAP, Cantera, pycalphad | Comparison with experimental rates, turnover frequencies and phase diagrams | Atoms are not tracked; tens to hundreds of simulations, minutes on an ordinary computer |
| Data-driven | Trains potentials, predicts properties, screens molecules or materials | MACE, CHGNet, RDKit, pymatgen | Scoring on a benchmark set or a held-out test set | About a thousand training configurations and one training run, about a day on one GPU |
| Interpretation of experimental data | Infers structures from spectra or diffraction data | Public spectral libraries and interpretation programs | Checking against the known structures one by one | A set of tens of unknowns, hours on an ordinary computer |

The sizes in the table are rough estimates that have not been measured; the measurement in step 2 prevails.

## Common pitfalls

- Incomplete conformer search, leaving energies off by several kcal/mol.
- Inconsistent solvent models and standard-state conversions.
- If the reference value is DFT, the agent judge only judges "agrees with a certain functional", not right or wrong.
- Experimental values from different sources contradict each other.
- Stereochemistry and tautomerism make string comparison mark correct answers wrong.
- Yield data in the literature is biased toward high yields; failed reactions are rarely recorded.
