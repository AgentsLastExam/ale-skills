# Chemistry: catalysis

This file adds content specific to catalysis to `references/disciplines/chemistry.md`, whose provisions still apply.

Scope: active sites, reaction mechanisms, activity and selectivity in heterogeneous catalysis, homogeneous catalysis, electrocatalysis and photocatalysis. For enzyme catalysis see `life-processes.md`; for catalytic methods whose purpose is a new synthetic reaction see `synthesis.md`; for the structure and stability of the catalytic material itself see `references/disciplines/materials.md`.

## Screening criteria

- Build with priority: the question comes down to quantities that can be computed on a surface model or a molecular model (adsorption energies, barriers of elementary steps, turnover frequency, limiting potential, selectivity), and single-crystal experiments, microkinetics or published computed values exist to compare against. An example is the active site and rate-determining step of ammonia synthesis and nitrogen fixation: the workflow of surface first-principles calculation followed by microkinetics is mature, and an experimental energy diagram on single-crystal surfaces exists to compare against.
- Build with priority: the conclusion is a relative ordering between crystal faces, metals or reaction routes. A relative ordering is less affected by functional error than an absolute value, for example the ordering of the N₂ dissociation rate on Fe(111), Fe(100) and Fe(110).
- Defer: questions in which the structure of the real active site is uncertain and the conclusion depends on model assumptions, for example low-temperature selective activation of methane; questions in which the treatment of solvent and electrode potential is still disputed in the field, for example the selectivity and overpotential of CO₂ electroreduction and oxygen evolution. For such questions, discuss with the expert a formulation that fixes the model in advance (the active-site structure, the computational hydrogen electrode model) and asks only for conclusions within the model.
- Defer: tasks that use the measured activity, lifetime or deactivation of a supported catalyst as the only basis for scoring. These quantities depend on preparation and test conditions and cannot be measured again within six hours.

## Matters to confirm in conversation

- The catalyst model: crystal face, supercell size, number of layers and of fixed layers, coverage; periodic model or cluster model; whether promoters, supports, defects and steps are included.
- What the active-site structure rests on (characterization evidence, consensus in the literature, or an assumption), and how far the conclusion depends on this model.
- Reaction conditions: temperature, pressure or partial pressures; for electrocatalysis the electrode potential, pH and electrolyte; whether solvent is included and how it is treated.
- The functional and dispersion correction, whether the calculation is spin-polarized, the value of +U, and whether the field accepts this setting.
- The energy reference: how gas-phase molecule energies, zero-point energies and entropy corrections are handled.
- Whether the comparison data comes from single-crystal experiments, supported-catalyst experiments or published calculations, and whether its conditions correspond to the model.
- The form of the conclusion: an absolute rate, a relative ordering or a choice between mechanisms; what the tolerance rests on (spread between functionals, experimental error).
- Whether a conclusion about the mechanism must be supported by microkinetics.

## Checking templates

The templates below add to the general templates in `references/disciplines/chemistry.md`.

| Template | Criterion | Scope |
|---|---|---|
| Recomputation on the submitted structures | With the settings fixed in the task statement, the agent judge computes single-point energies, forces and magnetic moments on the submitted intermediate and transition-state structures: the results agree with the values the submitter reports, and a transition state has exactly one imaginary frequency and connects the correct initial and final states. For a structure that fails, the corresponding values score nothing | Pure computation, must pass |
| Comparison with the reference computation | Adsorption energies and barriers of elementary steps agree within tolerance with the reference computation completed in step 2 under the same settings; the tolerance is set from the spread of energies observed in trial calculations | Pure computation, scientific discovery level 1–2 |
| Relative ordering | The ordering of barriers or activity across crystal faces, metals or routes agrees with the reference computation and with single-crystal experiments | Pure computation, or uses existing data |
| Recomputation of the microkinetics | The agent judge solves the steady-state equations again from the submitted energies: the turnover frequency is within an order of magnitude of the reference computation or of experiment, and the degree of rate control points to the same step | Pure computation, scientific discovery level 2–3 |
| Thermodynamic consistency | The energy changes of the steps in the energy diagram sum to the overall reaction energy; all species use the same energy reference; forward and reverse rate constants satisfy detailed balance | Must pass |
| Limiting potential | For electrocatalysis tasks: from the submitted free energies of the steps, the agent judge recomputes the limiting potential under the computational hydrogen electrode model and compares it with the reference computation | Pure computation |
| Design under a fixed scoring program | A proposed catalyst is scored by a descriptor or microkinetic model fixed in advance, which the agent judge recomputes itself; the score follows the margin above the baseline | Scientific discovery level 3 |

## Sources of existing data

- Computed data: Catalysis-Hub (adsorption energies and barriers of surface reactions, with structures and calculation settings); the OC20 and OC22 datasets of the Open Catalyst Project; the Materials Project (bulk structures). These values are computed, so they count as pure computation, not existing data.
- Experimental comparison: adsorption heats and reaction kinetics on single-crystal surfaces, for example the CE39 benchmark set of 39 experimental adsorption energies; NIST Chemistry WebBook and ATcT (gas-phase thermochemistry).
- Turnover frequencies and overpotentials reported in the literature depend on test conditions and on how they are normalized; check each one before using it for comparison.

## Preventing answer leakage

- Adsorption energies, barriers and energy diagrams are mostly published, so a direct comparison of numbers can be passed by searching. Make the submitted structures the object of scoring: the agent judge recomputes them, and values score only when the energies agree.
- The task statement gives only the calculation settings and pseudopotentials, with no structures, initial guesses or literature values; the results of the reference computation are kept only in `tests/`.
- For systems already in Catalysis-Hub and OC20, the structures can be downloaded directly. Switch to a crystal face, coverage or alloy composition that the databases do not contain, or ask for quantities the databases do not hold (transition states, vibrational frequencies, degree of rate control).
- The task statement contains no paper titles, DOIs or database entry IDs.

## Tools and compute

- Periodic first-principles calculation: Quantum ESPRESSO, GPAW, CP2K (open source); VASP requires a purchased license, issued separately to academic and to commercial users, and is not free for academics either.
- Structure building and transition-state search: ASE (NEB, dimer), Sella.
- Molecular catalysts: xtb and CREST (conformer search), Psi4, PySCF, ORCA.
- Microkinetics: CatMAP, Cantera.
- Machine-learned potentials: MACE, CHGNet and the pretrained models of the Open Catalyst Project can be used for coarse screening of adsorption configurations; final energies come from first-principles calculation.
- Compute: for a surface model of twenty to thirty atoms, solving one task requires computing tens of structures and several transition states, on the order of days to one or two weeks on a CPU cluster, with the transition-state search taking most of the time; the recomputation during review covers only single-point and vibrational calculations and is far smaller than solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- A magnetic system computed without spin polarization, or magnetic moments converged to the wrong solution.
- A molecular precursor state or another adsorption site missed, so the dissociation path that follows is wrong.
- A transition state not confirmed by vibrational analysis, or the highest image of an unconverged NEB taken as the barrier.
- Gas-phase molecule energies, zero-point energies and entropy corrections handled inconsistently, so the energies of the steps cannot be added.
- The step with the highest barrier taken directly as the rate-determining step. The rate-determining step depends on coverage and operating conditions and must be determined by microkinetics.
- A tolerance set tighter than the error of the functional itself. Adsorption energies differ between common functionals, and from experiment, on the order of 0.2–0.3 eV; compare trends against experiment and absolute values against the reference computation.
- No convergence test of the number of layers, the vacuum thickness and the k-points.
- The thermodynamic limiting potential from the computational hydrogen electrode model stated as a measured overpotential.
- Conclusions from a single-crystal model generalized directly to an industrial catalyst.

## Example: the mechanism of ammonia synthesis on Fe surfaces

Ertl established the mechanism of ammonia synthesis on iron by experiments on single-crystal surfaces: N₂ dissociates on the surface into nitrogen atoms, which are hydrogenated step by step to NH₃, and the dissociation of N₂ controls the overall rate; the dissociation rate on the crystal faces follows Fe(111) > Fe(100) > Fe(110), the same order as their activity for ammonia synthesis. The task asks the solving agent to reach this conclusion independently by first-principles calculation alone.

The following is illustrated for the Explanation class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 0.

- **Task statement and deliverables.** The task statement fixes every setting that affects the energies (functional, pseudopotentials, cutoff energy, k-points, the supercell and number of layers of Fe(111)) and provides no structures, initial guesses or literature values. The deliverables are structure files of each intermediate and transition state, a `results.json` collecting the values, an energy diagram and a short report. The format of the structure files and of `results.json` is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Adsorption and dissociation of N₂: find all the molecular adsorption states of N₂ on Fe(111), and give the dissociation path through the successive precursor states with its barriers.
  2. Hydrogenation path: the adsorption energies of N, NH, NH₂ and NH₃ and the barriers of the three hydrogenation steps.
  3. Choice between mechanisms: compare the dissociative route (N₂ breaks its bond, then is hydrogenated) with the associative route (N₂ is first hydrogenated to N₂H), and obtain from microkinetics the turnover frequency at 673 K and 20 atm and the degree of rate control of each step.
  4. Structure sensitivity: repeat the adsorption of N and the dissociation of N₂ on Fe(100) and Fe(110), and give the activity ordering of the three crystal faces.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the phenomenon (the quantities to be accounted for, which correspond to the single-crystal experimental energy diagram or to the activity ratio 418 : 25 : 1 of the crystal faces; the task statement names them without the literature values). The deliverable is the mechanism, as computation (structures and transition states) and as mathematics (the kinetic equations leading from barriers to rates). The causal claim of sub-question 3, "the dissociation of N₂ controls the overall rate", is checked by the degree of rate control, which plays the role of ablation in microkinetics.
- **Checks.** The agent judge recomputes the submitted structures with the fixed settings, checks the values the submitter reports and the imaginary frequencies of the transition states, then compares with the reference computation: the energy of the highest point of the N₂ dissociation path deviates by no more than 0.15 eV, the turnover frequency is within an order of magnitude of the reference computation, and the ordering of barriers across the three crystal faces agrees. DFT values are expected to differ from the experimental energy diagram by 0.2–0.3 eV, so the experimental energy diagram serves only as a plausibility check. The tolerances are provisional and are set from the spread of energies observed in trial calculations.
- **Tiers and scoring.** The adsorption configurations and transition states on Fe(111) form the first tier, the comparison of routes and the microkinetics the second, and structure sensitivity the third; completing only the first tier earns the corresponding score. The whole task has no more than 8 transition states, to keep the compute under control. The weights are set by the expert; for illustration: validity of structures 15, N₂ adsorption states and dissociation 25, hydrogenation path 20, conclusion on the mechanism 15, microkinetics 10, structure sensitivity 10, report 5.
- **Calibration cases.** The empty submission (score 0); literature energies copied without structures, or structures whose recomputation disagrees with the reported values (a shortcut; the corresponding values score 0); a submission that completes only the first tier (partially correct); the reference computation itself (a known result).
- **Other tasks of the same structure.** Change the metal (ammonia synthesis on Ru) or the reaction (CO oxidation on Pt); the workflow and the checks stay the same.
