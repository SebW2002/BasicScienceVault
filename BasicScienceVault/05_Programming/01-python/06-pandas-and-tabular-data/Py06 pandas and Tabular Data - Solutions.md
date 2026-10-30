---
tags: [programming, python, pandas, type/solution]
---
# Py06 pandas and Tabular Data – Solutions

> Worksheet: [[Py06 pandas and Tabular Data - Worksheet]] · Theory: [[Py06 pandas and Tabular Data]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. `(6, 3)`; `5` (count ignores NaN); `6`.
2. The `subject` values of rows with rt > 0.45: rows 1, 2, 5 → `"01", "01", "02"` (as a Series with index 1, 2, 5).
3. Rows at positions 1 and 2, column position 2 (`rt`): `0.50, 0.60`.
4. `df["rt"]` is a **Series**; `df[["rt"]]` is a one-column **DataFrame**.

## Level 2
5. face: (0.40 + 0.60 + 0.30)/3 = **0.433**; house: NaN skipped → (0.50 + 0.70)/2 = **0.60**.
6. (01, face) 0.50; (01, house) 0.50; (02, face) 0.30; (02, house) 0.70.
7. `df["rt"].mean()` = 2.5/5 = **0.50** (NaN skipped). The NumPy version gives **NaN**.
8. `.agg("mean")` gives one value per subject → length 2 (index = subject). `.transform("mean")` broadcasts each subject's mean back to its rows → length 6, aligned with `df` (useful for centering within subject).

## Level 3
9. ```python
   m = df.groupby(["subject", "condition"], as_index=False)["rt"].mean()
   wide = m.pivot(index="subject", columns="condition", values="rt")
   ```
   | subject | face | house |
   |---|---|---|
   | 01 | 0.50 | 0.50 |
   | 02 | 0.30 | 0.70 |
10. Subject 01's 3 rows each match 2 age rows → 6, plus subject 02's 3 rows → **9 rows** instead of 6. Catch with `df.merge(ages, on="subject", validate="many_to_one")` (raises an error) or by comparing `len()` before and after; fix with `ages.drop_duplicates()`.
11. Chained assignment: `df[mask]` creates a new object (Copy-on-Write), and the assignment modifies that temporary object. Correct: `df.loc[df["rt"] > 0.65, "rt"] = np.nan`.

## Level 4
12. `events["sample"] = (events["onset"] * 250).round().astype(int)` (add `- 1` only if a 1-based tool needs it).
13. Parse timestamps (`parse_dates`), set a **DatetimeIndex**, then `ts["speed"].resample("1h").mean()`; missing hours appear as NaN.
14. ```python
    import pandas as pd, numpy as np
    df = pd.DataFrame({"subject": ["01"]*3 + ["02"]*3,
                       "condition": ["face", "house", "face", "face", "house", "house"],
                       "rt": [0.40, 0.50, 0.60, 0.30, np.nan, 0.70]})
    print(df.groupby("condition")["rt"].mean())
    m = df.groupby(["subject", "condition"], as_index=False)["rt"].mean()
    print(m.pivot(index="subject", columns="condition", values="rt"))
    ages = pd.DataFrame({"subject": ["01", "01", "02"], "age": [24, 24, 31]})
    print(len(df.merge(ages, on="subject")))   # 9
    ```
