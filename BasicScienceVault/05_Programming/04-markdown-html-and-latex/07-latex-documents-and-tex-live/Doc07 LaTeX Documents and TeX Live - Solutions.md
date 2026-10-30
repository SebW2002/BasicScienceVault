---
tags: [programming, latex, bibliography, type/solution]
---
# Doc07 LaTeX Documents and TeX Live – Solutions

> Worksheet: [[Doc07 LaTeX Documents and TeX Live - Worksheet]] · Theory: [[Doc07 LaTeX Documents and TeX Live]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. a) `article` (or the journal's class) b) `report` (or `book`/the university's thesis class) c) `beamer`.
2. The document class file isn't installed. `tlmgr search --global --file apa7.cls` finds the package providing it (here `apa7`); `tlmgr install apa7` installs it. (MiKTeX installs it on demand; Overleaf has it.)
3. Preamble: `\usepackage[style=…]{biblatex}` + `\addbibresource{refs.bib}`; cite: `\parencite{key}` / `\textcite{key}`; print: `\printbibliography`; compile: `pdflatex → biber → pdflatex` (or `latexmk -pdf`).
4. `fontenc` with `T1` uses an 8-bit font encoding so accented characters are real glyphs (correct hyphenation, copy-paste, search). `lmodern` provides scalable Latin Modern fonts in that encoding (sharp PDF, needed by `microtype`).

## Level 2
5. The bibliography tool (biber for biblatex, bibtex for BibTeX) wasn't run, so LaTeX doesn't know the entries. Run biber and LaTeX again – or `latexmk -pdf`.
6. BibTeX (with `natbib` if needed): `.bst` styles only work with BibTeX; biblatex uses its own styles.
7. The bibliography style converts titles to sentence case. Protect capitals with braces: `title = {Updating {P300}: …}`.
8. Add `\addcontentsline{toc}{section}{Acknowledgements}` right after `\section*{Acknowledgements}` (use `chapter` instead of `section` in a report if it is a chapter-level heading).

## Level 3
9. ```bibtex
   @book{luck2014,
     author    = {Luck, Steven J.},
     title     = {An Introduction to the Event-Related Potential Technique},
     edition   = {2},
     publisher = {MIT Press},
     address   = {Cambridge, MA},
     year      = {2014}
   }
   ```
10. ```latex
    \usepackage[a4paper, left=3cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}
    \usepackage[T1]{fontenc}
    \usepackage{lmodern}
    \usepackage[english]{babel}
    \usepackage[style=authoryear]{biblatex}
    \addbibresource{refs.bib}
    ```
11. ```latex
    \begin{frame}{Methods}
      \begin{itemize}
        \item<1-> 24 participants, visual oddball
        \item<2-> 64-channel EEG, 500 Hz
        \item<3-> mixed models on single-trial P300
      \end{itemize}
    \end{frame}
    ```
    (Or `\begin{itemize}[<+->]` for automatic step-by-step items.)

## Level 4
12. ```latex
    \documentclass[12pt, a4paper]{report}
    % preamble: geometry, fontenc, lmodern, babel, biblatex, graphicx, hyperref ...
    \begin{document}
    \begin{titlepage} ... \end{titlepage}
    \pagenumbering{roman}
    \begin{abstract} ... \end{abstract}
    \tableofcontents
    \clearpage\pagenumbering{arabic}
    \chapter{Introduction}  ...
    \chapter{Study 1}       ...
    \chapter{General Discussion} ...
    \printbibliography[heading=bibintoc]
    \appendix
    \chapter{Supplementary Methods} ...
    \end{document}
    ```
13. The log/terminal shows latexmk running `pdflatex`, then `biber t13`, then `pdflatex` again (latexmk re-runs until references are stable); the PDF shows "Polich (2007)" and "(Polich, 2007)" and a reference list.
