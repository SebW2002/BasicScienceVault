---
aliases: [LaTeX Workshop, VS Code LaTeX, SyncTeX, latexmkrc, Pandoc]
tags: [programming, latex, vscode, pandoc, type/overview, neuro]
---
# Doc09 LaTeX with VS Code

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc09 LaTeX with VS Code - Worksheet|✏️ Worksheet]] · [[Doc09 LaTeX with VS Code - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
VS Code is a free editor that handles Python, R, MATLAB files, Markdown **and** LaTeX in one place, with git built in. With the **LaTeX Workshop** extension it compiles on save, shows the PDF next to the source, jumps between source and PDF (SyncTeX) and lists errors in the Problems panel. **Pandoc** connects your Markdown notes to LaTeX and PDF.

## LaTeX Workshop: compile, preview, SyncTeX
**Install:** a TeX distribution ([[Doc07 LaTeX Documents and TeX Live]]) + VS Code extension *LaTeX Workshop* (James Yu). Open the **folder** of your project (not just one file).
| Action | Shortcut (Windows/Linux; macOS: Cmd/Option) | Notes |
|---|---|---|
| build (compile) | Ctrl + Alt + B | default recipe: `latexmk` |
| view PDF | Ctrl + Alt + V | in a VS Code tab (or external viewer) |
| SyncTeX forward (source → PDF) | Ctrl + Alt + J | jumps to the current line in the PDF |
| SyncTeX backward (PDF → source) | Ctrl + click in the PDF | jumps to the source line |
| clean auxiliary files | command palette: "LaTeX Workshop: Clean up auxiliary files" | `.aux`, `.log`, `.fls`, … |
- By default, LaTeX Workshop **builds on save** and refreshes the PDF tab automatically.
- **SyncTeX** needs the `-synctex=1` flag (included in the default latexmk tool) and creates a `.synctex.gz` file.
- The TeX sidebar (TeX icon) shows the document outline, snippets for environments, and build commands.
- For multi-file documents (`\input{chapters/intro}`), put `% !TEX root = ../thesis.tex` in the first line of sub-files so building from any file compiles the main document.
- IntelliSense completes commands, `\ref`/`\cite` keys (from labels and `.bib` files) and file names in `\includegraphics`.

## Configuring the build tool (latexmk) in settings.json
LaTeX Workshop builds with **recipes** (a sequence of **tools**). The default uses latexmk with pdflatex. To change it, edit the workspace `settings.json` (*Ctrl + Shift + P → Preferences: Open Workspace Settings (JSON)*):
```json
{
  "latex-workshop.latex.tools": [
    {
      "name": "latexmk-lualatex",
      "command": "latexmk",
      "args": ["-synctex=1", "-interaction=nonstopmode", "-file-line-error",
               "-lualatex", "-outdir=%OUTDIR%", "%DOC%"]
    }
  ],
  "latex-workshop.latex.recipes": [
    { "name": "latexmk (lualatex)", "tools": ["latexmk-lualatex"] }
  ],
  "latex-workshop.latex.outDir": "%DIR%/build",
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.view.pdf.viewer": "tab"
}
```
- `%DOC%` = root file without extension, `%OUTDIR%` = output directory (here `build/`, keeping the project folder clean – add `build/` to `.gitignore`).
- `-interaction=nonstopmode` stops LaTeX from waiting for input on errors; `-file-line-error` prints errors as `file:line: message`, which VS Code turns into clickable problems.
- Alternatively configure latexmk itself with a `.latexmkrc` in the project (`$pdf_mode = 4;` for lualatex, `$out_dir = 'build';`) – then the same build works in the terminal, in VS Code and on a CI server.
- Workspace settings (`.vscode/settings.json`) travel with the project; user settings apply to all projects.

## Finding errors: Problems panel and log
- **Problems panel** (Ctrl + Shift + M): errors and warnings with file and line; click to jump. Fix the **first error** first.
- **Output panel → "LaTeX Compiler"**: the raw compiler output; the full `.log` file is in the output folder ([[Doc05 LaTeX Basics]] for reading messages).
- **Typical workflow when the build fails:** look at the first error → go to the line → check the last change (git diff helps) → if unclear, comment out blocks until it compiles.
- Status bar: a ✓ or ✗ shows whether the last build succeeded; "Kill LaTeX compiler process" if a build hangs.
- Linting extensions (ChkTeX, LTeX for grammar/spelling) catch style issues before they become errors.

## Markdown and LaTeX together: Pandoc
**Pandoc** converts between document formats – Markdown, LaTeX, HTML, Word, PDF (via LaTeX):
```bash
pandoc notes.md -o notes.pdf                                   # Markdown → PDF (via LaTeX)
pandoc notes.md -s -o notes.tex                                # → standalone LaTeX source to edit further
pandoc notes.md -o notes.docx                                  # → Word for co-authors
pandoc notes.md --citeproc --bibliography refs.bib --csl apa.csl -o notes.pdf   # with citations
pandoc notes.md --pdf-engine=xelatex -V geometry:margin=2.5cm -V mainfont="TeX Gyre Pagella" -o notes.pdf
pandoc paper.tex -o paper.docx                                 # LaTeX → Word (approximate)
```
- Markdown math (`$…$`, `$$…$$`) becomes real LaTeX math – your Obsidian formulas compile unchanged ([[Doc02 Math in Markdown]]).
- Citations `[@polich2007]` with a `.bib` file and a CSL style ([[Doc07 LaTeX Documents and TeX Live]]).
- Obsidian-specific syntax (wikilinks, callouts, embeds) isn't understood by Pandoc – convert first (Obsidian plugins such as *Pandoc Plugin* / *Enhancing Export*, or write portable Markdown).
- Quarto is built on Pandoc and adds code execution and cross-references ([[R10 R Markdown and Quarto]]).
- VS Code: the *Markdown All in One* and *Markdown Preview Enhanced* extensions preview Markdown with math; *vscode-pandoc* adds export commands.

## In neuroscience #neuro
- **One editor for everything:** analysis code (Python/R/MATLAB), the thesis in LaTeX, Markdown notes and git – fewer context switches.
- **Writing a paper from notes:** draft methods in Markdown (Obsidian), convert with Pandoc to LaTeX, polish in VS Code with the journal template.
- **Collaborative writing:** Overleaf for co-authors who don't want a local setup; VS Code + git (Overleaf can sync with git/GitHub) for you.
- **Continuous integration:** a GitHub Action compiles the thesis with latexmk on every push and stores the PDF – the same `.latexmkrc` as locally.

## Connections
- Compiling and errors → [[Doc05 LaTeX Basics]]; TeX distributions and bibliography → [[Doc07 LaTeX Documents and TeX Live]]
- Markdown → [[Doc01 Markdown Syntax]], [[Doc02 Math in Markdown]]
- Choosing formats → [[Doc10 When to Use What]]
- VS Code for code → [[Py00 Python Overview]], [[R01 R Basics and Syntax]]

## Key takeaways
- LaTeX Workshop: Ctrl+Alt+B build, Ctrl+Alt+V view, Ctrl+Alt+J / Ctrl+click SyncTeX; build on save.
- Configure recipes/tools in `.vscode/settings.json` (latexmk with `-synctex=1 -interaction=nonstopmode -file-line-error`), or in `.latexmkrc`.
- Problems panel + compiler log; fix the first error first; `% !TEX root` for multi-file projects.
- Pandoc turns Markdown (with math and citations) into LaTeX, PDF, HTML or Word.
