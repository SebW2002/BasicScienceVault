---
tags: [programming, matlab, type/worksheet]
---
# MAT01 MATLAB Basics and Syntax – Worksheet

> Theory: [[MAT01 MATLAB Basics and Syntax]] · Solutions: [[MAT01 MATLAB Basics and Syntax - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Predict the output
1. What is displayed? a) `x = 5` b) `x = 5;` c) `y = [1 2 3]` d) `class(7)` e) `class(int8(7))`
2. `int8(100) + int8(50)`, `int16(7) / int16(2)`, `uint8(3) - uint8(5)`
3. `length('gamma')`, `length("gamma")`, `strlength("gamma")`
4. `['Fz' 'Cz']`, `["Fz" "Cz"]` – sizes and classes? `"Fz" + "Cz"`?

## Level 2 – Traps
5. `'ab' + 'cd'` returns `[196 198]`. Why?
6. `if name == 'Cz'` errors when `name = 'Pz1'`. Why? Two correct ways to compare.
7. You set `mean = 3;` earlier. Now `mean([1 2 3])` returns an error ("Index exceeds…"). Why, and how do you fix it?
8. A script calls `filter(b, a, x)` but behaves strangely after you added a toolbox to the path. What could have happened? Which command helps?

## Level 3 – Write code
9. Create the char file name `'sub-03_ses-01_eeg.set'` from `s = 3; ses = 1;` with `sprintf`, and the same as a string with `+` and `compose`.
10. Print `Subject 3: 87.5 % correct` with `fprintf` from `s = 3; acc = 0.875;`.
11. Raw ADC values `raw = int16([30000 30000 -100])`. What does `mean(raw)` give, and what does `sum(raw)` give? (Hint: check the MATLAB docs for the output type of `sum` on integers – default `'native'`? or `'double'`?) Write the safe version.

## Level 4 – Neuro transfer
12. Why should every EEGLAB/FieldTrip analysis script start with explicit `addpath` commands (or a startup function) rather than relying on a manually set path?
13. Your colleague's code uses `cellfun(@(c) [c '_clean'], names, 'UniformOutput', false)` on a cell array of char. Rewrite with a string array.
14. 💻 In MATLAB (or GNU Octave), verify tasks 2–5 and print `which -all mean`.
