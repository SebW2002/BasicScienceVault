---
aliases: [Mistake Log MATLAB, Fehler MATLAB, MATLAB Bugs]
tags: [programming, matlab, type/mistakes]
---
# ⚠️ Mistakes – MATLAB

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · Template: [[Mistake Entry Template]]

**How to use:** after every worksheet – and every real bug – add a row to *My mistakes* with the quick check that would have caught it.

## Classic traps (pre-filled)
| ❌ Wrong | ✅ Right | Quick check / why | Topic |
|---|---|---|---|
| missing `;` on big arrays / in loops | end lines with `;` | console floods, slow | [[MAT01 MATLAB Basics and Syntax]] |
| variable named `mean`, `sum`, `filter`, `all`, `i` | other names; `clear mean` | built-in shadowed | [[MAT01 MATLAB Basics and Syntax]] |
| `'ab' + 'cd'` to join text | `['ab' 'cd']` or `"ab" + "cd"` | char + char adds codes | [[MAT01 MATLAB Basics and Syntax]] |
| `length("text")` for characters | `strlength("text")` | string is 1 × 1 | [[MAT01 MATLAB Basics and Syntax]] |
| `name == 'Cz'` for chars | `strcmp(name, 'Cz')` | length mismatch error | [[MAT01 MATLAB Basics and Syntax]] |
| computing with raw `int16` | `double(x)` first | integers saturate and round | [[MAT01 MATLAB Basics and Syntax]] |
| two toolboxes with the same function on the path | add only what's needed; `which -all f` | wrong function called | [[MAT01 MATLAB Basics and Syntax]] |
| `x * y` for element-wise product | `x .* y` | dimension error or matrix product | [[MAT02 MATLAB Matrices and Vectorization]] |
| `x ^ 2` on vectors | `x .^ 2` | needs square matrix | [[MAT02 MATLAB Matrices and Vectorization]] |
| `1 / x` element-wise | `1 ./ x` | – | [[MAT02 MATLAB Matrices and Vectorization]] |
| `x'` on complex data meaning plain transpose | `x.'` | `'` conjugates | [[MAT02 MATLAB Matrices and Vectorization]] |
| `mean(X)` on channels × time | `mean(X, 2)` (or the dimension you mean) | default dimension 1 | [[MAT02 MATLAB Matrices and Vectorization]] |
| `x(0)` / Python-style indices | `x(1)`; `x(end)` | 1-based | [[MAT02 MATLAB Matrices and Vectorization]] |
| `reshape` assumed row-wise | column-major | print a small example | [[MAT02 MATLAB Matrices and Vectorization]] |
| `inv(A) * b` | `A \ b` | accuracy | [[MAT02 MATLAB Matrices and Vectorization]] |
| growing arrays in loops | pre-allocate `zeros(n, 1)` | slow; editor warning | [[MAT03 MATLAB Control Flow and Functions]] |
| `for k = colvec` | `for k = colvec'` or `1:numel(colvec)` | one iteration only | [[MAT03 MATLAB Control Flow and Functions]] |
| `if vector` | `if all(...)` / `any(...)` | true only if all nonzero | [[MAT03 MATLAB Control Flow and Functions]] |
| `&` / `\|` in scalar `if` conditions | `&&` / `\|\|` | no short-circuit | [[MAT03 MATLAB Control Flow and Functions]] |
| function name ≠ file name | match them | file name wins | [[MAT03 MATLAB Control Flow and Functions]] |
| expecting a function to modify its input | return and reassign | pass by value | [[MAT03 MATLAB Control Flow and Functions]] |
| anonymous function expected to see later variable changes | recreate the handle | values captured at creation | [[MAT03 MATLAB Control Flow and Functions]] |
| `load("x.mat")` into the workspace | `S = load("x.mat")` | variables overwritten silently | [[MAT04 MATLAB Data Import and Files]] |
| `c(2)` when the content is needed | `c{2}` | `()` returns a cell | [[MAT04 MATLAB Data Import and Files]] |
| string concatenation of paths `[dir '/' f]` | `fullfile(dir, f)` | OS separators | [[MAT04 MATLAB Data Import and Files]] |
| `dir` order assumed numeric | zero-pad IDs / sort numerically | sub-10 before sub-2 | [[MAT04 MATLAB Data Import and Files]] |
| event `latency` treated as seconds | samples: `(lat − 1)/srate` | – | [[MAT04 MATLAB Data Import and Files]] |
| `plot` twice without `hold on` | `hold on` | first line disappears | [[MAT05 MATLAB Plotting]] |
| spectrogram upside down with `imagesc` | `axis xy` | low frequencies at the top | [[MAT05 MATLAB Plotting]] |
| `jet` / uncentred diverging maps | `parula`/uniform maps; symmetric `clim` | false edges | [[MAT05 MATLAB Plotting]] |
| exporting at screen size | set figure size in cm, `exportgraphics` vector | tiny fonts | [[MAT05 MATLAB Plotting]] |
| `butter(4, 40)` with Hz | `butter(4, 40/(fs/2))` | Wn must be < 1 | [[MAT06 MATLAB Signal Processing Toolbox]] |
| `filtfilt` on channels × time | transpose: works along columns | filters across channels | [[MAT06 MATLAB Signal Processing Toolbox]] |
| `filter` for ERP latencies | `filtfilt` offline | phase delay | [[MAT06 MATLAB Signal Processing Toolbox]] |
| high-order `[b, a]` IIR at very low cut-offs | SOS (`zp2sos`), `designfilt`, FIR | unstable, NaN | [[MAT06 MATLAB Signal Processing Toolbox]] |
| unscaled `abs(fft(x))` as amplitude | divide by N, double one-sided | peak ≠ amplitude | [[MAT06 MATLAB Signal Processing Toolbox]] |
| `findpeaks` distances in samples assumed seconds | pass `fs` | many peaks per spike | [[MAT06 MATLAB Signal Processing Toolbox]] |
| `ttest2` default assumed Welch | `"Vartype", "unequal"` | Student by default | [[MAT07 MATLAB Statistics Toolbox]] |
| reporting only `h` | statistic, df, p, CI, effect size | – | [[MAT07 MATLAB Statistics Toolbox]] |
| text column as predictor in `fitlm` without categorical | `categorical()` + reference level | – | [[MAT07 MATLAB Statistics Toolbox]] |
| permutation p = count/nPerm | (count + 1)/(nPerm + 1) | p = 0 impossible | [[MAT07 MATLAB Statistics Toolbox]] |
| `SkipSyncTests = 1` in data collection | 0; fix the display setup | timing unknown | [[MAT08 Psychtoolbox]] |
| `MakeTexture` inside trials | preload | missed flips | [[MAT08 Psychtoolbox]] |
| RT from `GetSecs` before `Flip` | use the flip timestamp | up to 1 frame error | [[MAT08 Psychtoolbox]] |
| no `try/catch` + `sca` | wrap the experiment | black screen after error | [[MAT08 Psychtoolbox]] |
| `pop_rmbase` in seconds | milliseconds; `pop_epoch` in seconds | baseline wrong | [[MAT09 EEGLAB]] |
| ICA on 0.1 Hz-filtered data | ICA on a 1 Hz copy, apply weights | poor components | [[MAT09 EEGLAB]] |
| ICA ignoring rank after average reference/interpolation | `"pca", rank` | ghost components | [[MAT09 EEGLAB]] |
| only GUI clicks, no script | copy `eegh`/`EEG.history` into a script | not reproducible | [[MAT09 EEGLAB]] |
| "FieldTrip" without version in methods | report version/date | defaults change | [[MAT10 MATLAB Neuroscience Toolboxes]] |
| results depend on leftover workspace in `publish` | `clear; close all` at the top | stale figures/variables | [[MAT11 MATLAB Live Scripts and Reports]] |
| `.mlx` as the only copy of analysis code in git | plain `.m` functions | binary diffs | [[MAT11 MATLAB Live Scripts and Reports]] |
| `cd`/absolute paths, `addpath(genpath(...))` of everything | project root + `fullfile`, targeted `addpath` | breaks elsewhere, shadowing | [[MAT12 MATLAB Reproducible Projects]] |
| `projectroot` assumed to exist | `currentProject().RootFolder` / `mfilename("fullpath")` | undefined function | [[MAT12 MATLAB Reproducible Projects]] |
| float tests without tolerance | `"AbsTol"`/`"RelTol"` | spurious failures | [[MAT12 MATLAB Reproducible Projects]] |

## My mistakes
| Date | ❌ What I did | ✅ Correct | Why / quick check | Link |
|---|---|---|---|---|
| | | | | |

## Patterns I notice
- 
