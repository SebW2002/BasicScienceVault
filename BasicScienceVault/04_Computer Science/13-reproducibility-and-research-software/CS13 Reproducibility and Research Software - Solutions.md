---
tags: [computer-science, reproducibility, type/solution]
---
# CS13 Reproducibility and Research Software – Solutions

> Worksheet: [[CS13 Reproducibility and Research Software - Worksheet]] · Theory: [[CS13 Reproducibility and Research Software]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. **Reproducibility:** the same data and code give the same results. **Replicability:** a new study with new data reaches the same conclusion. **Robustness:** different reasonable analysis choices on the same data give the same conclusion.
2. A snapshot of all tracked files, the author, date, message and a pointer to its parent commit(s). The hash uniquely identifies this exact state, so you can cite the code version used for a figure and check out exactly that version later.
3. **Yes:** scripts, `README.md`, `environment.yml`. **No:** raw data (too big; use an archive or DataLad), password file (security), participant names (data protection). **Figures:** usually not (they can be regenerated), except final versions for a paper release.
4. Findable, Accessible, Interoperable, Reusable.

## Level 2
5. Different package versions (e.g. NumPy, SciPy, MNE), different defaults, unset random seeds, different hardware or parallelisation (floating-point summation order, GPU non-determinism), different input data versions or paths, operating-system libraries (BLAS), locale settings (decimal comma).
6. A virtual environment isolates **Python packages** but uses the system's OS libraries and interpreter. A container bundles the **whole software stack** (OS libraries, tools, versions) into an image that runs the same on any machine. Use containers for complex pipelines with non-Python tools (FSL, FreeSurfer), for HPC clusters and for long-term archiving.
7. Cells can be run out of order, deleted or edited after running, so the visible code doesn't match the state that produced the output (**hidden state**). Prevent it by restarting the kernel and running all cells top to bottom before trusting or saving results; move core code into scripts or modules; record versions.
8. Good: "Fix high-pass cutoff: 300 → 500 Hz to suppress LFP leakage into spike band". Bad: "update", "stuff", "fixed".

## Level 3
9. $1 - 0.95^{10}\approx1 - 0.60 = 0.40$, so about a 40 % chance of at least one false positive.
10. **Preregistration:** a time-stamped public record of the plan before the analysis; the paper is still reviewed after the results. **Registered report:** the journal peer-reviews the introduction and methods **before** data collection and commits to publishing regardless of the results (in-principle acceptance), which eliminates publication bias.
11. Yes. Exploratory analyses are valuable but must be **clearly labelled** as exploratory (and deviations from the plan reported and justified). Their p-values have a different evidential weight; confirm with new data.
12. FAIR is about **how** data can be found and used (metadata, identifiers, standard formats, licence and access conditions). Sensitive health data can be well-described, findable and accessible under controlled conditions (application, data use agreement) without being openly downloadable.

## Level 4
13. a) **Pseudonymised** (a key exists, so this is still personal data). b) **Anonymised** (aggregated; no individual identifiable, provided the groups are not tiny). c) **Pseudonymised, effectively identifiable**: the combination of birth date, rare diagnosis and town makes re-identification likely, so it is not anonymous.
14. (1) Check that **consent** and ethics approval cover public sharing (and the GDPR legal basis). (2) **Deface** the images and remove identifying metadata (DICOM headers, dates; convert to NIfTI/BIDS; coarsen ages). (3) Organise in **BIDS**, run the validator, add a data dictionary and licence (e.g. CC0/CC-BY); check re-identification risk of other variables. (Also: data protection officer review if in doubt.)
15. ```bibtex
    @article{lovelace2026neural,
      author  = {Lovelace, Ada and Turing, Alan},
      title   = {Neural Codes},
      journal = {Journal of Imaginary Neuroscience},
      year    = {2026},
      volume  = {3},
      pages   = {1--10},
      doi     = {10.0000/jin.2026.001}
    }
    ```
16. $0.95^{20}\approx0.358$, so $1 - 0.358\approx0.64$ (64 %).
