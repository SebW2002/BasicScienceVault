<img width="910" height="213" alt="lockup-knowledge-neuron" src="https://github.com/user-attachments/assets/ffbcdc84-3d70-4c50-921a-6a889b6374da" />
# 🧠 BasicScienceVault

**An open Obsidian vault that reviews the foundations of neuroscience – mathematics, physics, chemistry, biology, methods, computer science and programming – from school level to the level of research papers.**

Every topic comes with a theory note (rules, worked examples, neuroscience applications), a worksheet (easy → hard, mostly pen and paper) and worked solutions. Notes are densely linked, so you can follow any concept from the maths to the neuron to the code.

> ⭐ Start in Obsidian with the note **[`000 BasicScienceVault`](000%20BasicScienceVault.md)** – the master roadmap.
> The vault uses Obsidian `[[wikilinks]]`, callouts and Mermaid diagrams: it is best read in **Obsidian**, not on GitHub.

---

## What's inside

| Area | Fields | Topics | Start note |
|---|---|---|---|
| **Mathematics** | arithmetic & algebra, functions & calculus (incl. ODEs, multivariable, Fourier), linear algebra, geometry & vectors, sets/logic/complex numbers | 30 | [`00 Roadmap`](00%20Roadmap.md) |
| **Neuroscience foundations** | physics, chemistry, biology, methods, computer science (concepts) | 47 | [`MOC-neuroscience-foundations`](neuro-foundations/MOC-neuroscience-foundations.md) |
| **Programming** | shared concepts, Python, R, MATLAB, Markdown/HTML/LaTeX | 47 | [`MOC-programming`](neuro-foundations/06-programming/MOC-programming.md) |

**124 topics** × (theory note + worksheet + solutions), 15 mistake logs with pre-filled classic traps, maps of content with learning paths, and a setup guide for all tools.

Each topic note contains:
- the concepts with worked examples,
- a **`#neuro`** section – where it matters in neuroscience,
- **`#math-link`** sections and **Connections** to other notes,
- **key takeaways**.

## How to use it

1. **Install Obsidian** (free, [obsidian.md](https://obsidian.md)).
2. **Get the vault:** *Code → Download ZIP*, or `git clone https://github.com/<SebW2002>/BasicScienceVault.git`.
3. In Obsidian: **Open folder as vault** → choose the folder → open `000 BasicScienceVault`.
4. Follow the six phases of the master roadmap: read the topic note → do the worksheet on paper → check the solutions → log your mistakes.
5. Optional but recommended: set up **Anki** flashcards, **VS Code**, Python, R, MATLAB and LaTeX with the **[Setup Guide (PDF)](setup/BasicScienceVault%20Setup%20Guide.pdf)**.

## Repository structure

```text
BasicScienceVault/
├── 000 BasicScienceVault.md      master roadmap (start here)
├── 00 Roadmap.md                 math roadmap
├── 01_Basics/ … 05_Foundations/  mathematics A–E (topic notes, Worksheets/, Solutions/, mistake logs)
├── neuro-foundations/
│   ├── MOC-neuroscience-foundations.md
│   ├── 01-chemistry/ 02-biology/ 03-methods/ 04-physics/ 05-computer-science/
│   └── 06-programming/           Python, R, MATLAB, Markdown/HTML/LaTeX
├── _Templates/                   templates for new topics, worksheets, solutions, mistakes, lecture notes
├── setup/                        setup guide (PDF + Markdown source), Python environment, R packages, MATLAB check
├── scripts/check_vault.py        consistency checks (links, structure, tables)
├── .github/                      issue/PR templates and the automatic check workflow
├── CONTRIBUTING.md               how to contribute
└── CHANGELOG.md
```

## Contributing

Found a mistake, have a better example, want to add a topic or translate something? Contributions are very welcome – see **[CONTRIBUTING.md](CONTRIBUTING.md)**.

- **Small fixes** (typos, a wrong number): open an [issue](../../issues/new/choose) or edit the file directly on GitHub (pencil icon → *Propose changes*).
- **New topics or larger changes:** fork → branch → pull request. Every pull request is checked automatically by `scripts/check_vault.py` (broken links, missing worksheets/solutions, malformed tables).
- **Questions and ideas:** use [Discussions](../../discussions).

## Licence

- Notes, worksheets, solutions and the setup guide: **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)** – you may share and adapt them, with attribution, under the same licence.
- Scripts and configuration files (`scripts/`, `setup/*.yml`, `setup/*.R`, `setup/*.m`, `.github/`): **MIT**.

## Disclaimer

This vault is a learning resource, not a textbook or a medical reference. The content was drafted with the help of an AI assistant (Claude) and reviewed by the maintainer; numerical answers and code examples were checked where possible, but errors are still possible. If you find one, please [open an issue](../../issues/new/choose) – that's exactly what the mistake logs teach: every error found makes the vault better.
