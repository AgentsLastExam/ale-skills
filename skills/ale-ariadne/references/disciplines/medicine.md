# Medicine

Tasks and answers are used only to evaluate an agent's research ability. They are not medical advice for patients. A task package must not contain any information that can identify a person.

## Subdomains

The directions of medicine and health differ widely in their objects of study, types of data and ways of verification. This file gives what is common to all of them. Once the expert has described the research problem, pick the subdomain file from the table below and read it as well; the files are in `references/disciplines/medicine/`. A subdomain file only adds what is specific to that direction (screening examples, checking templates, data sources, tools, pitfalls and a worked example); it does not alter the provisions of this file. When a problem spans two subdomains, read both files; when it is unclear where a problem belongs, ask the expert to say. Record the chosen subdomain under "Discipline" in the problem card.

| Subdomain | Scope | File |
|---|---|---|
| Health policy and economics | Payment and insurance design, cost-effectiveness analysis, health technology assessment, equity and access, regulation and ethics | `health-policy-economics.md` |
| Epidemiology and causal inference | Observational study design, bias, confounding and sensitivity analysis, surveillance and outbreak investigation, infectious disease modeling, evidence synthesis | `epidemiology.md` |
| Global and environmental health | Burden of disease, environmental and occupational exposure, nutrition and lifestyle, health behavior and intervention, health in low-resource settings | `global-environmental-health.md` |
| Health systems and implementation | Quality improvement and patient safety, implementation science, primary and community care, workforce and staffing, care coordination and referral | `health-systems.md` |
| Clinical trials and evidence generation | Randomized trial design, adaptive and platform trials, real-world evidence and external controls, endpoints and patient-reported outcomes, conduct, monitoring and analysis of trials | `clinical-trials.md` |
| Health informatics and clinical AI | EHR data modeling and phenotyping, clinical prediction models, decision support and deployment, standards and interoperability, privacy and distributed learning | `health-informatics.md` |
| Clinical assessment and digital phenotyping | Scales and psychometrics, wearables and passive sensing, mental health assessment and intervention, function, rehabilitation and sports medicine, pain and symptom measurement | `clinical-assessment.md` |
| Medical imaging | Acquisition and reconstruction, segmentation and quantitative imaging, radiomics and prognostic modeling, registration and multimodal fusion, image-guided intervention | `medical-imaging.md` |
| Physiological signals and monitoring | Cardiac electrophysiology and ECG, EEG and neuromonitoring, hemodynamics and circulatory modeling, respiration and ventilation, deterioration and bedside monitoring | `physiological-signals.md` |
| Laboratory medicine and biomarkers | Clinical chemistry and hematology, immunoassays and autoantibodies, infectious diagnostics, liquid biopsy and circulating markers, assay quality and interpretation | `laboratory-medicine.md` |
| Infectious disease and host response | Pathogen genomics and typing, antimicrobial therapy and stewardship, vaccine immunogenicity and effectiveness, management of HIV and chronic infection, host response and severity | `infectious-disease.md` |
| Pathology and tissue diagnosis | Histopathology and digital slides, immunohistochemistry and molecular pathology, tumor classification and staging, spatial omics on tissue, death certification and cause-of-death coding | `pathology.md` |
| Therapeutics and pharmacology | Pharmacokinetics and pharmacodynamics, dose individualization, drug safety and pharmacovigilance, resistance and combination therapy, formulation and delivery | `therapeutics-pharmacology.md` |
| Precision medicine and clinical genomics | Clinical variant interpretation, diagnostic sequencing, pharmacogenomics, polygenic risk and population genomics, cancer genomics and targeted therapy | `precision-medicine.md` |

For basic research questions whose object is cells, animal models or molecular mechanisms, see `references/disciplines/biology.md`.

## Screening criteria

- Build with priority: questions that can be answered with de-identified data that is public, or that the expert can obtain compliantly and is allowed to put into a task, and that have an independent validation set or an external cohort (prediction models, evaluation of diagnostic accuracy, reanalysis of clinical trial data, image analysis, evidence synthesis).
- Build with priority: conclusions that come down to a statistic defined in advance (AUROC, hazard ratio, sensitivity and specificity, calibration).
- Defer: tasks that need newly recruited patients or a new clinical trial to be judged (physical-world observation level 3); data under controlled access whose data use agreement does not allow redistribution; findings from single-center data with no external validation; answers that are treatment advice for a specific patient with no objective standard to judge by; data containing information that can identify a person.
- Defer: questions whose criterion of success can only be met by a prospective clinical study or by acceptance from a regulatory agency. Such a question often contains a sub-problem that can be checked on its own; discuss with the expert building the task on that sub-problem instead, and state in the problem card what the sub-problem shows and what it does not. Examples: the clinical protection of a universal vaccine against strains not included in its design cannot be judged here, while the population HLA coverage of conserved T-cell epitopes can be computed; the prospective sensitivity of early cancer screening by ctDNA from a single fingerstick drop of blood cannot be judged here, while the counting limit on the number of mutant molecules in the sampled volume can be derived and computed; regulatory acceptance of a surrogate endpoint for aging cannot be judged here, while whether a change in the marker mediates the change in outcome can be reanalyzed in existing interventional cohorts. Whether to switch to the sub-problem is the expert's decision.

## Matters to confirm in conversation

- Which kind of question it is (diagnosis, prognosis, treatment effect, screening), who the target population is, how the outcome is defined and at what time point it is measured.
- Where the data comes from, which version, and what the inclusion and exclusion criteria are.
- Whether the data use agreement allows putting the data into a task, and whether it requires users to sign the agreement too. The status of ethics approval.
- What the gold standard is (pathology, follow-up outcome, expert consensus), and how high the agreement between annotators is.
- How the external validation set relates to the development data (a different hospital, a different period, different equipment).
- Which confounders exist and how they are handled. Whether there is an analysis plan written in advance.
- How large a difference is clinically meaningful.
- How missing data is handled.

## Checking templates

Most templates below are implemented as numerical-check scripts that the agent judge calls; where the conclusion can be written as a Lean statement in advance, the agent judge checks it with the Lean tool; derivations, explanations and arguments are reviewed by the agent judge directly against the rubric. See `references/agent-judge.md`.

| Template | Criterion | Scope |
|---|---|---|
| Prediction metrics on a held-out set or external cohort | AUROC, calibration slope, Brier score and C-index computed on a hidden validation set | Uses existing data, scientific discovery level 2–3 |
| Comparison with reanalysis results | Given trial or cohort data and an analysis plan defined in advance, the effect estimate (hazard ratio, odds ratio, mean difference) and its confidence interval agree with the reference analysis within tolerance | Uses existing data, scientific discovery level 1–2 |
| Image segmentation or detection | Compared with held-out expert annotations: Dice, sensitivity, and false positives per case | Uses existing data |
| Comparison with an evidence synthesis | Given inclusion criteria, the agreement of the set of included studies and the pooled effect size with a reference systematic review | Uses existing data, scientific discovery level 2 |
| Statistics and reporting checks | Confidence intervals are reported; multiple-comparison correction was done; data is split by patient; calibration is reported; subgroup analyses were specified in advance | Must pass |
| Model recomputation | Given a model (pharmacokinetics, infectious disease transmission, decision analysis), the agent judge reruns it and checks the submitted parameters or conclusions | Pure computation |
| Replication in an independent cohort | A finding from the development set (a marker, a risk factor, a subtype) is re-tested on an independent cohort with a statistical test fixed in advance | Uses existing data, scientific discovery level 3 |
| Agent judge reviews against a rubric | Used when the result is a mechanistic explanation or clinical reasoning; every claim must point to an analysis result that can be recomputed or to literature that can be checked | Scientific discovery level 3 |

## Sources of existing data

- Critical care and electronic health records: MIMIC-IV, eICU-CRD. They are on PhysioNet, require completed training and a signed data use agreement, and cannot be redistributed.
- Physiological signals: the open databases on PhysioNet, such as the MIT-BIH Arrhythmia Database.
- Medical imaging: The Cancer Imaging Archive (TCIA), MIMIC-CXR, CheXpert, NIH ChestX-ray14, the Medical Segmentation Decathlon, and the data of the challenges on grand-challenge.org.
- Cohorts and surveys: NHANES (public); UK Biobank and All of Us are controlled-access and need an application.
- Oncology: TCGA (through the GDC); SEER needs an application.
- Clinical trials: registrations and results on ClinicalTrials.gov; participant-level data on Project Data Sphere, Vivli and YODA needs an application.
- Literature and evidence: PubMed; the Cochrane Library needs a subscription.
- Pharmacovigilance: FDA's FAERS.

## Preventing answer leakage

- One patient often has several records and several images. Split by patient; the same patient cannot appear on both sides.
- External validation must use data from a different center; otherwise features of the same hospital and the same equipment inflate the metrics.
- Labels of public datasets and the answers on challenge leaderboards can be downloaded. Keep held-out labels in the agent judge only, or use a subset whose annotations are not public.
- The primary results of a trial are already published. Ask for a pre-specified secondary analysis the paper did not report, or hide the trial's name and registration number.
- Features must not contain information produced only after the outcome, such as discharge diagnosis codes used to predict in-hospital death.
- Split by time so that no information from the future is used.

## Tools and compute

- Statistics: R (survival, lme4, metafor); Python (statsmodels, lifelines, scikit-learn, scikit-survival).
- Medical imaging: MONAI, nnU-Net, SimpleITK, pydicom, nibabel.
- Electronic health records: tools for the OMOP Common Data Model, the official MIMIC code repository.
- Pharmacokinetics: nlmixr2; NONMEM needs a commercial license.
- Compute: statistical analysis of tabular data needs only CPUs; training 3D image segmentation requires GPUs with large memory; imaging datasets run to tens or hundreds of GB.

## Common pitfalls

- Splitting by sample instead of by patient, so one patient's data leaks.
- Information from after the outcome mixed into the features.
- Reporting discrimination only, without calibration.
- Generalizing single-center results directly to other settings.
- Confounding and selection bias left unhandled, for example immortal time bias.
- Multiple comparisons, and subgroups picked after the fact.
- The gold standard is itself noisy. When agreement between annotators is low, widen the tolerance accordingly.
- When the positive rate is very low, AUROC looks better than it should; look at AUPRC as well.
- Data whose data use agreement forbids redistribution packaged into a task.
- Writing model output as treatment advice.
