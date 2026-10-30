---
aliases: [Mistake Log R, Fehler R, R Bugs]
tags: [programming, r, type/mistakes]
---
# ⚠️ Mistakes – R

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · Template: [[Mistake Entry Template]]

**How to use:** after every worksheet – and every real bug or wrong model – add a row to *My mistakes* with the quick check that would have caught it.

## Classic traps (pre-filled)
| ❌ Wrong | ✅ Right | Quick check / why | Topic |
|---|---|---|---|
| `mean(x, na.rm <- TRUE)` | `mean(x, na.rm = TRUE)` | `<-` creates a variable and passes it positionally | [[R01 R Basics and Syntax]] |
| `T`/`F` instead of `TRUE`/`FALSE` | write them out | `T` can be overwritten | [[R01 R Basics and Syntax]] |
| `as.numeric(factor_of_numbers)` | `as.numeric(as.character(f))` | gives level codes | [[R01 R Basics and Syntax]] |
| subject IDs as numbers in models | `factor(subject)` | continuous trend over IDs | [[R01 R Basics and Syntax]] |
| relying on alphabetical reference level | `relevel()` / `factor(levels = …)` | intercept = which group? | [[R01 R Basics and Syntax]] |
| `x[-1]` meaning "last element" (Python habit) | `x[length(x)]`; `-1` removes the first | – | [[R02 R Data Structures and Vectorization]] |
| unnoticed recycling of a shorter vector | check `length()`; match by key | no warning if lengths divide | [[R02 R Data Structures and Vectorization]] |
| `df[df$rt > 0.2]` (missing comma) | `df[df$rt > 0.2, ]` | selects columns instead of rows | [[R02 R Data Structures and Vectorization]] |
| `l["a"]` when you need the element | `l[["a"]]` / `l$a` | `[` returns a list | [[R02 R Data Structures and Vectorization]] |
| `matrix(1:6, 2)` assumed row-wise | column-major (`byrow = TRUE` if needed) | print it | [[R02 R Data Structures and Vectorization]] |
| `sapply` output type assumed | `vapply`/`map_dbl` | may return list or matrix | [[R02 R Data Structures and Vectorization]] |
| `for (i in 1:length(x))` | `seq_along(x)` | empty `x` → runs for 1, 0 | [[R03 R Control Flow and Functions]] |
| `if (vector)` / `if (NA)` | `any()`, `all()`, `!is.na(x) && …` | error | [[R03 R Control Flow and Functions]] |
| `x == NA` | `is.na(x)` | always NA | [[R03 R Control Flow and Functions]] |
| `x[x > 0]` with NAs in x | `x[which(x > 0)]` | NAs kept | [[R03 R Control Flow and Functions]] |
| modifying a data frame inside a function and not returning it | return and reassign | copy-on-modify | [[R03 R Control Flow and Functions]] |
| growing a vector with `c()` in a loop | pre-allocate | slow | [[R03 R Control Flow and Functions]] |
| `setwd("C:/Users/…")` | RStudio Project + `here()` | breaks elsewhere | [[R04 R Data Import and Tidy Data]] |
| `read_csv` on German Excel export | `read_csv2()` | one column "0,45;0,52" | [[R04 R Data Import and Tidy Data]] |
| leading zeros lost in IDs | `col_types = cols(subject = col_character())` | "01" → 1 | [[R04 R Data Import and Tidy Data]] |
| `df \|> lm(y ~ x)` | `lm(y ~ x, data = _)` | pipe fills the first argument | [[R04 R Data Import and Tidy Data]] |
| forgetting `ungroup()` | `.groups = "drop"`, `.by =`, `ungroup()` | later operations still grouped | [[R05 dplyr and tidyr]] |
| `filter(rt > 0.2)` assumed to keep NA rows | it drops them | count before/after | [[R05 dplyr and tidyr]] |
| join on duplicated keys | `relationship = "many-to-one"`, compare `nrow()` | rows multiply | [[R05 dplyr and tidyr]] |
| `lag()` without grouping | `group_by(subject, block)` first | crosses subjects | [[R05 dplyr and tidyr]] |
| `ggplot(...) \|> geom_point()` | `+` | – | [[R06 ggplot2 Visualization]] |
| `aes(colour = "blue")` | `geom_point(colour = "blue")` | legend "blue" | [[R06 ggplot2 Visualization]] |
| lines connect all conditions | `aes(group = …)` / `colour = …` | zig-zag line | [[R06 ggplot2 Visualization]] |
| `stat_summary` CI on trials | subject means first | pseudoreplication | [[R06 ggplot2 Visualization]] |
| interpreting main effects with interaction and treatment coding | centre / sum contrasts / emmeans | effects at reference level | [[R07 R Statistical Modelling]] |
| `lm` on repeated trials | mixed model or subject means | SEs too small | [[R07 R Statistical Modelling]] |
| Poisson GLM ignoring overdispersion | check deviance/df; quasipoisson / negbin | SEs too small | [[R07 R Statistical Modelling]] |
| reading glm coefficients as probabilities/rates | `exp()` → odds/rate ratios | link scale | [[R07 R Statistical Modelling]] |
| testing normality of raw data | residuals | Q–Q plot of `resid(m)` | [[R07 R Statistical Modelling]] |
| `aov` type I SS in unbalanced designs | state type; `car::Anova(type = 3)` + sum contrasts | order-dependent | [[R07 R Statistical Modelling]] |
| only random intercepts when effects vary by subject | add random slopes (if supported) | inflated false positives | [[R08 R Mixed-Effects Models]] |
| comparing REML fits with different fixed effects | ML (`anova()` refits) | – | [[R08 R Mixed-Effects Models]] |
| ignoring singular fit warnings | simplify random structure | variance 0 / correlation ±1 | [[R08 R Mixed-Effects Models]] |
| brms without checking Rhat/ESS | $\hat R\le1.01$, ESS, `pp_check()` | unconverged chains | [[R08 R Mixed-Effects Models]] |
| `signal::butter(4, 40)` in Hz | normalise: `40 / (fs/2)` | – | [[R09 R Neuroscience Packages]] |
| `signal` masking `dplyr::filter` | call `dplyr::filter` explicitly | strange errors | [[R09 R Neuroscience Packages]] |
| 0-based indices from Python used directly | `+ 1` | off by one | [[R09 R Neuroscience Packages]] |
| report works in console, fails on render | everything created inside the document | fresh session | [[R10 R Markdown and Quarto]] |
| cached chunk reading changed data | invalidate cache / file dependency | stale results | [[R10 R Markdown and Quarto]] |
| no `renv.lock` / `sessionInfo()` | `renv::snapshot()`, report versions | results change with updates | [[R11 R Reproducible Projects]] |
| tests only of properties | add a test against a known value | sign errors slip through | [[R11 R Reproducible Projects]] |

## My mistakes
| Date | ❌ What I did | ✅ Correct | Why / quick check | Link |
|---|---|---|---|---|
| | | | | |

## Patterns I notice
- 
