# Contributing to BasicScienceVault

Thank you for helping! This vault lives from corrections, better examples and new topics. All content is written in **English**.

## Ways to contribute

| You want to … | Do this |
|---|---|
| report an error (wrong formula, wrong solution, broken link) | open an issue with the template **"Content error"** |
| suggest a new topic or a better explanation | open an issue with the template **"New topic / improvement"**, or start a Discussion |
| fix a typo or a single line | edit the file on GitHub (pencil icon) → *Propose changes* → pull request |
| add or rewrite notes | fork the repository, work in Obsidian/VS Code, open a pull request (below) |

## Workflow for pull requests

1. **Fork** the repository (button *Fork* on GitHub) and **clone** your fork:
   `git clone https://github.com/<you>/BasicScienceVault.git`
2. Create a **branch** with a descriptive name: `git switch -c fix/b10-solution-task-7` or `topic/ph13-acoustics`.
3. Make your changes (see the conventions below). Open the folder as a vault in Obsidian to check that links and formulas render.
4. Run the checks locally: `python scripts/check_vault.py` (needs only Python 3).
5. **Commit** with a clear message (`Fix sign error in B10 solution 7`, `Add Ph13 Acoustics with worksheet and solutions`) and **push** to your fork.
6. Open a **pull request** against `main`. Fill in the checklist of the PR template. The automatic check must pass; a maintainer reviews the content.

Please keep one pull request to one topic or one kind of change – that makes reviewing much easier.

## Conventions

### Files and names
- Note names must be **unique in the whole vault** (Obsidian links by name). Use the field prefix and the next free number:

  | Field | Prefix | Folder |
  |---|---|---|
  | Math A–E | `A1`, `B13`, … | `01_Basics/` … `05_Foundations/` |
  | Physics, chemistry, biology, methods, computer science | `Ph`, `Ch`, `Bio`, `Meth`, `CS` + two digits | `neuro-foundations/0X-…/NN-topic-name/` |
  | Programming | `Prog`, `Py`, `R`, `MAT`, `Doc` + two digits | `neuro-foundations/06-programming/…/NN-topic-name/` |

- Each topic has exactly three notes: `<Name>`, `<Name> - Worksheet`, `<Name> - Solutions` (math: worksheets/solutions in the `Worksheets/` and `Solutions/` subfolders; other fields: all three in the topic folder).
- No characters in names that break links: avoid `: # | [ ] ^ /`. Write "Sets Logic and Quantifiers", not "Sets, Logic & Quantifiers".

### Structure of a topic note
Use `_Templates/Topic Note Template.md`. Required parts:
1. YAML front matter with `aliases` and `tags` (field tag, topic tag, `type/overview`, `neuro`).
2. Navigation line: `↑ MOC · ✏️ Worksheet · ✅ Solutions · ⚠️ Mistake log`.
3. `## Why this matters` – motivation in 2–3 sentences.
4. Concept sections with **worked examples**.
5. `## In neuroscience #neuro` – concrete applications.
6. `## Math links #math-link` (if math is used) and `## Connections` with wikilinks.
7. `## Key takeaways` – 3–5 bullets.
Programming notes also have `## Same idea in …` comparing the languages.

### Worksheets and solutions
- Levels: **1 Recall → 2 Understanding → 3 Calculation/code → 4 Neuroscience transfer**, easy to hard, about 12–15 tasks.
- Pen and paper by default. **At most one** task marked 🧮 (calculator) and, in programming worksheets, **at most one** marked 💻 (computer).
- Solutions show the **reasoning and intermediate steps**, not only results. Check numbers (and run code) before submitting.

### Writing style
- Clear, short sentences; define terms when first used; use SI units with a space (`20 ms`).
- Formulas in LaTeX: `$…$` inline, `$$…$$` display. Inside tables write absolute values as `\lvert x\rvert` and escape a literal pipe as `\|`.
- Link generously with `[[Note name]]` – but only to notes that exist. Link to a heading with `[[Note#Heading]]`.
- Diagrams with Mermaid code blocks.
- Neuroscience facts: prefer textbook knowledge; cite primary sources for specific claims (author, year) – especially for numbers that may change.

### When you add a topic, also update
- the field's **MOC** (topic table, recommended order, diagram if relevant, progress checklist),
- the **mistake log** of the field with 1–3 typical traps,
- **Connections** in related notes (both directions),
- for math topics used elsewhere: the section *Where this is used in the vault*,
- `CHANGELOG.md`.

## Personal files
Your own lecture notes, flashcards (e.g. from the *Obsidian to Anki* plugin, which writes ID comments into notes) and filled-in mistake logs are personal – please don't include them in pull requests. Keep them in a separate folder or branch.

## Code of conduct
Be kind and constructive. Critique content, not people. Explanations should be welcoming to beginners – everyone in this vault is here to learn.
