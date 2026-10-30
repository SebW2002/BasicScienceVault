---
tags: [programming, r, type/solution]
---
# R03 R Control Flow and Functions – Solutions

> Worksheet: [[R03 R Control Flow and Functions - Worksheet]] · Theory: [[R03 R Control Flow and Functions]] · Wrong? → [[Mistakes - R]]

## Level 1
1. 1 + 2 + 4 + 5 = **12** (3 and 6 skipped).
2. `9`, `27`, `1`.
3. `length(x)` is 0, so `1:0` = `c(1, 0)`: prints `1` and `0` (loop runs twice on an empty vector). Use `seq_along(x)` → loop doesn't run.
4. Error: "the condition has length > 1".

## Level 2
5. `NA`; `2`; `2 NA 5` (NA kept!); `2 5`; `1`.
6. Error "missing value where TRUE/FALSE needed". Safe: `if (!is.na(rt) && rt > 2) print("slow")` (`&&` short-circuits, so `rt > 2` isn't evaluated when `rt` is NA).
7. 28 rows had `NA` in `rt` or `cond` and were dropped silently by `na.omit`. Report this; check whether missingness differs by condition.

## Level 3
8. ```r
   dprime <- function(hit_rate, fa_rate) qnorm(hit_rate) - qnorm(fa_rate)
   ```
   $z(0.84)\approx1$, $z(0.16)\approx-1$ → $d'\approx2$. (Rates of exactly 0 or 1 give ±Inf: apply a correction such as $(h + 0.5)/(n + 1)$.)
9. ```r
   summarise_rt <- function(x, ...) list(mean = mean(x, ...), sd = sd(x, ...))
   summarise_rt(c(0.4, NA, 0.6), na.rm = TRUE)   # mean 0.5, sd 0.141
   ```
10. Copy-on-modify: the function changes a local copy and returns the value of the assignment (invisibly, the vector), not the data frame; the caller's `df` is unchanged. Fix: end with `df` and assign: `df <- add_column(df)`.

## Level 4
11. ```r
    results <- vector("list", length(files))
    for (i in seq_along(files)) {
      results[[i]] <- tryCatch(read.csv(files[i]),
                               error = function(e) { message(files[i], ": ", conditionMessage(e)); NULL })
    }
    ```
12. ```r
    library(dplyr)
    df <- df |> mutate(outcome = case_when(
      is.na(rt)  ~ "miss",
      rt < 0.15  ~ "anticipation",
      rt > 2     ~ "slow",
      .default   = "valid"))
    ```
    Order matters: the `is.na` test comes first.
13. ```r
    set.seed(1)
    p <- replicate(1000, t.test(rnorm(20, 0.5), rnorm(20, 0))$p.value)
    mean(p < 0.05)    # ≈ 0.33
    ```
    Only about one in three studies of this size would detect a true medium effect ([[CS06 Data Science Workflow]]).
