---
tags: [programming, matlab, reports, type/worksheet]
---
# MAT11 MATLAB Live Scripts and Reports – Worksheet

> Theory: [[MAT11 MATLAB Live Scripts and Reports]] · Solutions: [[MAT11 MATLAB Live Scripts and Reports - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Recall
1. Name three things a Live Script can contain that a plain `.m` script can't display inline.
2. What does `publish("a.m", "pdf")` do?
3. What does `%%` mean in a plain script, and in a script that is published?
4. Why are `.mlx` files problematic in git?

## Level 2 – Markup
5. Write `publish` markup for: a section "Methods", a paragraph, a bullet list with two items, and the display equation $f_\text{Nyquist} = f_s/2$.
6. How do you include the image `figs/setup.png` in a published report?
7. How do you hide the code but show results and figures in the published PDF?

## Level 3 – Debugging
8. Your published report shows a figure from a previous run instead of the current one, and a variable that isn't created in the script. Why? Fix.
9. A colleague changes one parameter in your `.mlx` and the git diff shows the whole file changed. What can you do?

## Level 4 – Neuro transfer
10. Plan an automatic QC report for each of 30 EEG subjects with `publish`. How do you pass the subject ID to the script?
11. Write the LaTeX for the ERSP definition $\text{ERSP}(f, t) = 10\log_{10}\frac{P(f, t)}{\bar P_\text{base}(f)}$ as it would appear in a `publish` comment.
12. 💻 Write a short script with two sections (load/simulate data; plot) and markup including one equation, then `publish` it as HTML and as PDF.
