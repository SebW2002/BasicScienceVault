---
tags: [programming, python, type/solution]
---
# Py02 Python Data Structures – Solutions

> Worksheet: [[Py02 Python Data Structures - Worksheet]] · Theory: [[Py02 Python Data Structures]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. `[1, 4, 1]`, `[5, 1, 4, 1, 3]`, `4` (unique: 1, 3, 4, 5), `2`.
2. `[1, 2, 1, 2, 1, 2]`, `[1, 2, 3]`, `5` (just parentheses around an int), `(5,)` (tuple). The comma makes the tuple.
3. `500`, `"none"`, `["fs", "n"]`, `True`.
4. `{2, 3}`, `{1, 3}`, `{1, 2, 5}`.

## Level 2
5. a) **tuple** – fixed, shouldn't change. b) **dict** – look-up by name. c) **set** – uniqueness. d) **list** – ordered, may grow.
6. Dict keys must be **hashable**, which requires immutability: if a key could change after insertion, the dict could no longer find it. Lists are mutable, tuples (of immutable items) are not.

## Level 3
7. `[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 5]` – `a` and `b` are the same list; `c` is a copy.
8. `[0.4, 0.5]`: the default list is created once when the function is defined and shared between calls. Fix:
   ```python
   def add_trial(rt, trials=None):
       if trials is None:
           trials = []
       trials.append(rt)
       return trials
   ```
9. Strings are immutable. Create a new string: `"T" + s[1:]` or `s.capitalize()`.

## Level 4
10. `valid = [rt for rt in rts if 0.15 <= rt <= 2.0]`
11. `{ch: i for i, ch in enumerate(chs)}` → `{"Fz": 0, "Cz": 1, "Pz": 2}`
12. Intersection `A & B = {"Fz", "Cz"}`; symmetric difference `A ^ B = {"Pz", "Oz", "T7"}`.
13. ```python
    trials = [{"condition": "face", "rt": 0.42},
              {"condition": "house", "rt": 0.55},
              {"condition": "face", "rt": 0.48}]
    sums, counts = {}, {}
    for t in trials:
        c = t["condition"]
        sums[c] = sums.get(c, 0) + t["rt"]
        counts[c] = counts.get(c, 0) + 1
    means = {c: sums[c] / counts[c] for c in sums}
    print(means)   # {'face': 0.45, 'house': 0.55} (up to float rounding)
    ```
    (In practice: `pd.DataFrame(trials).groupby("condition")["rt"].mean()`, see [[Py06 pandas and Tabular Data]].)
