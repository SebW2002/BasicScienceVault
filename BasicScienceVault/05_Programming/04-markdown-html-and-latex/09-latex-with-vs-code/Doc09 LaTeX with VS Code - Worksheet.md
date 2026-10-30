---
tags: [programming, latex, vscode, type/worksheet]
---
# Doc09 LaTeX with VS Code – Worksheet

> Theory: [[Doc09 LaTeX with VS Code]] · Solutions: [[Doc09 LaTeX with VS Code - Solutions]] · Log mistakes in [[Mistakes - Markdown HTML LaTeX]]
> Answer on paper; try things out only for tasks marked 💻.

## Level 1 – Recall
1. Which two things must be installed to compile LaTeX in VS Code?
2. What do Ctrl + Alt + B, Ctrl + Alt + V and Ctrl + Alt + J do in LaTeX Workshop?
3. What is SyncTeX, and which flag/file does it need?
4. Where do you see compile errors in VS Code?

## Level 2 – Configuration
5. In the tool definition, what do `%DOC%`, `%OUTDIR%`, `-interaction=nonstopmode` and `-file-line-error` mean?
6. You want LaTeX Workshop to use lualatex and put all auxiliary files into `build/`. Which two settings do you change? Why add `build/` to `.gitignore`?
7. Your thesis has `chapters/methods.tex` included with `\input`. Building while `methods.tex` is open fails ("missing \begin{document}"). Fix.
8. Why might a `.latexmkrc` file be better than VS Code settings for the build configuration?

## Level 3 – Pandoc
9. Write the Pandoc command that converts `methods.md` with citations from `refs.bib` (APA style file `apa.csl`) into a PDF.
10. Write the command that converts `methods.md` into a standalone `.tex` file. What does `-s` do?
11. Which parts of an Obsidian note won't survive a Pandoc conversion? How do you deal with them?

## Level 4 – Neuro transfer
12. Describe a workflow from Obsidian notes on your analysis methods to the methods chapter of a LaTeX thesis.
13. 💻 Set up VS Code + LaTeX Workshop, create a small project with `main.tex` and `chapters/intro.tex`, configure output into `build/`, compile, and test forward and backward SyncTeX.
