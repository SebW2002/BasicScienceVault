---
tags: [programming, latex, type/solution]
---
# Doc05 LaTeX Basics – Solutions

> Worksheet: [[Doc05 LaTeX Basics - Worksheet]] · Theory: [[Doc05 LaTeX Basics]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. `\documentclass{…}` (type of document); the **preamble** (packages, settings, macros, title data – no output); the **document body** between `\begin{document}` and `\end{document}` (the content).
2. A command is a single instruction (`\section{Methods}`, `\textbf{x}`); an environment applies to a region and has begin/end (`\begin{itemize} … \end{itemize}`).
3. `# $ % & _ { } ~ ^ \`. `Accuracy was 85\% ($n = 20$) \& stable` (or `\(n = 20\)`).
4. LaTeX writes labels and section numbers into the `.aux` file during the first run and reads them in the next; references are resolved only in the second pass. `latexmk` reruns automatically.

## Level 2
5. `\tau` is a math command used in text mode; LaTeX inserts `$` and complains. Fix: `The decay constant was $\tau = 20$~ms.` (or `\SI{20}{\milli\second}`).
6. An `itemize` environment was opened in line 23 and never closed. Add `\end{itemize}` at the right place.
7. `\SI` is defined by the `siunitx` package, which isn't loaded. Add `\usepackage{siunitx}` to the preamble (in newer versions also `\qty`).
8. `"` gives straight/wrong quote marks; `-` is a hyphen (too short for ranges). Use ``` ``stable'' ``` (or `\enquote{stable}` with `csquotes`) and `1--40~Hz`.

## Level 3
9. ```latex
   \documentclass{article}
   \title{Pilot report}
   \author{Your Name}
   \date{\today}
   \begin{document}
   \maketitle
   \section{Methods}
   \subsection{Participants}
   Twelve adults took part.
   \section*{Acknowledgements}
   We thank the participants.
   \end{document}
   ```
10. ```latex
    \begin{itemize}
      \item band-pass filter 0.1--30~Hz
      \item average reference
      \item ICA artefact removal
    \end{itemize}
    \begin{enumerate}
      \item The P300 is larger for oddballs.
      \item P300 latency correlates with reaction time.
    \end{enumerate}
    ```
11. ```latex
    \newcommand{\ms}{\textrm{ms}}
    \newcommand{\erp}[1]{\textbf{#1} ERP}
    % usage: 20~\ms, \erp{P300}
    ```
    (In math mode use `\mathrm{ms}`; for units in general prefer `siunitx`.)

## Level 4
12. The default `pdflatex` engine can't handle the Unicode character α typed directly in the text. Fixes: write it as math (`$\alpha$`), or switch to a Unicode engine (`pdf-engine: xelatex` / `lualatex` in Quarto's YAML) with a font that contains the glyph.
13. After a successful compile, introduce `\tau` in text, remove an `\end{itemize}`, and drop `\usepackage{siunitx}`: read the first `!` line and the `l.<n>` line number in the log each time.
