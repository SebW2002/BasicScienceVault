---
aliases: [MATLAB Control Flow, MATLAB Functions, Anonymous Functions, varargin, nargin, Local Functions]
tags: [programming, matlab, control-flow, functions, type/overview, neuro]
---
# MAT03 MATLAB Control Flow and Functions

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT03 MATLAB Control Flow and Functions - Worksheet|✏️ Worksheet]] · [[MAT03 MATLAB Control Flow and Functions - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
Lab MATLAB code is often one long script. Splitting it into **functions** – one per processing step – makes it testable and reusable, and loops over subjects become short and clear. You also need to read toolbox code: EEGLAB's `pop_` functions and FieldTrip's `ft_` functions use `varargin`, `nargin` and configuration structs everywhere.

## Control flow: for, while, if, switch
```matlab
for s = 1:numel(subjects)               % loop over indices
    fname = fullfile("data", subjects(s) + "_eeg.set");
    if ~isfile(fname)
        warning("missing %s", fname);
        continue                         % next iteration
    end
    ...
end
for ch = ["Fz" "Cz" "Pz"]                % loop over the columns of an array
    disp(ch)
end
while err > tol && iter < 1000           % && and || for scalar conditions
    ...
    iter = iter + 1;
end
switch lower(method)
    case "welch"
        P = pwelch(x);
    case {"fft", "periodogram"}          % several values
        P = abs(fft(x)).^2;
    otherwise
        error("Unknown method: %s", method);
end
```
- Every block ends with **`end`**; indentation is only for readability.
- `for k = M` loops over the **columns** of `M`: with a column vector you get **one** iteration containing the whole vector – a classic bug. Use row vectors (`1:n`) or `k = M(:)'`.
- `if x` with a vector `x` is true only if **all** elements are nonzero (and `x` isn't empty) – write `if all(...)` or `if any(...)` explicitly.
- `break` leaves a loop, `continue` skips to the next iteration.
- **try/catch** keeps a batch loop running: `try … catch err, fprintf(2, "%s: %s\n", subj, err.message); end`.
- **Pre-allocate** results before loops (`results = zeros(n, 1);` / `cell(n, 1)`); growing arrays in loops is slow.

## Function files, local functions, anonymous functions
**Function file** `bandpower_welch.m` (file name = function name):
```matlab
function [p, f] = bandpower_welch(x, fs, band)
%BANDPOWER_WELCH  Power of x in a frequency band (Welch PSD).
%   p = bandpower_welch(x, fs, band) with band = [fmin fmax] in Hz.
    [P, f] = pwelch(x, 2*fs, fs, [], fs);
    idx = f >= band(1) & f <= band(2);
    p = trapz(f(idx), P(idx));
end
```
- Outputs are named in the header (`[p, f] = …`); whatever those variables contain at the end is returned. Callers can ask for fewer: `p = bandpower_welch(...)`; `nargout` tells how many were requested.
- The comment block after the header is the `help` text.
- **Each function has its own workspace** (local scope); it sees only its inputs. Arrays are passed **by value** (copy-on-write: MATLAB copies only if the function modifies the input), so a function can't change the caller's variables – return results instead.
- **Local functions:** additional functions at the end of a function file (or a script, R2016b+) are visible only inside that file – good for helpers.
- **Nested functions** share variables with the enclosing function (used in GUIs; use sparingly).

**Anonymous functions** – one-line functions stored in a variable (a **function handle**):
```matlab
sigmoid = @(x) 1 ./ (1 + exp(-x));
sigmoid([-2 0 2])
mexp = @(p, t) p(1) * exp(-t / p(2)) + p(3);    % model for fitting
p = lsqcurvefit(mexp, [10 0.02 -70], t, v);     % needs Optimization Toolbox
arrayfun(@(k) numel(spikes{k}), 1:numel(spikes)) % count spikes per trial
cellfun(@isempty, names)
```
`@fname` creates a handle to an existing function: `integral(@sin, 0, pi)`. Anonymous functions capture the values of variables **at the time they're created**.

## varargin, nargin, name-value arguments
```matlab
function out = preprocess(x, fs, varargin)
    % defaults
    if nargin < 2, fs = 1000; end
    opts = struct("hp", 1, "lp", 40, "notch", 50);
    for k = 1:2:numel(varargin)              % parse name-value pairs
        opts.(varargin{k}) = varargin{k+1};
    end
    ...
end
preprocess(x, 500, "lp", 30, "notch", 60)
```
- `nargin` = number of inputs actually passed; use it for defaults. `varargin` is a **cell array** of the extra inputs; `varargout` for variable outputs.
- Modern alternative (R2019b+): an **`arguments` block** declares types, sizes, defaults and validation, including name-value arguments:
```matlab
function y = lowpass_filter(x, fs, opts)
    arguments
        x (:,:) double
        fs (1,1) double {mustBePositive}
        opts.Cutoff (1,1) double = 40
        opts.Order (1,1) double {mustBeInteger} = 4
    end
    [b, a] = butter(opts.Order, opts.Cutoff / (fs/2));
    y = filtfilt(b, a, x);
end
y = lowpass_filter(x, 500, Cutoff=30);       % Name=Value syntax (R2021a+)
```
- **Configuration structs** are the other common pattern: FieldTrip's `cfg = []; cfg.bpfreq = [1 40]; data = ft_preprocessing(cfg, data);` ([[MAT10 MATLAB Neuroscience Toolboxes]]).

## Same idea in Python and R
| MATLAB | Python | R |
|---|---|---|
| `for k = 1:n … end` | `for k in range(n):` | `for (k in 1:n) { }` |
| `switch/case/otherwise` | `match`/`if-elif` | `switch()` |
| `function [a, b] = f(x)` | `def f(x): return a, b` | `f <- function(x) list(a, b)` |
| `@(x) x.^2` | `lambda x: x**2` | `\(x) x^2` |
| `varargin`, `nargin` | `*args`, defaults | `...`, `missing()` |
| `arguments` block | type hints + defaults | `stopifnot`, defaults |
| `try/catch` | `try/except` | `tryCatch` |
→ [[Py03 Python Control Flow and Functions]], [[R03 R Control Flow and Functions]]

## In neuroscience #neuro
- **Subject loop** calling one function per step (`load → preprocess → epoch → save`), with `try/catch` and a log ([[MAT12 MATLAB Reproducible Projects]]).
- **Simulations:** an Euler loop for a LIF neuron (`for k = 2:nT … if V(k) >= Vth …`) or `ode45(@(t, y) hh_rhs(t, y, I), tspan, y0)` for Hodgkin–Huxley ([[B10 Differential Equations]], [[CS10 Dynamical and Computational Neuro Models]]).
- **Toolbox APIs:** EEGLAB `pop_` functions take name-value pairs (`pop_eegfiltnew(EEG, 'locutoff', 1)`); FieldTrip uses `cfg` structs.
- **Anonymous model functions** for curve fitting (membrane time constants, psychometric functions).

## Math links #math-link
- Function definition, inputs → outputs → [[B1 Properties of Functions]]
- Euler integration in loops, `ode45` → [[B10 Differential Equations]]
- Numerical integration `trapz`, `integral` → [[B7 Antiderivatives and Integration]]

## Connections
- Shared concepts → [[Prog00 Shared Programming Concepts]]
- Vectorised alternatives to loops → [[MAT02 MATLAB Matrices and Vectorization]]
- Files and folders in loops → [[MAT04 MATLAB Data Import and Files]]
- Testing functions → [[MAT12 MATLAB Reproducible Projects]]

## Key takeaways
- `for/while/if/switch … end`; `for` loops over **columns**; `&&`/`||` in conditions.
- One function per file (name = file name), outputs named in the header, local scope, pass-by-value.
- Anonymous functions `@(x) …` for one-liners and model functions; `@fname` for handles.
- Defaults via `nargin`, extra inputs via `varargin`, or better an `arguments` block.
