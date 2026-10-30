---
tags: [programming, python, pandas, type/worksheet]
---
# Py06 pandas and Tabular Data – Worksheet

> Theory: [[Py06 pandas and Tabular Data]] · Solutions: [[Py06 pandas and Tabular Data - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

Use this table for tasks 1–10:

| subject | condition | rt |
|---|---|---|
| 01 | face | 0.40 |
| 01 | house | 0.50 |
| 01 | face | 0.60 |
| 02 | face | 0.30 |
| 02 | house | NaN |
| 02 | house | 0.70 |

## Level 1 – Selecting
1. What are `df.shape`, `df["rt"].count()` and `len(df)`?
2. What does `df.loc[df["rt"] > 0.45, "subject"]` return?
3. `df.iloc[1:3, 2]`?
4. Difference between `df["rt"]` and `df[["rt"]]`?

## Level 2 – Grouping
5. Compute `df.groupby("condition")["rt"].mean()` by hand.
6. Compute `df.groupby(["subject", "condition"])["rt"].mean()` by hand.
7. What is `df["rt"].mean()` – and what would `df["rt"].to_numpy().mean()` give?
8. What's the difference between `.agg("mean")` and `.transform("mean")` after `groupby("subject")["rt"]`? Give the shape of each result.

## Level 3 – Reshaping and joining
9. Pivot the result of task 6 to wide format (subjects as rows, conditions as columns). Write the code and the resulting table.
10. `ages = pd.DataFrame({"subject": ["01", "01", "02"], "age": [24, 24, 31]})` (subject 01 entered twice). How many rows does `df.merge(ages, on="subject")` have? How would you catch this?
11. This line has no effect (pandas ≥ 3.0). Why? Correct it.
    `df[df["rt"] > 0.65]["rt"] = np.nan`

## Level 4 – Neuro transfer
12. A BIDS `events.tsv` has `onset` in seconds; the EEG has fs = 250 Hz. Write a line that adds a column `sample` with integer sample indices.
13. Wheel-running data with irregular timestamps over 3 days: you want mean speed per hour. Which pandas features do you use?
14. 💻 Build the table above in pandas and verify tasks 5, 6, 9 and 10.
