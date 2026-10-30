---
aliases: [Mistake Log Computer Science, Fehler Informatik, Misconceptions Computer Science]
tags: [computer-science, type/mistakes]
---
# ⚠️ Mistakes – Computer Science

> [[MOC-computer-science|↑ CS MOC]] · [[MOC-neuroscience-foundations|Neuroscience Foundations]] · Template: [[Mistake Entry Template]]

## Classic misconceptions and traps (pre-filled)
| ❌ Wrong | ✅ Right | Check / why | Topic |
|---|---|---|---|
| matrix shape (features × samples) passed where (samples × features) is expected | check the shape convention | print shapes | [[CS01 Mathematical Foundations]] |
| PCA without centring | centre (and usually standardise) first | first PC points to the mean | [[CS01 Mathematical Foundations]] |
| "PCs have biological meaning" | PCs are variance directions; may mix sources or reflect noise/motion | validate | [[CS01 Mathematical Foundations]] |
| "Euclidean distance = similarity of patterns" | depends on gain; cosine/correlation ignore scale | $(1,1)$ vs $(2,2)$ | [[CS01 Mathematical Foundations]] |
| "p = 0.03 means a 3 % chance the null is true" | P(data this extreme \| $H_0$) | – | [[CS02 Probability and Statistics]] |
| "Not significant = no effect" | absence of evidence ≠ evidence of absence; check power, CI | – | [[CS02 Probability and Statistics]] |
| ignoring base rates | posterior depends on the prior | screening example | [[CS02 Probability and Statistics]] |
| SEM shown as variability of data | SD = spread, SEM = precision of mean | – | [[CS02 Probability and Statistics]] |
| cells as independent samples (pseudoreplication) | unit of inference = animal/subject; mixed models | – | [[CS02 Probability and Statistics]] |
| "Correlation 0 ⇒ independent" | only no *linear* relation; MI can be > 0 | $Y = X^2$ | [[CS03 Information Theory]] |
| $D_{KL}$ treated as symmetric distance | asymmetric; can be infinite | – | [[CS03 Information Theory]] |
| MI from few trials taken at face value | upward bias; shuffle-correct | – | [[CS03 Information Theory]] |
| learning rate "the larger the faster" | too large diverges ($\lvert1 - \eta a\rvert > 1$) | – | [[CS04 Optimization]] |
| choosing λ on the test set | choose by (nested) CV | – | [[CS04 Optimization]] |
| "L2 makes weights exactly zero" | L1 does; L2 shrinks | – | [[CS04 Optimization]] |
| JPEG / 8-bit export of quantitative images | lossless TIFF/PNG, keep bit depth | – | [[CS05 Data Formats and Representation]] |
| missing units/sampling rate in files | store metadata with data (NWB, BIDS) | – | [[CS05 Data Formats and Representation]] |
| comparing floats with `==` | compare with a tolerance | 0.1 + 0.2 | [[CS05 Data Formats and Representation]] |
| CSV with decimal commas | use `.` decimals / TSV / explicit settings | – | [[CS05 Data Formats and Representation]] |
| z-scoring/feature selection before the train–test split | fit preprocessing inside training folds | leakage | [[CS06 Data Science Workflow]] |
| random splits of trials from same session/subject | grouped / blocked CV | – | [[CS06 Data Science Workflow]] |
| double dipping (select & test on same data) | independent selection | – | [[CS06 Data Science Workflow]] |
| bar plots hiding the data | show points / distributions | Anscombe | [[CS06 Data Science Workflow]] |
| pilot effect size used for power calculation | pilot effects are inflated | – | [[CS06 Data Science Workflow]] |
| accuracy on imbalanced classes | balanced accuracy, AUC, F1 | 95 % trivial | [[CS07 Machine Learning Fundamentals]] |
| "high training accuracy = good model" | evaluate on held-out data | – | [[CS07 Machine Learning Fundamentals]] |
| "decodable ⇒ the brain uses it" | information present ≠ used; confounds | – | [[CS07 Machine Learning Fundamentals]] |
| "k-means found 5 clusters, so there are 5 cell types" | clustering always returns clusters; validate | – | [[CS07 Machine Learning Fundamentals]] |
| stacking linear layers adds power | need nonlinearities | $W_2W_1 = W'$ | [[CS08 Deep Neural Networks]] |
| saliency maps as ground truth explanations | noisy hypotheses; validate | – | [[CS08 Deep Neural Networks]] |
| "CNN predicts IT ⇒ CNN = visual cortex" | many models predict similarly; key differences | – | [[CS08 Deep Neural Networks]] |
| credible interval = confidence interval | different definitions | – | [[CS09 Probabilistic and Bayesian Models]] |
| Kalman gain large when measurement noisy | gain small when $R$ large | $K = P/(P + R)$ | [[CS09 Probabilistic and Bayesian Models]] |
| HMM transition matrix columns sum to 1 | rows (from state i) sum to 1 (in this convention) | – | [[CS09 Probabilistic and Bayesian Models]] |
| fixed point with $f'(x^*) > 0$ is stable | stable if $f' < 0$ | – | [[CS10 Dynamical and Computational Neuro Models]] |
| dopamine = pleasure/reward itself | dopamine ≈ reward **prediction error** | omitted reward → dip | [[CS10 Dynamical and Computational Neuro Models]] |
| Euler with large Δt | unstable/inaccurate; reduce Δt | – | [[CS10 Dynamical and Computational Neuro Models]] |
| downsampling without low-pass filter | anti-alias first | alias at $f_s - f$ | [[CS11 Time Series and Signal Processing]] |
| causal IIR filter for offline waveform analysis | phase distortion; use filtfilt | – | [[CS11 Time Series and Signal Processing]] |
| CCG peak ⇒ direct synapse | could be common input; check latency, jitter controls | – | [[CS11 Time Series and Signal Processing]] |
| UMAP distances/cluster sizes interpreted | only local neighbourhoods meaningful | – | [[CS11 Time Series and Signal Processing]] |
| spike threshold from SD of trace | robust σ = median(\|x\|)/0.6745 | – | [[CS11 Time Series and Signal Processing]] |
| uncorrected whole-brain maps | FWE/FDR/permutation | dead salmon | [[CS12 Neuroimaging Data Analysis]] |
| cluster-forming threshold p < 0.01 parametric | p < 0.001 or permutation/TFCE | Eklund 2016 | [[CS12 Neuroimaging Data Analysis]] |
| MVPA CV across volumes | across runs | autocorrelation | [[CS12 Neuroimaging Data Analysis]] |
| classifier weights = activation map | transform to activation patterns (Haufe) | – | [[CS12 Neuroimaging Data Analysis]] |
| source localisation gives unique "true" sources | ill-posed; solution depends on constraints | – | [[CS12 Neuroimaging Data Analysis]] |
| "pseudonymised = anonymous" | pseudonymised data are still personal data | GDPR | [[CS13 Reproducibility and Research Software]] |
| sharing MRI with faces / DICOM headers | deface, anonymise headers | – | [[CS13 Reproducibility and Research Software]] |
| notebook results trusted without restart | restart & run all | hidden state | [[CS13 Reproducibility and Research Software]] |
| raw data in git | archives / DataLad / DVC | – | [[CS13 Reproducibility and Research Software]] |
| network speed in MB/s vs Mbit/s mixed up | 1 byte = 8 bits | – | [[CS14 Hardware Essentials]] |
| "GPU is always faster" | small/branchy tasks + transfer overhead can be slower | – | [[CS14 Hardware Essentials]] |

## My mistakes
| Date | ❌ What I thought / did | ✅ Correct | Why / test question | Link |
|---|---|---|---|---|
| | | | | |

## Patterns I notice
- 
