---
tags: [computer-science, data-science, type/worksheet]
---
# CS06 Data Science Workflow – Worksheet

> Theory: [[CS06 Data Science Workflow]] · Solutions: [[CS06 Data Science Workflow - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮.

## Level 1 – Cleaning
1. Data: 4, 5, 5, 6, 7, 8, 30. Compute the median, Q1, Q3, IQR (use the median of each half, excluding the overall median) and the IQR fences. Is 30 an outlier?
2. For the same data, compute the mean. Why are the median and IQR better here than the mean and SD?
3. Patients with severe symptoms more often miss the follow-up MRI. Which missingness mechanism is this? Why is it problematic?
4. Why should outlier exclusion criteria be fixed before looking at condition differences?

## Level 2 – Splits and CV
5. You have 100 trials and use 5-fold CV. How many trials are in each test fold? How many models are trained?
6. Why is the CV score of the best hyperparameter (chosen by the same CV) optimistic? What fixes it?
7. Data from 10 subjects, 200 trials each. You want to know whether a decoder generalises to **new subjects**. Which CV scheme? What would a random trial-wise split measure instead?
8. Why should you not use random K-fold splits on a continuous EEG time series cut into overlapping 1 s windows?

## Level 3 – Leakage detective
9. For each pipeline, say whether there is leakage and how to fix it:
   a) z-score all data → split → train/test
   b) select the 100 voxels with the highest t-value (all data) → cross-validated decoding
   c) split by run → fit PCA on training runs → transform test runs → decode
   d) data augmentation (rotated images) → random split
10. A study defines an ROI as voxels correlating with anxiety scores, then reports the correlation of mean ROI activity with anxiety: r = 0.85. Critique.

## Level 4 – Power and visualisation
11. An effect of $d = 0.5$ needs about 64 subjects per group for 80 % power. How many for $d = 0.25$? For $d = 1$?
12. Explain the "winner's curse" in underpowered studies.
13. A figure shows two bars with SEM error bars that don't overlap. Can you conclude a significant difference? What would be a better plot?
14. Why is the "jet" (rainbow) colour map discouraged for heat maps of brain activity?
15. 🧮 Rule of thumb $n\approx16/d^2$ per group: a pilot with 8 animals per group found $d = 1.2$. Compute the sample size for that $d$. Then compute it for a more realistic $d = 0.6$. Why might the pilot estimate be inflated?
