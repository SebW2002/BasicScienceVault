---
aliases: [R Data Structures, R Vectors, Data Frames, Lists in R, apply sapply lapply, purrr map, Recycling]
tags: [programming, r, data-structures, vectorization, type/overview, neuro]
---
# R02 R Data Structures and Vectorization

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R02 R Data Structures and Vectorization - Worksheet|✏️ Worksheet]] · [[R02 R Data Structures and Vectorization - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
In R, **vectorised thinking is the default**: almost every function works on whole vectors, and data frames are lists of vectors. Explicit loops are rarely needed – when they are, the `apply` family or `purrr::map` replaces them. Knowing which structure you have (vector, list, matrix, data frame) explains most R error messages.

## The four structures
| Structure | Dimensions | Element types | Create | Python analogue |
|---|---|---|---|---|
| **(atomic) vector** | 1 | **one** type | `c(1, 2, 3)`, `1:10`, `seq()`, `rep()` | 1-d NumPy array |
| **list** | 1 | **any**, mixed, nested | `list(fs = 1000, ch = c("Fz", "Cz"))` | dict / list |
| **matrix** (array) | 2 (n) | one type | `matrix(1:6, nrow = 2)`, `array(0, c(2, 3, 4))` | 2-d (n-d) array |
| **data frame** / tibble | 2 | one type **per column** | `data.frame(sub = ..., rt = ...)`, `tibble()` | pandas DataFrame |

### Vectors
```r
x <- c(4, 8, 15, 16, 23, 42)
x[1]; x[length(x)]       # first, last (1-based)
x[2:4]                   # 8 15 16 (both ends included)
x[-1]                    # all but the first
x[c(TRUE, FALSE)]        # logical index, recycled: elements 1, 3, 5
x[x > 10]                # logical filtering
names(x) <- letters[1:6]; x["c"]   # named elements
seq(0, 1, by = 0.25); seq_len(5); rep(c("A", "B"), times = 3); rep(c("A", "B"), each = 2)
```
- Combining different types **coerces** to the most general one: `c(1, "a", TRUE)` → all character. logical < integer < double < character.

### Lists
```r
meta <- list(subject = "01", fs = 1000, bad = c("T7", "Oz"))
meta$fs; meta[["fs"]]    # the element itself
meta["fs"]               # a sub-list containing the element
str(meta)
```
`[[ ]]` / `$` extract an element; `[ ]` returns a smaller list. Model results (`lm`, `t.test`) are lists – `res$p.value`.

### Matrices
```r
M <- matrix(1:6, nrow = 2)   # filled column by column (column-major!)
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6
M[2, 3]; M[, 1]; dim(M); t(M)
M %*% t(M)                   # matrix product;  * is element-wise
solve(A, b)                  # linear system
```

### Data frames
```r
df <- data.frame(subject = c("01", "01", "02"), cond = c("face", "house", "face"), rt = c(0.45, 0.52, 0.48))
df$rt; df[["rt"]]; df[2, "rt"]; df[df$rt > 0.46, ]   # note the comma: rows, all columns
nrow(df); ncol(df); names(df); summary(df)
```
A data frame is a **list of equal-length column vectors**. Tibbles (tidyverse) print more nicely and never convert types silently ([[R04 R Data Import and Tidy Data]]).

## Vectorisation as the default
```r
rt_ms <- rt * 1000                       # every element
z <- (x - mean(x)) / sd(x)               # z-scores in one line
valid <- rt > 0.15 & rt < 2              # logical vector
mean(valid)                              # proportion of TRUE
sum(x[x > 0])
ifelse(rt > 2, NA, rt)                   # vectorised if-else
cumsum(c(1, 2, 3)); diff(spike_times)    # ISIs
```
- **Recycling:** when lengths differ, the shorter vector is repeated: `c(1, 2, 3, 4) + c(10, 20)` → `11 22 13 24`. A warning only appears if the longer length is **not a multiple** of the shorter. Powerful (`x * 2`) and dangerous (silent misalignment).
- `sd()` and `var()` use $n - 1$; `mean`, `sum`, `max` return `NA` if any element is `NA` unless `na.rm = TRUE`.
- Many functions are vectorised over arguments too: `paste0("sub-", sprintf("%02d", 1:3))` → `"sub-01" "sub-02" "sub-03"`.

## apply, sapply, lapply, map
When there is no vectorised function, apply a function to each element/row/column:
```r
apply(M, 2, mean)                  # over columns (MARGIN 2); 1 = rows → same as colMeans(M)
lapply(files, read.csv)            # list in → list out
sapply(trials_list, length)        # simplifies to a vector if possible
vapply(x, sqrt, numeric(1))        # like sapply, but with a declared output type (safer)
library(purrr)
map(files, read_csv)               # list
map_dbl(subjects, \(s) mean(df$rt[df$subject == s]))   # numeric vector
map2_dbl(a, b, \(x, y) x / y)      # two inputs in parallel
```
- `\(x) x^2` is the short lambda syntax (R ≥ 4.1) for `function(x) x^2`.
- `purrr::map_*` functions have **type-stable** output (`map_dbl` always returns doubles or fails) – easier to reason about than `sapply`, which may return a vector, matrix or list depending on input.
- For data frames, grouped summaries are clearer with dplyr ([[R05 dplyr and tidyr]]).

## Same idea in Python and MATLAB
| R | Python | MATLAB |
|---|---|---|
| `x[2:4]` | `x[1:4]` | `x(2:4)` |
| `x[-1]` | `x[1:]` | `x(2:end)` |
| `list(a = 1)` | `{"a": 1}` | `struct("a", 1)` |
| `matrix(1:6, 2)` (column-major) | `np.arange(1, 7).reshape(2, 3, order="F")` | `reshape(1:6, 2, 3)` |
| recycling | broadcasting | implicit expansion |
| `sapply(x, f)` | list comprehension / `np.vectorize` | `arrayfun(f, x)` |
→ [[Py02 Python Data Structures]], [[Py05 NumPy and Arrays]], [[MAT02 MATLAB Matrices and Vectorization]]

## In neuroscience #neuro
- **ISIs:** `isi <- diff(spike_times)`; **CV:** `sd(isi) / mean(isi)` – two vectorised lines ([[CS11 Time Series and Signal Processing]]).
- **Per-subject files:** `map(files, read_csv) |> list_rbind()` reads and stacks all subjects ([[R04 R Data Import and Tidy Data]]).
- **EEG as a matrix:** channels × time with `colMeans` for the average reference; but large signal processing is usually done in Python/MATLAB and summaries are brought to R for statistics.
- **Recycling bug:** adding a per-condition baseline vector of the wrong length to a trial vector silently misaligns values – check `length()`.

## Math links #math-link
- Vectors and matrices, `%*%`, `t()`, `solve()` → [[C1 Matrices]], [[C3 Linear Systems and Gaussian Elimination]]
- Sums, means, cumulative sums → [[A7 Sums Products and Factorials]]
- Logical vectors as indicator functions and sets → [[E1 Sets Logic and Quantifiers]]

## Connections
- Basics and types → [[R01 R Basics and Syntax]]; shared concepts → [[Prog00 Shared Programming Concepts]]
- Loops, functions, NA → [[R03 R Control Flow and Functions]]
- Data frames from files → [[R04 R Data Import and Tidy Data]]; manipulation → [[R05 dplyr and tidyr]]

## Key takeaways
- Vector (one type), list (anything), matrix (2-d, one type, column-major), data frame (list of columns).
- `[[ ]]`/`$` extract, `[ ]` subsets; data frames index `df[rows, cols]`.
- Operations are vectorised; shorter vectors are recycled – check lengths.
- `apply` over matrix margins, `lapply`/`map` over lists; prefer type-stable `map_dbl`/`vapply`.
