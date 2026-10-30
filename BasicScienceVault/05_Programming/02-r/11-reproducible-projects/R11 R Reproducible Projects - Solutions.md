---
tags: [programming, r, reproducibility, type/solution]
---
# R11 R Reproducible Projects – Solutions

> Worksheet: [[R11 R Reproducible Projects - Worksheet]] · Theory: [[R11 R Reproducible Projects]] · Wrong? → [[Mistakes - R]]

## Level 1
1. Starts a fresh R session with the working directory set to the project folder, restores project settings and open files, and (with renv) activates the project library.
2. `"/home/anna/study/data/raw/a.csv"`.
3. `renv::init()`, `renv::snapshot()`, `renv::restore()`.
4. In git: `renv.lock`, `.Rprofile`, `renv/activate.R` (and `renv/settings.json`). Not: `renv/library/` (installed packages; rebuilt from the lockfile).

## Level 2
5. During rendering, the working directory is the folder of the `.qmd` file (`reports/`), so the relative path points to `reports/data/derived/rt.csv`. Fix: `read_csv(here("data", "derived", "rt.csv"))`.
6. Different package versions (lme4/optimiser defaults, Matrix) and/or a different R version; also an unset random seed in simulation-based steps. renv restores the exact package versions from the lockfile; `sessionInfo()` in the report documents what was used, so differences can be traced.
7. renv pins R packages, not R itself, system libraries (BLAS/LAPACK, compilers, GDAL) or the operating system – these can change numerical results. A container (Docker/Apptainer, e.g. rocker) pins all of it.
8. `expect_equal(0.1 + 0.2, 0.3)` passes (uses a numerical tolerance); `expect_identical` fails (the floats differ in the last bits).

## Level 3
9. ```r
   test_that("regular spike train has CV 0", {
     expect_equal(cv_isi(seq(0, 1, by = 0.1)), 0)
   })
   test_that("too few spikes give an error", {
     expect_error(cv_isi(c(0.1, 0.5)))
   })
   ```
10. ```r
    test_that("zscore standardises and keeps NA", {
      x <- c(1, 4, NA, 9, 16)
      z <- zscore(x)
      expect_equal(mean(z, na.rm = TRUE), 0)
      expect_equal(sd(z, na.rm = TRUE), 1)
      expect_identical(is.na(z), is.na(x))
    })
    ```
11. It tests nothing: `expect_true(TRUE)` always passes; the test only fails if `lmer` throws an error. Test something meaningful, e.g. simulate data with a known effect and `expect_equal(unname(fixef(m)["condB"]), 0.05, tolerance = 0.02)`.

## Level 4
12. - Purpose and design of the study, link to the paper/preregistration
    - Where to get the data (OpenNeuro/OSF ID) and where to put them (`data/raw/`, BIDS)
    - Requirements: R version, `renv::restore()`; Python environment for preprocessing (`environment.yml`)
    - Run order: `scripts/01_preprocess.py` → `scripts/02_extract.R` → `reports/analysis.qmd` (or one `make`/`targets::tar_make()` command)
    - Which script/chunk produces Figure 2, expected runtime
    - Random seeds, licence, contact, how to cite
13. ```r
    usethis::create_project("dprime-test"); renv::init()
    # write R/dprime.R and tests/testthat/test-dprime.R as in the note
    source("R/dprime.R"); testthat::test_dir("tests/testthat")   # all pass
    # bug: qnorm(fa) - qnorm(hit)  → the symmetry test still passes (both sides flip!),
    # the "zero for equal rates" test passes too – only a test with a known value catches it:
    # expect_equal(dprime(0.84, 0.16), 1.989, tolerance = 1e-3)
    ```
    Lesson: tests of properties (symmetry, zero) can miss sign errors; include at least one test against a **known value**.
