---
tags: [programming, latex, figures, tables, type/worksheet]
---
# Doc08 LaTeX Figures Tables and References – Worksheet

> Theory: [[Doc08 LaTeX Figures Tables and References]] · Solutions: [[Doc08 LaTeX Figures Tables and References - Solutions]] · Log mistakes in [[Mistakes - Markdown HTML LaTeX]]
> Write on paper or in a text editor; compile only for tasks marked 💻.

## Level 1 – Recall
1. What is a float, and what do `[tbp]` and `[H]` mean?
2. Why must `\label` come after `\caption`?
3. What are `\toprule`, `\midrule`, `\bottomrule`? Which package provides them?
4. Which image formats can `pdflatex` include directly? What do you do with an SVG?

## Level 2 – Debug
5. All figure references show "Figure 2" although they point to different figures. Cause?
6. `\ref{fig:erp}` shows `??` after compiling twice. Two possible causes.
7. A plot exported as JPG looks blurry with coloured blocks around lines in the PDF. Why? Better format?
8. The fonts in your figures are tiny compared to the text. Why, and how do you fix it at the source?

## Level 3 – Write
9. Write a figure environment including `figures/tuning.pdf` at 60 % of the text width, centred, with caption "Orientation tuning of 48 V1 neurons." and label `fig:tuning`.
10. Write a booktabs table with columns Group (left), Age (right), Female (right) and rows Patients 34.2 / 12, Controls 33.8 / 13, caption above, label `tab:demo`.
11. Write a sentence that refers to the figure and table of tasks 9 and 10 with cleveref, and the preamble lines needed (in the right order).

## Level 4 – Neuro transfer
12. Describe a workflow in which every thesis figure and table is regenerated automatically from the analysis code.
13. 💻 Export one plot from Python or R as PDF at 8.5 cm width, include it in a document with a booktabs table and `\cref` references, and compile.
