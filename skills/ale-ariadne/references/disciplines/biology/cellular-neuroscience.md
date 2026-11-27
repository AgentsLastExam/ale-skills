# Biology: cellular and circuit neuroscience

This file adds content specific to cellular and circuit neuroscience to `references/disciplines/biology.md`, whose provisions still apply.

Scope: synaptic transmission and plasticity (long-term potentiation and depression, release machinery and short-term dynamics, homeostatic and structural plasticity); neuronal cell types and atlases (transcriptomic taxonomies, dense electron-microscopy reconstruction); recording from and manipulating circuits (large-scale extracellular recording, two-photon and voltage imaging); neural development and wiring (axon guidance and circuit refinement); glia and neuroimmune interaction (microglial surveillance and pruning, astrocyte signaling and metabolic support). For sensory, motor and cognitive systems, whole-brain imaging and computational models of brain function see `systems-neuroscience.md`; for molecular structure calculations on receptors and ion channels see `molecular-biophysics.md`; for single-cell sequencing pipelines see `genomics-omics.md`; for the general mechanisms of intracellular transport, cytoskeleton and organelles see `cell-biology.md`; for early patterning of the nervous system see `developmental-biology.md`.

## Screening criteria

- Build with priority: synaptic plasticity questions that come down to a quantitative fit of published induction data plus prediction on held-out protocols, for example a single calcium-dependent rule that explains both the pairing-frequency dependence and the timing dependence. Sjöström and colleagues measured, in pairs of thick-tufted layer 5 pyramidal neurons of rat visual cortex, that pairing with the presynaptic spike 10 ms before the postsynaptic one gives LTP at 10 Hz and above but no lasting change at 0.1 Hz, while pairing with the postsynaptic spike 10 ms first gives LTD from 0.1 to 20 Hz and no LTD at 40 Hz and above. Model baselines for data of this kind already exist to compare against.
- Build with priority: recording-processing problems with true values to compare against, for example spike sorting. SpikeForest gathers 650 ground-truth recordings from eleven laboratories (about 35,000 ground-truth units, about 1.3 TB, including paired intracellular-extracellular recordings and simulated recordings) and evaluates ten common sorters through one pipeline; spike inference from calcium imaging has the spikefinder challenge, with 5 datasets and 92 recordings from 73 neurons, split into training and test by neuron, scored by Pearson correlation at 25 Hz.
- Defer: questions whose only basis for judgement is a new patch-clamp, imaging or behavioral experiment, for example the effect of blocking an ion channel on short-term plasticity. Preparation, recording and analysis take far more than six hours (physical-world observation level 3). Such questions can be reformulated as a test of a model's predictions on already public recordings.
- Defer: tasks whose conclusion is the "correct number" of cell types. The level and granularity of a transcriptomic taxonomy depend on clustering parameters and annotation convention; the whole-mouse-brain atlas is divided into 34 classes, 338 subclasses, 1,201 supertypes and 5,322 clusters, and the hierarchy itself is a convention, not a measurement. Such questions can be reformulated as label-transfer agreement across datasets, or as the reproducibility of already defined types on held-out donors and brain regions.
- Defer: dense electron-microscopy connectome conclusions that depend on manual proofreading, for example the complete list of downstream targets of a cell type. The adult fly whole-brain reconstruction contains 139,255 neurons and about 54.5 million synapses, but segmentation errors are settled only by proofreading. Such questions can be reformulated as segmentation or synapse-detection metrics on an already proofread subvolume.

## Matters to confirm in conversation

- Preparation and conditions: species, age, brain region and layer, in vitro or in vivo, temperature, extracellular calcium and magnesium concentration; these conditions set the numerical values of plasticity and firing properties directly.
- All parameters of the induction protocol: the spike timing difference, the pairing frequency, the number of pairings and the interval between repetitions, and how pre- and postsynaptic spikes are evoked.
- Recording method and sampling: electrode type and channel count, sampling rate and filter settings; frame rate, indicator and expression method for imaging.
- The preprocessing choices: which spike sorter and parameters, the unit selection criteria, how calcium signals are deconvolved, and how far these choices affect the conclusion.
- What the cell-type definition rests on (transcriptome, morphology, electrophysiology or projection), and the version and level of the atlas used.
- The form in which the conclusion is expressed: a percentage change in synaptic strength, a threshold, a classification accuracy, or model parameters.
- Where the tolerance comes from: variation between cells, the spread of repeats in the same preparation, or the randomness of the algorithm itself.
- The identifiability of the model parameters, that is whether several parameter sets fit the data equally well, and in what form this is reported.

## Checking templates

The templates below add to the general templates in `references/disciplines/biology.md`.

| Template | Criterion | Scope |
|---|---|---|
| Held-out induction protocols | On protocols not used in fitting (a changed pairing frequency or number of pairings, added timing jitter, a switch to spike triplets), the change in strength predicted by the model falls within the measured cell-to-cell error | Uses existing data, scientific discovery level 2–3 |
| Ablation of elements | With one element removed from the model (summation of calcium transients, the depression threshold, the difference between pre- and postsynaptic calcium amplitudes) and the model rerun, the corresponding phenomenon disappears or changes quantitatively | Pure computation, counts for part of the score |
| Re-examination of parameter identifiability | The agent judge refits from different initial values and checks whether the cost function is flat near its minima; the submitter must give a family of parameters or a confidence interval, and a single value scores nothing | Pure computation, must pass |
| Spike-sorting metrics on ground-truth recordings | Accuracy, miss rate and false-positive rate on paired ground-truth or simulated recordings, reported in strata by the waveform amplitude of the ground-truth unit | Uses existing data |
| Unit quality screening | The agent judge recomputes the quality metrics of the submitted units (refractory-period violation rate, amplitude cutoff, presence ratio over the recording), and units that fail do not enter the later conclusions | Uses existing data, must pass |
| Cell-type label transfer across datasets | The label agreement of a classifier trained on one atlas when applied to an independent dataset, with a report of which types cannot be distinguished | Uses existing data |
| Recomputation of electrophysiological features | With one feature-extraction pipeline, the agent judge recomputes spike threshold, half-width and adaptation index from the submitted membrane potential traces, and they agree with the values the submitter reports | Pure computation, must pass |

## Sources of existing data

- Ground-truth recordings: the 650 ground-truth recordings of SpikeForest; the calcium imaging with simultaneous electrophysiology of the spikefinder challenge, where the true values of the training set are public and those of the test set are not.
- Cell types, morphology and models: the Allen Cell Types Database holds electrophysiology NWB files for single neurons of mouse and human cortex, SWC morphological reconstructions for a subset of cells, and biophysical and GLIF models; the Allen Institute's ABC Atlas and the BICCN whole-mouse-brain cell-type atlas give a four-level taxonomy built from about 4 million quality-controlled single cells and about 4.3 million MERFISH cells; SEA-AD holds over 1.2 million cells of the middle temporal gyrus.
- Connectomes: the adult fly whole-brain reconstruction holds 139,255 neurons and about 54.5 million synapses and is queried through Codex; the MICrONS cubic-millimeter electron-microscopy reconstruction of mouse visual cortex holds over 200,000 cells and about half a billion synapses and is coregistered with calcium imaging of about 75,000 neurons, about 1.6 PB in all, obtained through MICrONS Explorer.
- Electrophysiology and imaging recordings: data in the DANDI archive are released in NWB format; Visual Coding – Neuropixels and Visual Coding – Optical Physiology of the Allen Brain Observatory are obtained through the AllenSDK, see also `systems-neuroscience.md`.
- The data points of published induction experiments often exist only inside a figure and must be requested from the original authors or read off the figure; the reading error must enter the tolerance and be stated in the research log.

## Preventing answer leakage

- The fitted model parameters have been published with the papers. Make the held-out induction protocols the object of scoring, and have the agent judge refit rather than use the parameters the submitter reports.
- The true values of public benchmarks may already be public. The training-set ground truth of spikefinder was released with the challenge, and the per-recording results of SpikeForest can be looked up online, so a search gives each sorter's score on a given recording. Use recordings that did not enter the benchmark, or ask for quantities the benchmark does not report (miss rates by stratum, sensitivity to parameters).
- Recordings from the same animal, the same slice or the same electrode cannot be split between the discovery set and the held-out set; different segments of one raw recording cannot be split either.
- The task statement contains no dataset IDs, cell IDs, figure numbers from papers or names of the original authors.
- Ground-truth annotations and the results of the reference fit stay in the agent judge material and never enter the solving agent's environment.

## Tools and compute

- Spike sorting and recording processing: SpikeInterface wraps Kilosort, MountainSort, SpyKING CIRCUS, Tridesclous, HerdingSpikes and WaveClus under one interface and provides quality metrics and ground-truth comparison; Phy is used for manual curation. Kilosort relies on a GPU, with at least 8 GB of GPU memory recommended.
- Imaging processing: CaImAn and suite2p, for motion correction, segmentation and deconvolution.
- Neuron and synapse modeling: NEURON, Brian2 and NEST; BluePyOpt for parameter fitting and eFEL for feature extraction; the code of published models can be found in ModelDB.
- Data format and archiving: NWB and pynwb, and the DANDI command-line client.
- Compute: fitting one plasticity rule takes minutes to hours on a single workstation but must be repeated many times to estimate the spread of the parameters; fully spike-sorting one 384-channel recording needs a GPU and tens to hundreds of GB of storage and takes hours, so give already sorted spike trains rather than raw waveforms whenever possible; electron-microscopy volumes and whole-brain atlases are too large, so a task takes only a subvolume or a processed matrix. The recomputation during review covers refitting and recomputing metrics and is smaller than solving. These are rough estimates; the measurement in step 2 prevails.

## Common pitfalls

- An incompletely stated induction protocol (number of pairings, repetition interval, temperature, extracellular calcium), so that what the model fits is not what the experiment did.
- Reporting the fit as a single parameter set. The cost function of a calcium-dependent plasticity model is nearly flat near its minima, and different initial values give different parameter sets with comparable goodness of fit.
- Testing the model on the same protocols used to fit it. The free parameters of the model suffice to restate the data and show no predictive power.
- Spike-sorting errors taken as a biological conclusion. Over-splitting and over-merging units change estimates of correlation, synchrony and tuning directly.
- Calcium signals used in place of spike trains for a quantitative comparison. Indicator kinetics and saturation make fluorescence amplitude a nonlinear function of spike count.
- Electrode drift left untreated, so the identity of a unit changes over a long recording.
- Statistical tests run with the cell as the unit, ignoring the variation between animals and slices.
- The number of transcriptomic clusters taken directly as the number of cell types, with no statement of the clustering parameters and the annotation level.
- Unproofread automatic segmentation taken as an established synaptic connection.

## Example: a calcium-based rule for synaptic plasticity

Long-term potentiation and depression at cortical synapses depend jointly on the timing and the rate of pre- and postsynaptic firing. Sjöström and colleagues varied the pairing frequency systematically in pairs of thick-tufted layer 5 pyramidal neurons of rat visual cortex and obtained two curves: pairing with the presynaptic spike 10 ms before the postsynaptic one gives LTP at 10 Hz and above, growing with frequency, and no lasting change at 0.1 Hz; pairing with the postsynaptic spike 10 ms first gives LTD from 0.1 to 20 Hz, and LTD disappears at 40 Hz and above. The rule proposed by Graupner and Brunel uses a single calcium trace: the transients evoked by pre- and postsynaptic spikes sum, the time the trace spends above a depression threshold and above a potentiation threshold drives depression and potentiation respectively, and synaptic efficacy switches stochastically between two stable states. The rule was fitted with a least-squares cost function separately to three bodies of data, hippocampal slices, hippocampal cultures (triplet and quadruplet protocols) and cortical slices (regular pairings from 0.1 to 50 Hz), and holds qualitatively on jittered protocols not used in the fit; its authors also note that different initial values give different parameter sets with comparable goodness of fit. The task asks the solving agent to arrive independently, from the same public data, at a rule that explains the frequency dependence and the timing dependence together.

The following is illustrated for the Explanation class; the class is assigned by the expert. Scientific discovery level 2, physical-world observation level 1.

- **Task statement and deliverables.** The task statement gives a set of induction protocols and their measured changes in synaptic strength, with cell counts and errors, and withholds the results of some protocols; it gives no model form, parameters or literature values. The deliverables are the equations of the rule and a family of parameters, a prediction for every protocol, the same set of predictions for each ablated version, and a short report. The format of the predictions is the unified output format.
- **Sub-questions.** Divided by scientific content, for illustration only:
  1. Frequency dependence: why +10 ms pairing produces no change at 0.1 Hz but produces LTP at 10 Hz and above, growing with frequency.
  2. Timing dependence and its disappearance: why −10 ms pairing produces LTD at low frequency and no LTD at 40 Hz and above.
  3. Differences between preparations: whether the same rule, with the calcium transient amplitudes and thresholds changed, covers the different timing curves seen in the hippocampal and cortical data together.
- **Given and deliverable.** The forms shown are for illustration; the expert decides which each sub-question needs. In every sub-question the given is the phenomenon (the measured change in strength for the corresponding protocol with its cell-to-cell error). The deliverable is the mechanism, as computation (running the rule without imposing the outcome and without tuning parameters per protocol, together with ablation: removing the summation of calcium transients, removing the depression threshold, setting the pre- and postsynaptic calcium amplitudes equal) and as mathematics (the equations leading from the time spent above each threshold to the steady-state efficacy, explaining why a rising frequency first strengthens depression and then crosses the potentiation threshold). The ablation is the causal check of "element X causes phenomenon Y".
- **Checks.** The agent judge reruns every protocol from the submitted equations and parameters and checks the values the submitter reports; it then compares prediction with measurement on the withheld protocols, where the deviation must fall within the cell-to-cell error of the measured value for that protocol. It then refits from different initial values to examine the identifiability of the parameters, and a single value that cannot be reproduced scores nothing. In each ablated version the corresponding phenomenon must disappear or change quantitatively. The tolerance is set from the cell-to-cell spread of the measurements and the spread of parameters over repeated fits, and must not be tighter than the error of the experiment itself.
- **Calibration cases.** The empty submission (score 0); a separate parameter set per protocol assembled into all the curves (a shortcut, which fails on the withheld protocols); a rule that explains the frequency dependence but fails on the timing curve (partially correct); a published calcium-based rule and its parameters (a known result).
- **Other tasks of the same structure.** Switch to the frequency dependence of short-term plasticity (the protocol dependence of facilitation and depression), or to the return of firing rate in homeostatic plasticity; the workflow and the checks stay the same.
