---
tags: [programming, matlab, visualization, type/worksheet]
---
# MAT05 MATLAB Plotting – Worksheet

> Theory: [[MAT05 MATLAB Plotting]] · Solutions: [[MAT05 MATLAB Plotting - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Recall
1. What do `figure`, `axes`, `hold on` and `axis xy` do?
2. `subplot(2, 3, 5)` – which row and column?
3. Which function exports a vector PDF that is tightly cropped?
4. Name two reasons to prefer `tiledlayout` over `subplot`.

## Level 2 – Debug
5. You plot two ERPs with `plot(t, a); plot(t, b);` and only `b` is visible. Why?
6. Your spectrogram shows low frequencies at the top. Fix.
7. A t-value map plotted with `imagesc(T); colorbar` ranges from −3 to 9; zero is shown in a greenish mid colour. Why misleading? Fix.
8. The figure looks fine on screen but fonts are tiny in the PDF placed in the paper at 8.5 cm width. What went wrong?

## Level 3 – Write code
9. Write code for an ERP (`t` in s, `mu` and `se` row vectors) with a shaded ± SE band, a dashed line at t = 0, and labels in ms and µV.
10. Write a 2 × 1 `tiledlayout`: top a spike raster from cell array `spk` (one vector of spike times per trial), bottom a PSTH with 10 ms bins; link the x-axes.
11. Plot an ISI histogram in ms (bins of 1 ms from 0 to 50 ms), normalised to probability.

## Level 4 – Neuro transfer
12. Which plot (and colour scaling) do you use for: a) baseline-normalised power (dB) over time × frequency b) a 90 × 90 correlation matrix between brain regions c) the distribution of RTs in two groups?
13. Why should the figure size be set *before* `exportgraphics`, not by scaling the PDF in the text editor?
14. 💻 Plot a 10 Hz sine with noise and its spectrogram (`spectrogram(x, 128, 96, [], fs, "yaxis")` if you have the Signal Processing Toolbox) in a `tiledlayout`, and export as a vector PDF of 12 × 8 cm.
