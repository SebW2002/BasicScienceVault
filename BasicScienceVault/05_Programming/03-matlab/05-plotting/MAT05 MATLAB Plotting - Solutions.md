---
tags: [programming, matlab, visualization, type/solution]
---
# MAT05 MATLAB Plotting – Solutions

> Worksheet: [[MAT05 MATLAB Plotting - Worksheet]] · Theory: [[MAT05 MATLAB Plotting]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. `figure` opens a new figure window; `axes` creates a plotting area; `hold on` keeps existing plots so new ones are added; `axis xy` puts the y-axis origin at the bottom (first matrix row at the bottom) for image plots.
2. Row 2, column 2 (tiles are numbered row-wise: 1 2 3 / 4 **5** 6).
3. `exportgraphics(fig, "f.pdf", "ContentType", "vector")`.
4. Tighter, adjustable spacing; tiles spanning several rows/columns; shared titles/labels for the layout; works well with `exportgraphics`.

## Level 2
5. Without `hold on`, the second `plot` replaces the first. Add `hold on` after the first plot.
6. Add `axis xy` after `imagesc` (or plot with `imagesc(t, f, S)` and set `set(gca, "YDir", "normal")`).
7. The colour scale isn't centred on 0, so zero is shown as a "positive-looking" colour and negative vs. positive values aren't distinguishable. Use a diverging colour map and symmetric limits: `m = max(abs(T(:))); clim([-m m])`.
8. The figure was created at screen size (e.g. 30 cm wide) and shrunk to 8.5 cm in the paper, which shrinks the fonts proportionally. Set `fig.Units = "centimeters"; fig.Position(3:4) = [8.5 6];` and font sizes before exporting.

## Level 3
9. ```matlab
   tm = t * 1000;
   fill([tm fliplr(tm)], [mu+se fliplr(mu-se)], [0.6 0.6 1], "EdgeColor", "none", "FaceAlpha", 0.4); hold on
   plot(tm, mu, "b", "LineWidth", 1)
   xline(0, "--")
   xlabel("Time (ms)"); ylabel("Amplitude (\muV)"); box off
   ```
10. ```matlab
    tl = tiledlayout(2, 1, "TileSpacing", "compact");
    ax1 = nexttile; hold on
    for k = 1:numel(spk)
        plot(spk{k}, k * ones(size(spk{k})), "k.", "MarkerSize", 4)
    end
    ylabel("Trial")
    ax2 = nexttile;
    edges = 0:0.01:1;
    counts = histcounts([spk{:}], edges);
    bar(edges(1:end-1) + 0.005, counts / (numel(spk) * 0.01), 1, "FaceColor", [0.5 0.5 0.5])
    xlabel("Time (s)"); ylabel("Rate (Hz)")
    linkaxes([ax1 ax2], "x")
    ```
    (`[spk{:}]` concatenates all trials – works if each cell is a row vector; the rate is counts / (trials × bin width).)
11. `histogram(isi * 1000, 0:1:50, "Normalization", "probability"); xlabel("ISI (ms)")`

## Level 4
12. a) `imagesc(times, freqs, P); axis xy; colorbar` with a **diverging** map and symmetric `clim` around 0 dB. b) `imagesc(C)` with a diverging map, `clim([-1 1])`, `axis square`, region labels. c) Box/violin or histograms (`boxchart`, `histogram` with transparency) **plus individual points** – not just bars.
13. Scaling the PDF changes line widths and font sizes together; you lose control over the final 8–9 pt text and consistent line weights across figures. Setting the size first means what you design is what's printed.
14. ```matlab
    fs = 250; t = 0:1/fs:4-1/fs;
    x = sin(2*pi*10*t) + 0.5*randn(size(t));
    fig = figure("Units", "centimeters", "Position", [2 2 12 8]);
    tiledlayout(2, 1, "TileSpacing", "compact")
    nexttile; plot(t, x); xlabel("Time (s)"); ylabel("a.u.")
    nexttile; spectrogram(x, 128, 96, [], fs, "yaxis"); colorbar
    exportgraphics(fig, "sine_spectrogram.pdf", "ContentType", "vector")
    ```
