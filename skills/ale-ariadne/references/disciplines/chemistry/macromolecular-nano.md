# Chemistry: macromolecular, supramolecular and nanochemistry

This file adds content specific to macromolecular, supramolecular and nanochemistry to `references/disciplines/chemistry.md`, whose provisions still apply.

Scope: polymer synthesis and control of chain structure, polymer physics and characterization (phase separation, crystallization and the glass transition, rheology), host–guest chemistry and molecular recognition, molecular self-assembly, and the formation of nanostructures and the role of surface ligands. For biological macromolecules such as proteins and nucleic acids see `life-processes.md`; for porous framework materials, functional inorganic materials and device properties see `references/disciplines/materials.md`; for the development and benchmarking of force fields, coarse-grained models and enhanced sampling themselves see `theory-computation.md`; for chemical reactions in colloids and at interfaces see `systems-solutions.md`.

## Screening criteria

- Build with priority: prediction of host–guest binding constants, for example the binding free energies of a cucurbituril or a deep-cavity cavitand with a set of guests. The input structures, submissions and experimental values of the successive blind challenges are public, the experimental values come from isothermal titration calorimetry with small uncertainties, the systems hold only tens to hundreds of atoms and fit on a single GPU, and a public null model exists to serve as a baseline.
- Build with priority: phase diagrams of block copolymers, for example where a symmetric diblock copolymer passes from disorder to lamellae. Self-consistent field theory is mature, the phase regions are set by two quantities, the interaction parameter and the volume fraction, and open-source implementations and experimental phase diagrams exist to compare against.
- Defer: the pathway and final morphology of molecular self-assembly, for example whether an amphiphile forms vesicles or micelles from solution. Coarse-grained simulation is feasible, but the result depends on the bead mapping and the interaction parameters, and whether the morphology has reached equilibrium is hard to judge. Discuss with the expert fixing the coarse-grained model and its parameters in advance and asking only for a phase boundary or a free-energy difference within that model, or switching to a comparison with experimental scattering peak positions rather than scoring on how a morphology is read off.
- Defer: prediction of the glass transition temperature. Simulated cooling rates are many orders of magnitude faster than experiment, so the value has to be extrapolated, different extrapolations differ appreciably, and the experimental value itself shifts with the measurement rate. Switch to an ordering or a difference within a series of polymers, with the sequence of cooling rates and the fitting procedure fixed in advance. The same holds for the depolymerization chemistry of recyclable polymers: bond-breaking barriers can be computed, while the actual depolymerization conditions depend on catalyst, temperature and mass transport and should not be the only basis for scoring.
- Defer: the growth mechanism of nanocrystals and the role of surface ligands. The conclusion depends strongly on synthesis conditions, and judging it requires new synthesis and characterization, which cannot be done within six hours.

## Matters to confirm in conversation

- The protonation states and net charges of host and guest, and how the experimental pH and buffer salt are handled.
- How the experimental values were measured (direct titration, competitive titration or NMR), the temperature and buffer composition, and whether the stoichiometry is 1:1.
- The convention for converting between a binding constant and a binding free energy, and the standard state.
- The mapping of the coarse-grained model and where its interaction parameters come from, and how far the conclusion depends on them.
- The chain length, dispersity and topology of the polymer system, the gap between the simulated chain length and the experimental sample, and whether entanglement is represented.
- The thermal history: cooling or heating rate, annealing time, and how these correspond to the experimental measurement conditions.
- The type of characterization data (scattering curve, thermal analysis trace, micrograph) and how the phase structure is judged from it.
- The form of the conclusion: an absolute binding free energy, an ordering within one host, or the position of a phase boundary; what the tolerance rests on (experimental uncertainty, spread between repeat runs, spread between parameter sets).

## Checking templates

The templates below add to the general templates in `references/disciplines/chemistry.md`.

| Template | Criterion | Scope |
|---|---|---|
| Recomputation of the binding free energy | With the force field, water model and ion concentration fixed in the task statement, the agent judge recomputes the binding free energy for a sample of host–guest systems and compares with the values the submitter reports | Pure computation, scientific discovery level 1–2 |
| Comparison with blind-challenge experimental values | On guests whose experimental values are held out, the RMSE, mean unsigned error and rank correlation are computed and compared with the null model on the same dataset; confidence intervals are given by bootstrapping | Uses existing data, scientific discovery level 2–3 |
| Systematic bias check | Whether the mean of the differences between predicted and experimental values departs significantly from zero. Common force-field combinations generally give too strong binding for host–guest systems, and this bias must be reported separately rather than folded into the random error | Uses existing data, counts for part of the score |
| Re-solution of the self-consistent field equations | The self-consistent field equations are solved again from the submitted interaction parameters and chain structure, the free energies of the candidate phases and the phase boundaries are compared, and the dependence of the solution on the initial field and the unit-cell parameters is checked | Pure computation |
| Comparison with scattering curves | A scattering intensity curve is computed from the submitted structure or morphology and compared with the ratios of the peak positions of an experimental small-angle scattering curve, rather than by matching micrographs | Uses existing data |
| Equilibrium and convergence check | The second half of the sampling gives the same conclusion as the first; the conclusion is unchanged after changing the initial configuration or the random seed; the chain relaxation time of a polymer system is shorter than the sampling time | Pure computation, must pass |
| Consistency of thermal history | The glass transition temperature is recomputed with the sequence of cooling rates fixed in the task statement and extrapolated by the agreed procedure; the conclusion is expressed as a difference within a series rather than as a single absolute value | Pure computation, counts for part of the score |

## Sources of existing data

- Blind challenges: the host–guest datasets of the successive SAMPL rounds. The series has included a host–guest component since its third round, and the hosts across the rounds include cucurbit[7]uril and cucurbit[8]uril, the Gibb deep-cavity cavitands OA and TEMOA, cyclodextrins and their derivatives, and the pillar[6]arene WP6; input structures, all submissions and experimental values are in public repositories; the repositories of the recent rounds put the code under MIT and the remaining materials under CC BY 4.0, while the earlier ones state MIT alone.
- Curated host–guest benchmarks: Taproom, holding 126 host–guest complexes (α- and β-cyclodextrin, cucurbit[7]uril and cucurbit[8]uril, OA and TEMOA) with their experimental values, under MIT.
- Binding data: the separately listed host–guest datasets of BindingDB; SupraBank (curated intermolecular interaction data, open to view, with registration required to download or to contribute, and entries checked for plausibility).
- Polymer properties: PoLyInfo from NIMS, polymer property data curated from the literature, with registration required, bulk scraping prohibited and no redistribution without permission.
- Cases where the reference values are themselves computed: the "right answers" of self-consistent field phase diagrams and of coarse-grained simulations come from computation, so such tasks are pure computation and not existing data.

## Preventing answer leakage

- Once a blind challenge closes, the experimental values and all submitted predictions become public. Switch to guests that the public datasets do not contain, or ask for quantities the datasets do not hold (the separation of binding enthalpy and entropy, free-energy differences between protonation states).
- The task statement contains no common names of hosts and guests, no challenge round names and no compound IDs; structures are supplied as coordinates and SMILES.
- Make the raw computed results, input files and trajectories of each system the object of scoring, not the statistics the submitter reports.
- Values in polymer property databases can be looked up directly. Switch to copolymer compositions or chain structures the databases do not contain, or split by publication date.
- The training sets of general machine-learned potentials and property-prediction models may already contain the target system; check before using one as a baseline.

## Tools and compute

- Molecular simulation and free energy: GROMACS, OpenMM, LAMMPS (open source); AmberTools is open source, while pmemd carries a separate license, is free for non-commercial use and may not be redistributed; the attach-pull-release workflow is available in pAPRika (BSD license).
- Coarse graining and soft matter: HOOMD-blue (BSD license, with both molecular dynamics and hard-particle Monte Carlo); the Martini force field, which maps about four heavy atoms to one bead.
- Self-consistent field and field-theoretic simulation: PSCF (GPL license, supporting two- and three-dimensional periodic structures and all space groups, with a GPU version).
- Polymer modeling and property calculation: RadonPy (BSD license, which computes properties of amorphous polymers automatically with LAMMPS and Psi4); RDKit for handling molecular and polymer structures.
- Reporting of results: cinnabar, which gives the error and correlation statistics of free-energy results with their confidence intervals on a common basis.
- Compute: an absolute binding free energy for one host–guest system takes on the order of hours to a day on a single GPU, and a round of a dozen or more guests is on the order of hundreds of GPU-hours; coarse-grained self-assembly simulations need a longer accumulated time; a self-consistent field calculation takes minutes to hours on an ordinary computer; the review can recompute only a few systems. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Buffer salt and ionic strength left out. Host–guest systems are extremely sensitive to them, and ignoring buffer ions can shift results by several kcal/mol.
- A protonation state of host or guest chosen wrongly. Protonation of carboxylates at high pH and deprotonation of a guest nitrogen can both change the conclusion, and several protonation states often lie close in energy.
- Common force-field combinations give too strong host–guest binding across the board; this is a known systematic bias, to be reported separately and not treated as random error.
- Systems whose stoichiometry is not 1:1 (ternary complexes, guest dimerization) treated as 1:1.
- A guest adopts several orientations in the cavity, and starting from a single orientation makes the result depend on the initial configuration.
- Dewetting and fluctuations in the number of waters inside the host cavity occur on nanosecond timescales, so the result is unstable when sampling is insufficient.
- A morphology read off a coarse-grained simulation before it has reached equilibrium, where changing the random seed gives a different morphology.
- Simulated cooling rates far above experiment, which make the glass transition temperature systematically too high; compared with experimental values without extrapolation.
- Simulated chain lengths far shorter than the experimental sample, so that entanglement and dispersity cannot show their effects.

## Example: blind prediction of host–guest binding free energies

Supramolecular host–guest systems are the standard object for testing binding free-energy methods: the systems hold only tens to hundreds of atoms, and the experimental values come from isothermal titration calorimetry with uncertainties usually no larger than 0.1 kcal/mol. In one public blind round the hosts were octa-acid (OA), tetra-endo-methyl-octa-acid (TEMOA) and cucurbit[8]uril (CB8): OA and TEMOA shared 8 guests and CB8 had a further 14; the measurements were made at 298 K, OA and TEMOA in 10 mM sodium phosphate buffer at pH 11.7 and CB8 in 25 mM sodium phosphate buffer at pH 7.4; the experimental values spanned 4.25 kcal/mol for OA and TEMOA together and 7.05 kcal/mol for CB8. Ten groups submitted 119 entries in all; the median RMSE of the entries on OA and TEMOA was 2.76 kcal/mol, only slightly better than the 3.00 kcal/mol of the previous round; every method using one common set of force fields without empirical correction gave stronger binding than experiment; and modeling the buffer ions explicitly from the experimental buffer composition lowered the RMSE on one host from 7.9 to 5.1 kcal/mol. The task asks the solving agent to beat the public baseline under the fixed experimental conditions.

The following is illustrated for the Development class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives the structures of hosts and guests, the buffer composition, the temperature and the pH, the definition of the metric (RMSE and rank correlation on held-out guests) and the baseline (a null model that redocks and rescores with MM-GBSA), together with the constraints to be maintained (one force-field setting throughout, the same set of guests, the number of repeat runs); it gives no experimental values and no published predictions. The deliverables are the binding free energy of each guest with its uncertainty, all input files and trajectory summaries, the comparison before and after each improvement, and a short report. The format of the numerical files is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Protonation states and net charges: the states used and what they rest on, and the result with another state instead.
  2. Buffer salt and ionic strength: the experimental buffer composition modeled explicitly, with results both with and without buffer ions.
  3. Binding pose and cavity water: the orientation of the guest in the cavity and the fluctuation in the number of waters, and whether the sampling is sufficient.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the part of the existing method the sub-question concerns, with the metric and the constraints to be maintained. The deliverable is the improvement and its contribution to the metric, as text (why this treatment raises the metric, and why constraints such as the force-field setting and the amount of sampling still hold) and as computation (the improved method and its metric; the metric with this treatment removed, for example without buffer ions, with a single fixed orientation, or with only one random seed, which is the ablation and establishes each treatment's contribution to the overall gain). The agent judge reruns and recomputes the metric; the values the submitter reports are not used.
- **Checks.** The agent judge recomputes the RMSE, mean unsigned error and Kendall τ on the held-out guests and gives confidence intervals by bootstrapping; it checks whether the mean of the differences between predicted and experimental values departs from zero; and it reruns a sample of systems to see whether the spread between repeat runs agrees with the uncertainty stated in the submission. The metric must exceed the null model and is compared with the best published result on that dataset, with the expert setting the level that earns full marks. The tolerance is set from the experimental uncertainty (no larger than 0.1 kcal/mol) and the spread between repeat runs, and may not be tighter than the latter.
- **Calibration cases.** The empty submission (score 0); published experimental values or published predictions copied without input files and trajectories (a shortcut, score 0); the null model that redocks and rescores with MM-GBSA (a baseline); a method that holds on some guests but fails on the held-out ones (partially correct); the best-performing public submission on that dataset (a known result).
- **Other tasks of the same structure.** Change the host family (cyclodextrins and their derivatives, pillar[6]arenes), or switch to reproducing the position of a phase boundary in a block copolymer phase diagram; the workflow and the checks stay the same.
