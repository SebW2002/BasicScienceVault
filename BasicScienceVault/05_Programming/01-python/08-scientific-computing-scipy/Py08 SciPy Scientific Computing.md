---
aliases: [SciPy, scipy.signal, scipy.stats, scipy.optimize, scipy.integrate, scipy.interpolate, find_peaks]
tags: [programming, python, scipy, signal-processing, statistics, optimization, type/overview, neuro]
---
# Py08 SciPy Scientific Computing

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py08 SciPy Scientific Computing - Worksheet|✏️ Worksheet]] · [[Py08 SciPy Scientific Computing - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
SciPy is the toolbox on top of NumPy: filters and spectra, probability distributions and tests, curve fitting and optimisation, ODE solvers and interpolation. These modules turn the maths of [[B10 Differential Equations]], [[B12 Fourier Analysis]] and [[CS02 Probability and Statistics]] into one-line function calls. Knowing what each call computes keeps you from using a black box.

## scipy.signal: filters, spectra, peaks
```python
from scipy import signal
fs = 1000
# 4th-order Butterworth band-pass 1–40 Hz, as second-order sections (numerically stable)
sos = signal.butter(4, [1, 40], btype="bandpass", fs=fs, output="sos")
x_filt = signal.sosfiltfilt(sos, x)          # zero-phase: forward + backward
# notch for line noise
b, a = signal.iirnotch(50, Q=30, fs=fs)
x_clean = signal.filtfilt(b, a, x_filt)
# power spectral density (Welch: average of windowed segments)
f, Pxx = signal.welch(x, fs=fs, nperseg=2 * fs)   # 2-s windows → 0.5 Hz resolution
# spectrogram
f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=256, noverlap=192)
# peaks
peaks, props = signal.find_peaks(v, height=0, distance=int(0.002 * fs), prominence=20)
```
- **Always pass `fs=`** so cut-offs are in Hz; otherwise they are fractions of the Nyquist frequency $f_s/2$.
- **`filtfilt`/`sosfiltfilt`** run the filter twice (forward and backward): **zero phase shift** (ERP latencies don't move) and doubled attenuation, but it is **non-causal** (uses future samples) – fine offline, not for real-time or for analyses of timing around events where acausal smearing matters. `lfilter`/`sosfilt` are causal but shift the phase.
- **IIR** (Butterworth) is efficient; **FIR** (`firwin`) has linear phase and is always stable ([[CS11 Time Series and Signal Processing]]).
- **Welch resolution** $\Delta f = f_s / n_\text{perseg} = 1/T_\text{window}$; longer windows → finer resolution, more variance ([[B12 Fourier Analysis]]).
- **`find_peaks`** finds local maxima; `height`, `distance` (min. samples between peaks) and `prominence` (how much a peak stands out) remove noise peaks. For troughs: `find_peaks(-x)`.
- Also useful: `signal.hilbert` (analytic signal → amplitude envelope and phase, [[E2 Complex Numbers]]), `signal.decimate`/`resample_poly` (anti-aliased downsampling), `signal.detrend`, `signal.correlate`, `signal.coherence`.

## scipy.stats: distributions and tests
```python
from scipy import stats
stats.norm(0, 1).cdf(1.96)          # 0.975
stats.norm.ppf(0.975)               # 1.96 (inverse CDF / quantile)
stats.poisson(4).pmf(2)             # P(K = 2) for λ = 4
stats.expon(scale=0.1).rvs(1000, random_state=rng)   # ISIs with mean 0.1 s
stats.ttest_ind(a, b)               # independent samples (Student; equal_var=False → Welch)
stats.ttest_rel(pre, post)          # paired
stats.ttest_1samp(diff, 0)
stats.mannwhitneyu(a, b); stats.wilcoxon(pre, post)   # non-parametric
stats.pearsonr(x, y); stats.spearmanr(x, y)
stats.f_oneway(g1, g2, g3)           # one-way ANOVA
stats.chi2_contingency(table)
stats.permutation_test((a, b), statistic, n_resamples=10_000, random_state=rng)
stats.bootstrap((x,), np.mean, confidence_level=0.95, random_state=rng)
```
- Distribution objects share methods: `pdf`/`pmf`, `cdf`, `ppf` (quantile), `sf` (= 1 − cdf, survival), `rvs` (random samples), `fit`.
- Results are objects with `.statistic` and `.pvalue` (and often `.confidence_interval()`).
- For regression models, mixed models and ANOVA tables use `statsmodels` (or R, [[R07 R Statistical Modelling]]). Multiple comparisons: `scipy.stats.false_discovery_control` (Benjamini–Hochberg) or `statsmodels.stats.multitest`.

## scipy.optimize: fitting and minimising
```python
from scipy import optimize
def expdecay(t, A, tau, c): return A * np.exp(-t / tau) + c
popt, pcov = optimize.curve_fit(expdecay, t, v, p0=[10, 0.02, -70])
perr = np.sqrt(np.diag(pcov))                 # standard errors
res = optimize.minimize(neg_log_lik, x0=[1.0, 0.1], args=(data,), method="L-BFGS-B",
                        bounds=[(0, None), (1e-4, None)])
root = optimize.brentq(lambda v: f(v), -100, 0)   # solve f(v) = 0 in a bracket
```
- `curve_fit` = non-linear least squares; give **good starting values** `p0` – bad ones converge to local minima or fail.
- `minimize` finds the minimum of any scalar function: negative log-likelihood (MLE), loss functions ([[CS04 Optimization]]). Check `res.success` and `res.message`.
- `brentq`/`root_scalar` solve equations numerically – e.g. the reversal potential of the GHK equation, fixed points of a model ([[A8 Solving Equations]]).

## scipy.integrate: integrals and ODEs
```python
from scipy import integrate
integrate.quad(lambda t: np.exp(-t / 0.01), 0, np.inf)      # (0.01, error)
integrate.trapezoid(current, t)                              # area under sampled data → charge
def lif(t, v, I): return (-(v + 70) + 10 * I) / 0.02         # dV/dt
sol = integrate.solve_ivp(lif, (0, 0.2), [-70], args=(1.5,), max_step=1e-4, dense_output=True)
sol.t, sol.y[0]
```
- `quad` integrates a **function**; `trapezoid`/`simpson` integrate **sampled data**.
- `solve_ivp` integrates $\dot{\mathbf y} = f(t, \mathbf y)$ with adaptive step size (RK45 default; `method="LSODA"`/`"BDF"` for stiff systems like Hodgkin–Huxley). Discontinuities (spike resets) need `events=` or a manual loop ([[B10 Differential Equations]], [[CS10 Dynamical and Computational Neuro Models]]).

## scipy.interpolate
```python
from scipy import interpolate
f = interpolate.interp1d(t_eye, x_eye, kind="linear", bounds_error=False, fill_value=np.nan)
x_on_eeg_clock = f(t_eeg)                      # resample to another time base
cs = interpolate.CubicSpline(t, y)             # smooth curve with derivatives
grid = interpolate.griddata(xy_electrodes, values, (gx, gy), method="cubic")   # 2-d scattered → grid
```
- Interpolation **invents** values between samples: fine for re-sampling smooth signals onto another clock, dangerous for filling long gaps. For downsampling signals use anti-aliasing (`decimate`), not plain interpolation.
- `np.interp` covers the simple 1-d linear case.

## Same idea in R and MATLAB
| SciPy | R | MATLAB |
|---|---|---|
| `butter`, `filtfilt` | `signal::butter`, `signal::filtfilt` | `butter`, `filtfilt` ([[MAT06 MATLAB Signal Processing Toolbox]]) |
| `welch`, `spectrogram` | `stats::spec.pgram`, `signal::specgram` | `pwelch`, `spectrogram` |
| `find_peaks` | `pracma::findpeaks` | `findpeaks` |
| `stats.ttest_ind` | `t.test` | `ttest2` ([[MAT07 MATLAB Statistics Toolbox]]) |
| `curve_fit`, `minimize` | `nls`, `optim` | `lsqcurvefit`, `fminsearch`, `fmincon` |
| `solve_ivp` | `deSolve::ode` | `ode45`, `ode15s` |
| `interp1d` | `approx`, `spline` | `interp1`, `griddata` |

## In neuroscience #neuro
- **EEG preprocessing:** high-pass 0.1–1 Hz, low-pass ~40 Hz, notch 50 Hz (Europe) / 60 Hz (US); zero-phase offline.
- **Band power:** Welch PSD, integrate over 8–12 Hz (`trapezoid` on `Pxx[band]`).
- **Spike detection** in extracellular data: band-pass 300–3000 Hz, threshold at ~4–5 × robust noise SD (median(|x|)/0.6745), `find_peaks(-x, height=thr)` ([[CS11 Time Series and Signal Processing]]).
- **Membrane time constant:** fit $A e^{-t/\tau} + c$ to the voltage response to a current step with `curve_fit` ([[Ph05 Capacitance and RC Circuits]]).
- **Hodgkin–Huxley** simulation with `solve_ivp` ([[Bio05 Neurons and Action Potentials]]).
- **Eye tracker at 500 Hz, EEG at 1000 Hz:** align with `interp1d` on a common clock after synchronising triggers.

## Math links #math-link
- Fourier, PSD, resolution $1/T$, convolution theorem → [[B12 Fourier Analysis]]
- ODEs, Euler vs. adaptive solvers → [[B10 Differential Equations]]
- Numerical integration as Riemann/trapezoid sums → [[B7 Antiderivatives and Integration]]
- Root finding → [[A8 Solving Equations]]; optimisation and gradients → [[B11 Multivariable Calculus]]
- Exponential decay fits → [[B2 Exponential Functions]]

## Connections
- Signal-processing concepts → [[CS11 Time Series and Signal Processing]], [[Ph09 Waves and Oscillations]]
- Tests and distributions → [[CS02 Probability and Statistics]]
- Optimisation → [[CS04 Optimization]]
- Neuro models → [[CS10 Dynamical and Computational Neuro Models]]
- Same in MATLAB → [[MAT06 MATLAB Signal Processing Toolbox]], [[MAT07 MATLAB Statistics Toolbox]]

## Key takeaways
- `signal`: design with `fs=`, prefer SOS; `filtfilt` = zero-phase offline; Welch for PSDs; `find_peaks` with prominence.
- `stats`: distributions with pdf/cdf/ppf/rvs; tests return statistic + p-value; non-parametric and permutation alternatives.
- `optimize`: `curve_fit` needs good `p0`; `minimize` for likelihoods; check convergence.
- `integrate`: `quad` for functions, `trapezoid` for samples, `solve_ivp` for ODEs.
- `interpolate`: re-sample onto other time bases; don't fill long gaps.
