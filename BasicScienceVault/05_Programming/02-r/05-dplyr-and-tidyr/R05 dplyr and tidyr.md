---
aliases: [dplyr, tidyr, filter select mutate summarise, group_by, pivot_longer, pivot_wider, Joins in R]
tags: [programming, r, tidyverse, tidy-data, type/overview, neuro]
---
# R05 dplyr and tidyr

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R05 dplyr and tidyr - Worksheet|✏️ Worksheet]] · [[R05 dplyr and tidyr - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
**dplyr** (transform) and **tidyr** (reshape) turn raw trial tables into the summaries and model inputs you need, with a small set of verbs that read like sentences: *filter the valid trials, group by subject and condition, summarise the mean RT*. This is the R counterpart of pandas ([[Py06 pandas and Tabular Data]]).

## The five core verbs
Every verb takes a data frame as first argument and returns a data frame – which makes them perfect for pipes ([[R04 R Data Import and Tidy Data]]).
```r
library(dplyr)
trials |>
  filter(!is.na(rt), rt > 0.15, rt < 2) |>          # rows (comma = AND)
  select(subject, condition, rt, correct) |>          # columns
  mutate(rt_ms = rt * 1000,                           # new / changed columns
         log_rt = log(rt)) |>
  group_by(subject, condition) |>                     # define groups
  summarise(mean_rt = mean(rt), acc = mean(correct),  # one row per group
            n = n(), .groups = "drop")
```
| Verb | Does | Notes |
|---|---|---|
| `filter()` | keep rows that match | rows where the condition is `NA` are **dropped** |
| `select()` | keep/reorder/rename columns | helpers: `starts_with("rt")`, `where(is.numeric)`, `-col` to drop |
| `mutate()` | add or modify columns (vectorised) | can use columns created earlier in the same call |
| `summarise()` | reduce each group to one row | `n()`, `mean`, `sd`, `median`, `quantile`, `first` |
| `group_by()` | split for the next operation | `ungroup()` or `.groups = "drop"` afterwards |
More: `arrange(desc(rt))`, `distinct()`, `count(condition)`, `rename()`, `relocate()`, `slice_max(rt, n = 3)`, `across(c(rt, acc), mean)`, `case_when()`, `if_else()`, `lag()`/`lead()`.

### group_by + mutate: within-group operations
```r
trials |>
  group_by(subject) |>
  mutate(rt_z = (rt - mean(rt)) / sd(rt),        # z-score within subject
         outlier = abs(rt_z) > 3,
         trial_in_block = row_number()) |>
  ungroup()
```
With `group_by`, `summarise` reduces groups; `mutate` keeps all rows but computes per group (like pandas `transform`). Since dplyr 1.1 you can also write `mutate(..., .by = subject)` without a separate `group_by`.

## pivot_longer and pivot_wider (tidyr)
```r
library(tidyr)
# wide: subject, Fz, Cz, Pz  →  long: subject, electrode, amp
long <- wide |> pivot_longer(cols = c(Fz, Cz, Pz), names_to = "electrode", values_to = "amp")
# columns like rt_face, rt_house, acc_face, acc_house → several variables in names
long <- wide |> pivot_longer(-subject, names_to = c(".value", "condition"), names_sep = "_")
#   → subject, condition, rt, acc
# long → wide (e.g. for a paired difference)
wide <- summary |> pivot_wider(id_cols = subject, names_from = condition, values_from = mean_rt) |>
  mutate(diff = face - house)
```
Also: `separate_wider_delim()` (split one column into several), `unite()`, `drop_na()`, `complete()` (make implicit missing combinations explicit), `fill()`.

## Joins
```r
participants <- read_tsv("participants.tsv")      # participant_id, age, group
trials |> left_join(participants, by = c("subject" = "participant_id"))
# dplyr ≥ 1.1: by = join_by(subject == participant_id)
```
| Join | Keeps |
|---|---|
| `left_join(x, y)` | all rows of `x`; `NA` where `y` has no match |
| `inner_join(x, y)` | only rows with a match in both |
| `full_join(x, y)` | all rows of both |
| `semi_join(x, y)` | rows of `x` that have a match (no columns added) – filtering |
| `anti_join(x, y)` | rows of `x` **without** a match – finding problems |
- **Check keys:** duplicated keys in `y` multiply rows. dplyr warns about many-to-many matches; use `relationship = "many-to-one"` to make it an error. Compare `nrow()` before and after.
- `anti_join(trials, participants)` shows trials whose subject is missing from the participant table – typos in IDs.

## Same idea in Python and MATLAB
| dplyr / tidyr | pandas | MATLAB |
|---|---|---|
| `filter` | `df[mask]`, `query` | `T(mask, :)` |
| `select` | `df[[cols]]` | `T(:, cols)` |
| `mutate` | `assign`, `df["x"] = …` | `T.x = …` |
| `group_by + summarise` | `groupby().agg()` | `groupsummary` |
| `group_by + mutate` | `groupby().transform()` | `grouptransform` |
| `pivot_longer` / `pivot_wider` | `melt` / `pivot` | `stack` / `unstack` |
| `left_join` | `merge(how="left")` | `outerjoin(..., "Type", "left")` |

## In neuroscience #neuro
- **Trial exclusion and summary** per subject and condition – the first step of almost every behavioural analysis; report `n()` after exclusion.
- **Within-subject z-scores** remove overall speed differences between participants.
- **ERP amplitudes** from Python in wide format (one column per electrode) → `pivot_longer` → mixed model with electrode as factor ([[R08 R Mixed-Effects Models]]).
- **Joining** trial data with participants (age, group, handedness) and with session information (time of day, medication).
- **Sequential effects:** `lag(correct)` gives the previous trial's outcome (post-error slowing).

## Math links #math-link
- Group means, SDs, z-scores → [[A7 Sums Products and Factorials]], [[CS02 Probability and Statistics]]
- Joins as relational set operations (inner = ∩, full = ∪, anti = difference) → [[E1 Sets Logic and Quantifiers]]
- Log-transformed RTs → [[B3 Logarithmic Functions]]

## Connections
- Tidy data and pipes → [[R04 R Data Import and Tidy Data]]
- Plotting the results → [[R06 ggplot2 Visualization]]
- Models → [[R07 R Statistical Modelling]], [[R08 R Mixed-Effects Models]]
- pandas equivalent → [[Py06 pandas and Tabular Data]]
- Outliers, missing data → [[CS06 Data Science Workflow]]

## Key takeaways
- `filter` rows, `select` columns, `mutate` new columns, `group_by` + `summarise` per group.
- `group_by` + `mutate` for within-group operations; `ungroup()` afterwards.
- `pivot_longer` to tidy, `pivot_wider` for paired/wide views.
- `left_join` most common; check keys and row counts; `anti_join` finds mismatches.
