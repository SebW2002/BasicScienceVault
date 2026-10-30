---
tags: [programming, r, type/worksheet]
---
# R04 R Data Import and Tidy Data – Worksheet

> Theory: [[R04 R Data Import and Tidy Data]] · Solutions: [[R04 R Data Import and Tidy Data - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Which function?
1. Which function reads: a) a CSV with `;` separators and decimal commas b) a BIDS `events.tsv` c) sheet "RT" of an Excel file d) a fitted model you saved yesterday e) a typed columnar file written by pandas?
2. What is the difference between `saveRDS` and `write_csv` for a data frame with factor columns?
3. Subject IDs "01", "02" become 1, 2 after import. Why, and how do you prevent it?

## Level 2 – Tidy or not?
4. Is each table tidy? If not, what's wrong?
   a) columns `subject, rt_face, rt_house, acc_face, acc_house`
   b) columns `subject, condition, electrode, amplitude`
   c) a column `cond_side` with values `"face_left"`, `"house_right"`
   d) columns `subject, age, trial, rt`, with `age` repeated on every trial row
5. Rewrite table a) in long format: which columns does the tidy version have?

## Level 3 – Pipes
6. Rewrite as a pipe: `round(mean(log(df$rt)), 2)`.
7. `df |> lm(rt ~ cond)` gives an error. Why? Write two correct versions.
8. What does `x |> f(y = 2)` evaluate to as a normal call?

## Level 4 – Neuro transfer
9. You have 30 PsychoPy files `data/raw/sub-XX_faces.csv`. Write the code to read all of them into one tibble that records which file each row came from, treating `"None"` as missing.
10. An MNE script exports a CSV with columns `subject, condition, Fz, Cz, Pz` (mean P300 amplitude per electrode). Which column structure do you need for a model `amp ~ condition * electrode`? (Code in [[R05 dplyr and tidyr]].)
11. 💻 Write two small CSVs (`sub-01.csv`, `sub-02.csv`) with `write_csv`, read them back with one `read_csv(files, id = "file")` call, and extract the subject number from the file name with `stringr::str_extract(file, "sub-\\d+")`.
