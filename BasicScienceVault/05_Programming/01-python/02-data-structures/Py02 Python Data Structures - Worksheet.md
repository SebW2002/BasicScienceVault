---
tags: [programming, python, type/worksheet]
---
# Py02 Python Data Structures – Worksheet

> Theory: [[Py02 Python Data Structures]] · Solutions: [[Py02 Python Data Structures - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Predict the output
1. `x = [3, 1, 4, 1, 5]`: `x[1:4]`, `x[::-1]`, `len(set(x))`, `x.count(1)`
2. `[1, 2] * 3`, `[1, 2] + [3]`, `(5)`, `(5,)` – which of the last two is a tuple?
3. `d = {"fs": 500, "n": 64}`: `d["fs"]`, `d.get("ref", "none")`, `list(d.keys())`, `"n" in d`
4. `{1, 2, 3} & {2, 3, 4}`, `{1, 2, 3} - {2}`, `{1, 2} | {5}`

## Level 2 – Which structure?
5. Choose list, tuple, dict or set and justify: a) shape of an array, b) the parameters of a filter by name, c) all unique condition labels, d) the list of files to process in order.
6. Why can't a list be a dictionary key, but a tuple can?

## Level 3 – Mutability
7. What is printed?
   ```python
   a = [1, 2, 3]
   b = a
   c = a.copy()
   b.append(4)
   c.append(5)
   print(a, b, c)
   ```
8. What does this print after the second call, and why? Fix it.
   ```python
   def add_trial(rt, trials=[]):
       trials.append(rt)
       return trials
   add_trial(0.4)
   print(add_trial(0.5))
   ```
9. `s = "theta"; s[0] = "T"` raises an error. Why? How do you get `"Theta"`?

## Level 4 – Comprehensions and neuro transfer
10. Write a list comprehension that keeps only reaction times between 0.15 and 2.0 s from `rts`.
11. Write a dict comprehension that maps each channel name in `chs = ["Fz", "Cz", "Pz"]` to its index.
12. Subject A has channels `{"Fz","Cz","Pz","Oz"}`, subject B `{"Fz","Cz","T7"}`. Which channels can you use for a group analysis that requires all subjects to have the channel? Which channels are in only one subject?
13. 💻 Build a list of 3 trial dicts (`condition`, `rt`) and compute the mean RT per condition with a dict. Run it.
