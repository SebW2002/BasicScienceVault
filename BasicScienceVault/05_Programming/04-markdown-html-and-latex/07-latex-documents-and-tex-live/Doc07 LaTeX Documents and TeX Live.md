---
aliases: [TeX Live, tlmgr, Document Classes, beamer, BibTeX, biblatex, geometry, Table of Contents]
tags: [programming, latex, bibliography, documentation, type/overview, neuro]
---
# Doc07 LaTeX Documents and TeX Live

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc07 LaTeX Documents and TeX Live - Worksheet|✏️ Worksheet]] · [[Doc07 LaTeX Documents and TeX Live - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
A thesis or paper needs more than sections and equations: the right **document class**, a **bibliography** managed from a reference database, sensible **page layout and fonts**, a **table of contents** and **headers/footers** – and a TeX installation that has all required packages. This note covers that "document machinery".

## TeX Live and installing packages with tlmgr
- **TeX Live** is the standard cross-platform TeX distribution (yearly releases; ~ 5000 packages in the full scheme). Alternatives: **MacTeX** (TeX Live for macOS), **MiKTeX** (Windows; installs missing packages on the fly), **TinyTeX** (small TeX Live, used by Quarto/R: `quarto install tinytex`), **Overleaf** (online, nothing to install).
- **tlmgr** (TeX Live Manager) manages packages:
```bash
tlmgr update --self --all           # update tlmgr and all packages
tlmgr install siunitx               # install a package (may need sudo on system-wide installs)
tlmgr info biblatex                 # information / whether installed
tlmgr search --global --file apa7.cls   # which package provides a missing file?
kpsewhich siunitx.sty               # where is (or isn't) a file found by TeX?
```
- A missing package shows up as `! LaTeX Error: File 'siunitx.sty' not found.` → find and install the package that provides it.
- Linux distributions often package TeX Live themselves (`apt install texlive-science`); there `tlmgr` usually can't be used – install via the package manager or use a vanilla TeX Live/TinyTeX.

## Document classes: article, report, beamer
| Class | Structure | Use |
|---|---|---|
| `article` | `\section`, no chapters; title on first page | papers, reports, exercise sheets |
| `report` | `\chapter` + sections; separate title page | theses, long reports |
| `book` | chapters, front/main/back matter, two-sided | books, monographs |
| `beamer` | `frame`s (slides), themes, overlays | presentations |
| others | `memoir`, `scrartcl`/`scrreprt` (KOMA-Script), journal and university templates (`elsarticle`, `revtex`, thesis classes) | – |
```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{metropolis}             % or default, Madrid, ...
\title{P300 and Working Memory}
\author{Anna Example}
\begin{document}
\frame{\titlepage}
\begin{frame}{Results}
  \begin{itemize}
    \item<1-> larger P300 for oddballs
    \item<2-> correlates with RT          % appears on the second click (overlay)
  \end{itemize}
  \includegraphics[width=0.7\textwidth]{figures/erp.pdf}
\end{frame}
\end{document}
```
Many universities provide an official thesis class or template – use it.

## Literature management with BibTeX or biblatex
References live in a **`.bib` file** (exported from Zotero/JabRef/Mendeley, or Google Scholar):
```bibtex
@article{polich2007,
  author  = {Polich, John},
  title   = {Updating {P300}: An integrative theory of {P3a} and {P3b}},
  journal = {Clinical Neurophysiology},
  year    = {2007},
  volume  = {118},
  number  = {10},
  pages   = {2128--2148},
  doi     = {10.1016/j.clinph.2007.04.019}
}
```
| | BibTeX (classic) | **biblatex** + biber (modern) |
|---|---|---|
| preamble | `\usepackage{natbib}` (author–year) or nothing | `\usepackage[style=apa]{biblatex}` + `\addbibresource{refs.bib}` |
| cite | `\cite{key}`, `\citep{key}`, `\citet{key}` (natbib) | `\cite{key}`, `\parencite{key}`, `\textcite{key}` |
| style | `\bibliographystyle{apalike}` (`.bst` files) | `style=` option (apa, numeric, authoryear, nature, …), easy to customise |
| print list | `\bibliography{refs}` | `\printbibliography` |
| run | `pdflatex → bibtex → pdflatex → pdflatex` | `pdflatex → biber → pdflatex` |
| Unicode in .bib | limited | full |
- Journals often require BibTeX with their `.bst` file; for theses and own documents, **biblatex + biber** is more flexible.
- `latexmk` detects which tool to run ([[Doc05 LaTeX Basics]]); Quarto/Pandoc use the same `.bib` files with CSL styles ([[R10 R Markdown and Quarto]]).
- Braces in `.bib` titles (`{P300}`) protect capitalisation from styles that lowercase titles.
- **Zotero + Better BibTeX** keeps a `.bib` file automatically in sync with stable citation keys.

## Page layout with geometry; fonts with fontenc and lmodern
```latex
\usepackage[a4paper, margin=2.5cm]{geometry}     % or top=, bottom=, left=, right=, includeheadfoot
\usepackage[T1]{fontenc}                         % 8-bit font encoding: correct hyphenation of ä, ö, ü, copy-paste
\usepackage{lmodern}                             % Latin Modern: scalable version of the default font
\usepackage[english]{babel}                      % language rules (hyphenation, "Figure"/"Abbildung")
\usepackage{microtype}                           % subtle spacing improvements
\usepackage{setspace} \onehalfspacing            % line spacing if required by your faculty
```
- `T1` + `lmodern` is the classic pdflatex combination. `T1` **without** a scalable font falls back to bitmap fonts (blurry PDF) and makes `microtype` fail with "auto expansion is only possible with scalable fonts" – load `lmodern` (or another T1 font package). With xelatex/lualatex use `fontspec` and system fonts (`\setmainfont{TeX Gyre Termes}`).
- Change fonts and margins in the **preamble** only – the content stays untouched.

## Table of contents, headers and footers
```latex
\tableofcontents          % generated from \section/\chapter (needs two runs)
\listoffigures \listoftables
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}                              % clear defaults
\fancyhead[L]{\leftmark}                % current chapter/section on the left
\fancyhead[R]{Anna Example}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\usepackage{hyperref}                   % clickable TOC, references, URLs, PDF bookmarks (load late)
\hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}
```
- `\section*` entries don't appear in the TOC; add them with `\addcontentsline{toc}{section}{Acknowledgements}`.
- Front matter numbering (roman i, ii, … for the abstract and TOC) in `report`: `\pagenumbering{roman}` … `\pagenumbering{arabic}`; `book` has `\frontmatter`/`\mainmatter`.
- `hyperref` should be loaded near the end of the preamble (before `cleveref`).

## In neuroscience #neuro
- **Thesis template:** `report` (or the university class) with chapters per study, biblatex with APA or the field's style, `geometry` per faculty rules.
- **Conference talks and lab meetings** in beamer – equations and figures look identical to the paper.
- **Journal submissions:** many neuroscience journals (J Neurosci, eLife, PLOS, Frontiers) accept LaTeX with their templates; Overleaf has most templates.
- **Shared `.bib`** files for a lab via Zotero group libraries.

## Connections
- Basics and compiling → [[Doc05 LaTeX Basics]]; math → [[Doc06 LaTeX Math]]
- Figures, tables, cross-references → [[Doc08 LaTeX Figures Tables and References]]
- Editor and build setup → [[Doc09 LaTeX with VS Code]]
- Citations in Quarto → [[R10 R Markdown and Quarto]]

## Key takeaways
- TeX Live (+ `tlmgr install`, `tlmgr search --global --file`), MiKTeX, TinyTeX, Overleaf.
- `article` (papers), `report`/`book` (theses), `beamer` (slides) – or your university template.
- References in a `.bib`; biblatex + biber (`\addbibresource`, `\parencite`, `\printbibliography`) or BibTeX (`\bibliographystyle`, `\bibliography`).
- Preamble controls layout: `geometry`, `fontenc` + `lmodern`, `babel`, `fancyhdr`, `hyperref`; `\tableofcontents` needs two runs.
