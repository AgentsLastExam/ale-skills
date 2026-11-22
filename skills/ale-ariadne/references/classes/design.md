# Class: Design

The law and a set of conditions to satisfy are known; a system or scheme that did not exist before is sought. The criterion is whether a system meeting all the conditions can be found.

## Matters to confirm with the expert for this class

- The set of conditions: every condition must be decidable, with its computation and threshold stated.
- The programs and settings the agent judge uses to recompute each condition, fixed in advance.
- The databases searched for novelty.
- Whether realisability is a condition, decided by the expert.
- How partial scores are computed, set by the expert.

## Problem tree

Root: the set of conditions, each of which can be decided.

Sub-questions are divided by scientific content, not by type of check, such as "convergence" or "recomputation"; the division is determined for the specific problem by the agent and the expert in step 2. A sub-question proposed by the solving agent outside the list is subject to the same requirements.

Each sub-question contains all three of the following; none may be omitted, and the three must correspond:

- **Condition**: the condition the sub-question concerns, with its criterion and threshold.
  - Check: the agent judge confirms that the condition as stated agrees with the task plan.
- **Computation**: an independent recomputation on the candidate confirming that the condition is met; values reported by the submitter are not used.
  - Check: the agent judge reruns the computation and calls numerical-check scripts.
- **Rationale**: which component of the candidate makes the condition hold, with the computed result after removing or replacing that component (ablation in the Design class) and the underlying principle.
  - Check: the agent judge reruns the computation with the component removed or replaced and reviews the rationale against the rubric.

Judgement of the root: all sub-questions hold; the candidate is not in the known databases (the agent judge searches the specified databases with the search tool); where the expert lists realisability as a condition, the candidate can be synthesised or fabricated.

## Necessary conditions

The "condition" and "computation" items of every sub-question hold, and novelty and (where listed) realisability are satisfied. The "rationale" item distinguishes a grounded design from a chance hit.

## Calibration cases

- A known system, expected to score 0.
- A candidate meeting only some conditions.
- A candidate with excellent proxy scores that violates a constraint.

## Common shortcuts and countermeasures

- Submitting a known system: the novelty check.
- Exploiting the scoring proxy, such as a molecule with a high docking score that cannot be synthesised: make realisability a condition and test with the corresponding calibration case.
- Self-reported values: the agent judge recomputes independently.

## Examples

The sub-questions below are divided by functional content and are illustrative; the actual division is confirmed by the expert.

- A drug molecule with given chemical properties: sub-questions may be binding to the target, selectivity against related targets, and drug-likeness; each contains condition, computation and rationale.
- A circuit topology and parameters under noise and lithographic precision constraints: sub-questions may be the functional metric, noise tolerance and process realisability.
