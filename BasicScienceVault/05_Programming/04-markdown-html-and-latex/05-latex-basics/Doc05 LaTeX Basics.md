---
aliases: [LaTeX Basics, documentclass, LaTeX Environments, pdflatex, latexmk, LaTeX Errors]
tags: [programming, latex, documentation, type/overview, neuro]
---
# Doc05 LaTeX Basics

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc05 LaTeX Basics - Worksheet|✏️ Worksheet]] · [[Doc05 LaTeX Basics - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
LaTeX is the standard for documents with serious mathematics: theses, papers in computational neuroscience and physics, lecture notes, and the PDF output of Quarto/R Markdown. You write plain text with **commands**; a TeX engine typesets it into a PDF with professional layout, automatic numbering, cross-references and bibliographies. It's also plain text – so it works with git.

## Structure of a document
```latex
\documentclass[11pt, a4paper]{article}   % document class + options
\usepackage[utf8]{inputenc}              % input encoding (default in modern LaTeX anyway)
\usepackage[T1]{fontenc}                 % font encoding (umlauts, hyphenation)
\usepackage{amsmath}                     % better math (Doc06)
\usepackage{graphicx}                    % figures (Doc08)

\title{The P300 in a Visual Oddball Task}
\author{Anna Example}
\date{\today}

\begin{document}                         % ← everything above is the preamble
\maketitle

\section{Introduction}
The P300 is a positive deflection of the event-related potential.

\end{document}
```
| Part | Role |
|---|---|
| `\documentclass[options]{class}` | type of document (`article`, `report`, `book`, `beamer`; [[Doc07 LaTeX Documents and TeX Live]]) and global options |
| **preamble** (between `\documentclass` and `\begin{document}`) | packages (`\usepackage`), settings, macros, title data – no text output |
| `\begin{document} … \end{document}` | the content |
- `%` starts a comment (to write a percent sign: `\%`).
- Blank line = new paragraph; single line breaks are spaces; multiple spaces = one space.
- Special characters that must be escaped: `# $ % & _ { } ~ ^ \` → `\# \$ \% \& \_ \{ \} \textasciitilde \textasciicircum \textbackslash`.

## Commands and environments
- **Commands** start with a backslash: `\section{Methods}`, `\textbf{bold}`, `\today`, `\\` (line break). Arguments in `{}` (mandatory) and `[]` (optional): `\documentclass[11pt]{article}`, `\includegraphics[width=0.8\textwidth]{erp.pdf}`.
- **Environments** mark a region with `\begin{name} … \end{name}`:
```latex
\begin{itemize}
  \item filter 0.1--30 Hz
  \item ICA artefact removal
\end{itemize}
\begin{enumerate} \item first \item second \end{enumerate}
\begin{quote} A quotation. \end{quote}
\begin{center} centred text \end{center}
\begin{equation} V = IR \end{equation}       % Doc06
```
- Every `\begin{x}` needs a matching `\end{x}` – mismatches are the most common error.
- **Own commands** (macros): `\newcommand{\eeg}{\textsc{eeg}}` then `\eeg{}`; with arguments: `\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}`.

## Sections and text formatting
```latex
\section{Methods}            % 1  Methods
\subsection{Participants}    % 1.1  Participants
\subsubsection{Exclusions}   % 1.1.1
\paragraph{Note.}            % run-in heading
\section*{Acknowledgements}  % * = unnumbered (and not in the table of contents)
\chapter{Introduction}       % only in report/book classes
```
| Formatting | Command |
|---|---|
| bold, italic, emphasis | `\textbf{}`, `\textit{}`, `\emph{}` (semantic; toggles italic) |
| monospace, small caps | `\texttt{}`, `\textsc{}` |
| sizes | `{\small …}`, `{\large …}`, `\footnotesize`, `\Large`, … |
| footnote | `\footnote{text}` |
| non-breaking space | `Fig.~3`, `5~ms` (keeps them on one line) |
| dashes | `-` hyphen, `--` en dash (ranges: 1--40 Hz), `---` em dash |
| quotes | ``` ``text'' ``` (or `\enquote{}` with csquotes) – not `"text"` |
| units | `\SI{5}{\milli\volt}` / `\qty{5}{\milli\volt}` with the `siunitx` package |
Numbering of sections, equations, figures and tables is automatic – insert a section and everything renumbers.

## Compiling with pdflatex / latexmk – and reading errors
```bash
pdflatex thesis.tex      # one pass: produces thesis.pdf, thesis.log, thesis.aux
pdflatex thesis.tex      # second pass: resolves \ref and the table of contents
latexmk -pdf thesis.tex  # runs pdflatex (+ biber/bibtex) as often as needed – recommended
latexmk -c               # clean auxiliary files
```
- LaTeX needs **several passes**: the first writes labels and section titles into the `.aux` file, the next reads them (that's why references show `??` after one run). Bibliographies need `biber`/`bibtex` in between ([[Doc07 LaTeX Documents and TeX Live]]). `latexmk` automates this.
- Engines: `pdflatex` (classic, fastest, limited Unicode), `xelatex`/`lualatex` (full Unicode and system fonts, needed for e.g. µ typed directly with modern fonts, or non-Latin scripts).
- Editors (VS Code + LaTeX Workshop, [[Doc09 LaTeX with VS Code]]; Overleaf online) run these commands for you.

**Reading error messages** (in the console and the `.log` file):
```text
! Undefined control sequence.
l.42 The membrane time constant \taus
                                      = RC.
```
- The line starting with `!` says **what**, `l.42` says **where** (line 42), and the line break in the excerpt shows **how far** LaTeX read before failing (here at `\taus` – a typo for `\tau`, and outside math mode anyway).
| Message | Typical cause |
|---|---|
| `Undefined control sequence` | typo in a command or missing package |
| `Missing $ inserted` | math command (`\alpha`, `_`, `^`) used outside math mode |
| `Missing } inserted` / `Runaway argument` | unbalanced braces |
| `\begin{itemize} on input line 12 ended by \end{document}` | environment not closed |
| `File 'erp.pdf' not found` | wrong path/name of a figure |
| `Overfull \hbox` (warning) | a line sticks into the margin (long word/URL) – cosmetic |
| `Reference 'fig:erp' undefined` (warning) | needs another run, or the label doesn't exist |
- **Fix the first error first** – later errors are often consequences. When stuck, press `x` + Enter to quit an interactive error prompt; comment out half of the document to locate the problem.

## Same idea in Markdown and HTML
Markdown `#` ↔ `\section`, `**bold**` ↔ `\textbf`, lists ↔ `itemize`/`enumerate`; HTML tags ↔ LaTeX environments. Pandoc converts between them ([[Doc10 When to Use What]]).

## In neuroscience #neuro
- **Theses and dissertations** with many equations, figures and references – LaTeX handles numbering and cross-references for hundreds of pages.
- **Computational neuroscience papers** (models, derivations) are usually written in LaTeX; many journals and bioRxiv accept LaTeX templates; Overleaf is common for collaborative writing.
- **PDF output of Quarto/R Markdown** goes through LaTeX – reading LaTeX errors helps when a report fails to render ([[R10 R Markdown and Quarto]]).
- **Lecture notes and exercise sheets** with exact maths (like this vault's formulas) – the math syntax is identical ([[Doc06 LaTeX Math]]).

## Math links #math-link
- Mathematical typesetting → [[Doc06 LaTeX Math]], [[Doc02 Math in Markdown]]

## Connections
- Math → [[Doc06 LaTeX Math]]; document classes, packages, bibliography → [[Doc07 LaTeX Documents and TeX Live]]
- Figures, tables, references → [[Doc08 LaTeX Figures Tables and References]]
- Editor setup → [[Doc09 LaTeX with VS Code]]
- When to use LaTeX → [[Doc10 When to Use What]]

## Key takeaways
- `\documentclass` → preamble (`\usepackage`) → `\begin{document} … \end{document}`.
- Commands `\name[opt]{arg}`; environments `\begin{x} … \end{x}` must match.
- `\section`, `\subsection` (numbered automatically), `\textbf`, `\emph`, `~`, `--`; escape `# $ % & _ { }`.
- Compile with `latexmk -pdf` (several passes); read errors from the first `!` line and `l.<line>`.
