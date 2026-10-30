---
aliases: [MATLAB Live Scripts, mlx, publish, MATLAB Reports, Live Editor]
tags: [programming, matlab, reports, reproducibility, latex, type/overview, neuro]
---
# MAT11 MATLAB Live Scripts and Reports

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT11 MATLAB Live Scripts and Reports - Worksheet|✏️ Worksheet]] · [[MAT11 MATLAB Live Scripts and Reports - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
An analysis is easier to understand – for your supervisor, your future self or a reviewer – when explanation, code, equations and figures sit together. MATLAB offers two ways: **Live Scripts** (interactive notebook-like documents) and **`publish`** (turning a normal script with comment markup into HTML/PDF). They play the role of Jupyter notebooks and R Markdown/Quarto ([[R10 R Markdown and Quarto]]).

## Live Scripts (.mlx)
- Created in the **Live Editor** (*New → Live Script*). The document mixes **text** (headings, lists, links, images), **code sections** and **output** shown inline or to the right (figures, tables, variables).
- **Run** section by section (Ctrl + Enter) or all; output updates in place.
- **Equations:** *Insert → Equation*, with a LaTeX editor ([[Doc06 LaTeX Math]]): $V(t) = V_\infty + (V_0 - V_\infty)e^{-t/\tau}$.
- **Live Controls:** sliders, drop-downs, check boxes bound to variables – e.g. choose a subject or filter cut-off and re-run; good for teaching and exploration.
- **Live Tasks:** point-and-click apps inside the script (e.g. *Clean Missing Data*, *Smooth Data*) that generate code you can inspect.
- **Export:** *Live Editor → Export* (PDF, HTML, Word, LaTeX, Markdown, Jupyter in recent releases) or from code: `export("analysis.mlx", "analysis.pdf")` (R2022a+).
- **Format:** classic `.mlx` files are zipped (binary), which makes **git diffs unreadable**; recent releases (R2025a+) can also store Live Scripts as plain-text `.m` files – prefer that if available. Otherwise keep the analysis logic in plain functions and use the Live Script as a thin report.
- Same caveat as notebooks: sections run in any order share one workspace – **clear and run all** before trusting a result.

## publish: reports from plain scripts
`publish` executes a normal `.m` script and turns its **comment markup** into a formatted document:
```matlab
%% P300 pilot analysis
% This report computes the grand-average ERP at *Pz* for
% oddball and standard trials.
%
% * Filter: 0.1–30 Hz
% * Reference: average
%
% The membrane equation, for comparison:
%
% $$ \tau \frac{dV}{dt} = -(V - E_L) + RI $$

%% Load data
S = load("derived/erp.mat");

%% Plot
plot(S.times, S.erp_oddball, S.times, S.erp_standard)
xlabel("Time (ms)"); ylabel("Amplitude (\muV)")
legend("oddball", "standard")
```
```matlab
publish("p300_report.m", "html")                                         % → html/p300_report.html
publish("p300_report.m", "format", "pdf", "outputDir", "reports", "showCode", false)
```
| Markup | Result |
|---|---|
| `%% Title` | section heading (first one = document title) |
| `% text` (after a `%%` line) | paragraph |
| `% *bold*`, `% _italic_`, `% \|monospace\|` | inline formatting |
| `% * item` / `% # item` | bullet / numbered list |
| `% $$ ... $$`, `% $x$` | LaTeX equations (display / inline) |
| `% <<figure.png>>` | include an image |
| `% <https://… link text>` | hyperlink |
| `%   indented code` | monospaced code block (not executed) |
- Formats: `html` (default), `pdf`, `doc`, `latex`, `xml`, `ppt`. Options: `showCode`, `evalCode`, `outputDir`, `maxOutputLines`, `figureSnapMethod`.
- Since the script is plain text, it diffs well in git and runs as a normal script too.
- `publish` runs in the base workspace by default – start the script with `clear` (or use a function wrapper) so results don't depend on leftover variables.

## Integrating formulas with LaTeX
- Live Editor equations and `publish` both use **LaTeX math syntax** (`\frac`, `\sum`, `\alpha`, `^`, `_`) – the same as Obsidian, Quarto and LaTeX documents ([[Doc02 Math in Markdown]], [[Doc06 LaTeX Math]]).
- Figure labels can use LaTeX: `xlabel("$\Delta F/F$", "Interpreter", "latex")`.
- `latex(sym_expression)` (Symbolic Math Toolbox) converts symbolic results to LaTeX code for papers.
- Export to LaTeX (*Export → LaTeX*) produces a `.tex` file plus figures you can include in a thesis ([[Doc05 LaTeX Basics]]).

## Same idea in Python and R
Jupyter notebooks / `# %%` scripts ([[Py01 Python Basics and Syntax]]); R Markdown / Quarto ([[R10 R Markdown and Quarto]]). Quarto can also render Jupyter notebooks, not MATLAB Live Scripts directly – export to Markdown/Jupyter first if you want one tool for everything.

## In neuroscience #neuro
- **Lab notebooks for analyses:** one Live Script per experiment step with explanations, parameters and QC figures – easy to share with the supervisor as PDF.
- **Teaching:** Live Controls to explore how filter cut-offs change an ERP or how τ changes the membrane response ([[Ph05 Capacitance and RC Circuits]]).
- **Automated QC reports:** a `publish`ed script per subject (bad channels, rejected trials, ICA components) – loop over subjects and write one HTML each.
- **Supplementary methods:** the published report documents exactly what was run, with versions (`ver` output at the end).

## Math links #math-link
- LaTeX equation syntax → [[Doc06 LaTeX Math]]
- Example equations: membrane equation → [[B10 Differential Equations]]

## Connections
- Basics, sections `%%` → [[MAT01 MATLAB Basics and Syntax]]
- Figures → [[MAT05 MATLAB Plotting]]
- Markdown/HTML/LaTeX outputs → [[Doc01 Markdown Syntax]], [[Doc04 HTML for Reports and Figures]], [[Doc05 LaTeX Basics]]
- Reproducibility → [[MAT12 MATLAB Reproducible Projects]], [[CS13 Reproducibility and Research Software]]

## Key takeaways
- Live Scripts = text + code + inline output, with equations, live controls and export to PDF/HTML/LaTeX.
- `.mlx` is binary – keep logic in `.m` functions or use plain-text Live Scripts (recent releases).
- `publish("script.m", "pdf")` turns comment markup (`%%`, `%`, `$$…$$`, `<<img>>`) into reports.
- LaTeX math syntax is the same everywhere: Live Editor, `publish`, Obsidian, Quarto, LaTeX.
