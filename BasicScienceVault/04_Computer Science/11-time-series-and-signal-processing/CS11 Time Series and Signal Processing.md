---
aliases: [Time Series and Signal Processing, Convolution, FIR IIR Filters, Spectral Analysis, Spike Sorting, Cross-correlogram, Signalverarbeitung]
tags: [computer-science, signal-processing, convolution, spike-sorting, type/overview, neuro]
---
# CS11 Time Series and Signal Processing

> [[MOC-computer-science|↑ CS MOC]] · [[CS11 Time Series and Signal Processing - Worksheet|✏️ Worksheet]] · [[CS11 Time Series and Signal Processing - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Almost all neural data are time series: voltage traces, spike trains, calcium signals, EEG, BOLD. Signal processing turns raw samples into interpretable quantities (spikes, oscillations, correlations, low-dimensional trajectories). Its building blocks (sampling, convolution, filtering, Fourier analysis) also appear in physics ([[Ph09 Waves and Oscillations]]) and in models (receptive fields, HRFs, synaptic kernels).

## Sampling theorem and aliasing (Nyquist–Shannon)
- A continuous signal containing no frequencies above $f_\text{max}$ can be reconstructed exactly from samples taken at $f_s > 2f_\text{max}$. $f_s/2$ is the **Nyquist frequency**.
- **Aliasing:** frequencies above $f_s/2$ fold back and appear as false lower frequencies. For $f_s/2 < f < f_s$, the alias appears at $f_s - f$.
- **Prevention:** an analogue **anti-aliasing low-pass filter** *before* digitisation; sample generously (spikes ≥ 20–30 kHz; EEG 250–1000 Hz). Downsampling digital data also requires low-pass filtering first (decimation).
- **Quantisation:** the ADC has finite resolution (e.g. 16 bits; [[CS05 Data Formats and Representation]]).

## Convolution and cross-correlation
**Convolution** (continuous and discrete):
$$(f * g)(t) = \int f(\tau)\,g(t - \tau)\,d\tau,\qquad(f * g)[n] = \sum_kf[k]\,g[n - k]$$
"Flip, shift, multiply, sum." It is commutative and associative.
- **Linear time-invariant (LTI) systems** are completely characterised by their **impulse response** $h$: output = input $* h$.
  - The membrane's response to a current is the current convolved with the exponential RC kernel ([[Ph05 Capacitance and RC Circuits]]).
  - The BOLD signal ≈ neural activity convolved with the HRF ([[Meth04 In Vivo Imaging]]).
  - A firing-rate estimate = spike train convolved with a Gaussian or exponential kernel.
  - Dendritic filtering of synaptic inputs = convolution with the cable's impulse response ([[Ph10 Signal Propagation and Cable Theory]]).
- **Convolution theorem:** convolution in time = **multiplication** in frequency: $\mathcal F\{f * g\} = \mathcal F\{f\}\cdot\mathcal F\{g\}$. This is why filtering is often done with FFTs.

**Cross-correlation** (no flip): $(f\star g)(\tau) = \sum_tf[t]\,g[t + \tau]$. It measures similarity as a function of **lag** τ. **Autocorrelation** is the cross-correlation of a signal with itself (it reveals periodicity and decay times).

## Filtering (FIR and IIR) and spectral analysis
| | **FIR** (finite impulse response) | **IIR** (infinite impulse response) |
|---|---|---|
| Equation | $y[n] = \sum_{k=0}^{M}b_kx[n - k]$ (only past and present inputs) | $y[n] = \sum_kb_kx[n - k] - \sum_{k\ge1}a_ky[n - k]$ (feedback from past outputs) |
| Example | moving average | first-order low-pass $y[n] = \alpha x[n] + (1 - \alpha)y[n - 1]$ (a discrete RC circuit); Butterworth, Chebyshev |
| Stability | always stable | can be unstable |
| Phase | **linear phase** possible (constant delay) | non-linear phase (distorts waveform timing) |
| Cost | needs many coefficients for sharp cut-offs | sharp responses with few coefficients |

- **Zero-phase filtering** (forward-backward, e.g. `filtfilt`) removes phase distortion offline (it is non-causal, so not usable in real time).
- **Filter artefacts:** ringing (Gibbs phenomenon) around sharp transients; edge effects; filters can make spikes look like oscillations. Always inspect filtered vs. raw data.

**Spectral analysis:**
- **DFT/FFT:** $X[k] = \sum_nx[n]e^{-2\pi ikn/N}$ ([[E2 Complex Numbers]]). The FFT computes it in $O(N\log N)$ instead of $O(N^2)$. Frequency resolution $\Delta f = f_s/N = 1/T$.
- **Power spectral density:** periodogram $\lvert X\rvert^2$ (noisy). **Welch's method** averages periodograms of overlapping windowed segments (less variance, coarser resolution). **Multitaper** methods average over orthogonal tapers.
- **Windowing** (Hann, Hamming) reduces **spectral leakage**, the smearing of power into neighbouring frequencies caused by cutting the signal.
- **Time–frequency analysis:** spectrograms (short-time FFT), **wavelets** (Morlet) with frequency-dependent windows, the Hilbert transform for instantaneous amplitude and phase ([[Ph09 Waves and Oscillations]]).

## Spike detection and spike sorting as pattern recognition
1. **Filter:** band-pass ~300–6000 Hz.
2. **Detect:** threshold crossings, typically at 4–5 × the noise σ. Estimate σ robustly as $\hat\sigma = \frac{\text{median}(\lvert x\rvert)}{0.6745}$ (Quiroga et al. 2004), because spikes inflate the ordinary SD.
3. **Extract** waveform snippets (~1–2 ms) around each event.
4. **Features:** PCA of the waveforms, amplitudes across channels (tetrodes, probes).
5. **Cluster** into putative units (GMMs, density-based clustering, template matching; Kilosort, MountainSort, via SpikeInterface).
6. **Curate:** merge or split clusters; quality metrics:
   - **refractory violations** (ISIs < ~1.5–2 ms should be rare)
   - isolation distance and L-ratio
   - amplitude stability (drift)

- **Challenges:** overlapping spikes, electrode **drift** (probes move relative to tissue), bursting cells with changing amplitudes, similar waveforms from different cells.
- **Classification:** single-unit vs. multi-unit activity; putative cell types (narrow-spiking interneurons vs. broad-spiking pyramidal cells).

## Autocorrelation and cross-correlation of spike trains
- **Peri-stimulus time histogram (PSTH):** spike counts aligned to an event, averaged over trials and divided by the bin width, giving a firing rate over time.
- **Autocorrelogram (ACG):** histogram of time differences between spikes of the same neuron. It shows a dip near 0 (**refractory period**), a peak at short lags (**bursting**), periodic side peaks (**rhythmic** firing).
- **Cross-correlogram (CCG):** histogram of spike-time differences between two neurons.
  - A **sharp, short-latency, asymmetric peak** (~1–3 ms) suggests a **monosynaptic** excitatory connection; a trough suggests inhibition.
  - A **broad, centred peak** suggests **common input** or shared slow modulation.
  - Correct for rate and slow co-modulation (shuffle predictors, jitter methods). Correlation alone is not proof of connectivity.
- **Spike-time tiling coefficient** and other measures avoid rate dependence. **Noise correlations** are computed from trial-to-trial spike counts ([[CS02 Probability and Statistics]]).

## Dimensionality reduction for population activity
| Method | Type | Key idea | Use |
|---|---|---|---|
| **PCA** | linear | maximal-variance orthogonal axes ([[CS01 Mathematical Foundations]]) | first look at population dynamics; trajectories |
| **Factor analysis (FA)** | linear, probabilistic | separates **shared** variance (latent factors) from **private** noise per neuron | shared variability, "communication subspaces" between areas |
| GPFA | linear + smooth in time | factors are Gaussian processes ([[CS09 Probabilistic and Bayesian Models]]) | single-trial smooth trajectories |
| dPCA, jPCA | linear, targeted | demixed task variables (stimulus, decision, time); rotational dynamics | motor cortex rotations, PFC task coding |
| **t-SNE, UMAP** | nonlinear | preserve **local** neighbourhoods in 2D/3D | visualisation of cell types, behavioural states; global distances and cluster sizes are **not** meaningful |
| Nonlinear latent models | LFADS, CEBRA | neural networks learn latent dynamics or embeddings ([[CS08 Deep Neural Networks]]) | single-trial dynamics, behaviour-aligned embeddings |

**Neural manifolds:** population activity often occupies a low-dimensional subspace whose geometry reflects the task (rings for head direction, tori for grid cells). Dimensionality estimates depend on noise, number of neurons and task complexity.

## In neuroscience #neuro
- **LFP analyses:** band power, phase–amplitude coupling, spike–field coherence, sharp-wave ripple detection (band-pass 150–250 Hz + envelope threshold).
- **Calcium imaging:** neuropil subtraction, $\Delta F/F$, spike inference by deconvolution (undoing the convolution with the indicator kernel).
- **Real-time processing:** causal filters for closed-loop stimulation (e.g. phase-locked stimulation), which can't use zero-phase filtering.

## Math links #math-link
- Fourier series and transforms (spectra, convolution theorem, k-space) → [[B12 Fourier Analysis]]
- Convolution as an integral → [[B7 Antiderivatives and Integration]]
- Fourier series and transforms; complex exponentials → [[E2 Complex Numbers]], [[B4 Trigonometric Functions]]
- Exponential kernels; IIR low-pass as a geometric series → [[B2 Exponential Functions]], [[A7 Sums Products and Factorials]]
- PCA, eigenvectors → [[C4 Eigenvalues and Eigenvectors]]
- $O(N\log N)$ vs. $O(N^2)$ → [[A3 Logarithms]]

## Connections
- In code → [[Py08 SciPy Scientific Computing]] (`scipy.signal`), [[MAT06 MATLAB Signal Processing Toolbox]], [[R09 R Neuroscience Packages]] (signal)
- Waves, Nyquist, filters (physics) → [[Ph09 Waves and Oscillations]]
- Recording methods → [[Meth03 Electrophysiology]]
- Data formats and SpikeInterface → [[CS05 Data Formats and Representation]]
- Clustering → [[CS07 Machine Learning Fundamentals]]
- Encoding models of spike trains → [[CS09 Probabilistic and Bayesian Models]]

## Key takeaways
- Sample at > 2 $f_\text{max}$ and low-pass first; aliases appear at $f_s - f$.
- Convolution (flip–shift–multiply–sum) describes LTI systems (RC, HRF, smoothing). In frequency space it becomes a multiplication.
- FIR: stable, linear phase. IIR: efficient, feedback, phase distortion (use filtfilt offline). Welch/multitaper for spectra; windows against leakage.
- Spike sorting: filter → threshold (MAD-based σ) → waveforms → PCA → cluster → curate (refractory violations).
- ACG shows refractoriness, bursting and rhythm; a sharp short-latency CCG peak suggests a monosynaptic connection, a broad one common input.
- PCA and FA (shared vs. private variance) for population dynamics; UMAP/t-SNE only for visualisation.
