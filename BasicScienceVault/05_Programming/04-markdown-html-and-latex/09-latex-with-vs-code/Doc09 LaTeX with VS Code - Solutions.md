---
tags: [programming, latex, vscode, type/solution]
---
# Doc09 LaTeX with VS Code – Solutions

> Worksheet: [[Doc09 LaTeX with VS Code - Worksheet]] · Theory: [[Doc09 LaTeX with VS Code]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. A TeX distribution (TeX Live/MacTeX/MiKTeX, including latexmk and Perl for latexmk on Windows) and the LaTeX Workshop extension.
2. Build the document; open the PDF preview; SyncTeX forward search (jump from the cursor's source line to the PDF position).
3. A mechanism that maps positions in the PDF to source lines and back. It needs the `-synctex=1` flag, which produces a `.synctex.gz` file.
4. In the Problems panel (Ctrl + Shift + M) and in the Output panel ("LaTeX Compiler") / the `.log` file.

## Level 2
5. `%DOC%`: path of the root `.tex` file without extension; `%OUTDIR%`: the output directory; `-interaction=nonstopmode`: don't stop and wait for user input on errors; `-file-line-error`: print errors as `file:line: error`, so VS Code can link them.
6. Define a tool/recipe with `latexmk -lualatex …` (`latex-workshop.latex.tools` + `latex-workshop.latex.recipes`) and set `latex-workshop.latex.outDir` to `%DIR%/build`. `build/` contains generated files that change on every compile (and can be regenerated), so they shouldn't clutter the repository.
7. Put `% !TEX root = ../main.tex` (path to the main file) in the first line of `methods.tex`, so LaTeX Workshop always compiles the root document.
8. It's independent of the editor: the same build runs in the terminal, in other editors, for co-authors and in continuous integration (GitHub Actions); VS Code settings only apply in VS Code.

## Level 3
9. `pandoc methods.md --citeproc --bibliography refs.bib --csl apa.csl -o methods.pdf`
10. `pandoc methods.md -s -o methods.tex` – `-s` (standalone) adds a complete preamble and `\begin{document}…\end{document}`; without it you get a fragment to `\input` into your thesis (often what you want for a chapter).
11. Wikilinks `[[…]]`, embeds `![[…]]`, callouts `> [!note]`, highlights `==…==`, Obsidian comments and tags. Convert them (export plugins), replace with standard Markdown (normal links, blockquotes) in notes meant for export, or post-process.

## Level 4
12. Keep a portable Markdown draft of the methods (standard links, `$…$` math, `[@key]` citations from the shared Zotero `.bib`). Convert with `pandoc methods.md -o chapters/methods.tex --natbib` (or `--biblatex`, so citations become `\citep`/`\autocite` commands handled by your thesis' bibliography). `\input{chapters/methods}` in the thesis, polish in VS Code, compile with latexmk.
13. Steps: open the folder in VS Code; `main.tex` with `\input{chapters/intro}`; `% !TEX root = ../main.tex` in `intro.tex`; workspace setting `"latex-workshop.latex.outDir": "%DIR%/build"`; Ctrl + Alt + B; Ctrl + Alt + V; Ctrl + Alt + J on a line → highlighted position in the PDF; Ctrl + click in the PDF → cursor in the source.
