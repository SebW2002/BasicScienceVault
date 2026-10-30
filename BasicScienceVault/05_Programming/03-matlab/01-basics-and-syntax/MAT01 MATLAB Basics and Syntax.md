---
aliases: [MATLAB Basics, MATLAB Syntax, Command Window, char vs string, Live Editor]
tags: [programming, matlab, syntax, type/overview, neuro]
---
# MAT01 MATLAB Basics and Syntax

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT01 MATLAB Basics and Syntax - Worksheet|✏️ Worksheet]] · [[MAT01 MATLAB Basics and Syntax - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
MATLAB ("MATrix LABoratory") has been the language of systems and cognitive neuroscience for decades: EEGLAB, FieldTrip, SPM, Psychtoolbox and countless lab scripts are MATLAB. Even if you mainly use Python, you'll read and run MATLAB code. Its basics are simple; the traps are **semicolons**, **1-based indexing** and the two kinds of text: **char vs. string**.

## Command Window, Editor, Live Scripts
| Part | What it is |
|---|---|
| **Command Window** | type a command, press Enter, see the result (`>>` prompt) |
| **Editor** | write **scripts** (`.m`) and **functions** (`.m` with `function` header); run with F5 or by typing the file name |
| **Live Editor** | **Live Scripts** (`.mlx`): code, formatted text, equations and output in one document ([[MAT11 MATLAB Live Scripts and Reports]]) |
| **Workspace** | all current variables (`whos` in the command window) |
| **Current Folder** | the working directory (`pwd`, `cd`); files here and on the **path** can be called |
- **Code sections:** `%%` starts a section in a script; **Ctrl + Enter** runs the current section – MATLAB's version of notebook cells.
- **The path:** MATLAB finds functions in the current folder and in folders on the search path (`addpath("toolboxes/eeglab")`, `path`, `which fname`). Two functions with the same name → the first on the path wins (**shadowing**): `which -all filter` shows all candidates.
- `clear` deletes variables, `clc` clears the screen, `close all` closes figures. `clear all` also unloads functions and breakpoints – rarely what you want in a script.

## Semicolon suppression, comments, help
```matlab
fs = 1000           % no semicolon: result is printed:  fs = 1000
x = randn(1, 1e6);  % semicolon: suppress output (essential for big arrays!)
% single-line comment
%{
  block comment
%}
v = [1 2 3 ...
     4 5 6];        % ... continues a line
help mean           % short help in the command window
doc mean            % full documentation page with examples
lookfor spectrum    % search help texts
```
- A missing semicolon in a loop prints every iteration and can slow a script dramatically.
- The first comment block of your own function is its `help` text.

## Variables and data types
```matlab
a = 3;            % double (the default numeric type!)
b = int16(3);     % 16-bit integer (raw EEG/ADC data)
c = single(3);    % 32-bit float (memory, GPUs)
d = true;         % logical
z = 3 + 4i;       % complex: abs(z) = 5, angle(z)
x = [1 2 3];      % row vector (spaces or commas)
y = [1; 2; 3];    % column vector (semicolons)
class(a), whos, isa(b, "integer"), isempty([])
1/0, -1/0, 0/0    % Inf, -Inf, NaN
```
- **Everything is a matrix:** a scalar is 1 × 1, a row vector 1 × n ([[MAT02 MATLAB Matrices and Vectorization]]).
- **Integer arithmetic saturates and rounds:** `int8(100) + int8(100)` = 127 (not overflow-wrap like C/NumPy); `int16(7) / int16(2)` = 4 (rounded). Convert raw data with `double(x)` before computing.
- Names are case-sensitive; don't overwrite built-ins (`sum = 5` breaks `sum()` until you `clear sum`).
- Other containers: **cell arrays** `{}` (mixed contents), **structs** `s.fs = 1000`, **tables** ([[MAT04 MATLAB Data Import and Files]]).

## Text: char vs. string
| | char array `'...'` | string `"..."` (R2016b+) |
|---|---|---|
| what it is | a row vector of characters (numbers underneath) | one text object (a 1 × 1 string array) |
| `length('theta')` / `strlength("theta")` | 5 | `length("theta")` = 1! use `strlength` → 5 |
| concatenation | `['sub-' '01']` → `'sub-01'` | `"sub-" + "01"` → `"sub-01"` |
| `+` | **adds character codes**: `'ab' + 'cd'` = `[196 198]` | joins text |
| arrays of text | rows must have equal length → use cell `{'Fz','Cz'}` | `["Fz" "Cz" "Pz"]` is a 1 × 3 string array |
| comparison | `strcmp(a, b)` (`==` compares character by character) | `a == b` works |
```matlab
subj = 7;
fname = sprintf('sub-%02d_task-rest_eeg.set', subj);   % char:  'sub-07_task-rest_eeg.set'
fname = "sub-" + compose("%02d", subj) + "_eeg.set";   % string
fprintf('Rate: %.1f Hz\n', 12.34);                      % print formatted text
num2str(pi, 4), str2double("0.5"), string(12), char("abc")
contains("sub-07_bold", "bold"), split("a_b_c", "_"), strrep(fname, ".set", ".fdt")
```
Older code and toolboxes (EEGLAB, SPM) use **char** and cell arrays of char; newer functions accept both. Convert with `string()`/`char()`/`cellstr()` when needed.

## Same idea in Python and R
| MATLAB | Python | R |
|---|---|---|
| `%` comment | `#` | `#` |
| `;` suppresses output | – (scripts don't print) | – |
| `help`, `doc` | `help()` | `?` |
| `x = [1 2 3]` | `np.array([1, 2, 3])` | `c(1, 2, 3)` |
| `"str"` / `'char'` | `str` | character |
| `sprintf` | f-strings | `sprintf` |
| `%%` sections | `# %%` cells | RStudio chunks |
→ [[Py01 Python Basics and Syntax]], [[R01 R Basics and Syntax]]

## In neuroscience #neuro
- **File names in loops** with `sprintf('sub-%02d', s)` for BIDS-like datasets.
- **Raw data types:** amplifier data often arrive as `int16`/`int32`; integer saturation and rounding silently distort averages if not converted to `double`.
- **Shadowing:** EEGLAB, FieldTrip and SPM all ship functions with common names; adding several toolboxes to the path at once causes "wrong function called" bugs – add only what you need (`ft_defaults` manages FieldTrip's path).
- **Command-window history** of a GUI session (EEGLAB's `eegh`) can be copied into a script for reproducibility ([[MAT09 EEGLAB]]).

## Math links #math-link
- Scientific notation `1e-3`, powers → [[A1 Exponent Rules]]
- Complex numbers `3 + 4i`, `abs`, `angle` → [[E2 Complex Numbers]]
- Vectors and matrices as the basic type → [[C1 Matrices]], [[D1 Vectors in 2D and 3D]]

## Connections
- Shared concepts (1-based indexing, types, NaN) → [[Prog00 Shared Programming Concepts]]
- Matrices → [[MAT02 MATLAB Matrices and Vectorization]]; functions → [[MAT03 MATLAB Control Flow and Functions]]
- Live Scripts → [[MAT11 MATLAB Live Scripts and Reports]]

## Key takeaways
- Command Window for quick checks, Editor for scripts/functions, Live Editor for documents; `%%` sections.
- End lines with `;` to suppress output; `help`/`doc` for documentation.
- Default type is double; integers saturate and round – convert raw data.
- `'char'` is a character vector (`+` adds codes), `"string"` is a text object (`+` joins).
