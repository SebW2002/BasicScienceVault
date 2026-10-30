---
aliases: [matplotlib, seaborn, Python Plotting, Figure and Axes, Colormaps, viridis]
tags: [programming, python, visualization, matplotlib, seaborn, type/overview, neuro]
---
# Py07 Python Plotting and Visualization

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py07 Python Plotting and Visualization - Worksheet|✏️ Worksheet]] · [[Py07 Python Plotting and Visualization - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
You look at data before you analyse them, and readers look at your figures before they read your text. matplotlib is the base layer of almost every Python plot (MNE, Nilearn and seaborn draw with it); seaborn adds statistical plots for tidy tables. The principles – show the data, label units, honest colour scales – are the same as in [[CS06 Data Science Workflow]].

## matplotlib: Figure and Axes
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 3))          # one Figure, one Axes
ax.plot(t, v, color="k", lw=0.8, label="Vm")
ax.axhline(-50, ls="--", color="grey", label="threshold")
ax.set(xlabel="Time (ms)", ylabel="Membrane potential (mV)", title="LIF neuron")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("figures/lif.pdf")                   # vector format
```
- **Figure** = the whole canvas; **Axes** = one plot panel with its own x/y axes. Always use this **object-oriented** style (`ax.plot`) instead of the state-based `plt.plot` for anything beyond a quick look: it's explicit which panel you're drawing in.
- Common methods: `plot` (lines), `scatter`, `bar`, `hist`, `errorbar`, `fill_between` (shaded CI), `imshow` / `pcolormesh` (images, spectrograms), `eventplot` (spike rasters), `boxplot`, `violinplot`.

### Subplots
```python
fig, axes = plt.subplots(2, 3, figsize=(9, 5), sharex=True, sharey="row")
for ax, ch in zip(axes.flat, channels):
    ax.plot(t, erp[ch])
    ax.set_title(ch)
fig.supxlabel("Time (s)")
# irregular layouts:
fig, axd = plt.subplot_mosaic([["raster", "raster"], ["psth", "tuning"]], layout="constrained")
```
`axes` is a NumPy array of Axes; `axes[1, 0]` is row 2, column 1.

### Images and colour bars
```python
im = ax.imshow(power, aspect="auto", origin="lower", cmap="viridis",
               extent=[t[0], t[-1], f[0], f[-1]])
fig.colorbar(im, ax=ax, label="Power (dB)")
```
`origin="lower"` puts low frequencies at the bottom; `extent` labels the axes with real units instead of pixel indices.

## seaborn for statistical plots
seaborn works directly on **long-format** DataFrames ([[Py06 pandas and Tabular Data]]): you name columns, it does grouping, colours and legends.
```python
import seaborn as sns
sns.stripplot(data=df, x="condition", y="rt", alpha=0.4)              # every point
sns.pointplot(data=df, x="condition", y="rt", errorbar=("ci", 95))    # mean + 95 % CI
sns.violinplot(data=df, x="condition", y="rt", hue="group", split=True)
sns.lineplot(data=erp_long, x="time", y="amplitude", hue="condition") # mean ± CI over trials
g = sns.relplot(data=df, x="stim", y="rate", col="area", kind="line") # small multiples (facets)
```
- `errorbar="sd"`, `"se"`, `("ci", 95)` or `("pi", 95)` – **say which one** in the caption.
- CIs are bootstrapped over rows: if rows are trials from several subjects, aggregate per subject first, otherwise the CI ignores the subject level ([[CS02 Probability and Statistics]], pseudoreplication).

## Colour maps for science
| Data | Colour map type | Examples |
|---|---|---|
| ordered, one direction (power, density, firing rate) | **sequential**, perceptually uniform | `viridis`, `cividis`, `magma`, `inferno` |
| signed, meaningful zero (t-values, ΔF/F, correlation) | **diverging**, centred on 0 | `RdBu_r`, `coolwarm`, `vlag` |
| unordered categories (conditions, cell types) | **qualitative** | `tab10`, seaborn `colorblind` |
| circular (phase, orientation) | **cyclic** | `twilight`, `hsv` |
- **Perceptually uniform:** equal steps in data look like equal steps in colour, and brightness increases monotonically, so the map also works in greyscale. `jet`/rainbow is not: it creates false edges ([[CS06 Data Science Workflow]]).
- **Colour-blind safe:** ~8 % of men have red–green colour vision deficiency. Avoid red vs. green as the only contrast; `viridis`, `cividis` and the seaborn `colorblind` palette are safe.
- **Centre diverging maps:** `ax.imshow(t_map, cmap="RdBu_r", vmin=-m, vmax=m)` with `m = abs(t_map).max()`, or `matplotlib.colors.TwoSlopeNorm(vcenter=0)`.

## Exporting
- **Vector** (`.pdf`, `.svg`) for line plots and publication figures; editable in Inkscape/Illustrator ([[Doc08 LaTeX Figures Tables and References]]).
- **Raster** (`.png`, `dpi=300`) for images with millions of points; `rasterized=True` on a heavy artist keeps the rest vector.
- Set font sizes for the final size: `plt.rcParams.update({"font.size": 8, "pdf.fonttype": 42})` (`fonttype 42` keeps text editable).

## Same idea in R and MATLAB
ggplot2 builds plots from data + aesthetics + geoms + facets ([[R06 ggplot2 Visualization]]), seaborn borrows this idea. MATLAB: `figure`, `tiledlayout`/`subplot`, `plot`, `imagesc`, `exportgraphics` ([[MAT05 MATLAB Plotting]]).

## In neuroscience #neuro
- **Spike raster + PSTH:** `ax.eventplot(list_of_spike_time_arrays)` on top, `ax.bar(bin_centers, rate)` below, sharing x.
- **Spectrogram / time–frequency plot:** `pcolormesh(t, f, 10*np.log10(Sxx))` with `viridis`, frequency on y.
- **Topographies and brain maps** are drawn by MNE (`evoked.plot_topomap`) and Nilearn (`plot_stat_map`) – both matplotlib underneath, so you can adjust them with `ax`/`fig` ([[Py10 Python Neuroscience Packages]]).
- **Statistical maps** (t, z) need a diverging map centred at 0 and a stated threshold.
- **Tuning curves:** mean rate ± SEM per stimulus with `errorbar`, individual neurons in light grey behind.

## Math links #math-link
- Log axes (`ax.set_yscale("log")`) for power spectra and power laws → [[B3 Logarithmic Functions]]
- Decibels $10\log_{10}(P/P_0)$ → [[A3 Logarithms]]
- Plotting functions to understand them → [[B8 Curve Sketching]]

## Connections
- Visualisation principles, error bars → [[CS06 Data Science Workflow]]
- Tidy data for seaborn → [[Py06 pandas and Tabular Data]]
- Spectra to plot → [[Py08 SciPy Scientific Computing]], [[CS11 Time Series and Signal Processing]]
- Figures in documents → [[Doc04 HTML for Reports and Figures]], [[Doc08 LaTeX Figures Tables and References]]

## Key takeaways
- `fig, ax = plt.subplots()`, then draw on `ax`; label axes with units.
- seaborn for tidy DataFrames; state what error bars show; aggregate per subject before CIs.
- viridis-type maps for sequential data, centred diverging maps for signed data; no jet.
- Export vector (PDF/SVG) for publications.
