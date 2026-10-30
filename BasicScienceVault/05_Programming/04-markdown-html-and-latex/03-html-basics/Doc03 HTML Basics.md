---
aliases: [HTML Basics, HTML Tags, HTML Attributes, CSS Basics]
tags: [programming, html, css, documentation, type/overview, neuro]
---
# Doc03 HTML Basics

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc03 HTML Basics - Worksheet|✏️ Worksheet]] · [[Doc03 HTML Basics - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
HTML is the language of web pages – and of the **reports** produced by Quarto, R Markdown, Jupyter, MATLAB `publish`, MNE's `Report` and fMRIPrep's QC pages. You don't need to become a web developer, but reading HTML lets you understand, fix and customise these outputs, and Markdown itself is converted to HTML for display ([[Doc04 HTML for Reports and Figures]]).

## Basic structure
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>P300 pilot report</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>P300 pilot</h1>
    <p>Grand-average ERP of <strong>12</strong> participants.</p>
  </body>
</html>
```
| Part | Role |
|---|---|
| `<!DOCTYPE html>` | declares modern HTML (HTML5) |
| `<html lang="en">` | root element; language for screen readers/hyphenation |
| `<head>` | metadata: character set, title (browser tab), CSS and scripts – not shown on the page |
| `<body>` | the visible content |
- An **element** = opening tag, content, closing tag: `<p>text</p>`. Some elements are **empty** (no content, no closing tag): `<img>`, `<br>`, `<meta>`, `<link>`.
- Elements **nest** like boxes: close them in reverse order (`<p><strong>x</strong></p>`, not `<p><strong>x</p></strong>`).
- Whitespace and line breaks in the source are collapsed into single spaces – layout comes from elements and CSS.
- `<meta charset="utf-8">` makes µ, ä, α display correctly.
- Comments: `<!-- not shown -->`.

## Important tags
| Tag | Meaning | Markdown equivalent |
|---|---|---|
| `<h1>` … `<h6>` | headings, levels 1–6 | `#` … `######` |
| `<p>` | paragraph | blank-line-separated text |
| `<a href="https://mne.tools">MNE</a>` | link (anchor) | `[MNE](https://mne.tools)` |
| `<img src="erp.png" alt="Grand-average ERP" width="400">` | image | `![Grand-average ERP](erp.png)` |
| `<strong>`, `<em>`, `<code>` | strong importance (bold), emphasis (italic), code | `**`, `*`, backticks |
| `<ul><li>…</li></ul>`, `<ol>` | unordered/ordered list | `-`, `1.` |
| `<table>`, `<tr>`, `<th>`, `<td>` | table, row, header cell, data cell | pipe tables |
| `<div>` | generic **block** container (own line) | – |
| `<span>` | generic **inline** container (inside text) | – |
| `<br>` | line break | two trailing spaces / `\` |
| `<pre><code>` | preformatted code block | fenced code |
```html
<table>
  <thead>
    <tr><th>Band</th><th>Range (Hz)</th></tr>
  </thead>
  <tbody>
    <tr><td>alpha</td><td>8–12</td></tr>
    <tr><td>gamma</td><td>30–100</td></tr>
  </tbody>
</table>
```
`colspan="2"` / `rowspan="2"` on a cell merges cells – something Markdown tables can't do.
- `alt` text on images is required for accessibility (screen readers) and shown if the image fails to load.
- **Relative paths** (`figures/erp.png`) keep a report folder portable; absolute local paths (`C:/…`) break when shared.

## Attributes, classes and IDs
Attributes add information to an element, written inside the opening tag as `name="value"`:
```html
<a href="#results" title="Jump to results">Results</a>
<h2 id="results">Results</h2>                  <!-- id: unique on the page; link target -->
<p class="note warning">Two subjects excluded.</p>   <!-- class: reusable label(s), for styling -->
<span class="sig">p = .003</span>
<img src="topo.png" alt="Topography at 350 ms" width="300">
```
- **`id`** must be unique; used for links (`#results`), CSS (`#results { }`) and JavaScript.
- **`class`** can be shared by many elements and an element can have several classes (space-separated); used for styling groups of elements.
- Other common attributes: `href`, `src`, `alt`, `width`/`height`, `title` (tooltip), `style` (inline CSS – avoid for anything big), `lang`, `data-*` (custom data).
- Quarto/Pandoc let you add classes and IDs from Markdown: `## Results {#results}`, `[p = .003]{.sig}`, `::: {.callout-note} … :::`.

## CSS: the basic idea (no deep dive)
**CSS** (Cascading Style Sheets) describes how elements **look**; HTML describes what they **are**.
```css
/* style.css */
body   { font-family: "Helvetica", sans-serif; max-width: 50em; margin: auto; }
h1, h2 { color: #2c3e50; }
.note  { background: #f4f6f7; border-left: 4px solid #3498db; padding: 0.5em 1em; }
.warning { border-left-color: #e67e22; }
#results { margin-top: 2em; }
table  { border-collapse: collapse; }
td, th { border-bottom: 1px solid #ccc; padding: 0.2em 0.6em; }
```
- A **rule** = selector + declarations: `selector { property: value; }`.
- Selectors: element (`p`), class (`.note`), ID (`#results`), descendant (`table td`), several (`h1, h2`).
- "Cascading": several rules can apply; more specific selectors (ID > class > element) and later rules win.
- Include CSS with `<link rel="stylesheet" href="style.css">` in `<head>` (or `<style>…</style>`); Quarto: `format: html: css: style.css`.
- Keep content (HTML) and design (CSS) separate: changing one file restyles the whole report.

## Same idea in Markdown and LaTeX
Markdown is a shorthand that converts to HTML (`# Title` → `<h1>Title</h1>`); raw HTML can be written inside most Markdown files (Obsidian, GitHub, Quarto). LaTeX separates structure and style similarly: `\section{}` (structure) and the document class/packages (style) ([[Doc05 LaTeX Basics]]).

## In neuroscience #neuro
- **QC reports** of fMRIPrep, MRIQC and MNE's `mne.Report` are HTML pages – knowing their structure helps when you need to extract or customise something.
- **Lab websites and project pages** (GitHub Pages) for sharing datasets and tools.
- **Online experiments** (PsychoJS/Pavlovia, jsPsych) run as HTML + JavaScript in the browser ([[Py11 PsychoPy Experiment Control]]).
- **Interactive figures** (Plotly, Bokeh, Nilearn's `view_img`) are embedded in HTML.

## Math links #math-link
- Formulas in HTML are rendered by MathJax/KaTeX from LaTeX syntax → [[Doc02 Math in Markdown]]

## Connections
- Markdown → HTML → [[Doc01 Markdown Syntax]]
- Reports and figures in HTML → [[Doc04 HTML for Reports and Figures]]
- When to use HTML → [[Doc10 When to Use What]]

## Key takeaways
- Skeleton: `<!DOCTYPE html>`, `<html>`, `<head>` (meta, title, CSS), `<body>` (content).
- Core tags: `h1–h6`, `p`, `a`, `img` (with `alt`), `table/tr/th/td`, `div` (block), `span` (inline).
- `id` = unique anchor, `class` = reusable label; both used by CSS.
- CSS rules `selector { property: value; }` style the content; keep style separate from structure.
