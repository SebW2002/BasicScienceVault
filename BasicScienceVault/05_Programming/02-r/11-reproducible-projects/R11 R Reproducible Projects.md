---
aliases: [R Reproducible Projects, RStudio Projects, here package, renv, testthat]
tags: [programming, r, reproducibility, testing, environments, type/overview, neuro]
---
# R11 R Reproducible Projects

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R11 R Reproducible Projects - Worksheet|✏️ Worksheet]] · [[R11 R Reproducible Projects - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
An R analysis is reproducible when a colleague can clone the folder, run one command and get your numbers. Three R tools make this routine: **RStudio Projects + here** (paths that work everywhere), **renv** (exact package versions) and **testthat** (checks that your functions compute what you think). Principles → [[CS13 Reproducibility and Research Software]].

## RStudio Projects and the here package
- An **RStudio Project** (`my-study.Rproj`) is a folder with a project file. Opening it sets the **working directory** to the project root, starts a fresh R session, and remembers open files.
- Never `setwd("C:/Users/anna/...")` in a script – it breaks on every other computer ([[Prog00 Shared Programming Concepts]]).
- **here** builds paths from the project root, wherever the script or Quarto file lives:
```r
library(here)
here()                                             # the project root (found via .Rproj, .here or .git)
d <- readr::read_csv(here("data", "raw", "sub-01_task-faces.csv"))
ggsave(here("figures", "fig1.pdf"), p)
```
This matters especially in Quarto/R Markdown files in subfolders, whose working directory is **their own folder** during rendering.

Recommended layout (same idea as in Python, [[Py13 Python Reproducible Projects and Testing]]):
```text
my-study/
├── my-study.Rproj
├── README.md
├── renv.lock
├── R/                  # functions: R/preprocess.R, R/stats.R
├── scripts/            # 01_import.R, 02_models.R, 03_figures.R
├── reports/            # analysis.qmd
├── tests/testthat/     # test files
├── data/raw/           # read-only
├── data/derived/
└── figures/
```
- Load your functions with `source(here("R", "stats.R"))`; for larger projects make an R package (`usethis::create_package()`), or use **targets** for a pipeline that only reruns steps whose inputs changed.

## renv for package versions
```r
renv::init()        # creates a project library + renv.lock
install.packages("lme4")   # installs into the project library
renv::snapshot()    # records exact versions (and sources) in renv.lock
renv::restore()     # on another computer: install exactly these versions
renv::status()      # are library and lockfile in sync?
```
- Each project gets its **own library**, so updating lme4 for project B doesn't change results of project A.
- Commit `renv.lock`, `.Rprofile` and `renv/activate.R` to git, but not the library itself.
- `renv.lock` records the R version too; renv doesn't install R itself – note it in the README (or use a container, e.g. rocker images).
- `sessionInfo()` / `sessioninfo::session_info()` print all versions – include them in reports.

## Testing with testthat
```r
# R/stats.R
dprime <- function(hit, fa) {
  stopifnot(all(hit > 0 & hit < 1), all(fa > 0 & fa < 1))
  qnorm(hit) - qnorm(fa)
}
# tests/testthat/test-dprime.R
test_that("dprime is zero for equal rates", {
  expect_equal(dprime(0.7, 0.7), 0)
})
test_that("dprime is symmetric", {
  expect_equal(dprime(0.84, 0.16), -dprime(0.16, 0.84))
})
test_that("dprime rejects rates of 0 or 1", {
  expect_error(dprime(1, 0.2))
})
```
Run with `testthat::test_dir("tests/testthat")` (or `devtools::test()` in a package).
- Expectations: `expect_equal` (with tolerance for floats), `expect_identical`, `expect_true`, `expect_error`, `expect_warning`, `expect_length`, `expect_snapshot`.
- Test what you can check independently: known values, symmetry, edge cases (NA, empty input, rates of 0/1), output shapes and column names, and a regression test for every bug you fix.
- **Simulation-based tests:** simulate data with a known effect and check that your analysis function recovers it (e.g. a mixed model returns the simulated slope within tolerance).

## Version control with Git (short)
RStudio has a Git pane (commit, push, diff). Commit code, `renv.lock`, Quarto files and small metadata; keep large raw data out of git. Tag the commit used for a submission ([[CS13 Reproducibility and Research Software]], [[MAT12 MATLAB Reproducible Projects]]).

## Same idea in Python and MATLAB
Python: project root + `pathlib`, `requirements.txt`/`environment.yml`/lock files, pytest ([[Py13 Python Reproducible Projects and Testing]]). MATLAB: MATLAB Projects, `fullfile`, `matlab.unittest` ([[MAT12 MATLAB Reproducible Projects]]).

## In neuroscience #neuro
- **Statistics are software-version dependent:** lme4 optimiser defaults, emmeans df methods and brms/Stan versions can change results slightly → renv lockfile + `sessionInfo()` in the supplement.
- **Shared lab analyses:** a project template with `here`, renv and a `README` lets new lab members run the pipeline on day one.
- **Peer review / data papers:** an archived project (OSF/Zenodo DOI) with `renv.lock` and a Quarto report regenerates every figure.
- **Tests for custom metrics** (d′, ISI statistics, ERP window means) catch silent errors before they reach the paper.

## Math links #math-link
- Known analytical results as test cases (e.g. $d' = 0$ for equal rates; $z(0.84)\approx1$) → [[CS02 Probability and Statistics]]
- Float tolerance → [[Prog00 Shared Programming Concepts]]

## Connections
- Paths and seeds → [[Prog00 Shared Programming Concepts]]
- Reports → [[R10 R Markdown and Quarto]]
- Principles → [[CS13 Reproducibility and Research Software]]
- Same in other languages → [[Py13 Python Reproducible Projects and Testing]], [[MAT12 MATLAB Reproducible Projects]]

## Key takeaways
- RStudio Project + `here()` paths; never `setwd()` to absolute paths.
- `renv::init()`, `snapshot()`, `restore()`; commit `renv.lock`.
- testthat: `test_that()` + `expect_*()`; test known values, edge cases and fixed bugs.
- Report `sessionInfo()`; tag the git commit of a submission.
