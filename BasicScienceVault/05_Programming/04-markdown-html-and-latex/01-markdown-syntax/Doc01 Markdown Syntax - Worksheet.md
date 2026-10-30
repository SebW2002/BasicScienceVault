---
tags: [programming, markdown, type/worksheet]
---
# Doc01 Markdown Syntax – Worksheet

> Theory: [[Doc01 Markdown Syntax]] · Solutions: [[Doc01 Markdown Syntax - Solutions]] · Log mistakes in [[Mistakes - Markdown HTML LaTeX]]
> Work on paper or in a plain text editor; check rendering only for tasks marked 💻.

## Level 1 – Write the Markdown
1. A level-2 heading "Methods", a paragraph with one **bold** word and one *italic* word, and inline code `mne.Epochs`.
2. A nested list: "Preprocessing" with sub-items "filter" and "ICA"; then "Statistics".
3. A link to `https://openneuro.org` with the text "OpenNeuro" and an image `figs/erp.png` with alt text "Grand-average ERP".
4. A Python code block that prints "hello".

## Level 2 – Predict the rendering
5. What is rendered?
   ```markdown
   Line one
   Line two

   Line three
   ```
   (In standard Markdown, not Obsidian's default view.)
6. What's wrong: `#Results` and `##  Discussion` directly under a paragraph without a blank line?
7. What happens to the table if a cell contains `a|b`? How do you fix it?
8. Is `[[Py05 NumPy and Arrays]]` a link on GitHub? Why or why not?

## Level 3 – Tables and more
9. Write a table with columns "Band", "Range (Hz)" (right-aligned) and rows for delta (1–4) and gamma (30–100).
10. Write a task list with "record pilot" (done) and "analyse pilot" (open), and a footnote after the sentence "The task followed Smith et al." pointing to the reference text.
11. Write an Obsidian callout of type `warning` with the title "Raw data" and the text "Never edit files in data/raw."

## Level 4 – Neuro transfer
12. Draft (in Markdown) a dataset `README` skeleton for an EEG study: title, description, folder structure in a code block, how to run the analysis, contact.
13. 💻 Paste your answers to tasks 1–11 into an Obsidian note and into a GitHub Gist (or any CommonMark preview), and list which elements render differently.
