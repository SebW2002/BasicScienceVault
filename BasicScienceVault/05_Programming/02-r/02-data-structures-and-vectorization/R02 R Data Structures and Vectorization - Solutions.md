---
tags: [programming, r, type/solution]
---
# R02 R Data Structures and Vectorization – Solutions

> Worksheet: [[R02 R Data Structures and Vectorization - Worksheet]] · Theory: [[R02 R Data Structures and Vectorization]] · Wrong? → [[Mistakes - R]]

## Level 1
1. `10 15`; `10 15`; `10 15 20`; `5 15` (logical index recycled: TRUE, FALSE, TRUE, FALSE).
2. `"1" "2" "TRUE"` (character). `1 1 0` (numeric; TRUE → 1).
3. ```text
        [,1] [,2]
   [1,]    1    4
   [2,]    2    5
   [3,]    3    6
   ```
   `M[2, ]` = `2 5`; `dim(M)` = `3 2`.
4. `1 2 3`; `"Cz"`; `"list"`; `"integer"`.

## Level 2
5. `1 -2 3 -4`. `11 22 13` **with a warning** (3 is not a multiple of 2).
6. `FALSE TRUE FALSE NA`; `NA`; `1`; `0.75`.
7. `y <- log(x) * 10`
8. `0.1 0.5 NA`

## Level 3
9. `M` = rows (1, 3, 5) and (2, 4, 6): `apply(M, 1, sum)` = `9 12`; `apply(M, 2, max)` = `2 4 6`.
10. `lapply` → a **list** of 3 elements (1, 4, 9); `sapply` → simplified to a **numeric vector** `1 4 9`.
11. `map_dbl(dfs, \(d) mean(d$rt, na.rm = TRUE))`

## Level 4
12. ```r
    isi <- diff(st)          # 0.03 0.12 0.06 0.15
    mean(isi)                # 0.09
    sd(isi) / mean(isi)      # CV ≈ 0.61
    ```
    (SD with n − 1: deviations −0.06, 0.03, −0.03, 0.06 → squares sum 0.009 → var 0.003 → SD ≈ 0.0548 → CV ≈ 0.61.)
13. `bl` is recycled: `bl[1], bl[2], bl[3], bl[1], …` is subtracted from trials 1–7 regardless of which condition they belong to, with only a warning (7 is not a multiple of 3). With 6 or 9 trials there'd be **no warning at all**. Match baselines by condition explicitly: `vals - bl[cond]` (with `cond` a factor/integer index) or a join.
14. ```r
    set.seed(1)
    df <- data.frame(subject = rep(c("01", "02", "03"), each = 2),
                     cond = rep(c("face", "house"), times = 3),
                     rt = rnorm(6, 0.5, 0.1))
    tapply(df$rt, df$cond, mean)
    sapply(split(df$rt, df$subject), mean)
    ```
