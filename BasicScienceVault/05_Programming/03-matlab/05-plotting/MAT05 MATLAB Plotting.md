---
aliases: [MATLAB Plotting, plot subplot histogram imagesc, tiledlayout, exportgraphics]
tags: [programming, matlab, visualization, type/overview, neuro]
---
# MAT05 MATLAB Plotting

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT05 MATLAB Plotting - Worksheet|✏️ Worksheet]] · [[MAT05 MATLAB Plotting - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
MATLAB figures are everywhere in older papers and in toolbox outputs (EEGLAB topoplots, SPM glass brains, FieldTrip multiplots). Making them yourself – traces, rasters, spectra, images – and exporting them properly as vector graphics is part of everyday analysis. The visualisation principles are language-independent ([[CS06 Data Science Workflow]], [[Py07 Python Plotting and Visualization]]).

## plot and the figure/axes model
```matlab
fig = figure("Color", "w", "Units", "centimeters", "Position", [2 2 12 7]);
ax = axes(fig);
plot(ax, t * 1000, erp_face, "LineWidth", 1); hold(ax, "on")
plot(ax, t * 1000, erp_house, "--", "LineWidth", 1)
xline(ax, 0, ":"); yline(ax, 0, "-", "Color", [0.7 0.7 0.7])
xlabel(ax, "Time (ms)"); ylabel(ax, "Amplitude (\muV)")
legend(ax, ["face" "house"], "Box", "off", "Location", "northeast")
box(ax, "off"); axis(ax, "tight")
```
- **Figure** = window; **axes** = one plot area; **graphics objects** (lines, images) live in axes. Passing `ax` explicitly avoids drawing into the wrong figure.
- `hold on` keeps existing content; without it each `plot` replaces the previous one.
- Line spec shorthand: `"k-"`, `"r--"`, `"o"`; or name–value: `"Color", [0 0 0]`, `"LineWidth", 1.5`, `"MarkerSize", 4`.
- Labels use TeX by default: `\mu`, `^2`, `_{rms}`; `"Interpreter", "latex"` for LaTeX ([[Doc06 LaTeX Math]]).
- Change properties afterwards: `h = plot(...); h.LineWidth = 2;` / `ax.FontSize = 9;`.

## subplot and tiledlayout
```matlab
figure
tiledlayout(2, 2, "TileSpacing", "compact", "Padding", "compact")  % modern (R2019b+)
nexttile; plot(t, x);           title("Raw")
nexttile; plot(f, 10*log10(P)); title("PSD"); xlabel("Hz")
nexttile([1 2]);                % a tile spanning two columns
imagesc(t, f, S); axis xy; colorbar; title("Spectrogram")
% older equivalent: subplot(2, 2, 1); ...
```
`tiledlayout`/`nexttile` give tighter spacing, shared titles (`title(tl, "...")`) and tiles that span rows/columns; `subplot(m, n, k)` (k counts **row-wise**) is still common in old code.

## histogram, imagesc and other plot types
```matlab
histogram(rt, "BinWidth", 0.05, "Normalization", "probability")
histogram(isi * 1000, 0:2:100)                % ISI histogram (ms), bins as edges
imagesc(t, 1:nTrials, trials_matrix); axis xy % image of a matrix with axis values
colormap(parula); colorbar                    % default perceptually ordered map
clim([-m m]); colormap(cmap_div)              % symmetric limits for signed data (caxis in old versions);
                                              % cmap_div = a diverging map, e.g. built from two colour ramps or from File Exchange
scatter(x, y, 10, "filled", "MarkerFaceAlpha", 0.5)
errorbar(conds, mu, sem, "o")
bar(categorical(["face" "house"]), [0.45 0.52])
boxchart(categorical(T.condition), T.rt)      % box plots (R2020a+)
patch / fill                                  % shaded areas (e.g. mean ± SEM)
```
- **`imagesc`** scales the colour range to the data; with `imagesc(x, y, C)` axes show real units; `axis xy` puts the first row at the **bottom** (default `axis ij` puts it at the top, like an image) – needed for spectrograms and time–frequency plots.
- **Colour maps:** `parula` (default since R2014b) is ordered and perceptually smooth, `turbo` is an improved rainbow (still not uniform); for publications prefer perceptually uniform maps (`parula`, or `viridis`-type maps from the File Exchange); avoid `jet`. For signed data, use a diverging map with **symmetric `clim`** ([[Py07 Python Plotting and Visualization]]).
- Shaded error band: `fill([t fliplr(t)], [mu+se fliplr(mu-se)], "b", "FaceAlpha", 0.2, "EdgeColor", "none")`.

## Figure export with exportgraphics
```matlab
exportgraphics(fig, "figures/fig2_erp.pdf", "ContentType", "vector")   % vector PDF
exportgraphics(fig, "figures/fig2_erp.png", "Resolution", 600)         % raster
exportgraphics(ax, "panelA.pdf")                                       % only one axes
```
- `exportgraphics` (R2020a+) crops tightly to the content; `ContentType "vector"` for line plots, raster for big images (`imagesc` of large matrices is embedded as an image anyway).
- Set the figure size in **centimetres** before exporting, so 9-pt fonts stay 9 pt in the paper.
- Older code uses `print(fig, "-dpdf", "-painters", "fig.pdf")` or `saveas` – both less precise in cropping.
- `savefig(fig, "fig.fig")` saves an editable MATLAB figure (only for MATLAB users).

## Same idea in Python and R
matplotlib copies MATLAB's plotting API (`plot`, `subplot`, `imshow`, `colorbar`) and adds the object-oriented `fig, ax` style ([[Py07 Python Plotting and Visualization]]). ggplot2 is declarative instead ([[R06 ggplot2 Visualization]]).

## In neuroscience #neuro
- **Spike raster:** `plot(spk_times, trial_idx, "k.", "MarkerSize", 4)` or `line` segments; PSTH below with `histogram`/`bar` and a shared x-axis (`linkaxes`).
- **ERP with SEM band** across subjects (`fill` + `plot`), stimulus onset as `xline(0)`.
- **Time–frequency maps:** `imagesc(times, freqs, power); axis xy; colorbar` with a diverging map for baseline-normalised power ([[MAT06 MATLAB Signal Processing Toolbox]]).
- **Topographies:** EEGLAB's `topoplot` and FieldTrip's `ft_topoplotER` build on these graphics objects ([[MAT09 EEGLAB]]).
- **Matrix plots** of connectivity/correlation with `imagesc` + symmetric limits.

## Math links #math-link
- Log scales (`set(gca, "YScale", "log")`, `semilogy`, `loglog`) → [[B3 Logarithmic Functions]]
- Decibels `10*log10(P)` → [[A3 Logarithms]]
- Plotting functions and curve shapes → [[B8 Curve Sketching]]

## Connections
- Matrices for images → [[MAT02 MATLAB Matrices and Vectorization]]
- Spectra and spectrograms to plot → [[MAT06 MATLAB Signal Processing Toolbox]]
- Figures in reports → [[MAT11 MATLAB Live Scripts and Reports]], [[Doc08 LaTeX Figures Tables and References]]
- Principles → [[CS06 Data Science Workflow]]

## Key takeaways
- `figure` → `axes` → `plot`/`imagesc`; `hold on` to overlay; pass the axes handle explicitly.
- `tiledlayout` + `nexttile` (modern) or `subplot` (classic) for panels.
- `imagesc(x, y, C)` + `axis xy` + `colorbar`; ordered colour maps, symmetric `clim` for signed data; no jet.
- `exportgraphics(fig, "f.pdf", "ContentType", "vector")` with the figure size set in cm.
