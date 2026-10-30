---
tags: [programming, r, type/worksheet]
---
# R01 R Basics and Syntax – Worksheet

> Theory: [[R01 R Basics and Syntax]] · Solutions: [[R01 R Basics and Syntax - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Predict the output
1. `typeof(5)`, `typeof(5L)`, `typeof(1:3)`, `class("Cz")`, `typeof(TRUE)`
2. `7 %/% 2`, `7 %% 2`, `2^3`, `0/0`, `1/0`
3. `x <- c(10, 20, 30); x[1]; x[3]; x[-1]; length(x)`
4. `NA > 1`, `NA == NA`, `is.na(NA)`, `NULL` vs. `NA` – what's the difference?

## Level 2 – Syntax and help
5. What is the difference between `mean(x, na.rm = TRUE)` and `mean(x, na.rm <- TRUE)`?
6. How do you find out which variant of the t-test `t.test()` computes by default?
7. What does `library(lme4)` do compared to `lme4::lmer()`?
8. Why is it risky to write `T` instead of `TRUE`?

## Level 3 – Factors
9. `cond <- factor(c("house", "face", "face", "scrambled"))`. What are `levels(cond)` and `as.integer(cond)`?
10. Make `"scrambled"` the reference level. Why does this matter for a regression `lm(rt ~ cond)`?
11. `snr <- factor(c("10", "5", "20"))`. What does `as.numeric(snr)` return? What's the correct conversion?
12. Subject IDs are stored as numbers 1–30 and used in a model. What goes wrong? How do you fix it?

## Level 4 – Neuro transfer
13. A sleep data frame has a column `stage` with values W, N1, N2, N3, REM. Write the code to make it an ordered factor in this order and count epochs per stage.
14. 💻 Create a vector of 6 reaction times with one `NA`, compute the mean with and without `na.rm`, convert a condition vector to a factor with a chosen reference level, and inspect both with `str()`.
