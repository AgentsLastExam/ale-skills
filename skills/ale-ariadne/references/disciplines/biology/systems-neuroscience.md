# Biology: systems and behavioral neuroscience

This file adds content specific to systems and behavioral neuroscience to `references/disciplines/biology.md`, whose provisions still apply.

Scope: sensory coding (visual representation and hierarchy, auditory and somatosensory coding, efficient and predictive coding); motor control and action (population dynamics of motor cortex, brain-machine interfaces); learning, memory and decision (hippocampal codes and replay, reinforcement learning and dopamine, evidence accumulation and choice); whole-brain imaging and connectivity (functional imaging and network states, whole-brain cellular imaging in small animals); computational models of brain function (recurrent network models of cortex, normative and Bayesian models of behavior, neural data analysis and latent dynamics). For synapses, cell types, recording technology and local circuits see `cellular-neuroscience.md`; for clinical imaging and patient cohorts see `references/disciplines/medicine.md`; for the development of statistical and machine learning methods themselves see `computational-biology.md`.

## Screening criteria

- Build with priority: latent dynamics and decoding problems on population recordings, which can be judged on a hidden held-out set with an accepted metric. The Neural Latents Benchmark '21 fixes "predict the activity of held-out neurons from held-in neurons" as the co-smoothing metric, scored in bits per spike relative to a trial-averaged baseline, over maze reaching and continuous reaching in motor cortex, a perturbation task in somatosensory area 2 and an interval-timing task in dorsomedial frontal cortex, with the data released on DANDI in NWB format.
- Build with priority: prediction of responses to held-out stimuli by sensory encoding models. Brain-Score scores the correlation between model predictions and the responses of macaque V1, V2, V4 and IT neurons to held-out images; Sensorium scores single-trial correlation in mouse V1 for natural images and video, and both supply training data and a fixed evaluation pipeline.
- Build with priority: decision models on large public recordings with standardized behavior. The brain-wide map of the International Brain Laboratory recorded 621,733 neurons with 699 Neuropixels probes in 139 mice across 12 laboratories, with the task standardized between laboratories and the data released under CC-BY 4.0.
- Defer: causal conclusions that can be judged only by a new in vivo recording, optogenetic manipulation or animal training, for example whether a brain region is necessary for a behavior. Training and recording take far more than six hours (physical-world observation level 3). Such questions can be reformulated as a test of a model's predictions on already public recordings, or as a correlational conclusion with its limits stated.
- Defer: tasks whose only conclusion is that "decoding accuracy is above chance". The chance level depends on the number of trials, class imbalance and the correlation between trials, so the construction of the null distribution (shuffled labels, pseudosessions, circular shifts) and the correction for multiple comparisons must be fixed with the expert in advance before such a task can be built.

## Matters to confirm in conversation

- The definition of the task and the behavioral variables: trial structure, the alignment point in time, how stimulus and response are coded, and how well trained the subject is.
- The brain region and layer recorded, how the probe localization is verified, and the unit selection criteria.
- The analysis time window and the bin width, which change decoding and dynamics conclusions directly.
- How the null distribution is constructed and how multiple comparisons are corrected, and at which step both are fixed in advance.
- How sessions and subjects are pooled: whether the unit of analysis is the session or the single unit, and how random effects are handled.
- Behavioral confounds: whether body movement, pupil, licking and posture are recorded at the same time and whether they enter the model.
- Metrics and baselines: bits per spike for co-smoothing, R² or accuracy for decoding, and how the comparison with the trial-averaged baseline is made.
- How large an effect has to be to matter, and whether the tolerance comes from variation between sessions or from the spread over repeated training runs.

## Checking templates

The templates below add to the general templates in `references/disciplines/biology.md`.

| Template | Criterion | Scope |
|---|---|---|
| Prediction of held-out neurons and held-out time | Activity of held-out neurons predicted from held-in neurons, scored in bits per spike relative to the trial-averaged baseline; the same metric is then computed for forward prediction over a held-out time segment | Uses existing data, scientific discovery level 2 |
| Significance against a null distribution | The agent judge rebuilds the null distribution in the way fixed in advance (pseudosessions or shuffled labels), recomputes the quantile of the decoding metric and applies the correction for multiple comparisons | Uses existing data, must pass |
| Ablation of behavioral confounds | Metrics are recomputed with body movement, pupil and other behavioral variables added to or removed from the model, to check that the claimed neural coding is not explained by the behavioral variables | Uses existing data, counts for part of the score |
| Generalization to held-out conditions | The model is re-evaluated on task conditions, stimulus sets or sessions not used in fitting, and the drop in the metric stays within what was agreed in advance | Uses existing data, scientific discovery level 2–3 |
| Comparison with the trial-averaged baseline | Single-trial prediction must beat a baseline that takes the trial average within each condition; a model that only reproduces the trial average scores nothing | Uses existing data, must pass |
| Recomputation of behavioral model parameters | Given the behavioral data, the agent judge refits the parameters of the decision model (evidence accumulation, reinforcement learning) and re-examines the model comparison with held-out likelihood or an information criterion | Pure computation |
| Rerunning a network model | The agent judge retrains or reruns the submitted recurrent network with several random seeds and checks that its dynamical features (fixed points, rotational structure, time constants) are reproducible rather than the result of one run | Pure computation, counts for part of the score |

## Sources of existing data

- Population recording benchmarks: the Neural Latents Benchmark '21, seven datasets over four tasks, released on DANDI in NWB format; its EvalAI submission channel closed in January 2026 and the test data are now published with the code.
- Standardized tasks and large-scale recordings: the brain-wide map of the International Brain Laboratory releases 459 recording sessions and 699 probe insertions, of which 45,085 of the 376,730 spike-sorted units pass quality screening, obtained from a public AWS bucket under CC-BY 4.0.
- Sensory coding: Visual Coding – Neuropixels, Visual Coding – Optical Physiology and the two Visual Behavior datasets of the Allen Brain Observatory, released in NWB and obtained through the AllenSDK; Brain-Score and Sensorium supply evaluation data and a fixed pipeline.
- Human neuroimaging: the public data of OpenNeuro, with directories organized under BIDS; the open access data of the Human Connectome Project need a registered account and acceptance of its data use terms, and its restricted data need a separate application. For data on patients and clinical outcomes see `references/disciplines/medicine.md`.
- When the "reference latent variables" or "reference firing rates" are themselves computed by a model, the task is pure computation, not existing data.

## Preventing answer leakage

- The test data of public benchmarks may already be public. The test data of the Neural Latents Benchmark were published with the code once the submission channel closed, so the true activity of the held-out neurons can simply be read off; when using data from that benchmark, make a separate held-out split, or use sessions on DANDI that did not enter the benchmark.
- Leaderboard scores and method descriptions can be found by searching. If the original metric of the benchmark is the only basis for scoring, copying a published model comes close to the best result; score generalization to held-out conditions, ablation results and significance against the null distribution together instead.
- Trials from the same session or the same subject cannot be split between the discovery set and the held-out set. Neighboring trials share slow drift and behavioral correlation, so a random split overstates generalization.
- The task statement contains no dataset IDs, session identifiers, subject numbers or figure numbers from papers.
- The true activity of the held-out time segment and the results of the reference fit stay in the agent judge material and never enter the solving agent's environment.

## Tools and compute

- Data access and formats: pynwb and the DANDI client; the AllenSDK; the Python client supplied by the International Brain Laboratory.
- Population analysis and latent dynamics: scikit-learn for decoding and cross-validation; latent variable models such as LFADS and CEBRA; Elephant for spike train statistics.
- Behavioral quantification: DeepLabCut and SLEAP, for pose estimation.
- Human imaging: fMRIPrep, Nilearn and MNE-Python.
- Network models: recurrent networks trained in PyTorch or JAX; spiking networks use Brian2 and NEST as elsewhere, see `cellular-neuroscience.md`.
- Compute: training a latent dynamics model once takes minutes to hours on a single GPU, and one task needs several training runs to estimate the spread over random seeds; preprocessing whole-brain imaging and large-scale recordings takes hours to days, so give aligned firing-rate matrices rather than raw data whenever possible. Review requires retraining and rebuilding the null distribution and may be of the same order as solving, so it must be estimated in advance. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- Decoding accuracy from a random split of trials taken as evidence of generalization. Neighboring trials share slow drift and behavioral correlation, so the split must be by session, by time segment or by condition.
- A null distribution whose construction does not match the correlation structure of the data, so significance is overstated. When shuffling labels destroys the temporal structure between trials, pseudosessions must be used instead.
- Choosing the brain region, time window or bin width on the same data and then reporting the significance under that choice.
- Body movement and posture explain a large share of neural activity and, when left out of the model, are mistaken for coding of task variables.
- Single-trial prediction and the trial average confused with each other. A model that only reproduces the trial average scores very low on a metric such as co-smoothing, and the converse also holds.
- The dynamics of a recurrent network from a single random seed taken as a conclusion. With a different initialization and different hyperparameters, the fixed-point structure and the rotational component may not appear.
- Pooling results across sessions with the single unit as the unit of analysis, ignoring the variation between sessions and subjects.
- A gain in decoding accuracy that comes from a larger number of units rather than from a difference in coding. Comparisons across brain regions must control the number of units and the number of trials.
- The dimension or structure of the latent variables interpreted directly as a computational mechanism, with no check of its robustness to bin width, smoothing parameters and the model family.

## Example: latent dynamics of motor cortex population activity

While a monkey reaches after a delay, population activity in primary motor cortex and dorsal premotor cortex evolves along a low-dimensional manifold. One account holds that the population activity approximates an autonomous dynamical system: the state during preparation sets the initial condition and the evolution during movement is governed mainly by internal dynamics; another account rests on the tuning of single neurons to kinematic variables. One testable requirement that separates them is that a dynamical model must predict, at the single-trial level, the activity of neurons not used in fitting, and not merely reproduce firing rates averaged within a condition. The Neural Latents Benchmark '21 fixes this requirement as co-smoothing: the activity of held-out neurons is predicted from a subset of neurons and scored in bits per spike relative to a trial-averaged baseline. The benchmark covers maze reaching and continuous reaching in motor cortex, somatosensory area 2 and an interval-timing task in dorsomedial frontal cortex, releases its data on DANDI in NWB format, and uses decoding of hand velocity as a secondary metric for the movement tasks. On data of this kind the task asks the solving agent for a model of the population activity and tests its predictions on held-out neurons, held-out time and held-out conditions.

The following is illustrated for the Prediction class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives spike count matrices for several sessions with the simultaneous behavioral variables and states the bin width and the alignment point; the activity of the held-out neurons, the held-out time segment and some task conditions are not provided. The deliverables are the predicted firing rate of every held-out neuron in every time bin, hand velocity decoded from the latent variables of the model, the same set of predictions for each ablated version, and a short report. The format of the firing-rate matrix and the decoding output is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Prediction of single-trial firing rates: give firing rates for the held-out neurons and compare with a baseline that takes the trial average within each condition.
  2. Extrapolation in time: predict the activity of the held-out time segment from the earlier activity, testing whether the model captures internal evolution rather than smoothing.
  3. Generalization across conditions: repeat both of the above on task conditions not used in fitting, and decode hand velocity from the same latent variables.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the target quantity as defined in the task statement; the true value is not provided to the solving agent. The deliverable is the prediction with its uncertainty, as text (the model family used and its approximations, with an argument that it applies at this bin width and trial count, and a comparison with a simpler model on small data) and as computation (the fit, with convergence and sensitivity analysis over bin width, latent dimension, regularization strength and random seed, which is ablation in the Prediction class, and an uncertainty estimate for the prediction). The comparison with the held-out true values is made by the agent judge.
- **Checks.** The agent judge reruns the submitted model and parameters and checks the values the submitter reports; it computes bits per spike relative to the trial-averaged baseline on the held-out neurons, the same metric for forward prediction on the held-out time segment, and the R² of decoded hand velocity on the held-out conditions. It then retrains several times with different random seeds and records the spread, which must be smaller than the gap to the baseline. The tolerance is set from the spread over repeated training runs and from the variation between sessions.
- **Calibration cases.** The empty submission (score 0); firing rates output as the trial average within each condition (a shortcut, which does not beat the baseline on the single-trial metric); a model that holds on the held-out neurons but fails on the held-out conditions (partially correct); a reproduction of a published method on the benchmark (a baseline).
- **Other tasks of the same structure.** Switch to perturbed and voluntary movement in somatosensory area 2, or to the interval-timing task in dorsomedial frontal cortex; the workflow and the checks stay the same.
