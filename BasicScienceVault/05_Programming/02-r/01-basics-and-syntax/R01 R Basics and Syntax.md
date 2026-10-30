---
aliases: [R Basics, R Syntax, RStudio, Factors, Assignment Arrow]
tags: [programming, r, syntax, factors, type/overview, neuro]
---
# R01 R Basics and Syntax

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R01 R Basics and Syntax - Worksheet|✏️ Worksheet]] · [[R01 R Basics and Syntax - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
R was built by statisticians for data analysis. In neuroscience and psychology it's the language for **statistics** – mixed models, Bayesian regression, publication-quality plots and reproducible reports. Its basics differ from Python in small but important ways: **1-based indexing**, the `<-` arrow, everything is a **vector**, and categorical variables are **factors**.

## Working environment: RStudio, VS Code, scripts, R Markdown
| Tool | What it is |
|---|---|
| **R** | the language and interpreter (the console: `>` prompt) |
| **RStudio** (Posit) | the standard IDE: script editor, console, environment, plots, help, Projects |
| **VS Code** + R extension (or Posit's **Positron**) | alternative editors, convenient if you also use Python/LaTeX |
| **script** (`analysis.R`) | code run top to bottom: `source("analysis.R")` or `Rscript analysis.R` |
| **R Markdown** (`.Rmd`) / **Quarto** (`.qmd`) | text + code chunks + output in one document → [[R10 R Markdown and Quarto]] |
- In RStudio, **Ctrl/Cmd + Enter** sends the current line to the console; **Ctrl/Cmd + Shift + S** sources the whole script.
- Work in **RStudio Projects** so the working directory is the project folder ([[R11 R Reproducible Projects]]).
- Turn off "restore .RData into workspace at startup": a fresh start every time keeps your scripts honest.

## Assignment with <-, help with ?
```r
fs <- 1000                 # assignment (Alt + - in RStudio)
fs = 1000                  # also works at top level, but <- is the convention
rt <- c(0.45, 0.52, 0.61)  # c() combines values into a vector
rt                         # print by typing the name
mean(rt)                   # function call
?mean                      # help page of mean
??"mixed model"            # search all help pages
help(package = "lme4")     # overview of a package
example(t.test)            # run the examples from the help page
```
- `=` is used for **function arguments**: `mean(x, na.rm = TRUE)`. Using `<-` for assignment and `=` for arguments keeps the two roles visible.
- Names: letters, digits, `.` and `_`; case-sensitive (`RT` ≠ `rt`); conventional style is `snake_case`.
- `#` starts a comment. Blocks use `{ }`; indentation is only for readability.
- Packages: `install.packages("lme4")` once, `library(lme4)` in every script; `pkg::fun()` calls a function without attaching the package (clear where it comes from).

## Base data types
| Type (`typeof`) | Example | Note |
|---|---|---|
| double | `3`, `0.5`, `1e-3`, `Inf` | **all numbers are doubles by default** |
| integer | `3L`, `1:10` | `L` suffix; ranges `a:b` give integers |
| character | `"Cz"`, `'face'` | strings |
| logical | `TRUE`, `FALSE`, `NA` | `T`/`F` exist but can be overwritten – write them out |
| complex | `3+4i` | `Mod()`, `Arg()` |
```r
class(3); typeof(3L); is.numeric(rt); as.integer("7"); as.character(12)
str(df)          # compact structure of any object – your best friend
5 %/% 2; 5 %% 2  # integer division 2, remainder 1
2^10             # power
```
- **Everything is a vector.** `3` is a numeric vector of length 1; there is no separate scalar type. Functions are vectorised by default ([[R02 R Data Structures and Vectorization]]).
- **Missing values:** `NA` (missing, of any type), `NaN` (not a number, e.g. `0/0`), `NULL` (absence of an object). `NA > 1` is `NA`, so comparisons can produce `NA` ([[R03 R Control Flow and Functions]]).

## Factors
A **factor** stores a categorical variable as integer codes plus a set of **levels** (labels):
```r
cond <- factor(c("face", "house", "face", "scrambled"))
levels(cond)             # "face" "house" "scrambled" (alphabetical by default)
cond <- factor(cond, levels = c("scrambled", "face", "house"))   # set the order
table(cond)              # counts per level
as.integer(cond)         # the underlying codes: 2 3 2 1
relevel(cond, ref = "scrambled")   # reference level for regression
droplevels(cond[cond != "house"])  # remove unused levels
```
- **Why factors matter:** in models (`lm`, `lme4`), the **first level is the reference category**; contrasts and dummy coding follow from the levels ([[R07 R Statistical Modelling]]). In ggplot2 the level order sets the order of axes and legends ([[R06 ggplot2 Visualization]]).
- **Ordered factors** (`factor(x, ordered = TRUE)`) for ordinal scales (Likert, sleep stages).
- **Trap:** `as.numeric(factor(c("10", "20", "5")))` gives the **codes** (1, 2, 3 by alphabetical level order), not the numbers. Use `as.numeric(as.character(f))`.
- Since R 4.0, `read.csv` and `data.frame` no longer convert strings to factors automatically (`stringsAsFactors = FALSE`); create factors explicitly.

## Same idea in Python and MATLAB
| R | Python | MATLAB |
|---|---|---|
| `x <- 3` | `x = 3` | `x = 3;` |
| `c(1, 2, 3)` | `np.array([1, 2, 3])` | `[1 2 3]` |
| `?mean` | `help(np.mean)` | `help mean` |
| `factor` | `pd.Categorical` / `category` dtype | `categorical` |
| `str(x)` | `df.info()`, `type(x)` | `whos`, `class(x)` |
| `TRUE`/`FALSE` | `True`/`False` | `true`/`false` |
→ [[Py01 Python Basics and Syntax]], [[MAT01 MATLAB Basics and Syntax]]

## In neuroscience #neuro
- **Experimental factors** – condition, group (patient/control), hemisphere, electrode site – are factors; setting the reference level decides what the regression coefficients mean.
- **Subject IDs** should be factors (or characters), never numbers: subject 10 is not "more" than subject 2.
- **Sleep stages** (W, N1, N2, N3, REM) as an ordered factor in sleep studies.
- **Help pages** of statistical functions state exactly which test variant is computed (e.g. `t.test` defaults to **Welch's** test) – read them.

## Math links #math-link
- Powers and scientific notation (`1e-3`, `2^10`) → [[A1 Exponent Rules]]
- Integer division and remainders → [[A5 Fractions]]
- Complex numbers `3+4i`, `Mod`, `Arg` → [[E2 Complex Numbers]]
- Categories as sets of levels → [[E1 Sets Logic and Quantifiers]]

## Connections
- Shared concepts (types, 1-based indexing) → [[Prog00 Shared Programming Concepts]]
- Next: vectors, lists, data frames → [[R02 R Data Structures and Vectorization]]
- Factors in models → [[R07 R Statistical Modelling]], [[R08 R Mixed-Effects Models]]
- Reports → [[R10 R Markdown and Quarto]]

## Key takeaways
- `<-` assigns, `=` passes arguments; `?fun` for help; `str()` to inspect.
- Numbers are doubles; everything is a vector; indexing starts at 1.
- Factors = codes + levels; the first level is the reference; never `as.numeric()` a factor of numbers directly.
- Work in RStudio Projects with a clean workspace.
