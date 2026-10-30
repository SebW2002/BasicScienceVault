---
tags: [programming, html, type/solution]
---
# Doc03 HTML Basics – Solutions

> Worksheet: [[Doc03 HTML Basics - Worksheet]] · Theory: [[Doc03 HTML Basics]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. `<head>`: metadata not shown on the page – `<meta charset>`, `<title>`, CSS (`<link>`, `<style>`), scripts. `<body>`: everything visible – headings, text, images, tables.
2. `<h2>Methods</h2>`, `<strong>64</strong> channels`, `<a href="https://sccn.ucsd.edu/eeglab">EEGLAB</a>`, `<img src="erp.png" alt="ERP">`.
3. `<div>` is a block container (starts on a new line, takes the full width); `<span>` is an inline container inside text. `id` is unique on the page (anchor, single element); `class` is a reusable label for any number of elements.
4. `<img>`, `<br>`, `<meta>` (void elements). `<p>` and `<td>` have content and closing tags (HTML allows omitting some closing tags, but write them).

## Level 2
5. Wrong nesting: `<strong>` must close before `<p>`: `<p>The <strong>P300</strong> was larger.</p>`.
6. Absolute local path – the image won't load for anyone else (use a relative path like `figs/erp.png` and keep the folder together); missing `alt` text.
7. IDs must be unique: links to `#fig1` and CSS/JavaScript targeting it hit only the first one (behaviour undefined); cross-references in reports break.
8. The file is UTF-8 but the browser decodes it with another encoding. Add `<meta charset="utf-8">` in `<head>` (and save the file as UTF-8).

## Level 3
9. ```html
   <table>
     <tr><th>Condition</th><th>Mean RT (ms)</th></tr>
     <tr><td>face</td><td>452</td></tr>
     <tr><td>house</td><td>498</td></tr>
   </table>
   ```
10. `<p>See the <a href="#stats">statistics section</a>.</p>` … `<h2 id="stats">Statistics</h2>`
11. ```css
    body { font-family: sans-serif; max-width: 45em; }
    .warning { border-left: 4px solid orange; }
    #summary { color: darkblue; }
    ```

## Level 4
12. They embed many figures (and sometimes interactive data/JavaScript) directly in the file: images are included either as **links to separate files** (`<img src="figures/x.png">`, small HTML but a folder to keep together) or **embedded as base64 data** (`<img src="data:image/png;base64,…">`, one self-contained but large file). Share large reports via a link/cloud folder, or reduce figure resolution.
13. ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Pilot report</title>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <h1>Pilot report</h1>
      <p>EEG from 5 participants, visual oddball.</p>
      <img src="erp.png" alt="Grand-average ERP at Pz" width="500">
      <table>
        <tr><th>Condition</th><th>Trials</th></tr>
        <tr><td>oddball</td><td>80</td></tr>
        <tr><td>standard</td><td>320</td></tr>
      </table>
      <div class="note">Subject 3 excluded (noisy recording).</div>
    </body>
    </html>
    ```
    with `style.css`: `.note { background: #eef; padding: 0.5em; border-left: 4px solid #36c; }`.
