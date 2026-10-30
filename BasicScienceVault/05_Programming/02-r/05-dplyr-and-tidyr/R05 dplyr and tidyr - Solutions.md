---
tags: [programming, r, tidyverse, type/solution]
---
# R05 dplyr and tidyr – Solutions

> Worksheet: [[R05 dplyr and tidyr - Worksheet]] · Theory: [[R05 dplyr and tidyr]] · Wrong? → [[Mistakes - R]]

## Level 1
1. **4** rows (0.42, 0.55, 0.48, 0.61): 0.10 fails, and the `NA` row is **dropped** (the condition is `NA`, not `TRUE`).
2. `face 3`, `house 3`.
3. `n = 6`, `m = (0.42 + 0.10 + 0.55 + 0.48 + 0.61)/5 = 2.16/5 = 0.432`.
4. Keeps all columns except `correct`.

## Level 2
5. face: rt 0.42, 0.48 → **m = 0.45**, acc = 1.0; house: 0.55, 0.61 → **m = 0.58**, acc = 0.5.
6. 4 rows: (01, face) 0.42, acc 1; (01, house) 0.55, acc 0; (02, face) 0.48, acc 1; (02, house) 0.61, acc 1.
7. `summarise` → 2 rows (one per subject); `mutate` → 6 rows (each row gets its subject's mean).
8. ```r
   trials |>
     group_by(subject) |>
     mutate(rt_z = (rt - mean(rt, na.rm = TRUE)) / sd(rt, na.rm = TRUE)) |>
     ungroup()
   ```

## Level 3
9. ```r
   wide |> pivot_longer(c(rt_face, rt_house), names_to = "condition",
                        names_prefix = "rt_", values_to = "rt")
   ```
10. ```r
    s |> pivot_wider(id_cols = subject, names_from = condition, values_from = m) |>
      mutate(diff = house - face)
    # 01: face 0.42, house 0.55, diff 0.13;  02: face 0.48, house 0.61, diff 0.13
    ```
11. `left_join`: **6** rows (subject 02's rows get `NA` for participant columns). `inner_join`: **3** rows (only subject 01). `anti_join`: **3** rows – subject 02's trials, which have no participant entry (→ fix IDs!).

## Level 4
12. ```r
    clean <- trials |>
      filter(!is.na(rt), between(rt, 0.15, 2)) |>
      group_by(subject) |>
      mutate(rt_z = (rt - mean(rt)) / sd(rt)) |>
      ungroup() |>
      filter(abs(rt_z) <= 3)
    clean |>
      filter(correct) |>
      summarise(mean_rt = mean(rt), n = n(), .by = c(subject, condition))
    ```
13. ```r
    trials |> group_by(subject, block) |> mutate(prev_correct = lag(correct)) |> ungroup()
    ```
    `lag()` shifts by one row. Without grouping, the first trial of subject 2 would get the last trial of subject 1 as its "previous" trial. Data must also be sorted by trial order (`arrange(subject, block, trial)`).
14. ```r
    library(dplyr); library(tidyr)
    trials <- tibble(subject = c("01","01","01","02","02","02"),
                     condition = c("face","face","house","face","house","house"),
                     rt = c(0.42, 0.10, 0.55, 0.48, NA, 0.61),
                     correct = c(TRUE, TRUE, FALSE, TRUE, FALSE, TRUE))
    nrow(filter(trials, rt > 0.15))
    trials |> filter(rt > 0.15) |> summarise(m = mean(rt), acc = mean(correct), .by = condition)
    s <- trials |> filter(rt > 0.15) |> summarise(m = mean(rt), acc = mean(correct), .by = c(subject, condition))
    s |> pivot_wider(id_cols = subject, names_from = condition, values_from = m) |> mutate(diff = house - face)
    ```
