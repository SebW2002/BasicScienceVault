---
tags: [programming, latex, type/worksheet]
---
# Doc05 LaTeX Basics – Worksheet

> Theory: [[Doc05 LaTeX Basics]] · Solutions: [[Doc05 LaTeX Basics - Solutions]] · Log mistakes in [[Mistakes - Markdown HTML LaTeX]]
> Write on paper or in a text editor; compile only for tasks marked 💻.

## Level 1 – Recall
1. Name the three parts of a LaTeX file and what goes into each.
2. What is the difference between a command and an environment? Give one example of each.
3. Which characters must be escaped in text? Write "Accuracy was 85% (n = 20) & stable" correctly.
4. Why does a fresh document show `??` instead of section numbers in references after one `pdflatex` run?

## Level 2 – Read the error
5. ```text
   ! Missing $ inserted.
   l.17 The decay constant was \tau
                                     = 20 ms.
   ```
   What's wrong? Fix.
6. ```text
   ! LaTeX Error: \begin{itemize} on input line 23 ended by \end{document}.
   ```
7. ```text
   ! Undefined control sequence.
   l.8 \SI
          {5}{\milli\volt}
   ```
8. A file uses `"stable"` for quotes and `1-40 Hz` for a range. Why does it look wrong in the PDF? Fix.

## Level 3 – Write LaTeX
9. Write a minimal `article` with title "Pilot report", your name, today's date, and the sections "Methods" (with a subsection "Participants") and an unnumbered "Acknowledgements".
10. Write an itemized list of three preprocessing steps and an enumerated list of two hypotheses.
11. Define a macro `\ms` that prints "ms" upright, and a macro `\erp{…}` that prints its argument in bold followed by " ERP".

## Level 4 – Neuro transfer
12. A Quarto report fails to render to PDF with `! LaTeX Error: Unicode character α (U+03B1) not set up for use with LaTeX.` Explain and give two fixes.
13. 💻 Compile your document from task 9 with `latexmk -pdf`, then introduce one error of each type from tasks 5–7 and read the log.
