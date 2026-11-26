# Step 2: Research and exploration of checks

This step is the core of the process. The agent and the expert carry out a round of research: decompose the problem into a problem tree, specify the claim, evidence and check for each leaf, actually run the computations and ablations, and prepare and trial-run the agent judge. The outputs are the problem tree, the research log and a checking plan.

## Procedure

1. **Read the class module and the discipline file.** Class modules are under `references/classes/`; pick the one for the class the expert set in step 1: Explanation `explanation.md`, Prediction `prediction.md`, Inversion `inversion.md`, Design `design.md`, Development `development.md`. Each has the class's problem-tree template, necessary conditions, calibration cases and common shortcuts. Discipline files are under `references/disciplines/`, with the discipline's common checking templates, data sources, ways to prevent answer leakage and common pitfalls. Both describe common practice; where they differ from the expert's judgment, follow the expert.
2. **Build the problem tree with the expert.** Work back from the deliverable on the problem card: ask the expert which evidence would establish the intended result, and record how the agent judge checks each item of evidence. These items become the leaves of the tree. Use the class template to organise the leaves; see "Problem tree" below. Write it to `tests/agent-judge/problem-tree.toml`, in the format of `templates/problem-tree.toml`.
3. **Specify claim, evidence and check for each leaf.** Evidence types are under "Evidence types" below; the check is which tools the agent judge calls, see `references/agent-judge.md`. List each leaf's necessary conditions as well.
4. **Run the computations.** Run the reference computation, obtain and inspect the data, and run the baseline to obtain its actual score; when a claim has the form "element X causes phenomenon Y", run the ablation, see "Ablation" below. Record every run in `research/research-log.md`: method, parameters and versions, result, compute and time. Record failed runs too.
5. **Prepare and trial-run the agent judge.** Write the numerical-check scripts and assemble the evaluation toolkit, reference material and calibration cases; see `references/agent-judge.md`. Have the agent judge actually review a few submissions (known results, the baseline, a deliberately worsened answer, a shortcut) and check that its per-leaf verdicts are sound.
6. **Report the results to the expert.** State what was run, what resulted, and what problems the agent itself observed. Ask the expert to judge whether these results are scientifically credible and to confirm the problem tree and each leaf's check. Write the expert's decisions and reasons into `research/verifier-decision.md`, including why checks that were not adopted were dropped.
7. **Carry out shortcut testing.** See "Shortcut testing" below.
8. **Measure the verification cycle and cost.** Fill in the "Measured" column of "Verification cycle and cost" in the problem card; see "Measuring the verification cycle and cost" below.

## Problem tree

Each task takes one top-level scientific question as its root and decomposes it level by level into sub-questions until every leaf can be checked on its own.

- **Root**: the scientific question to answer, and the criterion for it being answered.
- **Intermediate nodes**: sub-questions that must be answered to answer the level above.
- **Leaves**: the smallest units that can be checked independently. Each leaf states:
  - Claim: the conclusion the solving agent must give.
  - Evidence: each item of evidence that supports the claim.
  - Check: the tools the agent judge calls to check that evidence.
  - Necessary conditions: the conditions the claim must meet, and how each is checked.

Decompose by what must be answered to answer the root fully, not by what data or tools happen to exist. Sub-questions are divided by scientific content, not by type of evidence or type of check; one sub-question per effect is one way of dividing them, and the division is determined for the specific problem; one sub-question contains all the evidence it requires. Every sub-question must contain the three items set by its class, given in the class module: phenomenon, simulation and theory for Explanation; model, computation and comparison for Prediction; data, forward computation, and constraints and identifiability for Inversion; condition, computation and rationale for Design; principle, recomputation and ablation for Development. All sub-questions are visible to the solving agent by default and are written into the task statement.

Each leaf can be built as a separate sub-task, which helps the agent and the expert delimit context and design checks; when solving, the solving agent must handle all sub-questions together, and the agent judge reviews the evidence from all leaves together.

Sub-questions found during decomposition that the class module's template does not cover are recorded in the research log; after submission the project team adds them to the template.

## Evidence types

- **Simulation or computation**: reproduce the phenomenon computationally, or give numerical results.
- **Mathematical derivation**: show the claim holds with equations and derivation; formalisable parts are given as Lean proofs, with statements written in advance and confirmed by the expert.
- **Data comparison**: compare with existing observations or held-out data.
- **Experiment**: obtained through new experiments or observations; only for tasks at physical-world observation level 2, see "Tasks at physical-world observation level 2" below.

One sub-question usually requires several kinds of evidence, and they must correspond. In the Explanation class, for example, a sub-question requires the phenomenon (data comparison), the simulation (simulation evidence) and the theory (mathematical derivation): every element confirmed in simulation has a corresponding term or assumption in the equations.

## Necessary conditions

A scientific claim holds only if several necessary conditions hold together. The checks the agent judge runs can usually test only necessary conditions: passing all of them shows the claim may hold, but does not by itself establish it. List each leaf's necessary conditions and specify how each is checked.

## Ablation

When a claim has the form "element X causes phenomenon Y", establish the causal link by ablation:

1. Build a model with all candidate elements and confirm it reproduces phenomenon Y.
2. Remove one element at a time, keeping the rest fixed, and observe whether Y disappears or changes quantitatively.
3. Classify each element as essential, influential or negligible, and state the parameter range where the conclusion holds.

Physical elements are often coupled: checking each element separately cannot replace checking the whole, and enumerating combinations is computationally infeasible. Therefore:

- The solving agent proposes a combination of elements that reproduces the phenomenon; the task does not fix the combination in advance.
- Necessity comes first. Once the minimal combination that reproduces the phenomenon is found, the main part of the question is answered; the roles of other elements are incremental findings.
- Numerical-check scripts are written against the unified output format, not against individual elements; see "Unified output format" in `references/agent-judge.md`.

Where ablation sits in each class: within the "simulation" of each sub-question for Explanation, within the sensitivity analysis of "computation" for Prediction, within "rationale" for Design, and as the "ablation" item itself for Development.

## Evidence and checking tools

| Evidence | What the agent judge usually calls | Evidence to collect during research |
|---|---|---|
| Exact value or analytic solution | Numerical-check scripts | The reference value itself; where the tolerance comes from |
| Recomputation (numerical, simulation) | Rerunning, numerical-check scripts | The reference computation has run through; the compute one run takes; how much the result changes with another method or parameters |
| Existing data | Numerical-check scripts | Data version and license; how part is held out or split by time; whether the solving agent can find the answer online; measurement error |
| Metric relative to a baseline | Rerunning, numerical-check scripts | The baseline's real score; spread over repeated runs; distance to the metric's ceiling |
| Formal proof | Lean tool | Statement written in Lean and confirmed by the expert; a known proof, if any, passes |
| Derivation, explanation or argument | The agent judge reviews it directly against the rubric | An explanation accepted by the expert scores high and a deliberately wrong one low; repeated reviews of the same submission agree |
| Novelty | Search tool | The databases and how to search them |

## Shortcut testing

The purpose is to determine whether a score can be obtained without genuinely solving the problem.

1. Open a separate session without the current context. Give it only the draft task and the agent judge's materials.
2. Instruct it to attempt deliberately to circumvent the review: look up the answer online, hard-code the answer, alter the input data, add artificial driving terms or imposed outcomes, exploit loopholes in the checking scripts. The class module's "Common shortcuts and countermeasures" lists the usual shortcuts for that class.
3. Do this at least once, and record what was tried and the outcome in the research log.

How the outcome is used depends on the scientific discovery level:

- **Scientific discovery levels 1–2**: the review must not be fooled. If it was, revise the checks and try again.
- **Scientific discovery level 3**: not being fooled is not required. Record the cases that pass without truly solving the problem in the checking plan, so the expert can compare against them when judging answers later.

Every shortcut found becomes a calibration case with an expected score set by the expert; in step 4 it is built as a case that should not pass.

## Measuring the verification cycle and cost

Once the checks are set, have the agent judge actually review a few submissions and record the numbers in the "Measured" column of "Verification cycle and cost" in the problem card.

1. **Review three submissions.** Known results (if any, such as the expert's result or the best existing result), the baseline, and a deliberately worsened answer. For each, record review time, compute (including the agent judge's call costs) and score.
2. **Check that the scores separate.** The three scores should be ordered by quality. If they are not, or there are only "pass" and "fail", record this faithfully and ask the expert whether the score can reflect how close an answer is, for example by replacing a pass condition with an error measure or splitting into leaves of increasing difficulty. If the expert considers this impossible, record it faithfully; do not construct a continuous score artificially.
3. **Check that the scores are stable.** Review the same submission several times, record the spread, and compare it with the gap between good and poor answers.
4. **Record the cost of one full attempt.** Time and compute for the baseline to run from scratch to an answer. Record the same for any known result that has a runnable solution procedure.
5. **Record the parts needing a human separately.** For a task at scientific discovery level 3, the expert rules after the agent judge: how long the expert takes to examine one answer the agent judge found supported, and how many per week.

If the measurements are much higher than the expert's estimate in step 1, inform the expert, examine the cause together, and agree on a response: change checking tools, reduce what must be recomputed during review, or use the cheaper verification the expert accepted in step 1. Record the results faithfully in every case. Whether verification is fast enough is for the project team to judge, not the agent.

## Tasks at scientific discovery level 3

These tasks have no perfect check. The checks the agent judge runs form the proxy verifier proposed by the expert: it may be only a set of necessary conditions; an answer that meets them may be viable in some sense, and whether it really is viable is for the expert to judge.

Make these clear with the expert and record them:

- What each check examines.
- What passing shows.
- What passing does not show, that is, what further evidence the expert must examine to judge that the task is truly viable.

## Tasks at physical-world observation level 2

Judging these tasks needs a new experiment or observation, which cannot be done on the expert's side. The five steps go ahead as usual; only the part needing experiments cannot be run:

- Write the checks as usual: which instruments, what experiment, what data, and how the agent judge decides once the data are in.
- Run the parts that need no experiment as usual.
- For the parts that cannot be run, write "not run; needs an experiment to verify" in the research log and the checking plan. In the "Measured" column of the problem card, also write that these could not be measured.
- In the checks of steps 4 and 5 that need a score (calibration-case scores, trial-run scores), record these parts as not run. Do not fabricate experimental data to make them pass.

## If no workable check can be found

If none of the checks tried holds up, explain the situation to the expert and decide together whether to try others. If the expert thinks no workable check exists (at scientific discovery level 3, not even a useful necessary condition), put the task on hold. Write the hold and the reason in the problem card, and keep the research log.

## Matters to confirm before this step ends

- The expert has confirmed the problem tree: each leaf's claim, evidence, check and necessary conditions are written down.
- For causal claims, the ablation has been run, and each element's classification and parameter range recorded.
- The unified output format is set.
- The agent judge's materials (evaluation toolkit, reference material) and the calibration cases are ready; the expert has given the expected scores of the calibration cases, and the agent judge's scores fall within them.
- The tolerance or scoring range and its basis (method error, measurement error, run-to-run spread).
- The real scores of known results or the baseline.
- Whether the solving agent could find the answer online or in a database, and how that is prevented.
- Shortcuts have been sought and the results recorded.
- The "Measured" column of "Verification cycle and cost" in the problem card is filled in.
- Whether good, middling and poor submissions get separated scores, and how much repeated reviews of one submission spread, recorded.
- Scientific discovery level 3: the expert has said what the checks do not show.
- Physical-world observation level 2: how the experimental part is judged is written down, and what was not run is recorded as such.

## Output

- `tests/agent-judge/problem-tree.toml`, from `templates/problem-tree.toml`.
- `research/research-log.md`, from `templates/research-log.md`.
- `research/verifier-decision.md`, from `templates/verifier-decision.md`.
- `research/sources.md`, recording the sources of the data and code used.
