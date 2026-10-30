---
aliases: [LaTeX Figures, includegraphics, LaTeX Tables, booktabs, cleveref, Cross-references, Vector Graphics]
tags: [programming, latex, figures, tables, type/overview, neuro]
---
# Doc08 LaTeX Figures Tables and References

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc08 LaTeX Figures Tables and References - Worksheet|✏️ Worksheet]] · [[Doc08 LaTeX Figures Tables and References - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
Figures and tables carry the results of a thesis or paper. LaTeX places them as **floats**, numbers them, keeps captions consistent and updates every cross-reference automatically when you add a figure. Combined with **vector graphics** from Python/R/MATLAB, figures stay sharp and editable. Do this note as soon as you write your first report with figures.

## Figures with graphicx
```latex
\usepackage{graphicx}
\graphicspath{{figures/}}                     % where to look for images

\begin{figure}[tbp]                           % placement: top, bottom, separate page
  \centering
  \includegraphics[width=0.8\textwidth]{erp_pz}   % extension optional: .pdf, .png, .jpg
  \caption{Grand-average ERP at Pz for oddball and standard stimuli ($n = 24$). Shading: $\pm 1$ SEM.}
  \label{fig:erp}
\end{figure}
```
- `figure` is a **float**: LaTeX moves it to a good position (top/bottom of a page) instead of leaving a gap. Options `[tbp]`, `h` (here, if possible), `!` (try harder); `[H]` (from the `float` package) forces "exactly here" – use sparingly.
- `\label` **after** `\caption` (the caption creates the number).
- Size relative to the text: `width=0.8\textwidth`, `\linewidth`; or `height=5cm`; `keepaspectratio`.
- Formats with pdflatex: **PDF** (vector), **PNG** (raster), **JPG** (photos). Not SVG or EPS directly (see below).
- **Subfigures** with `subcaption`:
```latex
\usepackage{subcaption}
\begin{figure}[tbp]
  \centering
  \begin{subfigure}{0.48\textwidth}
    \includegraphics[width=\linewidth]{raster} \caption{Raster} \label{fig:raster}
  \end{subfigure}\hfill
  \begin{subfigure}{0.48\textwidth}
    \includegraphics[width=\linewidth]{psth} \caption{PSTH} \label{fig:psth}
  \end{subfigure}
  \caption{Responses of unit 12.}
  \label{fig:unit12}
\end{figure}
```
Often simpler: assemble multi-panel figures in Python/R (subplots, patchwork) with panel letters, and include one PDF.

## Tables with tabular and booktabs
```latex
\usepackage{booktabs}
\begin{table}[tbp]
  \centering
  \caption{Mean P300 amplitude (µV) at Pz.}       % table captions usually go above
  \label{tab:p300}
  \begin{tabular}{lrrr}
    \toprule
    Condition & Mean & SD   & $n$ \\
    \midrule
    Oddball   & 8.4  & 3.1  & 24 \\
    Standard  & 3.2  & 2.4  & 24 \\
    \bottomrule
  \end{tabular}
\end{table}
```
- Column spec: `l` left, `c` centre, `r` right, `p{3cm}` paragraph with fixed width; `|` adds vertical lines (avoid them).
- `&` separates cells, `\\` ends a row.
- **booktabs** rules: `\toprule`, `\midrule`, `\bottomrule` (and `\cmidrule{2-3}` for partial rules) – no vertical lines, no double lines: the professional look journals expect.
- `\multicolumn{2}{c}{Oddball}` spans columns; `multirow` package for rows.
- Align numbers at the decimal point with siunitx: column type `S` (`\begin{tabular}{l S[table-format=1.1] S[table-format=1.1]}`).
- Generate tables from data instead of typing numbers: `pandas.DataFrame.to_latex()`, R `knitr::kable(format = "latex")`, `modelsummary`, `xtable`; MATLAB: `table2latex` (File Exchange) – fewer transcription errors.
- Long tables over several pages: `longtable`; wide ones: `\resizebox` (shrinks fonts – better: `tabularx`, landscape with `pdflscape`).

## Cross-references with \label and \ref – and cleveref
```latex
\usepackage{hyperref}                 % clickable references (load late)
\usepackage[capitalise, noabbrev]{cleveref}   % load AFTER hyperref
...
As shown in Figure~\ref{fig:erp} and Table~\ref{tab:p300} ...
As shown in \cref{fig:erp} and \cref{tab:p300}; see also \cref{fig:raster,fig:psth} and \cref{eq:nernst}.
% → "Figure 1", "Table 1", "Figures 2a and 2b", "Equation (3)"
\pageref{fig:erp}                     % page number
```
- `\ref` gives only the number; you type "Figure~" (with `~` to avoid a line break). **cleveref**'s `\cref` adds the right name automatically, handles lists and ranges, and keeps naming consistent; `\Cref` at sentence start.
- Labels work for sections (`sec:`), figures (`fig:`), tables (`tab:`), equations (`eq:`) and list items.
- Unresolved references show `??` – compile again; if they persist, the label is misspelt or missing.

## Vector graphics: PDF and SVG
| Format | Type | In LaTeX |
|---|---|---|
| **PDF** | vector (or embeds raster) | `\includegraphics` directly ✅ |
| **SVG** | vector, web standard | convert to PDF first: `inkscape fig.svg --export-type=pdf` (Inkscape ≥ 1.0) or `rsvg-convert -f pdf`; or the `svg` package (`\includesvg{fig}`, needs Inkscape + `--shell-escape`) |
| **EPS** | vector (old) | converted automatically by `epstopdf` with pdflatex |
| PNG | raster, lossless | for images, heat maps with millions of pixels (≥ 300–600 dpi at final size) |
| JPG | raster, lossy | photos only – never for plots |
- **Export plots as PDF/SVG** from Python (`fig.savefig("erp.pdf")`), R (`ggsave("erp.pdf")`), MATLAB (`exportgraphics(..., "ContentType", "vector")`) at the **final size** (e.g. 8.5 cm or 17.5 cm wide) so fonts match the text ([[Py07 Python Plotting and Visualization]], [[R06 ggplot2 Visualization]], [[MAT05 MATLAB Plotting]]).
- **Inkscape** (free) edits SVG/PDF figures: panel letters, arrows, aligning panels; save as PDF for LaTeX.
- Font consistency: use the same font family in plots as in the document (or `pgfplots`/TikZ, PGF backend in matplotlib, for full integration).

## Same idea in Markdown/Quarto and HTML
Quarto: `![Caption](erp.pdf){#fig-erp width=80%}` and `@fig-erp`; tables with `#| label: tbl-…` ([[R10 R Markdown and Quarto]]). HTML: `<figure>` + `<figcaption>` ([[Doc04 HTML for Reports and Figures]]).

## In neuroscience #neuro
- **Thesis figures** from many analysis scripts: one script per figure writes `figures/figN.pdf`; the LaTeX document only includes them – rerun the scripts and recompile, and every figure is current.
- **Statistics tables** (model coefficients, demographics) generated from R/Python into `.tex` files and included with `\input{tables/demographics.tex}`.
- **Brain images** (topographies, fMRI slices) are raster inside – export as high-resolution PNG or a PDF with embedded raster; keep labels/colour bars as vector.
- **Journals** often require separate high-resolution figure files (TIFF/EPS/PDF) and captions in the text – keep the source vector files.

## Connections
- Basics → [[Doc05 LaTeX Basics]]; equation references → [[Doc06 LaTeX Math]]; packages/classes → [[Doc07 LaTeX Documents and TeX Live]]
- Making the figures → [[Py07 Python Plotting and Visualization]], [[R06 ggplot2 Visualization]], [[MAT05 MATLAB Plotting]]
- Editor workflow → [[Doc09 LaTeX with VS Code]]

## Key takeaways
- `figure` float + `\centering` + `\includegraphics[width=…]` + `\caption` + `\label` (after the caption).
- `tabular` with `l c r` columns, `&` and `\\`; booktabs `\toprule/\midrule/\bottomrule`; no vertical lines; generate tables from data.
- `\label`/`\ref` (with `~`), better `\cref` from cleveref (after hyperref).
- Vector PDF for plots (SVG → PDF via Inkscape), PNG for images; export at final size.
