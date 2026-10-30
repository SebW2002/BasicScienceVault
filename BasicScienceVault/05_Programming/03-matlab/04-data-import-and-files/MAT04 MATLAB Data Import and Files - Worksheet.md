---
tags: [programming, matlab, type/worksheet]
---
# MAT04 MATLAB Data Import and Files – Worksheet

> Theory: [[MAT04 MATLAB Data Import and Files]] · Solutions: [[MAT04 MATLAB Data Import and Files - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Which function?
1. Which function: a) a CSV with mixed text and numeric columns b) a CSV of numbers only c) a 5 GB variable you want to save d) read only 10 rows of that variable e) list the variables in a `.mat` file without loading them f) build a path that works on Windows and macOS.
2. Why is `S = load("x.mat")` safer than `load("x.mat")`?
3. `c = {'Fz', [1 2 3]}`. Classes of `c{1}`, `c(1)`, `c{2}(3)`?

## Level 2 – Structs
4. `s(1).rt = 0.4; s(2).rt = 0.6; s(3).rt = 0.5;`. What is `[s.rt]`, `mean([s.rt])`, `numel(s)`, `s(2)`?
5. EEGLAB: `EEG.event(4).latency = 2501` and `EEG.srate = 500`. At what time (s, from recording start, 1-based samples) is event 4?
6. Write code to get all channel labels from `EEG.chanlocs` as a string array.
7. FieldTrip: why is `data.trial` a cell array and not a 3-d matrix?

## Level 3 – Tables and folders
8. `T` has columns `subject`, `condition`, `rt`. Write: a) rows with rt between 0.15 and 2 b) a new column `rt_ms` c) the mean rt per condition.
9. `files = dir("data/sub-*.csv")` returns `sub-1.csv, sub-10.csv, sub-2.csv`. Why this order? Fix.
10. Write a loop that reads every `*_events.tsv` in all subfolders of `bids/` into tables and stacks them into one table with a `file` column.

## Level 4 – Neuro transfer
11. A Psychtoolbox experiment saved `results.mat` with a struct array `res` (fields `trial`, `cond`, `rt`, `correct`) for each participant. Describe how you convert all participants' files into one CSV for analysis in R.
12. A collaborator saved data with `-v7.3`. You work in Python. Which library do you use, and what should you expect about array dimensions?
13. 💻 Create a struct array with 3 trials, convert it with `struct2table`, add a column, write it to CSV with `writetable`, read it back with `readtable`, and compare.
