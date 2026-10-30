---
tags: [programming, python, visualization, type/solution]
---
# Py07 Python Plotting and Visualization – Solutions

> Worksheet: [[Py07 Python Plotting and Visualization - Worksheet]] · Theory: [[Py07 Python Plotting and Visualization]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. The Figure is the whole canvas (size, saving); an Axes is one panel with its own axes, data and labels. A Figure can contain many Axes.
2. `(3, 2)`; `axes[2, 0]` (or `axes[-1, 0]`).
3. a) sequential (viridis) b) diverging centred at 0 (RdBu_r) c) cyclic (twilight) d) qualitative (tab10 / colorblind).
4. PDF/SVG (vector) for line plots, diagrams and publication figures (sharp at any size, editable); PNG (raster, ≥ 300 dpi) for photos, images, very dense scatter plots.

## Level 2
5. Not perceptually uniform: brightness rises and falls, creating **false boundaries** (bands that look like features) and hiding real gradients; poor for colour-blind readers and in greyscale.
6. The 2000 trials are treated as independent, but trials within a subject are correlated; the relevant variability is **between subjects** (n = 20). Aggregate to one mean per subject and condition first, then plot (and connect paired points).
7. Without symmetric limits the map's midpoint (white) isn't at 0, so some positive values look neutral or negative. Set `vmin=-7.8, vmax=7.8` or use `TwoSlopeNorm(vcenter=0)`.
8. `origin="lower"` and `extent=[t0, t1, f0, f1]` (plus `aspect="auto"`).

## Level 3
9. ```python
   fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(5, 4))
   ax1.eventplot(trials, color="k", linelengths=0.8)
   ax1.set_ylabel("Trial")
   ax2.bar(centers, rate, width=dt, color="grey")
   ax2.set(xlabel="Time from stimulus (s)", ylabel="Rate (Hz)")
   fig.tight_layout()
   ```
10. No axis labels/units; state-based `plt` (unclear which axes); **JPEG** (lossy compression artefacts on lines, not vector) – use PDF/SVG; also no explicit size/fonts for the final figure.
11. ```python
    im = ax.imshow(C, cmap="RdBu_r", vmin=-1, vmax=1)
    fig.colorbar(im, ax=ax, label="Correlation r")
    ```

## Level 4
12. One point per subject per condition (strip/swarm plot), **lines connecting each subject's two points** (paired design), plus the mean with 95 % CI across subjects; y-axis "Amplitude (µV)", caption stating time window, electrodes, n = 24 and what the error bars mean.
13. Diverging map (e.g. `RdBu_r`, cold for negative, hot for positive) with symmetric limits; values with |t| < 3.1 transparent. Caption: statistic, threshold (and whether it's corrected: FWE/FDR, cluster-level), df or n, colour-bar meaning ([[CS12 Neuroimaging Data Analysis]]).
14. ```python
    import numpy as np, matplotlib.pyplot as plt
    from scipy.signal import spectrogram
    fs = 250; t = np.arange(0, 2, 1/fs)
    rng = np.random.default_rng(0)
    x = np.sin(2*np.pi*10*t) + 0.5*rng.standard_normal(t.size)
    f, tt, S = spectrogram(x, fs=fs, nperseg=64)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6, 5))
    a1.plot(t, x, lw=0.6); a1.set(xlabel="Time (s)", ylabel="Amplitude (a.u.)")
    im = a2.pcolormesh(tt, f, 10*np.log10(S), cmap="viridis", shading="auto")
    a2.set(xlabel="Time (s)", ylabel="Frequency (Hz)")
    fig.colorbar(im, ax=a2, label="Power (dB)")
    fig.tight_layout(); fig.savefig("spectrogram.pdf")
    ```
    `pcolormesh` uses the true axis values (low frequencies at the bottom automatically); with `imshow` you'd need `origin="lower"` and `extent`.
