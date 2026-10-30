---
tags: [programming, r, quarto, type/solution]
---
# R10 R Markdown and Quarto – Solutions

> Worksheet: [[R10 R Markdown and Quarto - Worksheet]] · Theory: [[R10 R Markdown and Quarto]] · Wrong? → [[Mistakes - R]]

## Level 1
1. YAML header (metadata, formats, options), Markdown text, code chunks (plus inline code).
2. `echo: false`: run the code and show the output, but hide the code. `eval: false`: show the code but don't run it. `include: false`: run it, show neither code nor output.
3. Evaluates the expression when rendering and inserts the result (e.g. `0.487`) into the text.
4. PDF (via LaTeX; also Beamer slides).

## Level 2
5. Rendering uses a **fresh session**; `erp` exists only in your interactive environment (created by code that isn't in the document, or a chunk executed out of order). Put the code that creates/loads `erp` into a chunk before it.
6. The cache is keyed on the chunk's code, not on the file's content; the code didn't change, so the cached result is reused. Fix: delete the cache, add the file as a dependency (`cache.extra = tools::md5sum("data.csv")` in knitr / `#| cache.extra: !expr tools::md5sum("data.csv")`), or don't cache file-reading chunks.
7. A chunk with `#| label: fig-erp` **and** a `fig-cap` (Quarto needs both the `fig-` prefix and a caption for a figure cross-reference).
8. Use a Unicode-capable engine (`pdf-engine: xelatex` or `lualatex` in the YAML; plain `pdflatex` is the one that fails), or write the symbol in math mode (`$\alpha$`) instead of typing the character. (Modern pdfLaTeX handles common characters like µ and ä, but not Greek letters typed as text.)

## Level 3
9. ```yaml
   ---
   title: "P300 pilot"
   format:
     html:
       toc: true
       code-fold: true
     pdf: default
   bibliography: refs.bib
   ---
   ```
10. ````markdown
    ```{r}
    #| label: fig-rt
    #| fig-cap: "Mean RT per condition."
    #| echo: false
    ggplot(subj_means, aes(condition, rt)) + geom_point()
    ```
    ````
11. ``The effect was significant, t(`r tt$parameter`) = `r round(tt$statistic, 2)`, p = `r sub("^0", "", format(round(tt$p.value, 3), nsmall = 3))`.`` (The `sub` removes the leading zero for APA style; packages like `papaja` or `report` format this automatically.)

## Level 4
12. Declare a parameter in the YAML (`params: subject: "sub-01"`) and use `params$subject` in the chunks to load that subject's files; then loop in a shell/R script: `for (s in subjects) quarto::quarto_render("qc.qmd", execute_params = list(subject = s), output_file = paste0("qc_", s, ".html"))`.
13. Every render would rerun the hour-long step; the report would be slow and fragile. Keep preprocessing in scripts that write derived files (e.g. cleaned epochs, summary CSVs); the report only reads these files and computes statistics/figures. Record which script version created them.
14. ````markdown
    ---
    title: "Test"
    format: html
    ---

    The mean is `r round(mean(mtcars$mpg), 1)` mpg.

    $$ V(t) = V_\infty + (V_0 - V_\infty)e^{-t/\tau} $$ {#eq-v}

    See @eq-v and @fig-mpg.

    ```{r}
    #| label: fig-mpg
    #| fig-cap: "Weight vs. mpg."
    library(ggplot2)
    ggplot(mtcars, aes(wt, mpg)) + geom_point()
    ```
    ````
    `quarto render test.qmd` (add `--to pdf` for PDF).
