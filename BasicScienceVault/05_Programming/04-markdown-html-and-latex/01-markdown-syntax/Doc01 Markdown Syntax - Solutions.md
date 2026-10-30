---
tags: [programming, markdown, type/solution]
---
# Doc01 Markdown Syntax – Solutions

> Worksheet: [[Doc01 Markdown Syntax - Worksheet]] · Theory: [[Doc01 Markdown Syntax]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. ```markdown
   ## Methods

   We recorded **64-channel** EEG in a *visual* oddball task and epoched with `mne.Epochs`.
   ```
2. ```markdown
   - Preprocessing
     - filter
     - ICA
   - Statistics
   ```
3. `[OpenNeuro](https://openneuro.org)` and `![Grand-average ERP](figs/erp.png)`
4. ````markdown
   ```python
   print("hello")
   ```
   ````

## Level 2
5. One paragraph "Line one Line two" (the single line break becomes a space), then a second paragraph "Line three". (A hard break needs two trailing spaces, a backslash at line end, or `<br>`.)
6. `#Results` without a space is **not** a heading in CommonMark (it stays text; in Obsidian it even becomes a tag `#Results`). Headings also need a blank line before them in many renderers. Correct: blank line, then `# Results` / `## Discussion` (one space is enough).
7. The `|` is read as a column separator, so the row gets an extra cell and the table breaks. Escape it: `a\|b` (or use HTML `&#124;`).
8. No – wikilinks are Obsidian/wiki syntax. GitHub shows the brackets as plain text. Use `[Py05](Py05%20NumPy%20and%20Arrays.md)` for portable links, or convert with a tool/plugin.

## Level 3
9. ```markdown
   | Band  | Range (Hz) |
   |-------|-----------:|
   | delta | 1–4        |
   | gamma | 30–100     |
   ```
10. ```markdown
    - [x] record pilot
    - [ ] analyse pilot

    The task followed Smith et al.[^smith]

    [^smith]: Smith, A. et al. (2020). Title. *Journal*, 1, 1–10.
    ```
11. ```markdown
    > [!warning] Raw data
    > Never edit files in data/raw.
    ```

## Level 4
12. ````markdown
    # Visual oddball EEG dataset

    64-channel EEG (BrainVision, 500 Hz) from 30 adults in a visual oddball task.
    Data are organised in BIDS.

    ## Structure
    ```text
    data/raw/sub-XX/eeg/   raw recordings (read-only)
    data/derived/          preprocessed epochs
    code/                  analysis code
    ```

    ## How to run
    1. `conda env create -f environment.yml`
    2. `python code/01_preprocess.py`
    3. `quarto render reports/analysis.qmd`

    ## Contact
    Name, e-mail · Licence: CC-BY 4.0
    ````
13. Typical differences: wikilinks, embeds `![[…]]`, callouts, `==highlights==` and `%% comments %%` are Obsidian-only; GitHub renders its own alerts (`> [!NOTE]`) but not Obsidian's custom callout titles in the same way; single line breaks show as breaks in Obsidian (default) but not on GitHub; footnotes and task lists work in both.
