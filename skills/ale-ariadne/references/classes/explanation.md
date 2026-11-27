# Class: Explanation

The system and the phenomenon are known; the law (mechanism, theory or model) is sought. There are two cases:

- Within an existing theoretical framework, the mechanism is unclear and a model must be built.
- A new physical theory is needed; the work is mainly theory construction and proof.

## Matters to confirm with the expert for this class

- The phenomenon to be explained and its quantitative features (frequency, amplitude, threshold, scaling relations), with the corresponding experimental data.
- Control phenomena: nearby conditions under which the phenomenon does not occur (another liquid, a changed parameter). The mechanism must explain both why the phenomenon occurs and why it does not.
- Existing explanations that have been ruled out, and the grounds; these go into the agent judge's reference material.
- The criteria for reproduction: how long, how large, what error threshold, set by the expert.
- Held-out conditions for independent prediction: which parameter combinations are not used to tune the model.

## Problem tree

Root: the phenomenon to be explained, with its quantitative features and the control phenomenon.

Sub-questions are divided by scientific content, not by type of check, such as "reproduction" or "derivation". One physical effect taking part in producing the phenomenon may constitute a sub-question, but the division is not limited to effects; it is determined for the specific problem by the agent and the expert in step 2. A sub-question proposed by the solving agent outside the list is subject to the same requirements.

Each sub-question distinguishes what is given, what is delivered and how it is checked:

- **Given**: the observable phenomenon corresponding to the sub-question and its quantitative features, matched to experimental data. The phenomenon is provided by the task and is what the mechanism must explain; it is not part of the deliverable.
- **Deliverable**: the mechanism that produces the phenomenon. Depending on the needs of the sub-question, it takes one or more of the following forms; the expert decides in step 2 which forms are needed, and not all three are required:
  - Text: an explanation of the mechanism, stating which elements produce the corresponding phenomenon through which process, and why the control phenomenon does not occur.
    - Check: the agent judge reviews it against the rubric.
  - Computation: without artificial driving or imposed outcomes, the simulation captures what the sub-question concerns and reproduces the corresponding phenomenon; with the relevant elements removed, the phenomenon disappears or changes quantitatively (ablation; see "Ablation" in `references/2-research.md`).
    - Check: the agent judge reruns the full model and the ablated models and calls numerical-check scripts to compare with experimental data on the unified output format; the error threshold is set by the expert.
  - Mathematics: equations and derivation showing how the corresponding phenomenon arises, including the energy source, mode selection or scaling of characteristic quantities, and the correspondence between quantities in the equations and those in simulation and experiment.
    - Check: formalisable parts are checked by the agent judge with the Lean tool; the rest is reviewed by the agent judge against the rubric.

Where several forms are used, they must correspond: every element in the text explanation has a counterpart in the simulation and the equations; every element confirmed in simulation has a corresponding term in the equations; and the quantitative conclusions of the derivation agree with simulation and experiment.

Judgement of the root: all sub-questions hold; a model combining all sub-questions reproduces the phenomenon as a whole, and its predictions for conditions not used in parameter tuning (held-out conditions) agree with the data.

### When a new physical theory is needed

Root: a phenomenon existing theory cannot explain.

1. **Consistency in limits**: the new theory reduces to existing theory in known limits.
   - Check: the agent judge calls the Lean tool or reviews the derivation directly.
2. **Explaining the phenomenon**: the new theory explains the target phenomenon quantitatively.
   - Check: the agent judge calls a numerical-check script to compare with data.
3. **Testable prediction**: the new theory makes a testable prediction existing theory does not.
   - Check: the agent judge reviews the basis of the prediction and, where data exist, compares with a numerical-check script.

## Necessary conditions

Every item in the problem tree holds. The final conclusion is the expert's.

## Calibration cases

- A simulation in which the phenomenon does not appear.
- A simulation with an imposed initial shape that then decays.
- A simulation driven by a periodic external force.
- A model that reproduces the phenomenon but fails the independent prediction.
- An existing explanation that has been ruled out.

## Common shortcuts and countermeasures

- Adding artificial driving or imposed initial conditions: forbidden explicitly in the reproduction check, and tested with the corresponding calibration cases to see whether the agent judge detects them.
- Fitting the phenomenon with many free parameters: require independent prediction.
- Restating the phenomenon without a mechanism: the deliverable of every sub-question must be a mechanism, and restating the phenomenon does not make a sub-question hold; where several forms are used, they must correspond.
- Reusing an explanation already ruled out: list ruled-out explanations and the grounds in the reference material.

## Example: star-shaped oscillation of a levitated drop

A water drop held up by a steady gas flow oscillates spontaneously into an n-pointed star (n = 2 to 6 in experiment, about 14 to 31 Hz), while a glycerine–water solution 60 times more viscous oscillates only up and down. The root question: how does a constant energy input turn into sustained oscillation and break circular symmetry.

The sub-questions below are divided by effect and are illustrative; the actual division and the forms each sub-question needs are confirmed by the expert.

1. **The effect of the gas flow feeding energy into the drop.**
   - Given: under constant flow the oscillation persists without decaying.
   - Deliverable, text: how a constant gas flow feeds energy into the surface and sustains the oscillation.
   - Deliverable, computation: a 3D simulation under steady flow produces oscillation spontaneously for at least 5 full cycles with amplitude above 5% of the radius; with the coupling between flow and surface removed, the oscillation decays.
   - Deliverable, mathematics: equations for the energy input, showing how a constant flow sustains periodic oscillation.
2. **The effect of surface tension in selecting the mode.**
   - Given: an n-pointed star, n = 2 to 6, about 14 to 31 Hz, with n varying with radius.
   - Deliverable, computation: the mode number and frequency in simulation agree with experimental data.
   - Deliverable, mathematics: equations for mode selection and frequency (for example, the correspondence with Rayleigh oscillation frequencies); formalisable parts proved in Lean.
3. **The effect of viscosity in suppressing star modes.**
   - Given: the glycerine solution oscillates only up and down.
   - Deliverable, text: how viscous damping suppresses higher modes while the lowest mode remains.
   - Deliverable, computation: with viscosity raised, the star modes disappear and only the up-and-down oscillation remains.

Judgement of the root: a model containing all of the above effects reproduces the star oscillation as a whole, and gives predictions agreeing with the data for radius and flow-rate combinations not used in tuning.
