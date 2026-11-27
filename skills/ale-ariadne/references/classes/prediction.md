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

Each sub-question distinguishes what is given, what is delivered and how it is checked:

- **Given**: the target quantity of the sub-question with its definition, conditions, units and required accuracy, provided by the task. The true value is not provided to the solving agent.
- **Deliverable**: the predicted value of the target quantity with an uncertainty estimate. Depending on the needs of the sub-question, it takes one or more of the following forms; the expert decides in step 2 which forms are needed, and not all three are required:
  - Text: the level of theory and the approximations used, with an argument that they apply under the target conditions; where needed, a comparison with a higher-level method on small systems.
    - Check: the agent judge reviews the argument against the rubric and calls numerical-check scripts on the comparison.
  - Computation: the numerical result, including convergence in the discretisation parameters (grid, basis set, system size, time step), sensitivity analysis on the key parameters and approximations (ablation in the Prediction class), and the uncertainty estimate.
    - Check: the agent judge reruns the computation and calls numerical-check scripts on the convergence trend and sensitivity.
  - Mathematics: an analytical derivation, asymptotic behaviour or scaling relation for the target quantity, where applicable.
    - Check: formalisable parts are checked by the agent judge with the Lean tool; the rest is reviewed by the agent judge against the rubric.
- **Comparison with the true value**: the agent judge calls numerical-check scripts to compare the prediction with held-out measurements, time-split new data or high-accuracy computations, and checks that the true value falls within the stated uncertainty. The comparison is done by the agent judge; the solving agent has no access to the true value.

Where several forms are used, they must correspond: the approximations argued in the text are those actually used in the computation, and analytical and numerical results agree where both apply.

Judgement of the root: all sub-questions hold and their results are mutually consistent.

## Necessary conditions

The deliverables of all sub-questions hold, and the true value falls within the stated uncertainty. The final conclusion rests with the expert.

## Calibration cases

- A result from a low-accuracy method.
- An unconverged result.
- A numerically correct result with no uncertainty.

## Common shortcuts and countermeasures

- Looking up published values: use new data split by time or unpublished systems; the task statement contains no identifiers that lead back to the answer, such as paper titles or database IDs.
- Simple extrapolation of existing data: choose true values outside the range existing data cover.

## Example: the Hubbard model

Determine ground-state properties of the two-dimensional Hubbard model at a given interaction strength and doping. The sub-questions below are divided by physical content and are illustrative; the actual division and the forms each sub-question needs are confirmed by the expert.

1. **Antiferromagnetic correlations.** Given: the target quantity is the spin correlation function. Deliverable, text: an argument that the numerical method applies in this parameter range. Deliverable, computation: spin correlation functions, with convergence extrapolation in system size and truncation parameters, and an error estimate. Check: comparison with high-accuracy benchmarks.
2. **Charge stripe order.** Given and deliverable as above, for the charge density distribution and the stripe period, with sensitivity to the interaction strength.
3. **d-wave pairing.** Given and deliverable as above, for the pairing correlation functions.
