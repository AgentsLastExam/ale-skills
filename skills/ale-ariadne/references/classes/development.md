# Class: Development

The law and a metric to improve are known; the level an existing system or method can reach on that metric is sought, with the current best result as the baseline.

## Matters to confirm with the expert for this class

- The metric's definition, computation and the current best result.
- Constraints that must be kept while improving, such as accuracy, conservation laws or reproducibility.
- Held-out systems or data for the generalisation check, not used in development.
- How the metric maps to a score between 0 and 1, set by the expert.

## Problem tree

Root: the definition and computation of the metric, and the best existing result.

Sub-questions are divided by scientific content, not by type of check, such as "convergence" or "recomputation"; the division is determined for the specific problem by the agent and the expert in step 2. A sub-question proposed by the solving agent outside the list is subject to the same requirements.

Each sub-question contains all three of the following; none may be omitted, and the three must correspond:

- **Principle**: the improvement the sub-question concerns and its scientific basis, explaining why it raises the metric and why the constraints to be maintained still hold.
  - Check: the agent judge reviews the argument against the rubric.
- **Recomputation**: the improved method rerun and the metric recomputed, with the constraints (for example accuracy, conservation laws, reproducibility) shown to be maintained.
  - Check: the agent judge reruns and calls numerical-check scripts; metrics reported by the submitter are not used.
- **Ablation**: the metric with this improvement removed, establishing its contribution to the overall gain (ablation in the Development class).
  - Check: the agent judge reruns the ablated version and reviews the attribution.

Judgement of the root: all sub-questions hold; the overall metric exceeds the best existing result; the improvement still holds on held-out systems or data not used in development.

## Necessary conditions

The "principle" and "recomputation" items of every sub-question hold, the overall metric exceeds the best existing result, and it holds on the held-out systems. The "ablation" item shows that the improvement can be explained and reused.

## Calibration cases

- The baseline method.
- A method with a higher metric that violates a constraint.
- A method that works only on the instances used in development.

## Common shortcuts and countermeasures

- Trading constraints for the metric: the constraint check.
- Tuning to the evaluation instances: the generalisation check.
- Self-reported metrics: the agent judge reruns and recomputes.

## Examples

The sub-questions below are divided by scientific content and are illustrative; the actual division is confirmed by the expert.

- Molecular dynamics balancing accuracy and speed: sub-questions may be the approximation of the interaction potential, the integration algorithm and the treatment of long-range interactions; each contains principle, recomputation and ablation.
- Accelerating parameter-space sampling in an astronomical data-processing pipeline. In an earlier trial the agent switched to Newton's method and gained about 700× in the first round. Sub-questions may be the likelihood computation, the sampling algorithm and the convergence criterion.
