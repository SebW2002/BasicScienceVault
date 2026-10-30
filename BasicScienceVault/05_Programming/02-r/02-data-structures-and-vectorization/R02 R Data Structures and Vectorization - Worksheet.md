---
tags: [programming, r, type/worksheet]
---
# R02 R Data Structures and Vectorization – Worksheet

> Theory: [[R02 R Data Structures and Vectorization]] · Solutions: [[R02 R Data Structures and Vectorization - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Predict the output
1. `x <- c(5, 10, 15, 20)`: `x[2:3]`, `x[-c(1, 4)]`, `x[x >= 10]`, `x[c(TRUE, FALSE)]`
2. `c(1, "2", TRUE)` – what type? `c(1, TRUE, FALSE)`?
3. `matrix(1:6, nrow = 3)` – write it out. What are `M[2, ]` and `dim(M)`?
4. `l <- list(a = 1:3, b = "Cz")`: `l$a`, `l[["b"]]`, `class(l["a"])`, `class(l[["a"]])`

## Level 2 – Vectorisation and recycling
5. `c(1, 2, 3, 4) * c(1, -1)`, `c(1, 2, 3) + c(10, 20)` – results, and does the second give a warning?
6. `rt <- c(0.3, 2.5, 0.6, NA)`: `rt > 1`, `sum(rt > 1)`, `sum(rt > 1, na.rm = TRUE)`, `mean(!is.na(rt))`
7. Rewrite without a loop: `for (i in seq_along(x)) y[i] <- log(x[i]) * 10`
8. `ifelse(c(0.1, 0.5, 2.4) > 2, NA, c(0.1, 0.5, 2.4))`?

## Level 3 – apply family
9. `M <- matrix(1:6, nrow = 2)`: `apply(M, 1, sum)` and `apply(M, 2, max)`?
10. What do `lapply(1:3, \(i) i^2)` and `sapply(1:3, \(i) i^2)` return (types)?
11. Write `map_dbl` code that gives the mean RT of each data frame in a list `dfs`.

## Level 4 – Neuro transfer
12. Spike times (s) `st <- c(0.05, 0.08, 0.20, 0.26, 0.41)`. Compute ISIs, mean ISI, CV (write code and the ISIs).
13. You have 3 conditions with baselines `bl <- c(0.1, 0.2, 0.3)` and a vector of 7 trial values. You write `vals - bl`. What happens and why is it dangerous?
14. 💻 Create a data frame of 3 subjects × 2 conditions with random RTs (`set.seed(1)`; `rnorm(6, 0.5, 0.1)`), compute the mean RT per condition with `tapply`, and per subject with `sapply(split(df$rt, df$subject), mean)`.
