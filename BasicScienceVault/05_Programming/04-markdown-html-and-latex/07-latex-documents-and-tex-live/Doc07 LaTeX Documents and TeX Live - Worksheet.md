---
tags: [programming, latex, bibliography, type/worksheet]
---
# Doc07 LaTeX Documents and TeX Live – Worksheet

> Theory: [[Doc07 LaTeX Documents and TeX Live]] · Solutions: [[Doc07 LaTeX Documents and TeX Live - Solutions]] · Log mistakes in [[Mistakes - Markdown HTML LaTeX]]
> Write on paper or in a text editor; compile only for tasks marked 💻.

## Level 1 – Recall
1. Which document class for: a) a 6-page paper b) a master's thesis with chapters c) a lab-meeting talk?
2. `! LaTeX Error: File 'apa7.cls' not found.` What does it mean, and which two `tlmgr` commands help?
3. Name the four commands/steps to produce a bibliography with biblatex (preamble, citing, printing, compiling).
4. What do `\usepackage[T1]{fontenc}` and `\usepackage{lmodern}` do?

## Level 2 – Understanding
5. Your references appear as **[polich2007]** in bold and the list is empty. What step is missing?
6. A journal requires `\bibliographystyle{jneurosci}`. Do you use BibTeX or biblatex? Why?
7. The title "Updating P300" appears as "Updating p300" in the bibliography. Why? Fix in the `.bib` file.
8. Your unnumbered "Acknowledgements" section is missing from the table of contents. Fix.

## Level 3 – Write
9. Write the `.bib` entry for: Luck, Steven J. (2014). *An Introduction to the Event-Related Potential Technique* (2nd ed.). MIT Press.
10. Write the preamble lines for A4 paper, 3 cm left margin and 2.5 cm elsewhere, English hyphenation, Latin Modern fonts, and biblatex with an author–year style reading `refs.bib`.
11. Write a beamer frame titled "Methods" with a three-item list whose items appear one after another.

## Level 4 – Neuro transfer
12. Set up the skeleton of a thesis (`report`): title page, abstract, table of contents with roman page numbers, three chapters, bibliography, appendix.
13. 💻 Create `refs.bib` with two entries, cite them with `\textcite` and `\parencite`, compile with `latexmk -pdf` and check that latexmk ran biber automatically (look at the log).
