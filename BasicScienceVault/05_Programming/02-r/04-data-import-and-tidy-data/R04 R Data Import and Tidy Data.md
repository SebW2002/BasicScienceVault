---
aliases: [R Data Import, readr, readxl, RDS, Parquet, Tidy Data, Pipe Operator]
tags: [programming, r, tidy-data, data-format, tidyverse, type/overview, neuro]
---
# R04 R Data Import and Tidy Data

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R04 R Data Import and Tidy Data - Worksheet|✏️ Worksheet]] · [[R04 R Data Import and Tidy Data - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
Statistics in R starts with getting data **in** (from PsychoPy CSVs, Excel sheets, Python exports) and getting it into **tidy** shape – one row per observation. Almost every function in the tidyverse, ggplot2 and lme4 expects tidy data. The **pipe** then lets you write analyses as readable chains of steps.

## Reading and writing files
| Format | Read | Write | Notes |
|---|---|---|---|
| CSV | `readr::read_csv("f.csv")`; base `read.csv()` | `write_csv(df, "f.csv")` | `read_csv2()` for `;` and decimal commas (German Excel) |
| TSV | `read_tsv()` | `write_tsv()` | BIDS `events.tsv`, `participants.tsv` |
| Excel | `readxl::read_excel("f.xlsx", sheet = "RT")` | `writexl::write_xlsx()` | read-only package, no Excel needed |
| RDS | `readRDS("f.rds")` | `saveRDS(obj, "f.rds")` | **any R object** (fitted models, factors with levels); R-only |
| Parquet | `arrow::read_parquet("f.parquet")` | `arrow::write_parquet()` | columnar, compressed, typed, fast; readable from Python (pandas) |
| SPSS/Stata | `haven::read_sav()`, `read_dta()` | | questionnaire data |
| `.mat`, HDF5 | `R.matlab::readMat()`, `rhdf5::h5read()` | | → [[R09 R Neuroscience Packages]] |
```r
library(readr)
df <- read_csv("data/raw/sub-01_task-faces.csv",
               col_types = cols(subject = col_character(), rt = col_double()),
               na = c("", "NA", "None"))     # PsychoPy writes "None" for misses
spec(df); problems(df)                        # how columns were parsed; parsing problems
```
- `readr` functions return **tibbles**, show the guessed column types, and don't turn strings into factors.
- **Specify `col_types`** for important columns (subject IDs as character keep leading zeros "01").
- Many files: `files <- list.files("data/raw", pattern = "_task-faces\\.csv$", full.names = TRUE)`, then `read_csv(files, id = "file")` reads and stacks them all, keeping the file name.
- **RDS vs. CSV:** RDS keeps types and factor levels exactly, but only R can read it; for exchange use CSV/TSV or Parquet.

## The tidy data principle
> Each **variable** is a column, each **observation** is a row, each type of observational unit is a table. (Wickham, 2014)

**Not tidy (wide):**
| subject | rt_face | rt_house |
|---|---|---|
| 01 | 0.45 | 0.52 |

**Tidy (long):**
| subject | condition | rt |
|---|---|---|
| 01 | face | 0.45 |
| 01 | house | 0.52 |
- Condition is a **variable**, so it belongs in a column, not in column names.
- Common untidy patterns: values in column names (`rt_face`), several variables in one column (`"face_left"`), one variable spread over several columns, several observational units in one table (trial data repeated with participant info on every row is fine for analysis but stored separately).
- Converting between long and wide → `pivot_longer` / `pivot_wider` ([[R05 dplyr and tidyr]]).
- The concept, also for Python and metadata → [[CS05 Data Formats and Representation]].

## The pipe: |> and %>%
```r
# nested – read from the inside out
summarise(group_by(filter(df, rt > 0.15), condition), m = mean(rt))
# piped – read from top to bottom: "then …"
df |>
  filter(rt > 0.15) |>
  group_by(condition) |>
  summarise(m = mean(rt))
```
- `x |> f(y)` means `f(x, y)`: the left side becomes the **first argument**.
- `|>` is the **native pipe** (R ≥ 4.1, no package needed); `%>%` comes from **magrittr** (loaded by the tidyverse). They are nearly identical for everyday use. Differences: `%>%` allows the placeholder `.` anywhere (`df %>% lm(rt ~ cond, data = .)`); `|>` uses `_` only for **named** arguments (`df |> lm(rt ~ cond, data = _)`, R ≥ 4.2); `|>` is slightly faster and needs no dependency.
- RStudio shortcut **Ctrl/Cmd + Shift + M** inserts a pipe (choose `|>` in the options).
- Keep pipes to one logical task (5–10 steps); assign intermediate results with clear names.

## Same idea in Python and MATLAB
pandas `read_csv`, `read_excel`, `read_parquet`; method chaining `df.query(...).groupby(...).agg(...)` is Python's pipe ([[Py06 pandas and Tabular Data]]). MATLAB `readtable`, `parquetread` ([[MAT04 MATLAB Data Import and Files]]).

## In neuroscience #neuro
- **PsychoPy output** (one CSV per participant, wide trial rows) → `read_csv(files, id = "file")` → tidy trial table ([[Py11 PsychoPy Experiment Control]]).
- **Exports from Python:** ERP amplitudes per subject × condition × electrode written as CSV/Parquet from MNE, read into R for mixed models ([[R08 R Mixed-Effects Models]]).
- **BIDS** `participants.tsv` (age, sex, group) joined with trial data by `participant_id` ([[R05 dplyr and tidyr]]).
- **Questionnaires** from REDCap/SPSS with `haven`.

## Math links #math-link
- Tidy data as a relation: rows = tuples, columns = attributes → [[E1 Sets Logic and Quantifiers]]
- Function composition $h(g(f(x)))$ written left to right with pipes → [[B1 Properties of Functions]]

## Connections
- Data structures, data frames → [[R02 R Data Structures and Vectorization]]
- Transforming tidy data → [[R05 dplyr and tidyr]]; plotting → [[R06 ggplot2 Visualization]]
- Formats and tidy data in general → [[CS05 Data Formats and Representation]]
- Python equivalent → [[Py04 Python Files and Data Formats]], [[Py06 pandas and Tabular Data]]

## Key takeaways
- `readr::read_csv` / `read_tsv` (specify `col_types`, `na`), `readxl` for Excel, `saveRDS` for R objects, Parquet for fast typed exchange.
- Tidy: variables in columns, observations in rows; condition belongs in a column.
- `x |> f(y)` = `f(x, y)`; `|>` native, `%>%` magrittr; placeholders `_` vs. `.`.
