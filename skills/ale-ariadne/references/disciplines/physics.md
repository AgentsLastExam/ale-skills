# Physics

## Screening criteria

- Build with priority: the target is a quantity that can be computed (an energy, a critical exponent, a cross section, a spectrum, an upper or lower bound), and there is an independent second route to check it, such as an analytic limit, another numerical method, or an experimental measurement.
- Build with priority: the target quantity is insensitive to details of the method, or its sensitivity can be stated quantitatively.
- Defer: phenomenological explanations that can only be judged by "looks reasonable"; a reference computation that exceeds the budget in a single run; results that depend on code or data that is not public.

## Matters to confirm in conversation

- What the target quantity is, and its units and conventions (natural units, normalization, sign conventions).
- Whether there is a known analytic limit or exact solution to compare against (weak coupling, large N, an integrable point, exact diagonalization of a small system).
- Which conserved quantities and symmetries must hold.
- Where numerical error comes from (finite size, truncation, time step, statistical error), and how each is extrapolated.
- If experimental data is used: which experiment, which data release, and how the systematic errors are given.
- What precision the field accepts, and how far off counts as wrong.

## Checking templates

Most templates below are implemented as numerical-check scripts that the agent judge calls; where the conclusion can be written as a Lean statement in advance, the agent judge checks it with the Lean tool; derivations, explanations and arguments are reviewed by the agent judge directly against the rubric. See `references/agent-judge.md`.

| Template | Criterion | Scope |
|---|---|---|
| Comparison with an analytic solution or exact value | A numerical answer agrees with the closed-form result within tolerance; a symbolic answer is tested for equivalence by substituting random numerical points | Pure computation, scientific discovery level 1–2 |
| Limit, symmetry and conservation checks | The answer reduces to the known result in known limits; energy, particle number, unitarity and sum rules are conserved within tolerance; dimensions are correct | Pure computation. Must pass, or counts for part of the score |
| Convergence check | Requires results for several grids, truncations or system sizes, and checks the extrapolated value and the order of convergence | Pure computation, scientific discovery level 2–3 |
| Recomputation by an independent method | The agent judge recomputes the submitted parameters or configuration with a different method, for example exact diagonalization for small systems, DMRG or QMC for large ones | Pure computation, scientific discovery level 3 |
| Checkable certificate | The submission is a bound, a construction, a counterexample or a formal proof; the agent judge checks it by direct substitution or with Lean | Pure computation, scientific discovery level 3 |
| Comparison with experimental data | Predicted quantities are compared with held-out measurements using χ² or pulls, with the experimental errors included | Uses existing data |

## Sources of existing data

HEPData, CERN Open Data, the compiled values of the Particle Data Group, NIST atomic spectra and fundamental constants data, and transport and spectroscopy data published alongside condensed matter papers.

## Preventing answer leakage

- Published numbers (critical exponents, ground-state energies) can almost always be found by searching. Change the parameters (lattice size, coupling strength, filling) so that the specific number has not been published.
- Or require intermediate quantities in addition to the final value; these are usually not in the paper.
- Split experimental comparisons by time: score only on measurements that appear in a newer data release.

## Tools and compute

- Symbolic and numerical: SymPy, NumPy/SciPy, Julia; Mathematica needs a license.
- Many-body and quantum: QuSpin, ITensor, TeNPy, NetKet.
- Classical simulation: LAMMPS (molecular dynamics), Dedalus and OpenFOAM (fluids).
- High energy: MadGraph, Pythia, ROOT.
- Formal proof: Lean.
- Compute: exact diagonalization is limited mainly by memory; QMC and DMRG consume CPU hours; fluids and neural-network quantum states need GPUs.

## Common pitfalls

- Inconsistent units and conventions, leaving the answer off by a constant factor.
- Finite-size effects mistaken for physical conclusions.
- Statistical errors underestimated because autocorrelation was not handled.
- A tolerance set tighter than the method's own systematic error, so that correct answers are marked wrong.
- A lower variational energy does not mean a better state; pair it with a variance or symmetry check.
- Floating-point precision and random seeds make results irreproducible.
