---
aliases: [Markdown Syntax, Markdown Basics, Obsidian Markdown, Footnotes, Task Lists]
tags: [programming, markdown, documentation, type/overview, neuro]
---
# Doc01 Markdown Syntax

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc01 Markdown Syntax - Worksheet|✏️ Worksheet]] · [[Doc01 Markdown Syntax - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
Markdown is plain text with a few symbols for structure. It's what this vault is written in, what Jupyter notebooks, R Markdown/Quarto, GitHub READMEs, lab wikis and many note apps use. Because it's plain text, it's **future-proof**, diffs well in git and converts to HTML, PDF, Word or LaTeX with Pandoc ([[Doc10 When to Use What]]).

## Headings, paragraphs, emphasis
```markdown
# Heading 1 (document title)
## Heading 2
### Heading 3

A paragraph is text separated by a **blank line**.
A single line break inside a paragraph is usually ignored (Obsidian shows it by default – a setting).

*italic* or _italic_, **bold**, ***bold italic***, ~~strikethrough~~, `inline code`, ==highlight== (Obsidian)
```
- Put a space after `#`; leave a blank line before and after headings, lists, tables and code blocks – many renderers need it.
- Use **one** `#` heading per document (the title), then `##`, `###` in order – this creates the outline and the table of contents.

## Lists
```markdown
- unordered item
- another
  - nested (indent 2–4 spaces)
1. ordered item
2. second
   1. nested ordered
```
Numbers in ordered lists don't need to be correct (`1.` `1.` `1.` renders as 1, 2, 3), but the first number sets the start.

## Links and images
```markdown
[MNE documentation](https://mne.tools)          external link
<https://openneuro.org>                          bare URL
![Electrode layout](figures/montage.png)         image (alt text in brackets)
[[Py05 NumPy and Arrays]]                        Obsidian wikilink to a note
[[Py05 NumPy and Arrays|NumPy note]]             wikilink with display text
[[Py05 NumPy and Arrays#Broadcasting]]           link to a heading
![[figures/montage.png]]                         Obsidian embed (image or note)
```
Wikilinks (`[[…]]`) are Obsidian/wiki syntax, not standard Markdown: GitHub and Pandoc show them as plain text unless converted.

## Code blocks
````markdown
```python
import numpy as np
x = np.linspace(0, 1, 1001)
```
````
- Fenced with three backticks; the language after the opening fence enables **syntax highlighting** (`python`, `r`, `matlab`, `bash`, `latex`, `yaml`, `json`).
- To show a fence inside a fence, use four backticks for the outer one (as above).
- Indenting by 4 spaces also makes a code block (old style; avoid inside lists).
- In Obsidian, ```` ```mermaid ```` blocks render diagrams (used throughout this vault).

## Tables
```markdown
| Band  | Range (Hz) | Typical state       |
|-------|-----------:|:--------------------|
| theta | 4–8        | memory, navigation  |
| alpha | 8–12       | relaxed, eyes closed|
```
- The second line separates header and body; colons set alignment (`:---` left, `---:` right, `:---:` centred).
- Columns don't need to line up in the source. A literal `|` inside a cell must be escaped as `\|` – that's why the wikilinks with display text in this vault's tables are written `[[note\|✏️]]`.
- Tables can't contain block elements (lists, code blocks); for complex tables use HTML ([[Doc03 HTML Basics]]) or generate them from data ([[R10 R Markdown and Quarto]]).

## Checklists, footnotes, quotes
```markdown
- [ ] filter raw data
- [x] check event codes          ← task list (GitHub, Obsidian, Quarto)

The P300 peaks around 300 ms after rare stimuli.[^1]

[^1]: Polich, J. (2007). Updating P300. *Clinical Neurophysiology*, 118, 2128–2148.

> A blockquote: quoted text or a remark.
> > Nested quote.

> [!tip] Obsidian callout
> Callouts are blockquotes with a type: note, tip, warning, example, info …
```
- **Task lists** are clickable in Obsidian (the progress lists in the MOCs of this vault).
- **Footnotes** are collected at the end of the rendered document; good for short references in notes (for papers use citations, [[Doc07 LaTeX Documents and TeX Live]]).
- **Horizontal rule:** `---` on its own line (with blank lines around; at the very top `---` starts YAML front matter instead).

## Front matter (YAML)
```markdown
---
aliases: [NumPy, ndarray]
tags: [programming, python]
---
```
Metadata at the top of a file: Obsidian uses `aliases` and `tags` (as in every note of this vault); Quarto/R Markdown use it for title, author and output formats ([[R10 R Markdown and Quarto]]); static-site generators for page settings.

## Markdown flavours
| Flavour | Used by | Extras |
|---|---|---|
| CommonMark | the standard core | – |
| GitHub Flavored Markdown (GFM) | GitHub, many tools | tables, task lists, strikethrough, autolinks, footnotes, alerts (`> [!NOTE]`) |
| Obsidian | this vault | wikilinks, embeds, callouts, highlights, tags `#tag`, comments `%% … %%` |
| Pandoc Markdown | Pandoc, Quarto, R Markdown | citations `[@key]`, cross-references, attributes `{.class}`, divs `:::` |
Write the common core when a document must work everywhere; use flavour-specific features where they help.

## In neuroscience #neuro
- **Lab notebooks and protocols** in Markdown (Obsidian, GitHub wiki): searchable, linkable, version-controlled.
- **README files** for datasets and code (BIDS requires a `README`; [[CS05 Data Formats and Representation]]), with run instructions in code blocks.
- **Jupyter/Quarto** text cells explain analyses next to the code ([[Py01 Python Basics and Syntax]], [[R10 R Markdown and Quarto]]).
- **Preregistrations and analysis plans** drafted in Markdown and converted to PDF with Pandoc ([[Doc10 When to Use What]]).

## Math links #math-link
- Formulas in Markdown → [[Doc02 Math in Markdown]]

## Connections
- Math → [[Doc02 Math in Markdown]]; HTML output → [[Doc03 HTML Basics]]
- Reports → [[R10 R Markdown and Quarto]], [[MAT11 MATLAB Live Scripts and Reports]]
- Choosing a format → [[Doc10 When to Use What]]
- READMEs in projects → [[Py13 Python Reproducible Projects and Testing]], [[R11 R Reproducible Projects]]

## Key takeaways
- `#` headings, `-`/`1.` lists, `[text](url)`, `![alt](img)`, fenced code with a language, pipe tables.
- Blank lines around blocks; escape `|` in table cells as `\|`.
- `- [ ]` task lists, `[^1]` footnotes, `>` quotes, YAML front matter at the top.
- Know your flavour: wikilinks and callouts are Obsidian; citations are Pandoc/Quarto.
