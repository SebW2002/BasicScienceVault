---
tags: [programming, latex, figures, tables, type/solution]
---
# Doc08 LaTeX Figures Tables and References – Solutions

> Worksheet: [[Doc08 LaTeX Figures Tables and References - Worksheet]] · Theory: [[Doc08 LaTeX Figures Tables and References]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. A float is an object (figure, table) that LaTeX may move to a better position (top/bottom of a page, a float page) instead of placing it exactly where it appears in the source. `[tbp]`: allowed positions top, bottom, separate page. `[H]` (float package): exactly here, no floating.
2. The number is created by `\caption`; a `\label` before it refers to the previous numbered element (e.g. the section), so the reference shows the wrong number.
3. Horizontal rules with proper spacing and weights for top, middle (below the header) and bottom of a table – from the **booktabs** package.
4. PDF, PNG, JPG (EPS via automatic conversion). SVG: convert to PDF (`inkscape fig.svg --export-type=pdf`) or use the `svg` package with Inkscape and `--shell-escape`.

## Level 2
5. The `\label`s are placed before the `\caption`s (or outside the figure environment), so they all pick up some other number – here apparently the same counter value. Put `\label` directly after `\caption` inside each figure.
6. The label name is misspelt / doesn't exist (check the warning "Reference … undefined"), or the label is in a part of the document that isn't compiled (e.g. `\include`d file excluded); also possible: `\label` inside a non-numbered environment.
7. JPEG compression is lossy and creates artefacts around sharp edges (lines, text). Use PDF (vector) – or PNG for raster data.
8. The figure was made at a large size (e.g. 20 cm wide) and scaled down to 8 cm in LaTeX, shrinking fonts. Export at the **final width** with the intended font size (e.g. 8 pt), then include at `width=\linewidth` (no further scaling).

## Level 3
9. ```latex
   \begin{figure}[tbp]
     \centering
     \includegraphics[width=0.6\textwidth]{figures/tuning}
     \caption{Orientation tuning of 48 V1 neurons.}
     \label{fig:tuning}
   \end{figure}
   ```
10. ```latex
    \begin{table}[tbp]
      \centering
      \caption{Demographics.}
      \label{tab:demo}
      \begin{tabular}{lrr}
        \toprule
        Group    & Age  & Female \\
        \midrule
        Patients & 34.2 & 12 \\
        Controls & 33.8 & 13 \\
        \bottomrule
      \end{tabular}
    \end{table}
    ```
11. ```latex
    % preamble – hyperref before cleveref
    \usepackage{booktabs}
    \usepackage{graphicx}
    \usepackage{hyperref}
    \usepackage[capitalise]{cleveref}
    % text
    Groups were matched (\cref{tab:demo}); tuning curves are shown in \cref{fig:tuning}.
    ```
    → "… (Table 1); tuning curves are shown in Figure 1."

## Level 4
12. Each figure/table has a script (`code/fig03_tuning.py`, `code/tab01_demographics.R`) that reads derived data and writes `figures/fig03.pdf` / `tables/tab01.tex` (e.g. via `to_latex()`/`kable()`); the thesis uses `\includegraphics{fig03}` and `\input{tables/tab01}`. A `Makefile`/`snakemake` (or one `run_all` script) runs all scripts, then `latexmk -pdf thesis.tex`. Any change in data or code → rerun → consistent PDF ([[CS13 Reproducibility and Research Software]]).
13. E.g. Python: `fig, ax = plt.subplots(figsize=(8.5/2.54, 6/2.54)); …; fig.savefig("erp.pdf")`; include with `\includegraphics[width=\linewidth]{erp}` inside a figure environment; compile with `latexmk -pdf` – references read "Figure 1"/"Table 1".
