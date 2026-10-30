---
tags: [programming, python, scipy, type/solution]
---
# Py08 SciPy Scientific Computing – Solutions

> Worksheet: [[Py08 SciPy Scientific Computing - Worksheet]] · Theory: [[Py08 SciPy Scientific Computing]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. a) `signal.butter(..., output="sos")` + `signal.sosfiltfilt` b) `signal.welch` c) `signal.find_peaks(v, height=0)` d) `stats.ttest_rel` e) `optimize.curve_fit` f) `integrate.solve_ivp` g) `interpolate.interp1d` (or `np.interp`).
2. `0.5`, `0.0`, ≈ `0.025`.
3. `quad` integrates a Python **function** adaptively (you can evaluate it anywhere); `trapezoid` integrates **sampled values** at given points.

## Level 2
4. Without `fs`, cut-offs are normalised to Nyquist (1 = $f_s/2$) and must be < 1. 40 is invalid → `ValueError`. With `fs=500` it means 40 Hz.
5. `filtfilt` filters forward then backward, so the phase shifts cancel (zero phase). `lfilter` is causal and delays (shifts) components. `filtfilt` is non-causal: not possible in real time (closed-loop, BCI) and can smear post-event activity to before the event (problematic for latency/onset analyses).
6. $\Delta f = 500/250 = 2$ Hz. For 0.25 Hz: `nperseg = 500/0.25 = 2000` (4 s windows). Price: fewer windows to average → noisier estimate (and needs ≥ 4 s of data per segment).
7. `height` (e.g. 0 mV), `distance` (e.g. 2 ms × fs), `prominence` (e.g. 20 mV).
8. Bad starting values (or wrong units: t in ms vs. s) → the optimiser wandered off. Give `p0=[A, 0.02, c]` with t in seconds, possibly `bounds`.

## Level 3
9. $P(0) = e^{-2}\approx0.135$; $P(K\ge1) = 1 - 0.135 = 0.865$. `stats.poisson(2).pmf(0)`, `stats.poisson(2).sf(0)` (sf(k) = P(K > k)).
10. ```python
    sos = signal.butter(4, 1, btype="highpass", fs=500, output="sos")
    eeg_hp = signal.sosfiltfilt(sos, eeg, axis=-1)
    ```
11. $P(\text{ISI} < 2) = 1 - e^{-2/50}\approx2/50 = 0.04$ → about **4 %**. Exact: `stats.expon(scale=50).cdf(2)` = 0.0392. (A Poisson process has no refractory period; real neurons show a gap.)

## Level 4
12. Load → band-pass 1–40 Hz and notch (`sosfiltfilt`) → re-reference → reject artefact segments → `f, P = signal.welch(eeg, fs=500, nperseg=1000, axis=-1)` (2-s windows, 0.5 Hz resolution) → `band = (f >= 8) & (f <= 12)` → `alpha = integrate.trapezoid(P[:, band], f[band], axis=-1)` (one value per channel); often log-transform before statistics.
13. ```python
    sol = integrate.solve_ivp(lambda t, V: (-(V + 65) + 10) / 0.010, (0, 0.1), [-65.0], max_step=1e-4)
    ```
    Analytic: $V(t) = V_\infty + (V_0 - V_\infty)e^{-t/\tau}$ with $V_\infty = -55$ mV: $V(0.1) = -55 - 10e^{-10}\approx-55.0$ mV (after 10 τ, steady state).
14. ```python
    import numpy as np
    from scipy import signal
    fs = 250; t = np.arange(0, 10, 1/fs)
    rng = np.random.default_rng(0)
    x = np.sin(2*np.pi*10*t) + rng.standard_normal(t.size)
    f, P = signal.welch(x, fs=fs, nperseg=2*fs)
    print(f[np.argmax(P)])   # 10.0 (resolution 0.5 Hz)
    ```
