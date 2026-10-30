---
tags: [programming, r, neuro-packages, type/solution]
---
# R09 R Neuroscience Packages – Solutions

> Worksheet: [[R09 R Neuroscience Packages - Worksheet]] · Theory: [[R09 R Neuroscience Packages]] · Wrong? → [[Mistakes - R]]

## Level 1
1. a) oro.nifti / neurobase (`readnii`) b) BayesFactor (`ttestBF(..., paired = TRUE)`) c) reticulate d) rhdf5 (or hdf5r) e) signal f) eegUtils g) brms h) psychometric or psych (ICC, Cronbach's α).
2. v7.3 `.mat` files are HDF5 files; R.matlab only reads the older v4/v5 formats. Use `rhdf5::h5read()` (or save as `-v7` in MATLAB).
3. Bioconductor: `install.packages("BiocManager"); BiocManager::install("rhdf5")`.

## Level 2
4. `signal::butter` expects cut-offs normalised to Nyquist (0–1). With fs = 500 Hz: `butter(4, c(1, 40) / 250, type = "pass")`.
5. `signal` defines its own `filter()`, which masks `dplyr::filter` (whichever package is loaded last wins). Fix: call `dplyr::filter(...)` explicitly, or don't attach signal (`signal::butter`, `signal::filtfilt`), or use the `conflicted` package.
6. Add 1: R indices start at 1, so `x[idx0 + 1]`.
7. MNE has mature, well-tested tools for EEG preprocessing (filters, ICA, epoching, source modelling) and handles large continuous data efficiently; R's strengths are statistical models (lme4, brms) and plots of the extracted measures.

## Level 3
8. BF10 = 0.2: the data are 5 times more likely under H0 than H1 → moderate evidence **for** the null (given the prior). BF01 = 1/0.2 = **5**.
9. One voxel = 2 × 2 × 2 = **8 mm³**. Field of view ≈ 182 × 218 × 182 mm (the MNI 2 mm template).

## Level 4
10. PsychoPy (experiment, triggers) → BIDS → MNE-Python (filtering, ICA, epochs, single-trial or per-subject amplitudes) → export tidy CSV/Parquet (`subject, trial, condition, electrode, amp`) → R: `read_csv`, dplyr, lme4/brms, ggplot2 → Quarto report ([[R10 R Markdown and Quarto]]). Alternatively reticulate to run the MNE part from R.
11. Last release/commit date and activity; number of open issues and response to them; availability on CRAN/Bioconductor (passes checks on current R versions); documentation and tests; citations/use in published work; licence; whether a better-maintained alternative exists.
12. ```r
    library(signal)
    fs <- 500; t <- seq(0, 2 - 1/fs, by = 1/fs)
    x <- sin(2*pi*5*t) + 0.5*sin(2*pi*50*t)
    bf <- butter(4, 30 / (fs/2), type = "low")
    y <- signal::filtfilt(bf, x)
    plot(t, x, type = "l", col = "grey", xlab = "Time (s)", ylab = "a.u.")
    lines(t, y, col = "black", lwd = 2)
    ```
