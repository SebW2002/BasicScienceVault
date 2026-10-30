---
aliases: [Mistake Log Programming, Fehler Programmierung, Programming Basics Mistakes]
tags: [programming, shared-concepts, type/mistakes]
---
# ⚠️ Mistakes – Programming Basics

> [[MOC-programming|↑ Programming MOC]] · [[Prog00 Shared Programming Concepts]] · Template: [[Mistake Entry Template]]
> Language-specific logs: [[Mistakes - Python]] · [[Mistakes - R]] · [[Mistakes - MATLAB]] · [[Mistakes - Markdown HTML LaTeX]]

**How to use:** this log is for mistakes that would happen in **any** language – off-by-one indices, NaN handling, shapes, paths, seeds. Language-specific syntax goes into the language logs.

## Classic traps (pre-filled)
| ❌ Wrong | ✅ Right | Quick check / why | Topic |
|---|---|---|---|
| copying indices between Python and R/MATLAB unchanged | 0-based ↔ 1-based: ±1 | first element is `x[0]` vs `x(1)` | [[Prog00 Shared Programming Concepts]] |
| Python slice `x[a:b]` assumed to include `b` | stop excluded; length `b − a` | `len(x[2:5]) == 3` | [[Prog00 Shared Programming Concepts]] |
| sample index ↔ time without the offset | Python `t = k/fs`; R/MATLAB `t = (k − 1)/fs` | sample 1 at t = 0 | [[Prog00 Shared Programming Concepts]] |
| `0.1 + 0.2 == 0.3` | compare with a tolerance | prints False | [[Prog00 Shared Programming Concepts]] |
| `x == NaN` / `x == NA` | `isnan` / `is.na` | never true | [[Prog00 Shared Programming Concepts]] |
| missing values coded as 0 or −999 | NaN / NA | means are wrong | [[Prog00 Shared Programming Concepts]] |
| assuming all functions skip NaN | check: pandas skips, NumPy/R/MATLAB don't by default | – | [[Prog00 Shared Programming Concepts]] |
| `while` loop whose condition never changes | update the variable inside | runs forever | [[Prog00 Shared Programming Concepts]] |
| `if` on a whole vector | `any()` / `all()` | error (R, Python) or "all true" (MATLAB) | [[Prog00 Shared Programming Concepts]] |
| loops over elements for maths | vectorised expression | slow, longer, error-prone | [[Prog00 Shared Programming Concepts]] |
| aggregating over the wrong axis/dimension | name the dimension; check the output shape | ERP has shape trials × time? | [[Prog00 Shared Programming Concepts]] |
| broadcasting/recycling with mismatched shapes | check shapes/lengths explicitly | silent misalignment | [[Prog00 Shared Programming Concepts]] |
| functions changing global variables | inputs as arguments, results as return values | results depend on call order | [[Prog00 Shared Programming Concepts]] |
| random numbers without a seed | fixed, reported seed | p-values change every run | [[Prog00 Shared Programming Concepts]] |
| absolute paths / `setwd` / `cd` in scripts | project-relative paths with path functions | breaks on other computers | [[Prog00 Shared Programming Concepts]] |
| editing raw data files | read raw → write derived | irreversible | [[Prog00 Shared Programming Concepts]] |
| clicking through a GUI without saving a script | script (or saved history) | not reproducible | [[Prog00 Shared Programming Concepts]] |

## My mistakes
| Date | ❌ What I did | ✅ Correct | Why / quick check | Link |
|---|---|---|---|---|
| | | | | |

## Patterns I notice
- 
