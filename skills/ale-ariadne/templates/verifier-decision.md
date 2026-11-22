# Checking plan

Scoring is performed by the agent judge: working from the problem tree, it calls tools leaf by leaf to gather evidence, gives a verdict per leaf, then combines them into an overall judgement and score. See `references/agent-judge.md`.

## Checks per leaf

| Leaf | Tools the agent judge calls | How it decides (quantity compared, against what, tolerance or scoring range) | Basis of the tolerance | Evidence (which run in the research log) |
|---|---|---|---|---|
| | | | | |

## Checks tried but not adopted

| Check | Evidence | Why not adopted |
|---|---|---|
| | | |

## The agent judge's materials

- Evaluation toolkit: (tools it may call; which ways of checking quantitative results are sound)
- Numerical-check scripts: (which ones, what each checks, input and output)
- Lean: (statement, Lean and Mathlib versions, whether the reference proof passes; "not used" if not used)
- Search: (databases and how to search; "not used" if not used)
- Reference material: (metrics and domain knowledge the evaluation rests on; explanations ruled out and the grounds)
- Rubric: (what each criterion checks, what evidence to look at)

## Calibration cases

| Case | Where it came from (which run or trial run) | Expected score or range set by the expert | Score from the agent judge |
|---|---|---|---|
| Empty submission | | 0 | |
| | | | |

## Summary

- How per-leaf verdicts combine into one score between 0 and 1:
- Real score of known results or the baseline:
- Spread of scores when the same submission is reviewed several times:
- Time and compute for one review (including agent judge call costs):
- The expert's reasons:

## Leakage prevention

- Where the solving agent might find the answer:
- How it is prevented: (changed parameters, split by time, offline or allowlist, hidden identifiers)

## Shortcuts found

| Shortcut | Evaded the agent judge | Corresponding calibration case |
|---|---|---|
| | | |

## For tasks at scientific discovery level 3

- What each check examines:
- What passing shows:
- What passing does not show:
- Aspects the expert must still examine to judge that the answer truly holds:
- Known cases that pass without truly solving the problem:
