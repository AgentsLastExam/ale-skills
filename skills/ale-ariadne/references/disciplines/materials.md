# Materials

## Screening criteria

- Build with priority: the target is a quantity in a structure–property relationship that can be computed or has been measured (formation energy, band gap, elastic constants, ionic conductivity, phase stability, adsorption energy), and it is clear whether the reference value is measured or computed.
- Build with priority: design and screening tasks with a scoring program fixed in advance and not changed afterwards, and a well-defined candidate space.
- Defer: properties that depend strongly on processing and microstructure when the task statement cannot supply that information; tasks that need synthesis and characterization taking more than six hours to be judged (physical-world observation level 3); reference values that exist only as the result of a single functional.

## Matters to confirm in conversation

- Whether the reference value is measured or comes from a computed database. If computed, which functional, with or without U, with or without spin–orbit coupling.
- How the structure is fixed: the experimental structure or the relaxed one, and whether there is disorder, defects or surface reconstruction.
- The temperature and pressure conditions, and how a 0 K computed value is compared with a room-temperature measurement.
- How strongly the property depends on the sample (single crystal, polycrystal, thin film, doping, grain size).
- What the scoring tolerance is based on: the scatter of experimental values, or the error of the computational method.
- How stability is defined: within how many meV/atom of the convex hull counts as stable.

## Checking templates

Most templates below are implemented as numerical-check scripts that the agent judge calls; where the conclusion can be written as a Lean statement in advance, the agent judge checks it with the Lean tool; derivations, explanations and arguments are reviewed by the agent judge directly against the rubric. See `references/agent-judge.md`.

| Template | Criterion | Scope |
|---|---|---|
| DFT recomputation | The agent judge relaxes or runs a single point on the submitted structure with fixed settings (functional, pseudopotentials, k-points, cutoff energy) and computes the formation energy and the distance from the convex hull | Pure computation, scientific discovery level 2–3 |
| Convergence and stability checks | k-points and cutoff energy are converged; the phonon spectrum has no imaginary frequencies; the elastic constants satisfy the mechanical stability conditions | Pure computation. Must pass, or counts for part of the score |
| Structure validity check | Symmetry, interatomic distances and charge balance are reasonable; structures are matched against known ones to remove duplicates | Pure computation, or uses existing data. Must pass |
| Comparison with measured data | Predicted values are compared with held-out measurements (band gap, conductivity, mechanical and thermal properties) | Uses existing data |
| Interpretation of characterization data | Given raw XRD or spectroscopy data, the answer is compared with the known phases or refinement results | Uses existing data, scientific discovery level 1–2 |
| Optimization metric | Find a material with better properties in the candidate space; the agent judge recomputes with a program fixed in advance, and the score follows the margin above the baseline | Scientific discovery level 3 |

## Sources of existing data

For materials, first separate two kinds of database, because they correspond to different physical-world observation levels.

- Measured databases (count as existing data): ICSD (commercial license), the Crystallography Open Database, Pauling File/MPDS (commercial), MatNavi from NIMS in Japan, the experimental band gap subset of Matbench, and tables in papers.
- Computed databases (count as pure computation, not existing data): Materials Project, OQMD, AFLOW, JARVIS-DFT, NOMAD, Alexandria, and OC20 and OC22 for catalysis.

## Preventing answer leakage

- Entries in computed databases can be queried directly through an API. Cut the environment off from the network, or leave these databases off the allowlist; or choose compositions and structures that are not in them.
- Split measured data by publication date.
- The task statement does not give the material's ID in any database.
- The training set of a universal machine-learned potential may already contain the target structure. Check before using one as the agent judge or the baseline.

## Tools and compute

- Structure handling: pymatgen, ASE, spglib.
- First principles: Quantum ESPRESSO, ABINIT, CP2K, GPAW (open source); VASP needs a commercial license, and its pseudopotentials may not be redistributed.
- Phonons and dynamics: phonopy, LAMMPS.
- Machine-learned potentials: MACE, CHGNet, M3GNet.
- Diffraction refinement: GSAS-II.
- Compute: a DFT relaxation of one structure takes a few to a few tens of CPU core-hours; phonons and hybrid functionals cost an order of magnitude more; long molecular dynamics and machine-learned potentials need GPUs.

## Common pitfalls

- Treating a computed database as ground truth; for example, band gaps computed with PBE are systematically too low.
- Comparing a 0 K computed value directly with a finite-temperature measurement.
- Energies from different pseudopotentials and settings cannot be compared directly; a convex hull must be computed with one consistent set of settings.
- Measured values for the same material vary widely from sample to sample.
- Metastable phases and disordered structures handled incorrectly.
- Licensing: VASP pseudopotentials and ICSD data cannot be packaged into a task.
