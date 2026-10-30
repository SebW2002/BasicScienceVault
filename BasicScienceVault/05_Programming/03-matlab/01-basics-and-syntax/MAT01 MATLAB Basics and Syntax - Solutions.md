---
tags: [programming, matlab, type/solution]
---
# MAT01 MATLAB Basics and Syntax – Solutions

> Worksheet: [[MAT01 MATLAB Basics and Syntax - Worksheet]] · Theory: [[MAT01 MATLAB Basics and Syntax]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. a) `x = 5` b) nothing c) `y = 1 2 3` (as a row) d) `'double'` e) `'int8'`.
2. `127` (saturates at the int8 maximum), `4` (3.5 rounded), `0` (unsigned saturates at 0).
3. `5`, `1` (one string object), `5`.
4. `'FzCz'` – 1 × 4 char; `["Fz" "Cz"]` – 1 × 2 string array; `"FzCz"` (1 × 1 string).

## Level 2
5. Char arrays are numeric character codes: 'a' = 97, 'b' = 98, 'c' = 99, 'd' = 100; `+` adds them element-wise: 97 + 99 = 196, 98 + 100 = 198.
6. `==` on char arrays compares element by element and needs equal lengths ('Cz' has 2, 'Pz1' has 3 characters) → error; with equal lengths it would return a logical vector, not one true/false. Use `strcmp(name, 'Cz')`, or strings: `string(name) == "Cz"`.
7. The variable `mean` shadows the function; `mean([1 2 3])` is interpreted as indexing the variable at positions 1, 2, 3. Fix: `clear mean` and don't use function names as variable names.
8. The toolbox contains its own `filter.m` that shadows MATLAB's built-in. `which -all filter` lists all `filter` functions on the path and which one is used.

## Level 3
9. `fname = sprintf('sub-%02d_ses-%02d_eeg.set', s, ses);` and `fname = "sub-" + compose("%02d", s) + "_ses-" + compose("%02d", ses) + "_eeg.set";`
10. `fprintf('Subject %d: %.1f %% correct\n', s, acc * 100);` (`%%` prints a literal `%`).
11. `mean` of integer input returns a **double** by default: (30000 + 30000 − 100)/3 = 19966.67. `sum` of integers by default returns the **same integer class** (`'native'` for integers) → saturates at 32767. Safe: `x = double(raw); sum(x)` → 59900, `mean(x)` → 19966.67 (or `sum(raw, 'double')`).

## Level 4
12. A manually set path differs between computers and sessions; scripts then call other toolbox versions or shadowed functions. Explicit `addpath` (or a project startup file, [[MAT12 MATLAB Reproducible Projects]]) documents exactly which toolboxes and versions are used and makes the script run elsewhere.
13. `names = string(names); clean = names + "_clean";` (string arrays support element-wise `+`).
14. In MATLAB: `int8(100) + int8(50)` → `127`; `'ab' + 'cd'` → `196 198`; `which -all mean` → the built-in plus any shadowing files. (GNU Octave behaves the same for integer saturation and char arithmetic; its string support differs.)
