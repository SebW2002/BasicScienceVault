---
tags: [programming, html, reports, type/solution]
---
# Doc04 HTML for Reports and Figures – Solutions

> Worksheet: [[Doc04 HTML for Reports and Figures - Worksheet]] · Theory: [[Doc04 HTML for Reports and Figures]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. They mark an image (or table/code) and its caption as one semantic unit – for accessibility, styling (e.g. centring both), cross-references and conversion tools. `<img>` + `<p>` are unrelated elements as far as the browser is concerned.
2. `open` shows the content expanded initially; without it, only the `<summary>` is visible until clicked.
3. Self-contained: images (base64), CSS and JavaScript are embedded in one file – portable, larger. Linked: the HTML references external files (`report_files/`, `figures/`), which must be shipped alongside.
4. a) SVG (vector line art) – or PNG; b) PNG (raster image; JPEG acceptable for photos but not for plots).

## Level 2
5. The report links to images in a folder (`report_files/` or `figures/`) that wasn't sent. Fix: send the whole folder (zipped), or re-render as self-contained (`embed-resources: true`).
6. `[Results](#results-discussion)` in Markdown, or `<a href="#results-discussion">Results</a>`.
7. `figure img { max-width: 100%; height: auto; }`

## Level 3
8. ```html
   <figure id="fig-psth">
     <img src="figures/psth.png" alt="Peri-stimulus time histogram of 34 units with a peak 50 ms after stimulus onset">
     <figcaption>Figure 2. PSTH of 34 units, 10 ms bins.</figcaption>
   </figure>
   ```
9. ```html
   <details>
     <summary>Full model output</summary>
     <pre>Linear mixed model fit by REML ...</pre>
   </details>
   ```
10. ```yaml
    format:
      html:
        embed-resources: true
        toc: true
        code-fold: true
    ```

## Level 4
11. Visible: subject ID, recording summary (duration, channels, sampling rate), key QC numbers (bad channels, % rejected epochs, number of ICA components removed), main figures (PSD before/after cleaning, ERP butterfly plot). Folded: full channel lists, per-component ICA maps, parameter dumps, logs, software versions.
12. The self-contained file is one large HTML (figures embedded as base64); the linked version is a small HTML plus a `_files` folder. In developer tools, the `<img>` element's `src` shows either a file path or a `data:image/png;base64,…` string.
