---
tags: [programming, python, type/worksheet]
---
# Py03 Python Control Flow and Functions – Worksheet

> Theory: [[Py03 Python Control Flow and Functions]] · Solutions: [[Py03 Python Control Flow and Functions - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Predict the output
1. `list(range(2, 11, 3))`, `list(range(5, 0, -2))`
2. ```python
   for i in range(6):
       if i == 4: break
       if i % 2 == 0: continue
       print(i)
   ```
3. ```python
   x = 0.12
   print("anticipation" if x < 0.15 else "valid")
   ```
4. What does `f()` return if `def f(): x = 3` (no `return`)?

## Level 2 – Arguments
5. `def filt(x, fs, l_freq=1.0, h_freq=40.0)`. Which calls are valid? a) `filt(x, 500)` b) `filt(x, h_freq=30, fs=500)` c) `filt(fs=500, x)` d) `filt(x, 500, 0.1, 30)`
6. What do `args` and `kwargs` contain after `f(1, 2, 3, ch="Cz", fs=500)` with `def f(a, *args, **kwargs)`?
7. `params = {"l_freq": 1, "h_freq": 30}`. Write the call of `filt` using `params` via unpacking.
8. What is printed and why?
   ```python
   n = 10
   def g():
       n = 5
       return n
   g(); print(n)
   ```

## Level 3 – Write code
9. Write `classify_rt(rt)` returning `"miss"` for `None`, `"anticipation"` below 0.15, `"slow"` above 2.0, else `"valid"`.
10. Write a generator `chunks(x, n)` yielding consecutive pieces of length `n` (the last may be shorter).
11. Sort `files = ["sub-10.edf", "sub-2.edf", "sub-1.edf"]` numerically by subject number with `sorted` and a `lambda`. What would plain `sorted(files)` give?

## Level 4 – Neuro transfer
12. Write the loop of a leaky integrate-and-fire neuron in pseudo-Python: `v` starts at −70 mV; each step `v += dt / tau * (-(v - E_L) + R * I)`; if `v >= v_th`, record the spike time and reset `v = v_reset`. Which control-flow elements do you need?
13. Why use a generator rather than a list for 1-second windows of a 10-hour recording?
14. 💻 Implement task 10, test it on `list(range(7))` with `n = 3`, and check that consuming the generator twice gives an empty second result.
