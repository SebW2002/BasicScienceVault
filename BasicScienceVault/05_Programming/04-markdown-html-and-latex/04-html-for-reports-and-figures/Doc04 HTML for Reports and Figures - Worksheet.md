---
tags: [programming, html, reports, type/worksheet]
---
# Doc04 HTML for Reports and Figures – Worksheet

> Theory: [[Doc04 HTML for Reports and Figures]] · Solutions: [[Doc04 HTML for Reports and Figures - Solutions]] · Log mistakes in [[Mistakes - Markdown HTML LaTeX]]
> Write on paper or in a text editor; render only for tasks marked 💻.

## Level 1 – Recall
1. What are `<figure>` and `<figcaption>` for? Why not just `<img>` followed by `<p>`?
2. What does `<details open>` do differently from `<details>`?
3. What is the difference between a self-contained HTML report and one with linked resources?
4. Which image format would you use in an HTML report for a) an ERP line plot b) a 3-D brain rendering screenshot?

## Level 2 – Read and fix
5. A colleague e-mails you `report.html`; all figures are broken images. Why? Two fixes.
6. In a rendered Quarto report, the heading "Results & Discussion" has `id="results-discussion"`. How do you link to it from another section?
7. Your report's figures are too wide on a laptop screen. Which CSS rule (for images inside figures) fixes it?

## Level 3 – Write
8. Write a `<figure>` for `figures/psth.png` with alt text and the caption "Figure 2. PSTH of 34 units, 10 ms bins."
9. Write a collapsible section titled "Full model output" containing a `<pre>` block.
10. Write the Quarto YAML that makes the HTML self-contained with a table of contents and folded code.

## Level 4 – Neuro transfer
11. You produce QC reports for 40 subjects. Which elements would you put in a per-subject HTML page, and what would you fold with `<details>`?
12. 💻 Render a small Quarto or R Markdown document to HTML twice (with and without `embed-resources`), compare file sizes and folder contents, and inspect a figure with the browser's developer tools.
