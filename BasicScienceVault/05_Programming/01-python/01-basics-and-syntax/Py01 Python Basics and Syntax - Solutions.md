---
tags: [programming, python, type/solution]
---
# Py01 Python Basics and Syntax – Solutions

> Worksheet: [[Py01 Python Basics and Syntax - Worksheet]] · Theory: [[Py01 Python Basics and Syntax]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. `3.5`, `3`, `-4` (floor rounds towards −∞), `1`, `512` (`**` is right-associative: $2^{(3^2)} = 2^9$).
2. `"am"` (indices 1, 2), `"ma"`, `6`, `"007"`.
3. `False`, `True` (non-empty string), `False`, `True`.
4. `3` (truncates), `2`, `4` (Python rounds halves to the nearest **even** number, "banker's rounding"), `0.001`.

## Level 2
5. `1`. `^` is bitwise XOR (binary 10 XOR 11 = 01). Power is `**`.
6. `print(f"sub-{s:02d} | {r:.2f} Hz | p = {p:.1e}")`
7. `return` is indented inside the loop, so the function returns after the first element. Dedent `return s` to the function level.
8. E.g. cells run out of order, a variable defined in a deleted cell still exists in memory, or a cell was edited but not re-run. The script always starts from a clean state.

## Level 3
9. ```python
   def samples_to_ms(n, fs):
       """Convert a number of samples to milliseconds.

       n  : number of samples
       fs : sampling rate in Hz
       """
       return n / fs * 1000
   ```
10. `1234 // 100 = 12` (cycle 12, counting from 0), `1234 % 100 = 34` (sample 34 within the cycle, i.e. phase $2\pi\cdot34/100$).
11. `int(fname.split("_")[0].split("-")[1])` → `12` (split by `_`, take `"sub-12"`, split by `-`, take `"12"`).

## Level 4
12. `t_event * fs = 129.8944` is a float; array indices must be integers. `x[int(round(t_event * fs))]` → index 130.
13. Amplitude $\lvert c\rvert = \sqrt{3^2 + 4^2} = 5$, phase $\arctan(4/3)\approx0.927$ rad. `abs(c)`; `cmath.phase(c)` or `np.angle(c)`.
14. ```python
    for i in range(1, 13):
        print(f"sub-{i:02d}_task-rest_eeg.edf")
    ```
    `range(1, 13)` stops before 13, giving 1…12.
