---
tags: [programming, shared-concepts, type/worksheet]
---
# Prog00 Shared Programming Concepts – Worksheet

> Theory: [[Prog00 Shared Programming Concepts]] · Solutions: [[Prog00 Shared Programming Concepts - Solutions]] · Log mistakes in [[Mistakes - Programming Basics]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Types and indexing
1. `x = [10, 20, 30, 40, 50]`. Give the element(s) returned by: a) Python `x[1]`, b) R `x[1]`, c) MATLAB `x(end)`, d) Python `x[1:3]`, e) MATLAB `x(2:3)`, f) R `x[-1]`.
2. Why is `0.1 + 0.2 == 0.3` false? How should you compare two floats instead?
3. Which of these values are logical/Boolean, which are strings: `TRUE`, `"TRUE"`, `True`, `'true'`, `true`?
4. A Python slice `x[a:b]` contains how many elements? Show that `x[:k]` and `x[k:]` together give `x` exactly once.

## Level 2 – Loops, conditions, functions
5. What does this pseudo-code print?
   ```text
   total = 0
   for i in 1, 2, 3, 4:
       if i is even: total = total + i
   print total
   ```
6. This loop never stops. Why? Fix it.
   ```text
   threshold = 1.0; v = 0
   while v < threshold:
       print v
   ```
7. A function `baseline_correct(x, baseline)` changes a global variable `data` instead of returning a result. Name two problems this causes.
8. What is the scope of a variable created inside a function? What happens to it after the function returns?

## Level 3 – Vectorisation and missing values
9. Rewrite as one vectorised expression (any language): a loop that computes `y[i] = 2 * x[i] + 1` for all `i`.
10. `rt = [0.45, NaN, 0.52, 0.10, 0.61]` (seconds). a) What is `mean(rt)` without NaN handling? b) Write a logical mask for valid trials: not missing and 0.15 ≤ rt ≤ 2. c) Which values remain?
11. Why does `x == NaN` never find missing values? What do you use instead?
12. EEG matrix `X` has shape 64 channels × 5000 samples. You compute `m` = mean over channels at each time point (shape 1 × 5000). What does `X - m` compute, and what is this operation called in EEG analysis?

## Level 4 – Reproducibility and paths (neuro transfer)
13. Your permutation test gives p = 0.048 on Monday and p = 0.052 on Tuesday with the same data. What is the likely cause? What do you change?
14. A shared script starts with `setwd("C:/Users/anna/Desktop/project")`. Why is this a problem for your colleague? What should the script do instead?
15. You're at `my-project/code/` and want to open `my-project/data/raw/sub-01.csv`. Write the relative path.
16. 💻 Convert between conventions: an event marker sits at sample 2500 (MATLAB/EEGLAB, 1-based, $f_s = 500$ Hz). a) At what time (s) after the first sample does it occur? b) What is its index in Python? Check with a few lines of code in a language of your choice.
