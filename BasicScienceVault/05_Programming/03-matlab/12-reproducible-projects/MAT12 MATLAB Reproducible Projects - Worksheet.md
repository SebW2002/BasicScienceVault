---
tags: [programming, matlab, reproducibility, type/worksheet]
---
# MAT12 MATLAB Reproducible Projects – Worksheet

> Theory: [[MAT12 MATLAB Reproducible Projects]] · Solutions: [[MAT12 MATLAB Reproducible Projects - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Recall
1. How do you get the project root folder a) inside a MATLAB Project b) in a plain script stored in `scripts/`?
2. What do `restoredefaultpath`, `ver` and `matlabRelease` do?
3. What is the difference between `verifyEqual`, `assertEqual` and `assumeTrue` in a test?
4. Which files of a MATLAB analysis belong in Git, and which do not?

## Level 2 – Understanding
5. A script starts with `cd('C:\Users\anna\Documents\EEG'); addpath(genpath('C:\toolboxes'))`. Name three problems.
6. Why are tests with `verifyEqual(testCase, a, b)` without tolerance risky for floating-point results?
7. Your analysis gives different ICA components on the cluster than on your laptop. Name two causes and fixes.
8. Why is it useful to keep a pinned copy (or an exact version tag) of EEGLAB/FieldTrip with a project?

## Level 3 – Write tests
9. Write a function-based test file `test_dprime.m` for `dprime(hit, fa)`: equal rates → 0; `dprime(0.84, 0.16)` ≈ 1.989 (tolerance 1e-3); rates of 1 → error.
10. Write a class-based test that checks `bandpower_welch(x, fs, [8 12])` is larger for a 10 Hz sine than for a 20 Hz sine of the same amplitude.
11. Write the command to run all tests in `tests/` and fail (error) if any test fails.

## Level 4 – Neuro transfer
12. Draft the structure of `run_all.m` for 25 subjects: path setup, version logging, subject loop with try/catch and a summary table of failures.
13. A reviewer asks for your code. List what you send so that the reviewer can reproduce Figure 3.
14. 💻 Create a small project folder with `code/firing_rate.m` and `tests/test_firing_rate.m` (from the note), run `runtests("tests")`, then introduce a bug and observe the failure report.
