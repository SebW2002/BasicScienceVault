---
aliases: [Mistake Log Markdown HTML LaTeX, Fehler LaTeX, Fehler Markdown, LaTeX Errors Log]
tags: [programming, markdown, html, latex, type/mistakes]
---
# ⚠️ Mistakes – Markdown, HTML & LaTeX

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · Template: [[Mistake Entry Template]]

**How to use:** whenever something renders wrongly or a document fails to compile, add a row with the error message and what fixed it – LaTeX errors repeat.

## Classic traps (pre-filled)
| ❌ Wrong | ✅ Right | Quick check / why | Topic |
|---|---|---|---|
| `#Heading` without space | `# Heading` | becomes text / a tag | [[Doc01 Markdown Syntax]] |
| no blank line before lists/tables/headings | blank lines around blocks | renders as one paragraph | [[Doc01 Markdown Syntax]] |
| a literal pipe character in a table cell | escape it as `\|`; in math use `\lvert…\rvert` | table breaks | [[Doc01 Markdown Syntax]] |
| wikilinks expected to work on GitHub/Pandoc | standard `[text](file.md)` links for export | shown as plain text | [[Doc01 Markdown Syntax]] |
| `x^10`, `e^-t/\tau` | `x^{10}`, `e^{-t/\tau}` | only the first token is raised | [[Doc02 Math in Markdown]] |
| `$ x $` with inner spaces | `$x$` | not recognised as math | [[Doc02 Math in Markdown]] |
| `$SNR$`, `$sin x$` | `$\text{SNR}$`, `$\sin x$` | italic letters = product | [[Doc02 Math in Markdown]] |
| `\label`/`\eqref` in Obsidian | `\tag{1}`; numbered refs in Quarto/LaTeX | not supported | [[Doc02 Math in Markdown]] |
| wrongly nested tags `<p><b>x</p></b>` | close in reverse order | broken layout | [[Doc03 HTML Basics]] |
| `<img>` without `alt` / absolute local `src` | `alt="…"`, relative path | inaccessible / broken image elsewhere | [[Doc03 HTML Basics]] |
| duplicate `id`s | unique IDs | links/CSS hit the wrong element | [[Doc03 HTML Basics]] |
| no `<meta charset="utf-8">` | add it | µ shows as "Âµ" | [[Doc03 HTML Basics]] |
| sending HTML report without its `_files` folder | `embed-resources: true` or send the folder | broken figures | [[Doc04 HTML for Reports and Figures]] |
| `%`, `&`, `_`, `#` unescaped in text | `\%`, `\&`, `\_`, `\#` | errors / text vanishes after `%` | [[Doc05 LaTeX Basics]] |
| math commands in text (`\tau`, `_`) | `$\tau$` | `Missing $ inserted` | [[Doc05 LaTeX Basics]] |
| unmatched `\begin`/`\end` | close every environment | `ended by \end{document}` | [[Doc05 LaTeX Basics]] |
| `"quotes"`, `1-40 Hz` | ``` ``quotes'' ```, `1--40~Hz` | wrong glyphs | [[Doc05 LaTeX Basics]] |
| fixing the last error first | fix the **first** `!` error | later errors are consequences | [[Doc05 LaTeX Basics]] |
| one compile pass, then worrying about `??` | `latexmk -pdf` | references need several passes | [[Doc05 LaTeX Basics]] |
| `$$…$$` in LaTeX documents | `\[…\]`, `equation` | plain-TeX spacing issues | [[Doc06 LaTeX Math]] |
| `align` without `&` | `a &= b \\` | misaligned | [[Doc06 LaTeX Math]] |
| `\label` before `\begin{equation}` / before `\caption` | inside, after the caption | wrong numbers | [[Doc06 LaTeX Math]] |
| `20 ms` inside math | `\qty{20}{\milli\second}` | italic "ms" = m·s | [[Doc06 LaTeX Math]] |
| `\ref` where "(1)" is wanted | `\eqref` / `\cref` | – | [[Doc06 LaTeX Math]] |
| `File 'x.sty' not found` ignored | `tlmgr search --global --file x.sty` → install | – | [[Doc07 LaTeX Documents and TeX Live]] |
| `T1` font encoding without `lmodern` | load `lmodern` (or another T1 font) | blurry bitmap fonts; microtype "auto expansion" error | [[Doc07 LaTeX Documents and TeX Live]] |
| citations as **[key]** | run biber/bibtex (or latexmk) | missing bibliography step | [[Doc07 LaTeX Documents and TeX Live]] |
| `.bst` style with biblatex | BibTeX for `.bst`, `style=` for biblatex | incompatible | [[Doc07 LaTeX Documents and TeX Live]] |
| capitals lost in titles ("p300") | protect with braces `{P300}` | style lowercases | [[Doc07 LaTeX Documents and TeX Live]] |
| `cleveref` loaded before `hyperref` | hyperref first, then cleveref | errors / wrong refs | [[Doc08 LaTeX Figures Tables and References]] |
| JPG for plots, figures scaled from huge sizes | vector PDF at final size | blurry, tiny fonts | [[Doc08 LaTeX Figures Tables and References]] |
| vertical lines and `\hline` everywhere | booktabs rules | cluttered tables | [[Doc08 LaTeX Figures Tables and References]] |
| `[H]` on every figure | `[tbp]`, let LaTeX float | big white gaps | [[Doc08 LaTeX Figures Tables and References]] |
| `\includegraphics{fig.svg}` | convert SVG → PDF (Inkscape) | unknown graphics extension | [[Doc08 LaTeX Figures Tables and References]] |
| building a sub-file of a multi-file project | `% !TEX root = ../main.tex` | "missing \begin{document}" | [[Doc09 LaTeX with VS Code]] |
| auxiliary files committed to git | `outDir` = `build/`, `.gitignore` | noisy diffs | [[Doc09 LaTeX with VS Code]] |
| Pandoc on Obsidian syntax | portable Markdown / export plugin | wikilinks and callouts lost | [[Doc09 LaTeX with VS Code]] |
| writing everything in LaTeX from day one | notes in Markdown, export when needed | slow note-taking | [[Doc10 When to Use What]] |

## My mistakes
| Date | ❌ What I did | ✅ Correct | Why / quick check | Link |
|---|---|---|---|---|
| | | | | |

## Patterns I notice
- 
