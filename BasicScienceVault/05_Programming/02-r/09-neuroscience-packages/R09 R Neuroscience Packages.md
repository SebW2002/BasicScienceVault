---
aliases: [R Neuroscience Packages, eegUtils, oro.nifti, neurobase, reticulate, BayesFactor, rhdf5]
tags: [programming, r, neuro-packages, eeg, fmri, bayes, type/overview, neuro]
---
# R09 R Neuroscience Packages

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R09 R Neuroscience Packages - Worksheet|✏️ Worksheet]] · [[R09 R Neuroscience Packages - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
R's neuroscience ecosystem is smaller than Python's or MATLAB's for **signal and image processing**, but it is the strongest for **statistics on the results**: mixed models, Bayesian models, psychometrics and figures. A common, sensible division of labour: preprocess EEG/fMRI/spikes in Python or MATLAB, export tidy summaries, model them in R – or call Python from R with **reticulate**.

## The landscape
| Package | What it does | Where to find it | Install |
|---|---|---|---|
| **eegUtils** | EEG import (BDF, CNT, BrainVision, EEGLAB `.set`), filtering, epoching, ICA, ERP and topographic plots (ggplot2-based) | GitHub `craddm/eegUtils`, r-universe | `install.packages("eegUtils", repos = c("https://craddm.r-universe.dev", "https://cloud.r-project.org"))` |
| **signal** | signal processing ported from Octave: `butter`, `filtfilt`, `fir1`, `specgram`, `resample` | CRAN | `install.packages("signal")` |
| **oro.nifti** | read/write NIfTI and ANALYZE images as S4 objects; `orthographic()` plots | CRAN | `install.packages("oro.nifti")` |
| **neurobase** | helper functions for `nifti` objects (masking, overlays, `ortho2`, `readnii`) | CRAN, GitHub `muschellij2/neurobase` | `install.packages("neurobase")` |
| **fmri** | fMRI analysis: GLM, adaptive smoothing, signal detection (Tabelow & Polzehl) | CRAN | `install.packages("fmri")` |
| **lme4 / lmerTest** | (generalised) linear mixed models; p-values via Satterthwaite | CRAN | → [[R08 R Mixed-Effects Models]] |
| **brms** | Bayesian multilevel regression with formula syntax, via Stan | CRAN | needs a C++ toolchain; backend rstan or cmdstanr |
| **rstan** | R interface to Stan: write your own Bayesian models | CRAN | `install.packages("rstan")` |
| **BayesFactor** | Bayes factors for t-tests, ANOVA, regression, correlations | CRAN | `install.packages("BayesFactor")` |
| **psychometric** | reliability, item analysis, correlation corrections (applied psychometric theory) | CRAN | `install.packages("psychometric")`; also see **psych** |
| **ggplot2** | grammar-of-graphics plotting | CRAN | → [[R06 ggplot2 Visualization]] |
| **tidyverse** | dplyr, tidyr, readr, purrr, ggplot2, stringr, forcats, … | CRAN | → [[R05 dplyr and tidyr]] |
| **reticulate** | call Python from R (MNE, NumPy, scikit-learn) and exchange objects | CRAN | `install.packages("reticulate")` |
| **R.matlab** | read/write MATLAB `.mat` files (v4/v5; **not** v7.3) | CRAN | `install.packages("R.matlab")` |
| **rhdf5** | read/write HDF5 (and v7.3 `.mat`, NWB internals) | **Bioconductor** | `BiocManager::install("rhdf5")`; CRAN alternative: `hdf5r` |
| spike-train analysis | e.g. **STAR** (Spike Train Analysis with R, Pouzat) | R-Forge; archived on CRAN since 2022 | install from the archive/R-Forge; often easier: Elephant in Python via reticulate |

> [!warning] Check availability
> Small neuroscience packages are maintained by few people and appear, move or disappear: eegUtils is installed from GitHub/r-universe, STAR was archived on CRAN, and a package called "spikeR" could not be found. Before building a project on a package, check its last release date, open issues and whether it is on CRAN. As far as I can tell there is **no CRAN Task View called "Neuroscience"**; the closest is **"MedicalImaging"** (Medical Image Analysis), plus "Psychometrics" and "Bayesian" for statistics.

## Mini-examples
### NIfTI images with oro.nifti / neurobase
```r
library(neurobase)
img <- readnii("sub-01_T1w.nii.gz")      # a nifti S4 object (array + header)
dim(img); pixdim(img)[2:4]                # matrix size, voxel size (mm)
mask <- img > quantile(img[img > 0], 0.2)
ortho2(img, mask, col.y = "red")          # orthogonal slices with overlay
mean(img[mask])
```

### Filtering with signal
```r
library(signal)
fs <- 500
bf <- butter(4, c(1, 40) / (fs / 2), type = "pass")   # cut-offs as fraction of Nyquist!
y <- filtfilt(bf, x)                                   # zero-phase
```
`signal` (like MATLAB's old API) needs **normalised** frequencies $f/(f_s/2)$ – unlike SciPy with `fs=` ([[Py08 SciPy Scientific Computing]]). Beware: `signal::filter` masks `dplyr::filter` and `stats::filter` – call `signal::filtfilt` explicitly.

### Python from R with reticulate
```r
library(reticulate)
use_virtualenv("~/.venvs/mne")             # or use_condaenv("mne")
mne <- import("mne")
raw <- mne$io$read_raw_fif("sub-01_raw.fif", preload = TRUE)
raw$filter(1, 40)
X <- raw$get_data()                         # converted to an R matrix (channels × times)
py_run_string("import numpy as np; z = np.arange(5)"); py$z
```
Python objects are accessed with `$`; NumPy arrays become R arrays (note **0- vs. 1-based** indices when you pass indices back, [[Prog00 Shared Programming Concepts]]).

### MATLAB and HDF5 files
```r
m <- R.matlab::readMat("results.mat")       # list of variables (v5 files)
rhdf5::h5ls("results_v73.mat")              # v7.3 files are HDF5
amp <- rhdf5::h5read("results_v73.mat", "amp")   # note: dimensions may appear transposed
```

### Bayes factors
```r
library(BayesFactor)
ttestBF(x = w$oddball, y = w$standard, paired = TRUE)   # BF10 for a paired difference
anovaBF(rt ~ condition + subject, data = d, whichRandom = "subject")
```
$BF_{10} = 6$: data are 6 times more likely under H1 than under H0 (with the default Cauchy prior on effect size; [[CS09 Probabilistic and Bayesian Models]]).

## Same idea in Python and MATLAB
Python: MNE, NiBabel, Nilearn, Elephant ([[Py10 Python Neuroscience Packages]]); MATLAB: EEGLAB, FieldTrip, SPM ([[MAT10 MATLAB Neuroscience Toolboxes]]). R's strength is modelling the outputs of these tools.

## In neuroscience #neuro
- **EEG in R end-to-end** is possible with eegUtils (import → filter → epoch → ICA → ERP/topoplots), but most labs preprocess in MNE/EEGLAB.
- **Neuroimaging in R:** oro.nifti + neurobase for image handling and ROI statistics; group analyses usually in FSL/SPM/AFNI/Nilearn, with R for ROI-level models.
- **Bayesian statistics** for replications and null results: BayesFactor for simple designs, brms for multilevel data.
- **Psychometrics:** reliability of questionnaires and of neural measures (split-half/test–retest of ERP amplitudes; ICC).

## Math links #math-link
- Normalised frequencies $f/(f_s/2)$, filters → [[B12 Fourier Analysis]], [[CS11 Time Series and Signal Processing]]
- Bayes factors as likelihood ratios → [[CS02 Probability and Statistics]], [[CS09 Probabilistic and Bayesian Models]]
- Image arrays and voxel sizes → [[C1 Matrices]]

## Connections
- Statistics → [[R07 R Statistical Modelling]], [[R08 R Mixed-Effects Models]]
- Data formats (NIfTI, HDF5, .mat) → [[CS05 Data Formats and Representation]], [[R04 R Data Import and Tidy Data]]
- Python ecosystem → [[Py10 Python Neuroscience Packages]]
- MATLAB toolboxes → [[MAT10 MATLAB Neuroscience Toolboxes]]

## Key takeaways
- R is strongest for **statistics on neural summaries**; heavy preprocessing is usually done in Python/MATLAB.
- eegUtils (EEG), signal (filters; normalised frequencies), oro.nifti/neurobase/fmri (MRI), BayesFactor/brms/rstan (Bayes), reticulate (Python), R.matlab/rhdf5 (files).
- Check maintenance status of small packages; rhdf5 comes from Bioconductor.
