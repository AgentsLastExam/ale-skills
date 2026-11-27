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

Each sub-question distinguishes what is given, what is delivered and how it is checked:

- **Given**: the condition the sub-question concerns, with its criterion and threshold, provided by the task and in agreement with the task plan; it is not part of the deliverable.
- **Deliverable**: a candidate meeting the condition (all sub-questions concern the same candidate) and the design rationale. Depending on the needs of the sub-question, it takes one or more of the following forms; the expert decides in step 2 which forms are needed, and not all three are required:
  - Computation: the computed result for the candidate under the condition; the computed result after removing or replacing the component that makes the condition hold (ablation in the Design class).
    - Check: the agent judge independently recomputes on the candidate to confirm that the condition is met, without using values reported by the submitter, and reruns the computation with the component removed or replaced.
  - Text: which component of the candidate makes the condition hold, and the underlying principle.
    - Check: the agent judge reviews the design rationale against the rubric.
  - Mathematics: a derivation or bound showing that the condition is met, where applicable.
    - Check: formalisable parts are checked by the agent judge with the Lean tool; the rest is reviewed by the agent judge against the rubric.

Where several forms are used, they must correspond: the component named in the text is the one removed or replaced in the ablation computation.

Judgement of the root: all sub-questions hold; the candidate is not in the known databases (the agent judge searches the specified databases with the search tool); where the expert lists realisability as a condition, the candidate can be synthesised or fabricated.

## Necessary conditions

Every condition is confirmed to be met by the agent judge's independent recomputation, and novelty and (where listed) realisability are satisfied. The design rationale distinguishes a grounded design from a chance hit.

## Calibration cases

- A known system, expected to score 0.
- A candidate meeting only some conditions.
- A candidate with excellent proxy scores that violates a constraint.

## Common shortcuts and countermeasures

- Submitting a known system: the novelty check.
- Exploiting the scoring proxy, such as a molecule with a high docking score that cannot be synthesised: make realisability a condition and test with the corresponding calibration case.
- Self-reported values: the agent judge recomputes independently.

## Examples

The sub-questions below are divided by functional content and are illustrative; the actual division and the forms each sub-question needs are confirmed by the expert.

- A drug molecule with given chemical properties: sub-questions may be binding to the target, selectivity against related targets, and drug-likeness; each is given one condition, and the deliverable is the computed result showing the candidate meets it, with the design rationale.
- A circuit topology and parameters under noise and lithographic precision constraints: sub-questions may be the functional metric, noise tolerance and process realisability.
