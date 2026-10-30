---
tags: [programming, python, type/solution]
---
# Py03 Python Control Flow and Functions – Solutions

> Worksheet: [[Py03 Python Control Flow and Functions - Worksheet]] · Theory: [[Py03 Python Control Flow and Functions]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. `[2, 5, 8]`, `[5, 3, 1]`
2. `1` and `3` (0 and 2 are skipped by `continue`; the loop breaks at 4).
3. `anticipation`
4. `None`

## Level 2
5. a) valid b) valid (keywords in any order after positional `x`) c) **invalid**: positional argument after a keyword argument is a `SyntaxError` d) valid (`l_freq=0.1`, `h_freq=30`).
6. `a = 1`, `args = (2, 3)`, `kwargs = {"ch": "Cz", "fs": 500}`.
7. `filt(x, 500, **params)`
8. `10`: the `n = 5` inside `g` creates a **local** variable; the global `n` is unchanged.

## Level 3
9. ```python
   def classify_rt(rt):
       if rt is None:
           return "miss"
       elif rt < 0.15:
           return "anticipation"
       elif rt > 2.0:
           return "slow"
       return "valid"
   ```
   The `None` test must come first, otherwise `None < 0.15` raises a `TypeError`.
10. ```python
    def chunks(x, n):
        for start in range(0, len(x), n):
            yield x[start:start + n]
    ```
11. `sorted(files, key=lambda f: int(f.split("-")[1].split(".")[0]))` → `["sub-1.edf", "sub-2.edf", "sub-10.edf"]`. Plain `sorted` compares strings character by character: `["sub-1.edf", "sub-10.edf", "sub-2.edf"]`. (Better: zero-pad names, `sub-01`.)

## Level 4
12. ```python
    v, spikes = -70.0, []
    for k in range(n_steps):               # for loop over time
        v += dt / tau * (-(v - E_L) + R * I[k])
        if v >= v_th:                      # condition
            spikes.append(k * dt)
            v = v_reset
    ```
    A `for` loop (sequential: each step depends on the previous one, so it can't be vectorised) and an `if` for threshold and reset.
13. A list of all windows would hold the whole recording in memory at once (10 h × 3600 s × e.g. 64 ch × 1000 Hz × 8 bytes ≈ 18 GB). A generator produces one window at a time.
14. ```python
    g = chunks(list(range(7)), 3)
    print(list(g))   # [[0, 1, 2], [3, 4, 5], [6]]
    print(list(g))   # []  – the generator is exhausted
    ```
