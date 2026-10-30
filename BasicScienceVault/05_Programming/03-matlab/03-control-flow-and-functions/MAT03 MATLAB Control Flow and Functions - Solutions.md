---
tags: [programming, matlab, type/solution]
---
# MAT03 MATLAB Control Flow and Functions – Solutions

> Worksheet: [[MAT03 MATLAB Control Flow and Functions - Worksheet]] · Theory: [[MAT03 MATLAB Control Flow and Functions]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. k = 1 → s = 1; k = 2 skipped; k = 3 → s = 4; k = 4 → break. **s = 4**.
2. **One** line: `3 1` – the loop runs over the columns of a 3 × 1 vector, i.e. once, with `k` being the whole column.
3. `no` – not all elements are nonzero.
4. `[1 3 5]` (the expression is element-wise).

## Level 2
5. MATLAB uses the **file name**: `myfilter(x, 500)` runs the function in `myfilter.m` (with a warning in the editor that names differ); `bandpass(...)` would not be found. Rule: the main function's name should equal the file name.
6. `a = stats(x)` → only the first output `m`; `[a, b] = stats(x)` → `m` and `s`.
7. No. Inputs are passed by value (copy-on-write): modifying `x` inside creates a local copy. Return the modified array and assign it in the caller.
8. `2`: the anonymous function captured `a = 2` when it was created; later changes to `a` don't affect it.

## Level 3
9. ```matlab
   function rate = firing_rate(spike_times, t_start, t_end)
   %FIRING_RATE  Mean firing rate (Hz) of spikes in [t_start, t_end).
   %   rate = firing_rate(spike_times, t_end) uses t_start = 0.
       if nargin == 2
           t_end = t_start;
           t_start = 0;
       end
       n = sum(spike_times >= t_start & spike_times < t_end);
       rate = n / (t_end - t_start);
   end
   ```
10. ```matlab
    switch band_name
        case "delta", band = [1 4];
        case "theta", band = [4 8];
        case "alpha", band = [8 13];
        case "beta",  band = [13 30];
        otherwise, error("Unknown band: %s", band_name);
    end
    ```
11. ```matlab
    function rate = firing_rate(spike_times, t_end, opts)
        arguments
            spike_times (:,1) double
            t_end (1,1) double {mustBePositive}
            opts.TStart (1,1) double = 0
        end
        n = sum(spike_times >= opts.TStart & spike_times < t_end);
        rate = n / (t_end - opts.TStart);
    end
    % firing_rate(st, 2, TStart=0.5)
    ```
    (Positional optional arguments *before* required ones aren't possible in an `arguments` block, so the window start becomes a name-value option.)

## Level 4
12. ```matlab
    dt = 1e-4; T = 0.5; nT = round(T/dt);
    tau = 0.02; EL = -0.07; Vth = -0.05; Vreset = -0.07; RI = 0.025;
    V = EL; spikes = [];
    for k = 1:nT                                % for loop: each step depends on the previous
        V = V + dt/tau * (-(V - EL) + RI);
        if V >= Vth                             % threshold condition
            spikes(end+1) = k * dt;  %#ok<AGROW>
            V = Vreset;
        end
    end
    ```
13. ```matlab
    failed = strings(0);
    for sub = subs
        try
            run_pipeline(sub);
        catch err
            fprintf(2, "%s failed: %s\n", sub, err.message);
            failed(end+1) = sub; %#ok<AGROW>
        end
    end
    ```
14. Analytical ISI = $0.02\cdot\ln\frac{0.025}{0.025 - 0.02} = 0.02\ln5\approx32.2$ ms → about 15 spikes in 0.5 s; `diff(spikes)` ≈ 0.0322 s (slightly different due to the time step).
