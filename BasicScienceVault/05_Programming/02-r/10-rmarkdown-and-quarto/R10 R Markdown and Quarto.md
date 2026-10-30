---
aliases: [R Markdown, Quarto, Code Chunks, Reproducible Reports, knitr]
tags: [programming, r, quarto, rmarkdown, reproducibility, markdown, type/overview, neuro]
---
# R10 R Markdown and Quarto

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R10 R Markdown and Quarto - Worksheet|✏️ Worksheet]] · [[R10 R Markdown and Quarto - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
Copying numbers from the R console into Word is where errors creep in – and every re-analysis means copying again. **R Markdown** and its successor **Quarto** combine text, code and results in one source file: render it, and every number, table and figure is recomputed from the data. This is "literate programming" for lab reports, supplementary material, theses and even papers.

## R Markdown vs. Quarto
| | R Markdown (`.Rmd`) | Quarto (`.qmd`) |
|---|---|---|
| engine | R package (`rmarkdown` + `knitr`) | stand-alone program (by Posit), uses knitr for R and Jupyter for Python/Julia |
| languages | mainly R | R, Python, Julia, Observable JS – also plain `.ipynb` notebooks |
| render | `rmarkdown::render("report.Rmd")` / Knit button | `quarto render report.qmd` / Render button |
| status | stable, widely used | the recommended choice for new projects |
Both use **Pandoc** to convert Markdown to HTML, PDF (via LaTeX), Word and slides ([[Doc10 When to Use What]]).

## Anatomy of a document
````markdown
---
title: "Oddball ERP – pilot analysis"
author: "Anna"
date: today
format:
  html:
    toc: true
    code-fold: true
  pdf: default
execute:
  echo: true
  warning: false
bibliography: refs.bib
---

## Methods
We recorded `r n_subjects` participants. Data were filtered 0.1–30 Hz.

```{r}
#| label: fig-erp
#| fig-cap: "Grand-average ERP at Pz."
#| fig-width: 6
#| fig-height: 3
library(ggplot2)
ggplot(erp, aes(time, amp, colour = condition)) + geom_line()
```

The P300 was larger for oddballs (@fig-erp), $t(`r tt$parameter`) = `r round(tt$statistic, 2)`$, as in @polich2007.
````
1. **YAML header** (between `---`): title, output formats, options, bibliography.
2. **Markdown text** ([[Doc01 Markdown Syntax]]).
3. **Code chunks** ```` ```{r} ```` … ```` ``` ```` – executed in order, in one fresh R session.
4. **Inline code** `` `r expression` `` – inserts computed values into sentences.

## Code chunks and options
| Option (Quarto `#\|` style) | R Markdown style | Effect |
|---|---|---|
| `#\| echo: false` | `{r, echo=FALSE}` | hide code, show results |
| `#\| eval: false` | `eval=FALSE` | show code, don't run it |
| `#\| include: false` | `include=FALSE` | run, show nothing (setup chunks) |
| `#\| warning: false` / `message: false` | same | suppress warnings/messages |
| `#\| cache: true` | `cache=TRUE` | reuse results of slow chunks (careful: invalidation) |
| `#\| label: fig-erp` | `{r fig-erp}` | name; `fig-` prefix enables cross-references |
| `#\| fig-cap:` | `fig.cap=` | caption |
| `#\| fig-width: 6` | `fig.width=6` | size in inches |
- A typical first chunk loads packages and data (`include: false`), sets `set.seed()` and `theme_set()`.
- Rendering runs in a **clean session** – objects from your interactive console don't exist. That's the point: if it renders, it's reproducible.
- Heavy computation (preprocessing for an hour) belongs in scripts that write results to files; the report reads those files.
- Python chunks: ```` ```{python} ```` (Quarto with Jupyter, or R Markdown with reticulate).

## Output formats: HTML and PDF
| Format | Needs | Good for |
|---|---|---|
| `html` | nothing extra | lab reports, supplementary material, interactive plots, code folding; self-contained with `embed-resources: true` |
| `pdf` | a LaTeX installation (`quarto install tinytex` or TeX Live, [[Doc07 LaTeX Documents and TeX Live]]) | theses, submissions, printing |
| `docx` | – (optional reference doc for styles) | co-authors who edit in Word |
| `revealjs` / `beamer` | – / LaTeX | slides |
| `manuscript`, journal templates | Quarto extensions | papers |
Several formats from one source: `quarto render report.qmd --to all`. How the HTML output is structured → [[Doc04 HTML for Reports and Figures]].

## Formulas, tables, references
- **Formulas:** LaTeX math in `$...$` (inline) and `$$...$$` (display) – the same as in Obsidian ([[Doc02 Math in Markdown]], [[Doc06 LaTeX Math]]). Numbered equations in Quarto: `$$ V(t) = V_\infty + (V_0 - V_\infty)e^{-t/\tau} $$ {#eq-membrane}`, referenced with `@eq-membrane`.
- **Tables:** Markdown pipe tables for static content; for data frames `knitr::kable(df, digits = 2)`, or packages `gt`, `flextable`, `modelsummary` (regression tables), `tinytable`. Caption + label `#| label: tbl-demo` → `@tbl-demo`.
- **Citations:** a BibTeX file (`bibliography: refs.bib`), cite with `[@polich2007]` or `@polich2007`; a CSL file sets the citation style (APA, Nature, …) – same `.bib` as LaTeX ([[Doc07 LaTeX Documents and TeX Live]]).
- **Cross-references** (Quarto): `@fig-…`, `@tbl-…`, `@eq-…`, `@sec-…`.

## Same idea in Python and MATLAB
Jupyter notebooks (Python) – also renderable by Quarto ([[Py01 Python Basics and Syntax]]); MATLAB Live Scripts and `publish` ([[MAT11 MATLAB Live Scripts and Reports]]).

## In neuroscience #neuro
- **Analysis reports per subject** generated in a loop with parameters: `quarto render qc.qmd -P subject:sub-07` → one QC report per participant (artefacts, trial counts, bad channels).
- **Supplementary material** with all statistics computed inline – no transcription errors between output and text.
- **Preregistration and registered reports:** the analysis document can be written and run on simulated data before data collection ([[CS13 Reproducibility and Research Software]]).
- **Theses:** Quarto books (`project: type: book`) with chapters, cross-references and a bibliography, rendered to PDF via LaTeX.

## Math links #math-link
- LaTeX formulas in reports → [[Doc02 Math in Markdown]], [[Doc06 LaTeX Math]]

## Connections
- Markdown and math → [[Doc01 Markdown Syntax]], [[Doc02 Math in Markdown]]
- HTML and PDF outputs → [[Doc04 HTML for Reports and Figures]], [[Doc05 LaTeX Basics]]
- Figures → [[R06 ggplot2 Visualization]]; models and tables → [[R07 R Statistical Modelling]]
- Reproducible projects → [[R11 R Reproducible Projects]], [[CS13 Reproducibility and Research Software]]

## Key takeaways
- One source = text + code + results; render in a clean session.
- YAML header → formats and options; chunks `{r}` with `#|` options; inline `` `r x` ``.
- HTML needs nothing extra, PDF needs LaTeX; one source can give several formats.
- LaTeX math, `kable`/`gt` tables, `@citations` and `@fig-` cross-references.
