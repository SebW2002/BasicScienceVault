---
tags: [programming, matlab, reproducibility, type/solution]
---
# MAT12 MATLAB Reproducible Projects – Solutions

> Worksheet: [[MAT12 MATLAB Reproducible Projects - Worksheet]] · Theory: [[MAT12 MATLAB Reproducible Projects]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. a) `proj = currentProject; root = proj.RootFolder;` b) `root = fileparts(fileparts(mfilename("fullpath")));` (folder of the script, then one level up).
2. `restoredefaultpath` resets the search path to MATLAB's factory default (removing all added toolboxes); `ver` lists MATLAB and installed toolbox versions; `matlabRelease` returns the release (e.g. R2025b) as an object.
3. `verifyEqual`: records a failure and continues the test; `assertEqual`: records a failure and stops the current test; `assumeTrue`: if false, marks the test as filtered/skipped (precondition not met, e.g. toolbox missing) rather than failed.
4. In Git: `.m` code, tests, the `.prj` and `resources/project`, README, small config/metadata files, `.gitignore`. Not: raw/derived data, large `.mat` files, figures that can be regenerated, (usually) third-party toolboxes themselves (document their versions instead, or use submodules).

## Level 2
5. Absolute paths only exist on Anna's PC; `cd` makes behaviour depend on where you are; `genpath` on a folder of toolboxes adds **everything**, including conflicting versions and their test folders (shadowing); toolbox versions are undocumented.
6. Floating-point results differ in the last bits depending on operation order, CPU and MATLAB version; exact equality can fail although the result is correct. Use `"AbsTol"`/`"RelTol"`.
7. Different MATLAB/toolbox versions (or different BLAS/CPU libraries) – pin and log versions; random initialisation without a fixed seed – set `rng(seed)` before `runica` (and store the ICA weights so you don't need to recompute).
8. Toolbox updates change defaults and fix (or introduce) bugs; with a pinned version you can rerun the analysis years later and get the same results, and you can report the exact version.

## Level 3
9. ```matlab
   function tests = test_dprime
       tests = functiontests(localfunctions);
   end
   function testEqualRates(tc)
       verifyEqual(tc, dprime(0.7, 0.7), 0, "AbsTol", 1e-12);
   end
   function testKnownValue(tc)
       verifyEqual(tc, dprime(0.84, 0.16), 1.989, "AbsTol", 1e-3);
   end
   function testRateOfOne(tc)
       verifyError(tc, @() dprime(1, 0.2), ?MException);
   end
   ```
   (Requires `dprime` to check its inputs and throw an error for rates of 0 or 1.)
10. ```matlab
    classdef TestBandpower < matlab.unittest.TestCase
        methods (Test)
            function alphaPeak(tc)
                fs = 250; t = 0:1/fs:10-1/fs;
                p10 = bandpower_welch(sin(2*pi*10*t), fs, [8 12]);
                p20 = bandpower_welch(sin(2*pi*20*t), fs, [8 12]);
                tc.verifyGreaterThan(p10, 100 * p20);
            end
        end
    end
    ```
11. `results = runtests("tests"); assertSuccess(results);` (or from the shell: `matlab -batch "assertSuccess(runtests('tests'))"`).

## Level 4
12. ```matlab
    % run_all.m
    root = fileparts(fileparts(mfilename("fullpath")));
    restoredefaultpath; addpath(fullfile(root, "code"));
    addpath(fullfile(root, "toolboxes", "eeglab")); eeglab nogui
    logf = fopen(fullfile(root, "logs", "run_" + string(datetime("now", "Format", "yyyyMMdd_HHmm")) + ".txt"), "w");
    fprintf(logf, "MATLAB %s, EEGLAB %s\n", version, eeg_getversion);
    rng(1234);
    subs = "sub-" + compose("%02d", (1:25)');
    status = strings(25, 1);
    for k = 1:25
        try
            preprocess_subject(subs(k), root);
            status(k) = "ok";
        catch err
            status(k) = "FAILED: " + err.message;
        end
        fprintf(logf, "%s: %s\n", subs(k), status(k));
    end
    fclose(logf);
    disp(table(subs, status));
    ```
13. A link to the repository (tagged release/DOI) with: README (requirements, MATLAB release, toolbox versions, data source, run order), all functions and scripts, the exact parameters/config, tests, instructions on where to put the data (BIDS), and which script produces Figure 3 (plus expected runtime); the data themselves via a repository (OpenNeuro, DANDI, OSF) if allowed.
14. `runtests("tests")` → table shows e.g. 3 passed. After changing `firing_rate` to `n * (t_end - t_start)`, `testSimpleRate` fails with a diagnostic showing "Actual Value: 20, Expected Value: 5" (10 spikes × 2 s instead of 10 / 2 s).
