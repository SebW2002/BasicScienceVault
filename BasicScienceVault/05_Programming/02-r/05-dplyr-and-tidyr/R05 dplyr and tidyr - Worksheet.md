---
tags: [programming, r, tidyverse, type/worksheet]
---
# R05 dplyr and tidyr – Worksheet

> Theory: [[R05 dplyr and tidyr]] · Solutions: [[R05 dplyr and tidyr - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

Table `trials` for tasks 1–8:

| subject | condition | rt | correct |
|---|---|---|---|
| 01 | face | 0.42 | TRUE |
| 01 | face | 0.10 | TRUE |
| 01 | house | 0.55 | FALSE |
| 02 | face | 0.48 | TRUE |
| 02 | house | NA | FALSE |
| 02 | house | 0.61 | TRUE |

## Level 1 – Verbs
1. How many rows does `filter(trials, rt > 0.15)` return? Why not 5?
2. Result of `trials |> count(condition)`?
3. Result of `trials |> summarise(n = n(), m = mean(rt, na.rm = TRUE))`?
4. What does `select(trials, -correct)` do?

## Level 2 – Groups
5. Compute by hand: `trials |> filter(rt > 0.15) |> group_by(condition) |> summarise(m = mean(rt), acc = mean(correct))`.
6. Same with `group_by(subject, condition)`. How many rows?
7. What is the difference in output size between `group_by(subject) |> summarise(m = mean(rt, na.rm = TRUE))` and `group_by(subject) |> mutate(m = mean(rt, na.rm = TRUE))`?
8. Write code that adds a column `rt_z` with z-scores **within subject** (ignore NA).

## Level 3 – Reshape and join
9. `wide` has columns `subject, rt_face, rt_house`. Write `pivot_longer` code giving `subject, condition, rt` with condition values `"face"`/`"house"`.
10. Turn the summary from task 6 into wide format with columns `subject, face, house`, and add `diff = house - face`.
11. `participants` has rows for subjects "01" and "03". What do `left_join(trials, participants, by = "subject")`, `inner_join(...)` and `anti_join(trials, participants, by = "subject")` return (row counts)?

## Level 4 – Neuro transfer
12. Write a pipeline: exclude RTs outside 0.15–2 s and NA, then exclude trials with |within-subject z| > 3, then compute mean correct-trial RT per subject × condition, keeping the number of trials.
13. Post-error slowing: add a column `prev_correct` (previous trial's accuracy within each subject and block). Which function, and why must you group first?
14. 💻 Build `trials` in R and check your answers to tasks 1, 5, 6 and 10.
