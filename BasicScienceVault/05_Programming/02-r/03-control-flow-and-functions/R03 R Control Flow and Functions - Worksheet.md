---
tags: [programming, r, type/worksheet]
---
# R03 R Control Flow and Functions – Worksheet

> Theory: [[R03 R Control Flow and Functions]] · Solutions: [[R03 R Control Flow and Functions - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Predict the output
1. ```r
   total <- 0
   for (i in 1:6) {
     if (i %% 3 == 0) next
     total <- total + i
   }
   total
   ```
2. `f <- function(x, k = 2) x^k; f(3); f(3, 3); f(k = 0, x = 5)`
3. `x <- c(); for (i in 1:length(x)) print(i)` – what is printed? Why?
4. `if (c(TRUE, FALSE)) "yes"` – what happens in R ≥ 4.2?

## Level 2 – NA
5. `x <- c(2, NA, 5, -1)`: `mean(x)`, `mean(x, na.rm = TRUE)`, `x[x > 0]`, `x[which(x > 0)]`, `sum(is.na(x))`
6. `rt <- NA; if (rt > 2) print("slow")` – what happens? Rewrite safely.
7. A model `lm(rt ~ cond, data = df)` has 480 rows but `nobs()` returns 452. What happened?

## Level 3 – Write functions
8. Write `dprime(hit_rate, fa_rate)` returning $z(H) - z(FA)$ with `qnorm`. Compute $d'$ for H = 0.84, FA = 0.16 ($z(0.84)\approx1$).
9. Write `summarise_rt(x, ...)` that returns a list with the mean and SD of `x`, passing `...` (e.g. `na.rm = TRUE`) to both.
10. Find the bug:
    ```r
    add_column <- function(df) {
      df$rt_ms <- df$rt * 1000
    }
    add_column(df); head(df$rt_ms)
    ```

## Level 4 – Neuro transfer
11. Write a loop over `files` that reads each CSV, catches errors with `tryCatch`, and stores the results in a pre-allocated list.
12. Classify trial outcomes vectorised: `rt` NA → "miss", < 0.15 → "anticipation", > 2 → "slow", else "valid". Use `dplyr::case_when()`.
13. 💻 Simulate a power analysis: for `n` = 20 per group and a true difference of 0.5 SD, run 1000 simulated t-tests (`set.seed(1)`) and estimate the power as the proportion of p < 0.05. (Expected ≈ 0.33.)
