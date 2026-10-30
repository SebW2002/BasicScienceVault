---
tags: [programming, r, type/solution]
---
# R01 R Basics and Syntax – Solutions

> Worksheet: [[R01 R Basics and Syntax - Worksheet]] · Theory: [[R01 R Basics and Syntax]] · Wrong? → [[Mistakes - R]]

## Level 1
1. `"double"`, `"integer"`, `"integer"`, `"character"`, `"logical"`.
2. `3`, `1`, `8`, `NaN`, `Inf`.
3. `10`, `30`, `20 30` (negative index removes element 1), `3`.
4. `NA`, `NA`, `TRUE`. `NA` is a missing value **inside** a vector (it has a length-1 slot); `NULL` means "no object at all" (length 0): `length(c(1, NA)) == 2`, `length(c(1, NULL)) == 1`.

## Level 2
5. The first passes the argument `na.rm` the value `TRUE`. The second **creates a variable** `na.rm` in your workspace and passes its value **positionally** as the second argument (`trim`) – a silent bug. Use `=` for arguments.
6. `?t.test`: the default is `var.equal = FALSE`, i.e. **Welch's** t-test.
7. `library()` attaches the whole package so you can call `lmer()` directly; `lme4::lmer()` calls one function without attaching (clear origin, no name clashes).
8. `T` and `F` are ordinary variables that can be overwritten (`T <- 0`), changing your code's meaning; `TRUE`/`FALSE` are reserved words.

## Level 3
9. Levels alphabetical: `"face" "house" "scrambled"`; codes `2 1 1 3`.
10. `cond <- relevel(cond, ref = "scrambled")` (or `factor(cond, levels = c("scrambled", "face", "house"))`). In `lm`, the intercept is the mean of the reference level and each coefficient is the difference of a level **from the reference**; with "scrambled" as reference you get face − scrambled and house − scrambled.
11. Levels alphabetical as strings: `"10" "20" "5"` → codes `1 3 2`, so `as.numeric(snr)` gives `1 3 2`. Correct: `as.numeric(as.character(snr))` → `10 5 20` (or `as.numeric(levels(snr))[snr]`).
12. The model treats subject as a continuous predictor (a linear trend over subject number) instead of 30 separate groups. Fix: `df$subject <- factor(df$subject)` – and in mixed models use it as a random effect ([[R08 R Mixed-Effects Models]]).

## Level 4
13. ```r
    sleep$stage <- factor(sleep$stage, levels = c("W", "N1", "N2", "N3", "REM"), ordered = TRUE)
    table(sleep$stage)
    ```
14. ```r
    rt <- c(0.45, 0.52, NA, 0.61, 0.39, 0.70)
    mean(rt)                 # NA
    mean(rt, na.rm = TRUE)   # 0.534
    cond <- factor(c("face", "house", "face", "house", "face", "house"))
    cond <- relevel(cond, ref = "house")
    str(rt); str(cond)       # num [1:6] ...;  Factor w/ 2 levels "house","face": 2 1 2 1 2 1
    ```
