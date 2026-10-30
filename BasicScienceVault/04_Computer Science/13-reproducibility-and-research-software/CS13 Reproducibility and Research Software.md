---
aliases: [Reproducibility and Research Software, Version Control, Containers, Open Science, FAIR, Preregistration, GDPR, Reproduzierbarkeit]
tags: [computer-science, reproducibility, open-science, version-control, ethics, type/overview, neuro]
---
# CS13 Reproducibility and Research Software

> [[MOC-computer-science|↑ CS MOC]] · [[CS13 Reproducibility and Research Software - Worksheet|✏️ Worksheet]] · [[CS13 Reproducibility and Research Software - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
A result is only scientific if others (including future you) can **reproduce** it: same data + same code gives the same result. They should also be able to **replicate** it (new data, same conclusion). Many analysis results can't be reproduced because the code, software versions or data are missing. This note covers concepts, not programming: how to keep histories, environments, data and ethics in order.

**Terminology:**
- **Reproducible**: same data and code give the same numbers.
- **Replicable**: new data, same question, the same finding holds.
- **Robust**: different reasonable analyses lead to the same conclusion.
- **Generalisable**: the finding holds in other populations and settings.

## Version control (commits, branches, reproducible histories)
**Git** (and platforms like GitHub/GitLab) records the full history of a project.
| Concept | Meaning |
|---|---|
| **Repository** | the project folder plus its complete history |
| **Commit** | a snapshot of all tracked files, with a message, author, date and a unique **hash** (ID). Small, logical commits with informative messages ("fix filter cutoff from 300 to 500 Hz") |
| **History** | a chain (more precisely, a directed acyclic graph) of commits. You can go back to any state, see who changed what and why, and find when a bug appeared |
| **Branch** | a parallel line of development (try an analysis variant without breaking the main version); **merge** it back when ready |
| **Tag / release** | a named commit, e.g. "v1.0, code as used for the paper" (archive with a DOI via Zenodo) |
| **Remote** | a copy on a server for backup and collaboration; pull requests for review |

- **Put in version control:** code, configuration, small text files, documentation, manuscripts in text formats (LaTeX, Markdown, this vault!).
- **Keep out:** large raw data, passwords and personal data (`.gitignore`). For data, use data-versioning tools (DataLad / git-annex, DVC) or archives.
- **Link results to commits:** every figure should be traceable to the code version and data version that produced it.

## Environment management and containers (conceptual)
- The same code can give different results (or crash) with different versions of Python, NumPy, MNE, SPM, FSL… Defaults change between versions, and numerical libraries differ.
- **Record and pin dependencies:** environment files listing package versions (`requirements.txt`, `environment.yml`, lock files); one isolated **virtual environment** per project (venv, conda).
- **Containers** (Docker; **Apptainer/Singularity** on HPC clusters) bundle the operating system libraries, software and versions into one image that runs identically everywhere. They are lighter than virtual machines (they share the host's kernel). Neuroimaging pipelines (fMRIPrep) are distributed as containers.
- **Other sources of non-reproducibility:**
  - **random seeds** (set and record them for model training, permutations, bootstraps)
  - parallel computing order
  - **hidden state in notebooks** (cells run out of order; restart and run all before trusting results)
  - manual steps clicked in a GUI (script them, or at least log them)
- **Workflow managers** (Snakemake, Nextflow, Make) define the pipeline from raw data to figures as rules, so everything can be re-run with one command.

## Open science: preregistration, data sharing, FAIR
- **Why:** the replication crisis. Many published effects are not replicable, because of low power, flexible analyses and publication bias ([[CS06 Data Science Workflow]]).
- **Questionable research practices:**
  - **p-hacking**: trying analyses until p < 0.05
  - **HARKing**: hypothesising after the results are known
  - selective reporting
  - the **garden of forking paths**: many implicit analysis choices
- **Preregistration:** record the hypotheses, design, sample size, exclusion criteria and analysis plan in a time-stamped document **before** data collection or analysis (OSF, AsPredicted). Exploratory analyses remain allowed but are **labelled** as such. **Registered reports:** journals review and accept the plan before the results exist, which removes publication bias.
- **Data and code sharing:** repositories with DOIs (Zenodo, OSF, Figshare); domain archives (**OpenNeuro** for BIDS, **DANDI** for NWB, EBRAINS); code on GitHub archived with a release.
- **FAIR principles:**
  - **F**indable (persistent identifiers, rich metadata, indexed)
  - **A**ccessible (retrievable by standard protocols, possibly with authentication)
  - **I**nteroperable (standard formats and vocabularies: BIDS, NWB, ontologies)
  - **R**eusable (clear licence, provenance, community standards)
  - FAIR ≠ fully open: sensitive data can be FAIR with controlled access.
- **Licences:** CC-BY for data and text; MIT, BSD or GPL for code. Without a licence, others legally can't reuse your work.
- **Preprints** (bioRxiv, medRxiv) speed up dissemination; open peer review.

## Documentation and literature management
- **Project documentation:**
  - a **README** (purpose, structure, how to run)
  - data dictionaries / codebooks (each variable: meaning, unit, allowed values)
  - comments and docstrings explaining *why*
  - an electronic **lab notebook** (dated entries of what was done, decisions and their reasons)
  - a CHANGELOG
- **Folder structure:** raw data (read-only) / derived data / code / results / figures / docs. Consistent file naming (ISO dates `2026-10-30`, no spaces, versioning by git rather than `final_v3_REAL.docx`).
- **Literature management:**
  - **reference managers** (Zotero, JabRef, Mendeley) store PDFs, metadata, notes and tags
  - **BibTeX** entries have a **citation key**, a type (`@article`) and fields (author, title, journal, year, doi)
  - citation styles are generated automatically
  - **DOIs** identify papers permanently
  - Zotero can export to Obsidian (literature notes linked to your topic notes).

```bibtex
@article{hodgkin1952quantitative,
  author  = {Hodgkin, A. L. and Huxley, A. F.},
  title   = {A quantitative description of membrane current and its application to conduction and excitation in nerve},
  journal = {The Journal of Physiology},
  year    = {1952},
  volume  = {117},
  number  = {4},
  pages   = {500--544},
  doi     = {10.1113/jphysiol.1952.sp004764}
}
```

## Ethics and data protection (GDPR, anonymisation of neural and health data)
- **GDPR** (EU General Data Protection Regulation, in German DSGVO):
  - **Health data**, **genetic data** and **biometric data** are **special categories** (Art. 9) that need an explicit legal basis (typically informed consent, or research exemptions under national law) and strong safeguards.
  - Principles: lawfulness, purpose limitation, **data minimisation**, accuracy, storage limitation, integrity and confidentiality, accountability.
  - Participants have rights (information, access, deletion).
  - Data transfers outside the EU (e.g. to US cloud services) need a legal basis.
  - Institutions have data protection officers. Collaborations need data processing or sharing agreements.
- **Pseudonymisation vs. anonymisation:**
  - **Pseudonymised:** identifiers replaced by codes, with a key that still exists somewhere. **Still personal data** under GDPR.
  - **Anonymised:** re-identification is no longer reasonably possible. Then it is outside GDPR, but true anonymisation is **hard** for rich data.
- **Neural data are identifying:**
  - structural MRI contains the **face**, so **deface** before sharing
  - DICOM headers contain names and dates ([[CS05 Data Formats and Representation]])
  - functional connectivity profiles can "fingerprint" individuals
  - EEG and genetic data can be identifying
  - rare diagnoses plus age plus location can re-identify people
- **Research ethics:**
  - approval by an **ethics committee / IRB**
  - **informed consent** that explicitly covers data sharing and future use
  - incidental findings in MRI
  - vulnerable groups
  - neurotechnology ethics (mental privacy, BCIs)
  - for animal research, licences and the **3Rs** (Replace, Reduce, Refine)
  - transparent reporting (ARRIVE guidelines for animal studies)
- **AI-specific issues:** bias in training data (models trained on unrepresentative cohorts), privacy of models trained on health data, explainability requirements for clinical use.

## In neuroscience #neuro
- **BIDS + fMRIPrep + containers + OpenNeuro** is an end-to-end reproducible pipeline for neuroimaging. **NWB + DANDI + SpikeInterface** does the same for physiology.
- **NARPS** (70 teams, same data, different results) and **multiverse analyses** show why preregistration and robustness checks matter.

## Math links #math-link
- Probability of at least one false positive across $k$ analysis paths, $1 - (1 - \alpha)^k$ → [[CS02 Probability and Statistics]], [[A1 Exponent Rules]]
- Logic of claims (exploratory vs. confirmatory) → [[E1 Sets Logic and Quantifiers]]
- Hashes as fingerprints (very large numbers of possible values, $2^{160}$ for SHA-1) → [[A1 Exponent Rules]]

## Connections
- In code → [[Py13 Python Reproducible Projects and Testing]], [[R11 R Reproducible Projects]], [[MAT12 MATLAB Reproducible Projects]], [[R10 R Markdown and Quarto]], [[Doc09 LaTeX with VS Code]]
- Data formats and metadata → [[CS05 Data Formats and Representation]]
- Workflow, power, leakage → [[CS06 Data Science Workflow]]
- Analytical flexibility in imaging → [[CS12 Neuroimaging Data Analysis]]
- Computing infrastructure → [[CS14 Hardware Essentials]]
- Vault workflow and templates → [[00 Roadmap]], [[Lecture Note Template]]

## Key takeaways
- Reproducible (same data and code) ≠ replicable (new data).
- Git: commits (snapshots with hash and message), branches, tags for the paper version. Keep big or personal data out.
- Pin environments; containers run identically everywhere; set seeds; restart notebooks; script everything.
- Preregister; share data and code with DOIs and licences; follow FAIR (findable, accessible, interoperable, reusable).
- Document (README, data dictionary, lab notebook); manage literature with Zotero/BibTeX and DOIs.
- GDPR: health data are special categories; pseudonymised ≠ anonymous; deface MRI, scrub DICOM headers; ethics approval and consent for sharing.
