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

Each sub-question distinguishes what is given, what is delivered and how it is checked:

- **Given**: how the existing method handles the part the sub-question concerns, together with the metric and the constraints to be maintained set at the root; these are provided by the task and are not part of the deliverable.
- **Deliverable**: the improved method for this part and its contribution to the metric. Depending on the needs of the sub-question, it takes one or more of the following forms; the expert decides in step 2 which forms are needed, and not all three are required:
  - Computation: the improved method (code) and its metric; the metric with this improvement removed, establishing its contribution to the overall gain (ablation in the Development class).
    - Check: the agent judge reruns the improved method and the ablated version, recomputes the metric with numerical-check scripts and checks that the constraints (for example accuracy, conservation laws, reproducibility) are maintained, without using metrics reported by the submitter; it reviews the attribution.
  - Text: the improvement and its scientific basis, explaining why it raises the metric and why the constraints to be maintained still hold.
    - Check: the agent judge reviews the argument against the rubric.
  - Mathematics: a derivation of complexity, error bounds or convergence, where applicable.
    - Check: formalisable parts are checked by the agent judge with the Lean tool; the rest is reviewed by the agent judge against the rubric.

Where several forms are used, they must correspond: the improvement described in the text is the one actually used in the code and removed in the ablation.

Judgement of the root: all sub-questions hold; the overall metric exceeds the best existing result; the improvement still holds on held-out systems or data not used in development.

## Necessary conditions

The improvement of every sub-question is confirmed by the agent judge's rerun with the constraints maintained; the overall metric exceeds the best existing result, and it holds on the held-out systems. The basis of the improvements and the ablation results show that the improvement can be explained and reused.

## Calibration cases

- The baseline method.
- A method with a higher metric that violates a constraint.
- A method that works only on the instances used in development.

## Common shortcuts and countermeasures

- Trading constraints for the metric: the constraint check.
- Tuning to the evaluation instances: the generalisation check.
- Self-reported metrics: the agent judge reruns and recomputes.

## Examples

The sub-questions below are divided by scientific content and are illustrative; the actual division and the forms each sub-question needs are confirmed by the expert.

- Molecular dynamics balancing accuracy and speed: sub-questions may be the approximation of the interaction potential, the integration algorithm and the treatment of long-range interactions; each delivers one improvement, with its recomputed metric and ablation result.
- Accelerating parameter-space sampling in an astronomical data-processing pipeline. In an earlier trial the agent switched to Newton's method and gained about 700× in the first round. Sub-questions may be the likelihood computation, the sampling algorithm and the convergence criterion.
