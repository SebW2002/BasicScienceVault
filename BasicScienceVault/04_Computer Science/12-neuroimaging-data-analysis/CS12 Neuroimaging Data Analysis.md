---
aliases: [Neuroimaging Data Analysis, fMRI Preprocessing, fMRI GLM, MVPA, RSA, Source Localization, Multiple Comparisons Neuroimaging]
tags: [computer-science, neuroimaging, fmri, glm, mvpa, rsa, type/overview, neuro]
---
# CS12 Neuroimaging Data Analysis

> [[MOC-computer-science|↑ CS MOC]] · [[CS12 Neuroimaging Data Analysis - Worksheet|✏️ Worksheet]] · [[CS12 Neuroimaging Data Analysis - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Human neuroscience relies heavily on fMRI, EEG and MEG. Between the scanner and the published brain map lies a long chain of preprocessing, statistical modelling and correction for multiple comparisons. Each step embodies maths from this vault (linear algebra, statistics, optimisation), and each has pitfalls that have produced false results in the past.

## fMRI preprocessing pipeline
| Step | What | Math / notes |
|---|---|---|
| Quality control | inspect raw images, artefacts, signal dropout | – |
| **Slice timing correction** | slices are acquired at different times within each TR; interpolate to a common time | temporal interpolation |
| **Motion correction (realignment)** | align each volume to a reference | **rigid-body** transform: 6 parameters (3 translations, 3 rotations), 4×4 matrices ([[C1 Matrices]]); the parameters are later used as nuisance regressors |
| Distortion correction | correct susceptibility distortions (field maps, reverse phase encoding) | – |
| **Coregistration** | align the functional images to the subject's anatomical T1 | rigid body (6 parameters), cross-modal cost (mutual information, [[CS03 Information Theory]]) |
| **Normalisation (registration)** | warp each brain into a **standard space** (MNI) | affine (12 parameters: + scaling, shear) + nonlinear deformation; Jacobian determinants ([[C2 Determinants]]) |
| **Spatial smoothing** | convolve with a 3D Gaussian kernel, e.g. FWHM 6 mm | increases SNR and inter-subject overlap; blurs fine patterns; $\text{FWHM} = 2\sqrt{2\ln2}\,\sigma\approx2.355\sigma$ |
| Temporal filtering | high-pass (remove slow drifts, e.g. < 1/128 Hz) | [[CS11 Time Series and Signal Processing]] |
| **Confound regression / denoising** | motion parameters, CSF and white-matter signals, physiological noise (CompCor = PCA of noise regions), **scrubbing** of high-motion volumes (framewise displacement) | linear regression; head motion creates spurious connectivity |

Standardised tools: **fMRIPrep** (robust, reproducible, BIDS-based; [[CS05 Data Formats and Representation]]), SPM, FSL, AFNI, FreeSurfer.

## The general linear model (GLM) for fMRI activation
For each voxel, the time series $\mathbf y$ ($T$ volumes) is modelled as
$$\mathbf y = X\boldsymbol\beta + \boldsymbol\varepsilon$$
- **Design matrix** $X$ ($T\times p$): columns = **regressors**. Task regressors = stimulus timing (boxcars or events) **convolved with the HRF** ([[CS11 Time Series and Signal Processing]], [[Meth04 In Vivo Imaging]]), plus nuisance regressors (motion, drifts) and an intercept.
- **Estimate** by least squares: $\hat{\boldsymbol\beta} = (X^TX)^{-1}X^T\mathbf y$ ([[C3 Linear Systems and Gaussian Elimination]]). Noise is autocorrelated, so **prewhitening** (generalised least squares) is used.
- **Contrasts:** test a linear combination $\mathbf c^T\boldsymbol\beta$, e.g. faces > houses with $\mathbf c = (1, -1, 0, \dots)$.
  $$t = \frac{\mathbf c^T\hat{\boldsymbol\beta}}{\sqrt{\hat\sigma^2\,\mathbf c^T(X^TX)^{-1}\mathbf c}}$$
  Collinear regressors inflate $(X^TX)^{-1}$, giving large variances and weak t-values ([[C2 Determinants]]).
- **Two levels:**
  - **First level** (within subject): β maps per subject.
  - **Second level** (group): test the subject-level contrast images across subjects (random effects; one-sample t-test, ANOVA, mixed models). The group result generalises to the population; a fixed-effects analysis only to these subjects.
- The same framework is used for EEG/MEG time courses and for calcium imaging.

## Multivariate pattern analysis (MVPA) and decoding
- Instead of testing each voxel separately (**univariate**), use the **pattern** across many voxels as the feature vector for a classifier (logistic regression, linear SVM; [[CS07 Machine Learning Fundamentals]]). This is sensitive to fine-grained, distributed information that averaging would destroy.
- **Cross-validation across runs** (leave-one-run-out), because volumes within a run are temporally correlated (leakage, [[CS06 Data Science Workflow]]).
- **Searchlight:** run the decoder in a small sphere around every voxel, giving a map of local information content.
- **Significance:** permutation tests (shuffle labels within runs) rather than binomial tests against 50 %.
- **Time-resolved decoding** (EEG/MEG): train and test at each time point. **Temporal generalisation:** train at time $t_1$ and test at $t_2$, which reveals stable vs. evolving codes (King & Dehaene 2014).
- **Interpretation:** decodable ≠ used by the brain; decoding can exploit confounds (e.g. reaction time, eye movements). Classifier weights are not directly interpretable as activation maps (transform them to activation patterns, Haufe et al. 2014).

## Representational similarity analysis (RSA)
1. For each pair of conditions (e.g. 92 images), compute the dissimilarity of their response patterns (1 − Pearson correlation, Euclidean, or cross-validated Mahalanobis "crossnobis"; [[CS01 Mathematical Foundations]]). This gives the **representational dissimilarity matrix (RDM)**: $n\times n$, symmetric, with zeros on the diagonal and $\frac{n(n-1)}{2}$ unique entries.
2. Compute RDMs for **models**: stimulus features, CNN layers ([[CS08 Deep Neural Networks]]), behavioural similarity judgements, other brain regions, other species, other methods (fMRI ↔ MEG fusion).
3. **Compare RDMs** (e.g. Spearman correlation of upper triangles; Kendall's τ_A for categorical models).
4. Benchmark against the **noise ceiling** (how well the best possible model could do given data reliability).

Classic finding (Kriegeskorte et al. 2008): human and monkey IT have similar representational geometries for objects (animate vs. inanimate, faces).

**Advantage:** RSA abstracts away from the measurement format (voxels, neurons, units), so representations can be compared across brains, methods and models.

## Multiple comparison correction in neuroimaging
A whole-brain analysis tests ~50,000–200,000 voxels. At α = 0.05 uncorrected, thousands of false positives are expected (famously, "activation" in a dead salmon, Bennett et al. 2009).
| Approach | Controls | Notes |
|---|---|---|
| Bonferroni | FWER | too conservative because neighbouring voxels are correlated (smoothness) |
| **Random field theory** (SPM) | FWER | uses image smoothness ("resels") to estimate the effective number of independent tests |
| **Permutation / max-statistic** | FWER | null distribution of the **maximum** statistic across the brain from sign flips or label permutations; few assumptions |
| **FDR** (Benjamini–Hochberg) | expected fraction of false discoveries among the reported voxels | more power; interpret as "≤ 5 % of reported voxels are false" |
| **Cluster-level inference** | FWER for clusters | threshold voxels (cluster-defining threshold), then test cluster size. Lenient thresholds (p < 0.01) with parametric methods gave inflated false positives (Eklund et al. 2016); use p < 0.001 or permutation; **TFCE** avoids an arbitrary threshold |
| ROI analysis | fewer tests | ROIs must be defined **independently** (no double dipping) |

EEG/MEG: cluster-based permutation tests over time × channels (or time × frequency) are standard (Maris & Oostenveld 2007).

## Source localisation for EEG and MEG as an inverse problem
- **Forward problem** (well-posed): given current sources $\mathbf s$ in the brain, predict sensor data: $\mathbf x = L\mathbf s + \mathbf n$. The **lead field** $L$ (sensors × sources) is computed from a head model (MRI-based BEM/FEM, conductivities, sensor positions; Maxwell's equations, [[Ph06 Magnetism and Induction]]).
- **Inverse problem** (ill-posed): estimate $\mathbf s$ from $\mathbf x$. Typically there are ~64–300 sensors but ~5,000–20,000 source locations, so the system is **underdetermined**, with infinitely many solutions ([[C3 Linear Systems and Gaussian Elimination]]). Some sources (radial for MEG) are almost invisible.
- **Constraints and regularisation pick one solution:**
  - **Dipole fitting:** assume a few equivalent current dipoles; fit position and orientation (non-linear optimisation).
  - **Minimum-norm estimate (MNE):** the smallest-energy solution consistent with the data, $\hat{\mathbf s} = L^T(LL^T + \lambda I)^{-1}\mathbf x$ (ridge regression; [[CS04 Optimization]]). It is biased towards superficial sources; noise-normalised variants (dSPM, sLORETA, eLORETA) correct for this.
  - **Beamformers** (LCMV, DICS): spatial filters that pass activity from one location and suppress others, using the data covariance. They are good for oscillatory sources but suppress correlated sources.
  - **Bayesian approaches** (sparse priors, hierarchical models).
- **Resolution:** ~cm. Point-spread and **leakage** between nearby sources cause spurious connectivity, so use leakage-robust connectivity measures (imaginary coherence, orthogonalised envelopes).

## In neuroscience #neuro
- Large consortia (Human Connectome Project, UK Biobank, ABCD) depend on standardised preprocessing and robust statistics.
- **Analytical flexibility:** 70 teams analysing the same fMRI dataset reached different conclusions (Botvinik-Nezer et al. 2020, NARPS). This motivates preregistration, standard pipelines and multiverse analyses ([[CS13 Reproducibility and Research Software]]).

## Math links #math-link
- Fourier series and transforms (spectra, convolution theorem, k-space) → [[B12 Fourier Analysis]]
- GLM, normal equations, $(X^TX)^{-1}$ → [[C1 Matrices]], [[C3 Linear Systems and Gaussian Elimination]], [[C2 Determinants]]
- Rigid, affine and nonlinear transforms → [[C1 Matrices]], [[D1 Vectors in 2D and 3D]]
- Gaussian smoothing as 3D convolution → [[B7 Antiderivatives and Integration]]
- Correlation distances for RDMs → [[CS01 Mathematical Foundations]], [[D2 Dot and Cross Product]]
- Underdetermined systems and regularisation → [[C3 Linear Systems and Gaussian Elimination]], [[CS04 Optimization]]

## Connections
- In code → [[Py10 Python Neuroscience Packages]] (MNE, Nilearn), [[Py09 Python Machine Learning Libraries]] (decoding), [[MAT09 EEGLAB]], [[MAT10 MATLAB Neuroscience Toolboxes]] (SPM, FieldTrip)
- Imaging physics and BOLD → [[Meth04 In Vivo Imaging]], [[Ph06 Magnetism and Induction]]
- EEG/MEG recording → [[Meth03 Electrophysiology]]
- Statistics and multiple testing → [[CS02 Probability and Statistics]]
- Decoding and leakage → [[CS07 Machine Learning Fundamentals]], [[CS06 Data Science Workflow]]
- BIDS → [[CS05 Data Formats and Representation]]

## Key takeaways
- Preprocessing: slice timing → motion correction (6 parameters) → coregistration → normalisation to MNI (12 + nonlinear) → smoothing (FWHM ≈ 2.355σ) → filtering → confound regression.
- GLM: $\mathbf y = X\boldsymbol\beta + \boldsymbol\varepsilon$, regressors = events ⊛ HRF, contrasts $\mathbf c^T\boldsymbol\beta$, first and second level.
- MVPA decodes patterns (cross-validate across runs, permutation tests). RSA compares representational geometries via RDMs.
- Correct for ~10⁵ tests: RFT, permutation max-statistic, FDR, clusters with strict thresholds or TFCE.
- EEG/MEG source localisation: $\mathbf x = L\mathbf s$, underdetermined; regularised solutions (MNE ≈ ridge), beamformers, dipoles.
