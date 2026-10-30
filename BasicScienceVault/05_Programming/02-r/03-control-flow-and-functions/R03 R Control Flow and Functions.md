---
aliases: [R Control Flow, R Functions, Dots Argument, NA Handling in R]
tags: [programming, r, control-flow, functions, missing-values, type/overview, neuro]
---
# R03 R Control Flow and Functions

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R03 R Control Flow and Functions - Worksheet|✏️ Worksheet]] · [[R03 R Control Flow and Functions - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
Even in vectorised R you need conditions, the occasional loop (over files, over simulations), and your own functions – for preprocessing steps you repeat, for custom summaries, for plotting themes. R's functions have two features Python users must learn: the **last expression is returned**, and `...` passes arguments on. And because `NA` is everywhere in real data, **NA handling** decides whether results are right.

## if / else
```r
if (is.na(rt)) {
  status <- "miss"
} else if (rt < 0.15) {
  status <- "anticipation"
} else {
  status <- "valid"
}
status <- if (rt > 2) "slow" else "ok"     # if is an expression and returns a value
```
- `if` needs **one** `TRUE`/`FALSE`. A vector of length > 1 is an **error** since R 4.2; `NA` gives "missing value where TRUE/FALSE needed".
- For vectors use `ifelse(test, yes, no)` or `dplyr::if_else()` (type-strict) / `dplyr::case_when()` for several conditions ([[R05 dplyr and tidyr]]).
- Scalar logic: `&&`, `||` (short-circuit, length-1 only); vectorised logic: `&`, `|`, `!`. Use `&&`/`||` in `if`.
- `switch(method, welch = ..., fft = ..., stop("unknown method"))` selects by name.

## Loops: for, while, repeat
```r
for (f in files) {                  # over elements
  d <- read.csv(f)
}
for (i in seq_along(files)) {       # over indices – safe also for empty vectors
  results[[i]] <- process(files[i])
}
while (delta > tol) { ... }
repeat { ...; if (done) break }
```
- `next` skips to the next iteration (Python's `continue`), `break` leaves the loop.
- **`1:length(x)` trap:** if `x` is empty, `1:0` is `c(1, 0)` and the loop runs twice. Use `seq_along(x)` / `seq_len(n)`.
- **Pre-allocate** results (`vector("list", n)`, `numeric(n)`) instead of growing a vector with `c()` in every iteration (slow, quadratic).
- Loops are fine for files and simulations; for element-wise maths use vectorised code ([[R02 R Data Structures and Vectorization]]).

## Functions
```r
bandpower <- function(psd, freqs, band = c(8, 12), log = FALSE) {
  idx <- freqs >= band[1] & freqs <= band[2]
  p <- sum(psd[idx])
  if (log) p <- log10(p)
  p                                  # last expression is the return value
}
bandpower(psd, f)                    # default band
bandpower(psd, f, band = c(4, 8), log = TRUE)
```
- `return(x)` exists for early exits; otherwise the last evaluated expression is returned. Return several results as a **list**: `list(mean = m, sd = s)`.
- Arguments are matched by **name**, then by **position**; names can be abbreviated (avoid that).
- **Default arguments are evaluated lazily** (when first used), and may refer to other arguments: `function(x, n = length(x))`.
- **Copy-on-modify:** a function can't change the caller's objects; modifying an argument inside changes only a local copy. Results must be returned.
- **Scope:** variables created inside are local; R looks up unknown names in the environment where the function was **defined** (lexical scoping). Don't rely on global variables – pass them as arguments.
- Check inputs: `stopifnot(is.numeric(x), length(band) == 2)` or `if (...) stop("message")`; `warning()` for non-fatal issues.

### The dots argument `...`
```r
my_mean <- function(x, ...) mean(x, ...)       # pass extra arguments through
my_mean(c(1, NA, 3), na.rm = TRUE)              # 2
plot_erp <- function(df, ...) ggplot(df, aes(time, amp, ...)) + geom_line()
summarise_all <- function(...) { args <- list(...); length(args) }
```
`...` collects any number of extra arguments – the counterpart of Python's `*args, **kwargs` and MATLAB's `varargin` ([[Py03 Python Control Flow and Functions]], [[MAT03 MATLAB Control Flow and Functions]]).

## Handling NA
| Situation | Behaviour | What to do |
|---|---|---|
| arithmetic `NA + 1` | `NA` | intended: you notice |
| `mean`, `sum`, `sd`, `max`, `quantile` | `NA` if any `NA` | `na.rm = TRUE` (deliberately!) |
| comparisons `NA > 0` | `NA` | in filters, `dplyr::filter` drops NA rows; base `x[x > 0]` keeps `NA` elements |
| test | `x == NA` is always `NA` | `is.na(x)` |
| count missing | – | `sum(is.na(x))`, `colSums(is.na(df))` |
| remove | – | `na.omit(df)`, `tidyr::drop_na(df, rt)`, `complete.cases(df)` |
| `cor(x, y)` | `NA` | `use = "complete.obs"` or `"pairwise.complete.obs"` |
| models (`lm`, `lmer`) | rows with NA in used variables are **dropped silently** (`na.action = na.omit`) | check `nobs(model)` |
- `x[x > 0]` with `NA` in `x` returns `NA` elements in the result; use `x[which(x > 0)]` or `x[!is.na(x) & x > 0]`.
- `NA` has types (`NA_real_`, `NA_character_`); `NaN` is also `is.na()` but not vice versa (`is.nan(NA)` is `FALSE`).
- Missing data mechanisms (MCAR/MAR/MNAR) decide whether dropping is OK ([[CS06 Data Science Workflow]]).

## Same idea in Python and MATLAB
| R | Python | MATLAB |
|---|---|---|
| `if (c) { } else if { }` | `if c: … elif …:` | `if c … elseif … end` |
| `for (x in xs) { }` | `for x in xs:` | `for x = xs … end` |
| `next` | `continue` | `continue` |
| last expression returned | explicit `return` | output variable in header |
| `...` | `*args, **kwargs` | `varargin` |
| `mean(x, na.rm = TRUE)` | `np.nanmean(x)` | `mean(x, "omitnan")` |

## In neuroscience #neuro
- **Batch processing** of per-subject files: `for (f in files) { … }` with `tryCatch()` so one corrupt file doesn't stop the loop.
- **Custom functions** for repeated steps: computing d′ from hit and false-alarm rates, summarising ERP windows, converting RTs.
- **Simulations / power analyses:** a `for` loop (or `replicate()`) that simulates data and fits a model 1000 times, with `set.seed()` ([[CS06 Data Science Workflow]]).
- **Missed responses** coded as `NA` (not 0) – models drop them; report how many.

## Math links #math-link
- Functions as mappings with parameters → [[B1 Properties of Functions]]
- d′ = $z(H) - z(FA)$ uses the inverse normal CDF (`qnorm`) → [[CS02 Probability and Statistics]]
- Logical operators and truth tables → [[E1 Sets Logic and Quantifiers]]

## Connections
- Shared concepts → [[Prog00 Shared Programming Concepts]]
- Vectorised alternatives → [[R02 R Data Structures and Vectorization]], [[R05 dplyr and tidyr]]
- NA in models → [[R07 R Statistical Modelling]]
- Testing your functions → [[R11 R Reproducible Projects]]

## Key takeaways
- `if` needs one TRUE/FALSE (use `&&`, `||`); vectors → `ifelse`/`case_when`.
- `seq_along()` instead of `1:length()`; pre-allocate.
- The last expression is returned; return lists for several values; `...` passes arguments on.
- `NA` propagates; use `na.rm = TRUE` consciously; models drop NA rows silently.
