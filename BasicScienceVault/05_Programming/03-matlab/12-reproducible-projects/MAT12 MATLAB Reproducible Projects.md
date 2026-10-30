---
aliases: [MATLAB Projects, matlab.unittest, MATLAB Git, MATLAB Path Management, currentProject]
tags: [programming, matlab, reproducibility, testing, version-control, type/overview, neuro]
---
# MAT12 MATLAB Reproducible Projects

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT12 MATLAB Reproducible Projects - Worksheet|✏️ Worksheet]] · [[MAT12 MATLAB Reproducible Projects - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
MATLAB code is often hard to rerun: it depends on a manually set **path**, on toolbox versions nobody wrote down, on files in someone's Desktop folder. A reproducible MATLAB project has a fixed **folder structure**, manages its **path** in code, contains **unit tests**, and lives in **Git**. Principles → [[CS13 Reproducibility and Research Software]].

## Project folders and path management
```text
oddball-eeg/
├── oddball.prj            # MATLAB Project file (optional but recommended)
├── README.md
├── startup_project.m      # adds paths, checks versions
├── code/                  # functions: preprocess_subject.m, compute_erp.m
├── scripts/               # run_all.m, 01_preprocess.m, 02_erp.m
├── tests/                 # test files
├── toolboxes/             # pinned versions of EEGLAB/FieldTrip (or document them)
├── data/raw/              # read-only (BIDS)
├── data/derived/
└── figures/
```
**Paths built from the project root – never from `cd` or absolute strings:**
```matlab
root = fileparts(fileparts(mfilename("fullpath")));   % in scripts/: one level up
% with a MATLAB Project:
proj = currentProject;  root = proj.RootFolder;       % (matlab.project.currentProject)
addpath(fullfile(root, "code"));
addpath(fullfile(root, "toolboxes", "eeglab"));  eeglab nogui
rawdir = fullfile(root, "data", "raw");
outdir = fullfile(root, "data", "derived");  if ~isfolder(outdir), mkdir(outdir); end
```
- There is **no built-in `projectroot` function**: use `currentProject().RootFolder` (R2019a+) inside a MATLAB Project, or derive the root from `mfilename("fullpath")`.
- **MATLAB Projects** (*New → Project*): open the `.prj` and MATLAB sets the project path, runs startup/shutdown files, tracks files and dependencies (*Dependency Analyzer*) and integrates with Git. Closing the project removes its paths again.
- `restoredefaultpath` before switching projects avoids leftover toolbox paths; never `savepath` toolboxes globally for a project.
- **Record versions:** `ver`, `version`, `matlabRelease` (R2020b+), toolbox versions (`eeg_getversion`, `ft_version`, `spm("Ver")`) – write them to a log or the report.
- `rng(seed)` at the start of anything random ([[Prog00 Shared Programming Concepts]]).

## Unit tests with matlab.unittest
**Function-based tests** (simplest):
```matlab
% tests/test_firing_rate.m
function tests = test_firing_rate
    tests = functiontests(localfunctions);
end

function testSimpleRate(testCase)
    verifyEqual(testCase, firing_rate(0.1:0.1:1.0, 0, 2), 5, "AbsTol", 1e-12);
end

function testEmpty(testCase)
    verifyEqual(testCase, firing_rate([], 0, 1), 0);
end

function testBadWindow(testCase)
    verifyError(testCase, @() firing_rate(1, 2, 1), ?MException);   % or a specific error ID
end
```
**Class-based tests** (fixtures, parameters):
```matlab
classdef TestBaseline < matlab.unittest.TestCase
    methods (Test)
        function meanIsZero(testCase)
            x = randn(10, 200) + 5;
            y = baseline_correct(x, 1:50);
            testCase.verifyEqual(mean(y(:, 1:50), 2), zeros(10, 1), "AbsTol", 1e-12);
        end
    end
end
```
```matlab
results = runtests("tests");          % run all tests in the folder
table(results)                        % pass/fail overview
assertSuccess(results);               % error if any test failed (for CI)
```
- `verify*` (continue after a failure) vs. `assert*` (stop the test) vs. `assume*` (skip if a precondition fails, e.g. toolbox missing).
- Useful qualifications: `verifyEqual` (with `AbsTol`/`RelTol` for floats), `verifyTrue`, `verifySize`, `verifyError`, `verifyWarning`.
- Test **known results** (a pure sine → spectral peak at its frequency; exponential decay → τ), **invariants** (baseline mean 0, sizes), **edge cases** (empty, NaN), and every bug you fix.
- `buildtool` (R2022b+) with a `buildfile.m` can run tests and other tasks; GitHub Actions has official MATLAB actions for continuous integration.

## Version control with Git
- MATLAB has built-in Git support (*Source Control* panel, Projects integration): commit, branch, diff, push.
- Commit `.m` functions, scripts, tests, the `.prj` and its `resources/` folder, README, and small metadata; not raw data, derived data or large `.mat` files (use `.gitignore`; data in DataLad/OpenNeuro/DANDI).
- `.mlx` and `.mat` are binary – diffs are poor; MATLAB's comparison tool can diff them inside MATLAB, but plain `.m` is better for code under version control ([[MAT11 MATLAB Live Scripts and Reports]]).
- **Toolboxes:** record exact versions (tag/commit) – as Git submodules, a `toolboxes/` folder with a README, or at least in the methods.
- Tag the commit that produced a paper's results (`git tag v1.0-submission`); archive it with a DOI (Zenodo).

## Same idea in Python and R
Python: `pathlib` + project root, environments, pytest ([[Py13 Python Reproducible Projects and Testing]]). R: RStudio Projects + `here`, renv, testthat ([[R11 R Reproducible Projects]]). MATLAB lacks a standard environment/lock file for third-party toolboxes – so documenting and pinning toolbox versions is your job.

## In neuroscience #neuro
- **EEGLAB/FieldTrip/SPM versions** change defaults (filters, ICA, normalisation templates) – pin and report them.
- **Batch over subjects** with `run_all.m` that logs successes/failures and versions; can run on a cluster with `matlab -batch "run_all"`.
- **Tests on simulated data:** an ERP pipeline should recover a simulated P300 of known amplitude and latency; a spike detector should find simulated spikes ([[CS11 Time Series and Signal Processing]]).
- **Sharing:** many journals require code; a Project + README + tagged release makes it runnable for reviewers.

## Math links #math-link
- Known analytical results as test oracles (e.g. LIF ISI $\tau\ln\frac{RI}{RI - \Delta V}$) → [[B10 Differential Equations]]
- Float tolerances → [[Prog00 Shared Programming Concepts]]

## Connections
- Path problems and shadowing → [[MAT01 MATLAB Basics and Syntax]]
- Folders and files → [[MAT04 MATLAB Data Import and Files]]
- Reports → [[MAT11 MATLAB Live Scripts and Reports]]
- Principles → [[CS13 Reproducibility and Research Software]]

## Key takeaways
- Fixed folder layout; paths from the project root with `fullfile` (`currentProject().RootFolder` or `mfilename("fullpath")`) – no `projectroot` built-in.
- MATLAB Projects manage paths, startup files and Git; `restoredefaultpath` between projects.
- `matlab.unittest`: function-based (`functiontests`) or class-based tests, `verifyEqual` with tolerances, `runtests`.
- Git for code (plain `.m`), not data; pin and report MATLAB and toolbox versions; `rng(seed)`.
