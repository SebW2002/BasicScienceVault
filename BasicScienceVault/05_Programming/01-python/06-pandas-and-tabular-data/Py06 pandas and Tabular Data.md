---
aliases: [pandas, DataFrame, Series, groupby, merge, pivot, DatetimeIndex, resample]
tags: [programming, python, pandas, tidy-data, type/overview, neuro]
---
# Py06 pandas and Tabular Data

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py06 pandas and Tabular Data - Worksheet|✏️ Worksheet]] · [[Py06 pandas and Tabular Data - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
Behavioural data, trial tables, participant information, event files, spike-sorting summaries – most data **around** a recording are tables. pandas gives Python what R has with data frames and dplyr ([[R05 dplyr and tidyr]]): labelled columns of different types, filtering, grouping, joining and reshaping.

## DataFrame and Series
```python
import pandas as pd
df = pd.DataFrame({
    "subject":   ["01", "01", "02", "02"],
    "condition": ["face", "house", "face", "house"],
    "rt":        [0.45, 0.52, 0.48, None],
})
df.shape; df.dtypes; df.head(); df.describe()
df["rt"]                  # a Series (one column with the index)
df[["subject", "rt"]]     # a DataFrame (list of columns)
```
- A **Series** = 1-d labelled array; a **DataFrame** = dict of Series sharing one **index** (row labels).
- Each column has one dtype; text columns are `str`/`object`; use `category` for factors with few levels.
- `.loc[rows, cols]` selects **by label**, `.iloc[rows, cols]` **by position** (0-based, end-exclusive):
  `df.loc[df["rt"] > 0.5, "subject"]`, `df.iloc[0:2, 1]`.

## Filtering, new columns, sorting
```python
valid = df[(df["rt"] > 0.15) & (df["rt"] < 2)]          # Boolean mask, & | ~
faces = df.query("condition == 'face' and rt < 0.5")    # same, as a string
df["rt_ms"] = df["rt"] * 1000                            # vectorised new column
df = df.assign(log_rt=lambda d: np.log(d["rt"]))         # chainable
df.sort_values(["subject", "rt"], ascending=[True, False])
```
- **Copy-on-Write** (default since pandas 3.0): every selection behaves like a copy. Chained assignment `df[df.rt > 1]["rt"] = np.nan` **does nothing** – always assign with one `.loc`: `df.loc[df["rt"] > 1, "rt"] = np.nan`.

## groupby: split – apply – combine
```python
df.groupby("condition")["rt"].mean()
df.groupby(["subject", "condition"])["rt"].agg(["mean", "std", "count"])
summary = (df.groupby(["subject", "condition"], as_index=False)
             .agg(mean_rt=("rt", "mean"), n=("rt", "size")))
df["rt_z"] = df.groupby("subject")["rt"].transform(lambda x: (x - x.mean()) / x.std())
```
`agg` reduces each group to one row; `transform` returns a result with the **original** shape (within-subject z-scores).

## merge, concat, pivot
```python
participants = pd.DataFrame({"subject": ["01", "02"], "age": [24, 31]})
df = df.merge(participants, on="subject", how="left")   # join like SQL
all_subj = pd.concat([df1, df2], ignore_index=True)     # stack rows
wide = summary.pivot(index="subject", columns="condition", values="mean_rt")
long = wide.reset_index().melt(id_vars="subject", var_name="condition", value_name="mean_rt")
```
| `how` | keeps |
|---|---|
| `inner` | only keys in both tables |
| `left` | all rows of the left table (NaN where no match) |
| `outer` | all keys of both |
Check row counts after a merge: **duplicated keys multiply rows**. `validate="many_to_one"` catches this.

**Long vs. wide:** long ("tidy") = one row per observation, needed for groupby, seaborn and mixed models; wide = one row per subject, conditions as columns, for paired comparisons ([[R04 R Data Import and Tidy Data]], [[CS05 Data Formats and Representation]]).

## Missing values
```python
df.isna().sum()                    # missing per column
df.dropna(subset=["rt"])           # drop rows with missing rt
df["rt"].fillna(df["rt"].median()) # impute (think first!)
df["rt"].mean()                    # skips NaN by default (skipna=True)
```
pandas **skips** NaN in aggregations by default, NumPy does not ([[Prog00 Shared Programming Concepts]]). Count non-missing values with `.count()`, all rows with `.size`.

## Time series: DatetimeIndex and resample
```python
ts = pd.read_csv("wheel.csv", parse_dates=["time"]).set_index("time")
ts.loc["2026-03-01 10:00":"2026-03-01 10:05"]     # slice by time
ts["speed"].resample("1s").mean()                  # downsample to 1 s bins
ts["speed"].rolling("500ms").mean()               # moving average
pd.to_timedelta(df["onset"], unit="s")            # durations
```
For regularly sampled physiological signals use NumPy/MNE with a sampling rate; pandas time indices shine for **irregular, wall-clock** data: behaviour logs, wearables, sleep scoring, multi-day experiments.

## Same idea in R and MATLAB
| pandas | dplyr / tidyr | MATLAB table |
|---|---|---|
| `df[mask]`, `query` | `filter()` | `T(T.rt > 0.15, :)` |
| `df[["a","b"]]` | `select()` | `T(:, ["a" "b"])` |
| `assign` | `mutate()` | `T.new = ...` |
| `groupby().agg()` | `group_by() \|> summarise()` | `groupsummary` |
| `merge` | `left_join()` | `join`, `outerjoin` |
| `melt` / `pivot` | `pivot_longer` / `pivot_wider` | `stack` / `unstack` |
| `resample` | `lubridate` + `summarise` | `timetable`, `retime` |
→ [[R05 dplyr and tidyr]], [[MAT04 MATLAB Data Import and Files]]

## In neuroscience #neuro
- **BIDS `events.tsv`** → DataFrame with `onset`, `duration`, `trial_type`; convert to sample indices for epoching ([[Py10 Python Neuroscience Packages]]).
- **Trial-level behaviour** in long format → mixed models with `statsmodels` or R/lme4 ([[R08 R Mixed-Effects Models]]).
- **Spike-sorting output** (`nwb.units.to_dataframe()`): filter units by quality metrics (`isi_violations < 0.5`, `firing_rate > 0.1`).
- **Merging** behavioural logs with participant tables; checking `len()` before/after catches duplicated subject IDs.

## Math links #math-link
- Group means and SDs, z-scores → [[A7 Sums Products and Factorials]], [[CS02 Probability and Statistics]]
- Joins as set operations on keys (inner = ∩, outer = ∪) → [[E1 Sets Logic and Quantifiers]]
- Log transforms of RTs → [[B3 Logarithmic Functions]]

## Connections
- Tidy data, metadata → [[CS05 Data Formats and Representation]]; missing data, outliers → [[CS06 Data Science Workflow]]
- Reading files → [[Py04 Python Files and Data Formats]]; arrays underneath → [[Py05 NumPy and Arrays]]
- Plotting tidy data → [[Py07 Python Plotting and Visualization]] (seaborn)
- The R equivalent → [[R05 dplyr and tidyr]]

## Key takeaways
- DataFrame = labelled columns sharing an index; `.loc` by label, `.iloc` by position.
- Filter with masks (`& | ~`), assign with a single `.loc` (Copy-on-Write).
- groupby → `agg` (one row per group) or `transform` (same shape).
- Check row counts after `merge`; long format for analysis, wide for paired views.
- Aggregations skip NaN by default.
