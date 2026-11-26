# Step 3: Expert confirmation of the task plan

Compile what the first two steps have established into a task plan and ask the expert to confirm it. This is the only point in the process at which the expert's formal confirmation is required. Once confirmed, the task package is built according to this plan.

## Procedure

1. **Draft the plan.** Write it from `templates/plan.md`, drawing all content from the problem card, the problem tree, the research log and the checking plan. Do not introduce at this step anything that has not been discussed with the expert. Check the scoring against the agreed deliverable in both directions: a sound answer that uses another method receives the credit it deserves, and a full score establishes the agreed result. Resolve any mismatch with the expert before confirmation.
2. **Explain the plan in terms the expert can readily follow.** Send the plan to the expert together with a brief explanation: what the solving agent will receive, what it must submit, how the score is computed, and in which cases it scores full marks or 0.
3. **Await the expert's explicit confirmation.** If the expert requests changes, make them and ask the expert to review again. Do not enter step 4 before the expert has explicitly confirmed.
4. **Record the confirmation.** At the end of the plan, record the date and the expert's own words. If the expert has not explicitly confirmed, record nothing.

## Contents of the plan

- **Task scope**: the problem the solving agent must solve, the inputs provided, and what is withheld. For an iterative task, specify which feedback the solver will receive after a submission.
- **Deliverables**: the files to be submitted, their format and their paths.
- **Problem tree**: the root question, the sub-questions, and each leaf's claim, evidence and necessary conditions. Sub-questions are written into the task statement by default.
- **Unified output format**: the format of the output that all solutions to a sub-question submit.
- **Scoring**: the tools the agent judge calls for each leaf and how it decides; the rubric; the tolerance or scoring range; whether partial credit is given; how per-leaf verdicts are combined into one score between 0 and 1.
- **Calibration cases**: the list of cases and the expected score or range of each. At least the empty submission (expected score 0) is included; where known results exist (the expert's result, a published result, the baseline), they are listed as cases as well. The task does not require a reference solution to exist.
- **Acceptance notes**: content used only for construction and withheld from the solving agent, including the reference answer, key intermediate quantities and the shortcuts found in step 2.
- **Resources**: CPU, memory, GPU, time limit.
- **Network access**: offline, allowlist or open. An allowlist must list the addresses; open access must be justified.
- **Data**: the data used, with version and licence, which parts are given to the solving agent and which are reserved for the review.

## Additional content for tasks at scientific discovery level 3

- What each check run by the agent judge examines.
- What passing shows, and what it does not show.
- After the agent judge finds an answer supported, which aspects the expert must examine to judge whether it truly holds.

## Changes after confirmation

Any change to the goal, deliverables or scoring of the task requires first revising the plan and then obtaining the expert's reconfirmation. Changes limited to wording, environment fixes or programming errors require no reconfirmation.

A substantive change to the plan invalidates the earlier confirmation; once the expert reconfirms, record the confirmation again at the end of the plan. A change limited to wording leaves the confirmation in force.

## Output

`research/plan.md`
