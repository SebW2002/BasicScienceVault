---
title: "BasicScienceVault – Setup Guide"
subtitle: "Obsidian, Anki, Git, VS Code, Python, R, MATLAB, LaTeX, Pandoc & Quarto"
tags: [setup]
---

# Overview

This guide sets up everything you need to work with **BasicScienceVault**: the note app to read and extend the vault, flashcards, version control, and the programming and writing tools used in the programming part (Py, R, MAT and Doc notes). You don't need everything on day one – the table shows **when** each tool becomes relevant.

| # | Tool | What for | Needed from | Cost |
|---|---|---|---|---|
| 1 | **Obsidian** (+ plugins, Minimal theme) | reading and working with the vault | day 1 | free |
| 2 | **Anki** + AnkiConnect | flashcards from your notes and mistake logs | day 1 (optional) | free (desktop) |
| 3 | **Git** + GitHub account | backups, updates, contributing | when you want to sync or contribute | free |
| 4 | **VS Code** + extensions | one editor for Python, R, MATLAB, Markdown, LaTeX | programming stage P1 | free |
| 5 | **Python** (Miniforge + `bsv` environment) | Py01–Py13 | P1–P2 | free |
| 6 | **R** + RStudio | R01–R11 | P4 | free |
| 7 | **MATLAB** + toolboxes | MAT01–MAT12 | P5 | licence (usually via university) |
| 8 | **LaTeX** (TeX Live / MacTeX / MiKTeX) | Doc05–Doc09, PDF reports | P3b | free |
| 9 | **Pandoc** + **Quarto** | conversions, reports (Doc09, R10) | P3/P4 | free |
| 10 | **Zotero** + Better BibTeX | references for reports and the thesis | when you write | free |

**Recommended order:** 1 → 2 → 4 → 5 → 3 → 8 → 9 → 6 → 7 → 10. The commands are given for **Windows**, **macOS** and **Linux** where they differ. Text in `monospace` is typed exactly as shown; a `$` at the beginning of a line means "type this in a terminal" (don't type the `$`).

> **Terminal:** Windows – *Windows Terminal* / *PowerShell* (or the *Miniforge Prompt* for Python); macOS – *Terminal*; Linux – your terminal emulator.

The helper files mentioned below live in the vault's `setup/` folder: `environment.yml` (Python), `install_r_packages.R` (R), `check_matlab_setup.m` (MATLAB), and `.vscode/extensions.json` (VS Code recommendations).

# Getting the vault

**Option A – download:** download the ZIP from the GitHub repository (*Code → Download ZIP*) and unpack it, e.g. to `Documents/BasicScienceVault`.

**Option B – clone with Git** (after section 3; recommended, because you can pull updates):

```bash
$ cd ~/Documents
$ git clone https://github.com/<user>/BasicScienceVault.git
```

Keep the vault in a normal folder (not in a system or program folder). Cloud folders (OneDrive, iCloud, Dropbox) work, but don't combine them with Git sync on the same folder – use one of the two.

# 1 · Obsidian

## Install and open the vault

1. Download Obsidian from **obsidian.md** and install it (Windows, macOS, Linux; also iOS/Android).
2. Start Obsidian → **Open folder as vault** → choose the `BasicScienceVault` folder.
3. When asked, **trust the author** of the vault only if you want to enable the plugins (see below) – the vault itself contains only Markdown files.
4. Open the note **`000 BasicScienceVault`** – that's the start page. Pin it: right-click the tab → *Pin*, or add it to **Bookmarks**.

## Recommended settings

Open *Settings* (gear icon, bottom left).

| Section | Setting | Value | Why |
|---|---|---|---|
| Files and links | Use \[\[Wikilinks\]\] | **on** | the vault uses wikilinks |
| | New link format | Shortest path when possible | note names are unique |
| | Automatically update internal links | **on** | renaming a note keeps links working |
| | Default location for new attachments | In the folder specified below → `_attachments` | images in one place |
| | Excluded files | `setup/` (optional) | keeps helper files out of search and graph |
| Editor | Readable line length | on | comfortable reading |
| | Properties in document | Visible (or Hidden) | YAML metadata (tags, aliases) |
| | Default view for new tabs | Editing view / Live Preview | formulas render while you type |
| Appearance | Theme | Minimal (see below) | |
| Core plugins | Templates → Template folder location | `_Templates` | insert the vault's templates |

**Core plugins** to keep enabled (*Settings → Core plugins*): Backlinks (*show backlinks at bottom of document*), Outgoing links, Outline, Graph view, Tags view, Page preview, Bookmarks, Templates, Command palette, Quick switcher, File recovery (automatic snapshots), Canvas, Word count.

**Useful shortcuts:** `Ctrl/Cmd + O` quick switcher (open a note by name), `Ctrl/Cmd + P` command palette, `Ctrl/Cmd + E` toggle edit/reading view, `Ctrl/Cmd + click` open a link in a new tab, `Ctrl/Cmd + G` graph view. Hover over a link while holding `Ctrl/Cmd` for a preview.

**Graph view colour groups** (*Graph view → Settings → Groups → New group*), one query per area:

| Group | Query |
|---|---|
| Math | `path:01_Basics OR path:02_Analysis OR path:"03_Linear Algebra" OR path:"04_Geometry & Vectors" OR path:05_Foundations` |
| Physics, chemistry, biology | `path:neuro-foundations/04-physics OR path:neuro-foundations/01-chemistry OR path:neuro-foundations/02-biology` |
| Methods | `path:neuro-foundations/03-methods` |
| Computer science | `path:neuro-foundations/05-computer-science` |
| Programming | `path:neuro-foundations/06-programming` |

Use the filter `-tag:#type/worksheet -tag:#type/solution` to see only the topic notes.

## Community plugins

*Settings → Community plugins → Turn on community plugins → Browse*, search for the name, **Install**, then **Enable**. Community plugins are made by volunteers; install only what you need.

| Plugin | Recommendation | What it does in this vault |
|---|---|---|
| **Obsidian to Anki** (listed as *Obsidian_to_Anki*) | ⭐ recommended | sends flashcards written in your notes to Anki (setup in section 2) |
| **Spaced Repetition** | alternative to Anki | flashcards and note reviews directly inside Obsidian |
| **Style Settings** | ⭐ with Minimal | exposes theme options |
| **Minimal Theme Settings** | ⭐ with Minimal | colours, line width, table and image options of the Minimal theme |
| **Dataview** | ⭐ recommended | queries over the vault, e.g. lists of all worksheets or your own lecture notes |
| **Latex Suite** | ⭐ recommended | fast formula typing with snippets (`mk` → inline math, `dm` → display math, `/` → `\frac{}{}`) |
| **Obsidian Git** | recommended if you use Git | automatic commits/pulls from inside Obsidian (section 3) |
| **Advanced Tables** | useful | formats Markdown tables, Tab moves between cells |
| **Omnisearch** | useful | better full-text search (also inside PDFs) |
| **Excalidraw** | useful | hand-drawn sketches and diagrams (circuits, neurons) inside notes |
| **Tag Wrangler** | useful | rename and merge tags |
| **Zotero Integration** | when you write | insert citations and literature notes from Zotero |
| **Templater** | advanced | templates with logic (dates, prompts); the core Templates plugin is enough to start |

**Dataview example** – put this in any note to list all worksheets of the programming part:

````markdown
```dataview
TABLE file.folder AS "Folder"
FROM #type/worksheet AND "neuro-foundations/06-programming"
SORT file.name ASC
```
````

Your own lecture notes (`#lecture`) with their linked topics:

````markdown
```dataview
LIST file.outlinks
FROM #lecture
SORT file.ctime DESC
```
````

## Theme: Minimal

1. *Settings → Appearance → Themes → Manage* → search **Minimal** (by kepano) → *Install and use*.
2. Install and enable the community plugins **Minimal Theme Settings** and **Style Settings**.
3. In *Minimal Theme Settings* try: a light/dark colour scheme you like, **line width** "normal", **tables and images** "wide" (the vault has many wide tables), and **focus mode** for distraction-free reading.
4. Optional in *Style Settings → Minimal*: heading colours, monospace font size (code blocks), and colourful headings or *Fancy cursor*.

Alternatives: *Things*, *AnuPpuccin*, *Prism*. The vault works with every theme – choose what is readable for you.

## Mobile and sync

Obsidian Sync (paid, end-to-end encrypted), iCloud (iOS/macOS), or Git (Obsidian Git also works on mobile, but more slowly). Never use two sync methods on the same folder.

# 2 · Anki and the Obsidian to Anki plugin

## Install Anki and AnkiConnect

1. Download **Anki** from **apps.ankiweb.net** and install it. Create a free AnkiWeb account if you want to sync to your phone (AnkiDroid is free; AnkiMobile for iOS is paid).
2. In Anki: *Tools → Add-ons → Get Add-ons…* → enter the code **`2055492159`** (*AnkiConnect*) → *OK* → restart Anki.
3. *Tools → Add-ons* → select *AnkiConnect* → *Config* and make sure the list `webCorsOriginList` contains Obsidian:

```json
"webCorsOriginList": [
    "http://localhost",
    "app://obsidian.md"
]
```

4. Restart Anki. **Anki must be running** whenever the plugin sends cards.

## Configure the plugin

1. In Obsidian install and enable **Obsidian to Anki** – with Anki running, so it can read your note types.
2. In the plugin settings set a **Default Deck**, e.g. `BasicScienceVault`. Optionally map folders to decks (*Folder Deck* table), e.g. `neuro-foundations/04-physics` → `BasicScienceVault::Physics`.
3. Turn on **Add File Link** (each card links back to its note) and **Add Context** (shows the heading path).

## Writing cards

Write cards anywhere in a note, between `START` and `END`. The first line is the Anki note type (`Basic`, `Basic (and reversed card)`, `Cloze` …):

```text
TARGET DECK
BasicScienceVault::Physics

START
Basic
Membrane time constant τ = ?
Back: $\tau = R_m C_m$ – the time to reach 63 % of the final voltage change.
END

START
Basic
Python: how many elements does `x[2:5]` have?
Back: 3 – the stop index is excluded.
END
```

Then click the **Anki icon** in the left ribbon (or run *Obsidian to Anki: Scan vault* from the command palette). Formulas in `$…$` are converted to Anki's MathJax format. The plugin adds an ID comment (`<!--ID: …-->`) below each card – **don't delete it**, it links the card to Anki for later updates.

**Tips**

- Keep cards in **your own notes** – e.g. one note `Cards - Physics` per field, or a *Flashcards* section in your mistake logs – rather than inside the shared topic notes. This keeps the vault easy to update from GitHub.
- Best sources for cards: your **mistake-log entries**, formulas from the *Key takeaways*, and one question per worksheet level-1 task.
- One fact per card; ask *why* and *when*, not only *what*.
- **Alternative without Anki:** the *Spaced Repetition* plugin uses `question::answer` lines and reviews them inside Obsidian.

# 3 · Git and GitHub

1. Install **Git**: Windows – **git-scm.com** (keep the defaults; choose VS Code as editor); macOS – `xcode-select --install` or Homebrew `brew install git`; Linux – `sudo apt install git`.
2. Tell Git who you are (once):

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
$ git config --global init.defaultBranch main
```

3. Create a free account on **github.com**. For a graphical interface install **GitHub Desktop**, or use the Git panel in VS Code.
4. Optional: in Obsidian install **Obsidian Git** → set *Auto commit-and-sync interval* (e.g. 30 min) and *Pull on startup*. Your personal settings (`.obsidian/workspace*.json`) are excluded by the vault's `.gitignore`.

How to contribute changes back is described in `CONTRIBUTING.md` in the repository.

# 4 · VS Code

1. Download **Visual Studio Code** from **code.visualstudio.com** and install it. On Windows tick *Add to PATH* and *Open with Code*.
2. *File → Open Folder* → choose the vault folder. VS Code reads `.vscode/extensions.json` and offers to **install the recommended extensions** – accept.
3. Or install them from a terminal:

```bash
$ code --install-extension ms-python.python
$ code --install-extension ms-python.vscode-pylance
$ code --install-extension ms-toolsai.jupyter
$ code --install-extension charliermarsh.ruff
$ code --install-extension REditorSupport.r
$ code --install-extension MathWorks.language-matlab
$ code --install-extension James-Yu.latex-workshop
$ code --install-extension ltex-plus.vscode-ltex-plus
$ code --install-extension quarto.quarto
$ code --install-extension yzhang.markdown-all-in-one
$ code --install-extension bierner.markdown-mermaid
$ code --install-extension mechatroner.rainbow-csv
$ code --install-extension eamodio.gitlens
$ code --install-extension streetsidesoftware.code-spell-checker
```

| Extension | For |
|---|---|
| Python, Pylance, Jupyter, Ruff | Python scripts and notebooks, completion, linting/formatting (Py01–Py13) |
| R | running R code, plots, help (needs the R package `languageserver`, installed by `install_r_packages.R`) |
| MATLAB (MathWorks) | editing and running `.m` files (needs a local MATLAB; set *MATLAB: Install Path* in the settings) |
| LaTeX Workshop, LTeX+ | compiling LaTeX with preview and SyncTeX; grammar/spell checking (Doc05–Doc09) |
| Quarto | rendering `.qmd` reports (R10) |
| Markdown All in One, Markdown Mermaid | Markdown editing and preview with diagrams |
| Rainbow CSV, GitLens, Code Spell Checker | readable CSV files, Git history, spelling |

**Useful settings** (*Ctrl/Cmd + Shift + P → Preferences: Open User Settings (JSON)*):

```json
{
  "files.autoSave": "onFocusChange",
  "editor.rulers": [88],
  "[markdown]": { "editor.wordWrap": "on" },
  "[latex]": { "editor.wordWrap": "on" },
  "latex-workshop.latex.outDir": "%DIR%/build",
  "python.terminal.activateEnvironment": true
}
```

**Alternatives:** RStudio (for R), the MATLAB desktop (for MATLAB) and JupyterLab (for notebooks) are equally fine – the vault notes mention both.

# 5 · Python

## Install Miniforge

**Miniforge** is a small conda distribution that uses the community channel *conda-forge* and includes the fast installer *mamba*.

- **Windows:** download the installer from **github.com/conda-forge/miniforge** → *Just me* → keep the defaults. Afterwards use the **Miniforge Prompt** (or run `conda init powershell` once in it to use conda in PowerShell/VS Code).
- **macOS/Linux:**

```bash
$ curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
$ bash Miniforge3-$(uname)-$(uname -m).sh
```

Close and reopen the terminal; `conda --version` should print a version.

## Create the vault environment

In the vault folder:

```bash
$ mamba env create -f setup/environment.yml      # takes a few minutes
$ conda activate bsv
$ python -c "import numpy, scipy, pandas, sklearn, mne, nilearn; print('ok')"
```

The environment `bsv` contains NumPy, SciPy, pandas, matplotlib, seaborn, statsmodels, scikit-learn, JupyterLab, pytest, Ruff, h5py, Zarr, PyNWB, MNE (+ mne-bids, mne-icalabel), NiBabel, Nilearn, Neo, Elephant, SpikeInterface, Brian2, DANDI and Nipype – everything used in Py01–Py10 and Py13.

- **Jupyter:** `jupyter lab` in the activated environment, or open an `.ipynb` in VS Code and choose the kernel **bsv**.
- **VS Code:** *Ctrl/Cmd + Shift + P → Python: Select Interpreter* → `bsv`.
- **Update later:** `mamba env update -f setup/environment.yml --prune`.
- **Rule:** one environment per project ([[Py13 Python Reproducible Projects and Testing]]); never install packages into the system Python.

## PyTorch (Py09)

PyTorch is installed separately because the right build depends on your hardware. In the activated `bsv` environment, use the command shown on **pytorch.org → Get Started** for your system; for a laptop without an NVIDIA GPU the CPU build is enough:

```bash
$ pip install torch torchvision
$ python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

## PsychoPy (Py11)

Use the **standalone PsychoPy installer** from **psychopy.org → Download** (it brings its own Python with all audio/video dependencies). Don't install PsychoPy into `bsv` – its dependencies conflict with other packages.

## NEURON (Py10, optional)

macOS/Linux: `pip install neuron` in `bsv`. Windows: use the installer from **neuron.yale.edu** (or WSL).

# 6 · R

1. **R:** download from **cran.r-project.org** (*Download R for Windows/macOS/Linux*) and install.
2. **Build tools** (needed for packages that compile code, e.g. brms/Stan):
   - Windows: **Rtools** matching your R version (from CRAN → *Windows → Rtools*).
   - macOS: `xcode-select --install` in the Terminal.
   - Linux (Debian/Ubuntu): `sudo apt install r-base-dev libcurl4-openssl-dev libssl-dev libxml2-dev libhdf5-dev libfontconfig1-dev`.
3. **RStudio Desktop:** download from **posit.co → RStudio Desktop** (free). Alternatives: VS Code with the R extension, or Posit's *Positron*.
4. **RStudio settings** (*Tools → Global Options*): *General* – untick *Restore .RData into workspace at startup*, set *Save workspace to .RData on exit* to **Never**; *Code* – tick *Use native pipe operator |>*.
5. **Packages:** open the vault folder in RStudio (or R) and run

```r
source("setup/install_r_packages.R")
```

   This installs the tidyverse, here, renv, lme4/lmerTest, emmeans, afex, brms, BayesFactor, psych/psychometric, signal, oro.nifti, neurobase, fmri, reticulate, R.matlab, hdf5r, Quarto/rmarkdown, testthat, languageserver, plus `rhdf5` (Bioconductor) and `eegUtils` (r-universe). It prints how many packages were installed. brms compiles models with Stan on first use – this needs the build tools from step 2.
6. **Python from R** (R09): `reticulate::use_condaenv("bsv")`.

# 7 · MATLAB

## MATLAB and MathWorks toolboxes

1. Get MATLAB through your university licence (*MathWorks account with your university e-mail* → *Install*), or a student/home licence. Check the licence conditions of your institute.
2. In the installer select at least:
   - **Signal Processing Toolbox** (MAT06; used by EEGLAB and FieldTrip)
   - **Statistics and Machine Learning Toolbox** (MAT07)
   - **Image Processing Toolbox** (`niftiread`, images)
   - **Optimization Toolbox** (curve fitting)
   - optional: Curve Fitting, Deep Learning, Parallel Computing
3. Later additions: *Home → Add-Ons → Get Add-Ons*.

## Third-party neuroscience toolboxes

Put them into **one folder outside the vault**, e.g. `~/toolboxes/`, and add them to the path **in your scripts**, not permanently ([[MAT12 MATLAB Reproducible Projects]]). Never use `addpath(genpath(...))` on a whole toolbox folder.

| Toolbox | Get it | Set up / test |
|---|---|---|
| **EEGLAB** (MAT09) | **sccn.ucsd.edu/eeglab** → download ZIP | `addpath("~/toolboxes/eeglab…"); eeglab` – then *File → Manage EEGLAB extensions*: ICLabel, Clean Rawdata (included), bva-io, bids-matlab-tools, ERPLAB |
| **FieldTrip** (MAT10) | **fieldtriptoolbox.org** → Download | `addpath("~/toolboxes/fieldtrip"); ft_defaults` |
| **SPM** (MAT10) | **fil.ion.ucl.ac.uk/spm** (or GitHub `spm/spm`) | `addpath("~/toolboxes/spm"); spm fmri` |
| **Psychtoolbox-3** (MAT08) | **psychtoolbox.org** → Download (installer ZIP) | `cd` into the folder, run `SetupPsychtoolbox`, then `PsychtoolboxVersion`; Windows: also install **GStreamer** (64-bit MSVC runtime, see the PTB download page); macOS: allow MATLAB under *Privacy & Security → Accessibility / Input Monitoring* for keyboard input |
| **Brainstorm**, **CONN**, **Chronux** | see [[MAT10 MATLAB Neuroscience Toolboxes]] | as needed |

**Check everything:** in MATLAB, `cd` to the vault and run `run("setup/check_matlab_setup.m")` – it prints the MATLAB version, which toolboxes are licensed and which third-party toolboxes are on the path.

**Without a licence:** GNU **Octave** (free) runs basic MATLAB code and Psychtoolbox; Brainstorm offers a compiled stand-alone version.

# 8 · LaTeX

| System | Distribution | Install |
|---|---|---|
| Windows | **TeX Live** (install-tl-windows from **tug.org/texlive**) or **MiKTeX** (**miktex.org**) | TeX Live: full scheme (~ 8 GB, everything included). MiKTeX: small, installs packages on demand; for `latexmk` also install **Strawberry Perl** |
| macOS | **MacTeX** (**tug.org/mactex**) | the `.pkg` installer (TeX Live + tools) |
| Linux | **TeX Live** | `sudo apt install texlive-latex-extra texlive-science texlive-bibtex-extra texlive-fonts-recommended biber latexmk` (or `texlive-full`) |
| any | **Overleaf** (overleaf.com) | online, nothing to install |
| small | **TinyTeX** | `quarto install tinytex` – enough for Quarto/R Markdown PDFs |

**Test:** save this as `test.tex` and run `latexmk -pdf test.tex` (or *Build* in VS Code):

```latex
\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern, amsmath, siunitx}
\begin{document}
The membrane time constant is $\tau = R_m C_m \approx \qty{20}{\milli\second}$.
\end{document}
```

Missing package? TeX Live: `tlmgr search --global --file <name>.sty`, then `tlmgr install <package>` (Linux distribution packages: install the matching `texlive-…` package instead). MiKTeX asks to install it automatically.

**Inkscape** (**inkscape.org**, free) converts SVG figures to PDF for LaTeX and lets you edit figures (Doc08).

# 9 · Pandoc and Quarto

- **Pandoc:** **pandoc.org/installing** (Windows/macOS installer; Linux `sudo apt install pandoc` or the newer `.deb` from GitHub). Test: `pandoc --version`. Example: `pandoc note.md -o note.pdf` (needs LaTeX) or `-o note.docx`.
- **Quarto:** **quarto.org → Get Started** → installer. Test: `quarto check` – it reports which of Python (`bsv`), R/knitr and LaTeX it finds. Quarto ships its own Pandoc.
- In VS Code, the Quarto extension adds *Render* and *Preview* buttons; RStudio supports Quarto directly.

# 10 · Zotero and Better BibTeX

1. Install **Zotero** (**zotero.org**) and the browser connector.
2. Install the **Better BibTeX** add-on (**retorque.re/zotero-better-bibtex** → download the `.xpi`; Zotero → *Tools → Plugins → Install Plugin From File*).
3. Right-click a collection → *Export Collection…* → format **Better BibLaTeX** (or Better BibTeX) → tick **Keep updated** → save as `refs.bib` in your project. The file now updates automatically when you add references.
4. Use the same `refs.bib` in LaTeX (Doc07), Quarto/R Markdown (R10) and Pandoc (Doc09); in Obsidian the *Zotero Integration* plugin can insert citations.

# Check everything

| Tool | Command / action | Expected |
|---|---|---|
| Obsidian | open `000 BasicScienceVault`, click a few links, open the graph | links open, formulas and diagrams render |
| Anki | Obsidian: *Obsidian to Anki: Scan vault* with one test card | the card appears in Anki |
| Git | `git --version` | a version number |
| VS Code | `code --version` | a version number |
| Python | `conda activate bsv` then `python -c "import mne; mne.sys_info()"` | list of package versions |
| R | `source("setup/install_r_packages.R")` | "Installed: n of n packages" |
| MATLAB | `run("setup/check_matlab_setup.m")` | licensed toolboxes are `true`, toolbox paths shown |
| LaTeX | `latexmk -pdf test.tex` | `test.pdf` with the formula |
| Quarto | `quarto check` | Python, R, LaTeX found |

# Troubleshooting

| Problem | Solution |
|---|---|
| Obsidian: formulas show as raw `$…$` | you're in source mode – switch to Live Preview or reading view (`Ctrl/Cmd + E`) |
| Obsidian: wide tables cut off | Minimal Theme Settings → tables "wide"; or turn off *Readable line length* |
| Obsidian to Anki: "Failed to connect" | Anki is not running, or `app://obsidian.md` missing in AnkiConnect's `webCorsOriginList`; restart Anki |
| `conda` not found (Windows) | use the Miniforge Prompt, or run `conda init powershell` there once and reopen PowerShell |
| VS Code uses the wrong Python | *Python: Select Interpreter* → `bsv` |
| R package fails to compile | build tools missing (Rtools / Xcode command line tools / `r-base-dev`); restart R |
| `brms` model doesn't compile | check `pkgbuild::has_build_tools(debug = TRUE)` |
| MATLAB calls the wrong function (e.g. `filter`) | toolboxes shadow each other: `restoredefaultpath`, add only what you need, `which -all filter` |
| Psychtoolbox "SYNCHRONIZATION FAILURE" | one monitor, native resolution, 100 % scaling, current graphics driver (see [[MAT08 Psychtoolbox]]) |
| LaTeX: `File 'xyz.sty' not found` | install the package (`tlmgr` / MiKTeX console / distribution package) |
| `latexmk` not found on Windows (MiKTeX) | install Strawberry Perl, restart the terminal |
| Quarto PDF fails with Unicode errors | set `pdf-engine: xelatex` or `lualatex` in the YAML header |

*BasicScienceVault – Setup Guide. Part of the BasicScienceVault repository; corrections welcome via GitHub issues.*
