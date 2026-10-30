---
tags: [programming, matlab, reports, type/solution]
---
# MAT11 MATLAB Live Scripts and Reports – Solutions

> Worksheet: [[MAT11 MATLAB Live Scripts and Reports - Worksheet]] · Theory: [[MAT11 MATLAB Live Scripts and Reports]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. Any three: formatted text with headings, rendered equations, inline figures/output, images, hyperlinks, live controls (sliders, drop-downs), live tasks.
2. Runs the script and creates a PDF document from its comment markup, code and output (figures, printed results).
3. Plain script: a **code section** (run with Ctrl + Enter). Published: the start of a new **section with heading** in the report.
4. They are zipped binary files: git can't show meaningful line-by-line differences, and merges are impossible.

## Level 2
5. ```matlab
   %% Methods
   % EEG was recorded at 500 Hz.
   %
   % * Filter: 0.1–30 Hz
   % * Reference: average
   %
   % $$ f_\mathrm{Nyquist} = \frac{f_s}{2} $$
   ```
6. `% <<figs/setup.png>>` (in a comment block; the path is relative to the script or output folder).
7. `publish("a.m", "format", "pdf", "showCode", false)`.

## Level 3
8. `publish` runs in the base workspace, so leftover variables (and open figures) from earlier work are used. Start the script with `clear; close all;` (or create a fresh state another way) and make sure every variable is created in the script.
9. Store the Live Script in plain-text format (R2025a+), keep the analysis logic in `.m` functions and make the `.mlx` a thin report, or export it (e.g. to `.m` or Markdown) for versioning.

## Level 4
10. Write the report script so it reads a variable (e.g. `subject`) that must exist; then loop: `for s = subjects, subject = s; publish("qc_report.m", "format", "html", "outputDir", fullfile("reports", s), "codeToEvaluate", sprintf('subject = "%s"; qc_report', s)); end` (`codeToEvaluate` sets the subject before the script runs). Alternatively make `qc_report` a function and publish a tiny wrapper script per subject.
11. `% $$ \mathrm{ERSP}(f, t) = 10\log_{10}\frac{P(f, t)}{\bar{P}_\mathrm{base}(f)} $$`
12. ```matlab
    %% Simulated alpha rhythm
    % A 10 Hz rhythm with noise, sampled at $f_s = 250$ Hz:
    %
    % $$ x(t) = \sin(2\pi\cdot 10\, t) + \varepsilon(t) $$
    fs = 250; t = 0:1/fs:2-1/fs; rng(1);
    x = sin(2*pi*10*t) + 0.5*randn(size(t));

    %% Plot
    plot(t, x); xlabel("Time (s)"); ylabel("a.u.")
    ```
    Save as `alpha_demo.m`; `publish("alpha_demo.m", "html")` and `publish("alpha_demo.m", "pdf")`.
