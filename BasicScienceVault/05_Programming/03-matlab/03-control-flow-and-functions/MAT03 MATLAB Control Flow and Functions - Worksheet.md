---
tags: [programming, matlab, type/worksheet]
---
# MAT03 MATLAB Control Flow and Functions – Worksheet

> Theory: [[MAT03 MATLAB Control Flow and Functions]] · Solutions: [[MAT03 MATLAB Control Flow and Functions - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Predict the output
1. ```matlab
   s = 0;
   for k = 1:10
       if mod(k, 4) == 0, break; end
       if mod(k, 2) == 0, continue; end
       s = s + k;
   end
   s
   ```
2. `for k = [1; 2; 3], disp(size(k)), end` – how many lines and what?
3. `if [1 1 0], disp("yes"), else, disp("no"), end`
4. `f = @(x) 2*x + 1; f([0 1 2])`

## Level 2 – Functions
5. A file `myfilter.m` starts with `function y = bandpass(x, fs)`. You call `myfilter(x, 500)`. What happens? What's the rule?
6. `function [m, s] = stats(x)`: what do `a = stats(x)` and `[a, b] = stats(x)` return?
7. Inside a function you do `x(1) = 0;` on an input array. Does the caller's array change? Why?
8. `a = 2; g = @(x) a * x; a = 10; g(1)` – result? Why?

## Level 3 – Write code
9. Write a function `rate = firing_rate(spike_times, t_start, t_end)` with help text that counts spikes in the window and divides by its length. Make `t_start` default to 0 when only one input is given.
10. Write a `switch` that maps `"delta"`, `"theta"`, `"alpha"`, `"beta"` to frequency bands `[1 4]`, `[4 8]`, `[8 13]`, `[13 30]` and errors otherwise.
11. Rewrite the default/parsing logic of task 9 with an `arguments` block.

## Level 4 – Neuro transfer
12. Write the Euler loop for a LIF neuron: `dt = 1e-4`, `tau = 0.02`, `EL = -0.07`, `Vth = -0.05`, `Vreset = -0.07`, `R*I = 0.025` V for 0.5 s; store spike times. Which loop/condition constructs do you need?
13. Write a subject loop over `subs = ["sub-01" "sub-02" "sub-03"]` that calls `run_pipeline(sub)`, catches errors and records which subjects failed.
14. 💻 Implement task 12, count the spikes, and compare the ISI with the analytical value $\tau\ln\frac{RI}{RI - (V_{th} - E_L)}$.
