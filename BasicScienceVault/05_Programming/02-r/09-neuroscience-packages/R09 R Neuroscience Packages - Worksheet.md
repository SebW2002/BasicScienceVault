---
tags: [programming, r, neuro-packages, type/worksheet]
---
# R09 R Neuroscience Packages – Worksheet

> Theory: [[R09 R Neuroscience Packages]] · Solutions: [[R09 R Neuroscience Packages - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Which package?
1. Match: a) read a NIfTI file b) Bayes factor for a paired t-test c) call MNE-Python from R d) read a v7.3 `.mat` file e) a Butterworth filter f) ERP topographic plots in ggplot style g) a Bayesian mixed model with formula syntax h) test–retest reliability of a questionnaire.
2. Why can't `R.matlab::readMat()` read a file saved with `save(..., "-v7.3")` in MATLAB? What do you use instead?
3. From which repository do you install rhdf5, and with which command?

## Level 2 – Understanding
4. `butter(4, c(1, 40), type = "pass")` in the `signal` package with fs = 500 Hz gives an error or nonsense. Why? Correct it.
5. After `library(signal)`, `df |> filter(rt > 0.2)` stops working. Why? Two fixes.
6. A reticulate call returns event sample indices from MNE (0-based). You use them to index an R vector. What must you do?
7. Why might you preprocess EEG in MNE and only do the statistics in R?

## Level 3 – Interpret
8. `ttestBF` gives BF10 = 0.2. Interpret. What is BF01?
9. A NIfTI image has `pixdim` 2 × 2 × 2 mm and dimensions 91 × 109 × 91. What is the volume of one voxel, and roughly the field of view in each direction?

## Level 4 – Neuro transfer
10. Plan an R-centred workflow for an EEG study: which steps in which tool, which file format between them?
11. You want to check whether a neuroscience package is safe to rely on for your thesis. Name four things to check.
12. 💻 Install `signal`, create 2 s of a 5 Hz + 50 Hz signal at fs = 500 Hz, low-pass at 30 Hz with a 4th-order Butterworth and `filtfilt`, and plot raw and filtered signal.
