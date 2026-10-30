---
tags: [programming, r, reproducibility, type/worksheet]
---
# R11 R Reproducible Projects – Worksheet

> Theory: [[R11 R Reproducible Projects]] · Solutions: [[R11 R Reproducible Projects - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Recall
1. What does opening an `.Rproj` file do?
2. What does `here("data", "raw", "a.csv")` return in a project at `/home/anna/study`?
3. Name the three renv functions for initialising, recording and recreating an environment.
4. Which files of an renv project go into git, which not?

## Level 2 – Understanding
5. Your Quarto report in `reports/analysis.qmd` reads `read_csv("data/derived/rt.csv")` and fails on render, though the same line works in the console. Why? Fix.
6. A colleague runs your code a year later and gets slightly different mixed-model estimates. Name two likely causes and how renv/`sessionInfo()` help.
7. Why doesn't renv fully guarantee reproducibility? What else would you need?
8. What's the difference between `expect_equal` and `expect_identical` for `0.1 + 0.2` vs `0.3`?

## Level 3 – Write tests
9. Write testthat tests for `cv_isi(spike_times)` (coefficient of variation of ISIs): a perfectly regular spike train gives 0; fewer than 3 spikes gives an error.
10. Write a test that `zscore(x)` returns a vector with mean 0 and SD 1 (within tolerance) and keeps `NA` at the same positions.
11. Find the problem with this test: `test_that("model works", { m <- lmer(rt ~ cond + (1|subj), d); expect_true(TRUE) })`.

## Level 4 – Neuro transfer
12. Draft a README (bullet points) for an EEG analysis project so that a new lab member can reproduce Figure 2.
13. 💻 Create an RStudio Project with `renv::init()`, write `R/dprime.R` and `tests/testthat/test-dprime.R` from the note, and run the tests. Then add a bug (swap the arguments) and watch which test fails.
