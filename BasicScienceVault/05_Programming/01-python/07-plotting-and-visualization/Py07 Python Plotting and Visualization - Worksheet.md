---
tags: [programming, python, visualization, type/worksheet]
---
# Py07 Python Plotting and Visualization – Worksheet

> Theory: [[Py07 Python Plotting and Visualization]] · Solutions: [[Py07 Python Plotting and Visualization - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Recall
1. What is the difference between a Figure and an Axes?
2. `fig, axes = plt.subplots(3, 2)`. What is `axes.shape`? How do you address the panel in the last row, first column?
3. Name the colour map type (sequential, diverging, qualitative, cyclic) for: a) firing-rate heat map b) t-map of a contrast c) LFP phase d) five cell types.
4. When do you save as PDF/SVG, when as PNG?

## Level 2 – Understanding
5. Why is `jet` a poor choice for a power spectrogram? Name two concrete problems.
6. A seaborn `pointplot` of RT per condition is drawn from 20 subjects × 100 trials, with `errorbar=("ci", 95)`. Why is the CI misleadingly narrow? Fix it.
7. A t-map ranges from −2.1 to 7.8 and is shown with `RdBu_r` without `vmin`/`vmax`. What will the reader misjudge?
8. `imshow(spectrogram)` shows high frequencies at the top-left and the axes show pixel numbers. Which two arguments fix this?

## Level 3 – Write code
9. Write code for a 2 × 1 figure with shared x-axis: top a spike raster (`eventplot` of `trials`, a list of arrays), bottom a PSTH (`bar(centers, rate, width=dt)`), axes labelled.
10. Find three problems: `plt.plot(t, v); plt.savefig("fig.jpg")` – a membrane potential trace for a paper.
11. Write the `imshow` call for a correlation matrix `C` (values −1 … 1) with a correct colour map and colour bar.

## Level 4 – Neuro transfer
12. Sketch (in words) a figure that shows ERP amplitudes for two conditions in 24 subjects honestly. What plot elements do you use?
13. You show a group-level fMRI t-map thresholded at |t| > 3.1. Which colour map and colour limits? What must the caption state?
14. 💻 Plot a 10 Hz sine plus noise (2 s, fs = 250 Hz) and, in a second panel, its spectrogram with `scipy.signal.spectrogram`, viridis, `origin="lower"`, a colour bar in dB, and save as PDF.
