# Class: Prediction

The law and the system are known; the phenomenon is sought: a quantity, curve or field under given conditions.

## Matters to confirm with the expert for this class

- The definition of the target quantity, its conditions, units, conventions and required precision.
- The source of the true value: held-out measurements, new data split by time, or high-accuracy calculations.
- The accepted method error in the field, and how far off counts as wrong.
- Whether published values can be found by search; if so, how to change parameters or use unpublished systems.

## Problem tree

Root: the phenomenon or target quantity to be predicted, with its definition, conditions, units and required precision.

Sub-questions are divided by scientific content, not by type of check, such as "convergence" or "recomputation"; the division is determined for the specific problem by the agent and the expert in step 2. A sub-question proposed by the solving agent outside the list is subject to the same requirements.

Each sub-question contains all three of the following; none may be omitted, and the three must correspond:

- **Model**: the level of theory and the approximations used for the sub-question, with an argument that they apply under the target conditions; where needed, a comparison with a higher-level method on small systems.
  - Check: the agent judge reviews the argument against the rubric and calls numerical-check scripts on the comparison.
- **Computation**: the numerical result of the sub-question, including convergence in the discretisation parameters (grid, basis set, system size, time step) and sensitivity analysis on the key parameters and approximations (ablation in the Prediction class).
  - Check: the agent judge reruns the computation and calls numerical-check scripts on the convergence trend and sensitivity.
- **Comparison**: an uncertainty estimate for the result and a comparison with the true value.
  - Check: the agent judge calls numerical-check scripts to compare with held-out measurements, time-split new data or high-accuracy computations, and checks that the true value falls within the stated uncertainty.

Judgement of the root: all sub-questions hold and their results are mutually consistent.

## Necessary conditions

All three items of every sub-question hold. The final conclusion rests with the expert.

## Calibration cases

- A result from a low-accuracy method.
- An unconverged result.
- A numerically correct result with no uncertainty.

## Common shortcuts and countermeasures

- Looking up published values: use new data split by time or unpublished systems; the task statement contains no identifiers that lead back to the answer, such as paper titles or database IDs.
- Simple extrapolation of existing data: choose true values outside the range existing data cover.

## Example: the Hubbard model

Determine ground-state properties of the two-dimensional Hubbard model at a given interaction strength and doping. The sub-questions below are divided by physical content and are illustrative; the actual division is confirmed by the expert.

1. **Antiferromagnetic correlations.** Model: argue that the numerical method applies in this parameter range. Computation: spin correlation functions, with convergence extrapolation in system size and truncation parameters. Comparison: an error estimate and a comparison with high-accuracy benchmarks.
2. **Charge stripe order.** Model, computation and comparison as above, for the charge density distribution and the stripe period, with sensitivity to the interaction strength.
3. **d-wave pairing.** Model, computation and comparison as above, for the pairing correlation functions.
