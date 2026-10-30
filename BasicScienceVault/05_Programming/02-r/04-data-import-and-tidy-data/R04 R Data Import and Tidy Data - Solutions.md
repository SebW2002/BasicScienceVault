---
tags: [programming, r, type/solution]
---
# R04 R Data Import and Tidy Data – Solutions

> Worksheet: [[R04 R Data Import and Tidy Data - Worksheet]] · Theory: [[R04 R Data Import and Tidy Data]] · Wrong? → [[Mistakes - R]]

## Level 1
1. a) `read_csv2()` (or `read_delim(delim = ";", locale = locale(decimal_mark = ","))`) b) `read_tsv()` c) `readxl::read_excel(path, sheet = "RT")` d) `readRDS()` e) `arrow::read_parquet()`.
2. `saveRDS` stores the R object exactly (types, factor levels and their order, attributes) but only R can read it; `write_csv` writes plain text – factors become strings, levels/order are lost, but every program can read it.
3. The column was guessed as numeric, so leading zeros vanish. Use `col_types = cols(subject = col_character())`.

## Level 2
4. a) **Not tidy:** two variables (condition, measure) are encoded in the column names. b) **Tidy.** c) **Not tidy:** two variables in one column → `separate_wider_delim(cond_side, "_", names = c("cond", "side"))`. d) Tidy for analysis (each row is a trial; `age` is a subject-level variable repeated) – for storage, keep a separate participants table and join when needed.
5. `subject, condition, rt, acc` (one row per subject × condition) – or fully long `subject, condition, measure, value`.

## Level 3
6. `df$rt |> log() |> mean() |> round(2)`
7. The pipe puts `df` into the **first** argument of `lm`, which is `formula`. Correct: `df |> lm(rt ~ cond, data = _)` (R ≥ 4.2) or `lm(rt ~ cond, data = df)`; with magrittr `df %>% lm(rt ~ cond, data = .)`.
8. `f(x, y = 2)`

## Level 4
9. ```r
   library(readr)
   files <- list.files("data/raw", pattern = "^sub-\\d+_faces\\.csv$", full.names = TRUE)
   trials <- read_csv(files, id = "file", na = c("", "NA", "None"))
   ```
10. Long format with columns `subject, condition, electrode, amp` – electrode must be a variable (factor), not three columns. `pivot_longer(c(Fz, Cz, Pz), names_to = "electrode", values_to = "amp")`.
11. ```r
    library(readr); library(stringr); library(dplyr)
    write_csv(tibble(trial = 1:2, rt = c(0.4, 0.5)), "sub-01.csv")
    write_csv(tibble(trial = 1:2, rt = c(0.6, 0.7)), "sub-02.csv")
    d <- read_csv(c("sub-01.csv", "sub-02.csv"), id = "file") |>
      mutate(subject = str_extract(file, "sub-\\d+"))
    d   # 4 rows: file, trial, rt, subject
    ```
