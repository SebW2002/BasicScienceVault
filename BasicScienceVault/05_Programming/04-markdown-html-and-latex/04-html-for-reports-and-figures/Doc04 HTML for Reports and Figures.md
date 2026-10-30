---
aliases: [HTML Reports, figure and figcaption, details and summary, Self-contained HTML]
tags: [programming, html, reports, reproducibility, type/overview, neuro]
---
# Doc04 HTML for Reports and Figures

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc04 HTML for Reports and Figures - Worksheet|✏️ Worksheet]] · [[Doc04 HTML for Reports and Figures - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
HTML is the natural format for **analysis reports**: it shows figures, tables, code and text together, can fold away details, include interactive plots, and opens in every browser. Quarto, R Markdown, Jupyter, MATLAB `publish` and neuro tools (MNE `Report`, fMRIPrep, MRIQC) all produce HTML. Understanding a few semantic elements lets you write, read and fix these reports. Basics → [[Doc03 HTML Basics]].

## Figures with figure and figcaption
```html
<figure id="fig-erp">
  <img src="figures/erp_pz.svg" alt="Grand-average ERP at Pz for oddball and standard trials" width="600">
  <figcaption><strong>Figure 1.</strong> Grand-average ERP at Pz (n = 24). Shading: ±1 SEM across subjects.</figcaption>
</figure>
<p>The P300 was larger for oddballs (<a href="#fig-erp">Figure 1</a>).</p>
```
- `<figure>` groups an image (or plot, table, code listing) with its caption; `<figcaption>` is the caption – semantic, so screen readers and converters know they belong together.
- Give figures an `id` so text can link to them.
- **Image formats:** SVG (vector, sharp at any zoom, small for line plots), PNG (raster, lossless; for images/heat maps), avoid JPEG for plots (compression artefacts) ([[Py07 Python Plotting and Visualization]], [[R06 ggplot2 Visualization]]).
- `alt` describes the content for people who can't see the image; the caption explains it for everyone.

## Interactive elements: details and summary
```html
<details>
  <summary>Preprocessing parameters (click to expand)</summary>
  <ul>
    <li>Band-pass 0.1–30 Hz, zero-phase FIR</li>
    <li>ICA (extended Infomax), components removed with ICLabel ≥ 0.9</li>
  </ul>
</details>
<details open>
  <summary>Excluded participants</summary>
  <p>sub-03 (excessive movement), sub-17 (technical failure)</p>
</details>
```
- A collapsible section **without JavaScript**: `<summary>` is always visible, the rest appears on click; `open` makes it expanded by default.
- Ideal for long tables, full model output, code, per-subject QC – the report stays readable.
- Works inside Markdown in Obsidian, GitHub and Quarto too. Quarto alternatives: `code-fold: true` (fold code chunks), callouts with `collapse="true"`, tabsets (`::: {.panel-tabset}`).

## Understanding HTML output of R Markdown, Quarto and MATLAB
What a rendered report contains:
| Part | Typical HTML | Where it comes from |
|---|---|---|
| title, author, date | `<header>`, `<h1 class="title">` | YAML header |
| table of contents | `<nav id="TOC">` with links to heading IDs | `toc: true` |
| headings | `<h2 id="results">` (IDs generated from the text) | `## Results` |
| code chunk | `<div class="cell"><pre class="sourceCode r"><code>…` | ```` ```{r} ```` |
| output | `<pre>` (text), `<img>` / `<figure>` (plots), `<table>` | chunk results |
| math | `<span class="math inline">\(...\)</span>` rendered by MathJax/KaTeX | `$...$` |
| styling | `<link>`/`<style>` with Bootstrap/theme CSS | `theme:`, `css:` |
| scripts | `<script>` (MathJax, interactive widgets, code folding) | format options |
- **Self-contained vs. linked:** Quarto `embed-resources: true` (R Markdown `self_contained: true`) embeds images (base64), CSS and JavaScript into **one** HTML file – easy to e-mail, but larger. Otherwise the HTML links to a `report_files/` folder that must travel with it.
- **MATLAB `publish`** writes `html/report.html` plus PNGs of each figure in the same folder ([[MAT11 MATLAB Live Scripts and Reports]]).
- **Jupyter:** `jupyter nbconvert --to html notebook.ipynb` (or Quarto: `quarto render notebook.ipynb`).
- **Inspect** a report in the browser with *right-click → Inspect* (developer tools) to see which element/CSS rule produces what you see – the fastest way to find the selector to restyle it.
- Customising: a small CSS file (`css: custom.css` in Quarto) for fonts, figure widths, callout colours.

## In neuroscience #neuro
- **MNE `Report`**: `report = mne.Report(title="sub-01"); report.add_raw(raw, title="Raw"); report.add_epochs(epochs, title="Epochs"); report.save("sub-01_report.html")` – a browsable QC page per subject ([[Py10 Python Neuroscience Packages]]).
- **fMRIPrep / MRIQC** HTML reports with interactive registration overlays (SVG animations) – the standard for visual QC.
- **Supplementary material** as one self-contained HTML (all statistics with folded code) shared on OSF.
- **Interactive figures:** Plotly/Bokeh in Python, `plotly`/`htmlwidgets` in R, Nilearn's `view_img` (3-D brain viewer) embedded in reports.

## Math links #math-link
- Formulas in HTML reports via MathJax/KaTeX → [[Doc02 Math in Markdown]]

## Connections
- HTML basics → [[Doc03 HTML Basics]]
- Report tools → [[R10 R Markdown and Quarto]], [[MAT11 MATLAB Live Scripts and Reports]], [[Py10 Python Neuroscience Packages]]
- Figures → [[Py07 Python Plotting and Visualization]], [[R06 ggplot2 Visualization]], [[MAT05 MATLAB Plotting]]
- HTML vs. PDF/LaTeX → [[Doc10 When to Use What]]

## Key takeaways
- `<figure>` + `<img alt>` + `<figcaption>` for captioned figures; IDs for linking.
- `<details>`/`<summary>` fold long content without JavaScript.
- Rendered reports = headings with IDs, code in `<pre><code>`, figures as `<img>`, math via MathJax, theme CSS.
- Self-contained (one big file) vs. linked resources (folder must travel); inspect with browser dev tools.
