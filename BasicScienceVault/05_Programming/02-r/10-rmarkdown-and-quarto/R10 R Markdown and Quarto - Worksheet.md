---
tags: [programming, r, quarto, type/worksheet]
---
# R10 R Markdown and Quarto – Worksheet

> Theory: [[R10 R Markdown and Quarto]] · Solutions: [[R10 R Markdown and Quarto - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Anatomy
1. Name the three main parts of an `.Rmd`/`.qmd` file.
2. What is the difference between `echo: false`, `eval: false` and `include: false`?
3. What does `` `r round(mean(df$rt), 3)` `` do inside a sentence?
4. Which output format needs a LaTeX installation?

## Level 2 – Debugging
5. Your report runs fine chunk by chunk in RStudio but fails on Render with "object 'erp' not found". Why? Fix.
6. A chunk with `cache: true` reads `data.csv`. You update the CSV but the figure doesn't change. Why?
7. `@fig-erp` shows "?@fig-erp" in the output. What's missing?
8. A PDF render fails with "LaTeX Error: Unicode character α (U+03B1) not set up for use with LaTeX" (you typed α directly in the text). Two fixes.

## Level 3 – Write
9. Write a YAML header for a report titled "P300 pilot", rendering to HTML with a table of contents and folded code, and to PDF, with a bibliography `refs.bib`.
10. Write a chunk that shows a figure with caption "Mean RT per condition." and label for cross-referencing, without showing the code.
11. Write a sentence with inline code reporting a t-test result `tt` as "t(23) = 2.71, p = .012" (use `tt$parameter`, `tt$statistic`, `tt$p.value`).

## Level 4 – Neuro transfer
12. Describe how you would produce one QC report per subject for 40 EEG participants with one Quarto file.
13. Why should the hour-long ICA preprocessing not run inside the report? How do report and preprocessing communicate?
14. 💻 Create `test.qmd` with a YAML header, one paragraph containing an inline value, one equation with a label, one figure chunk (any ggplot), and render it to HTML (and to PDF if LaTeX is installed).
