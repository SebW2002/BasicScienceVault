---
aliases: [Exponential Functions, Exponentialfunktion, e-function]
tags: [analysis, exponential, function, type/overview, neuro]
---
# B2 Exponential Functions

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B2 Exponential Functions - Worksheet|✏️ Worksheet]] · [[B2 Exponential Functions - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
The single most important function in neuroscience. Whenever a quantity changes at a rate **proportional to itself** – a membrane charging, a synaptic current decaying, transmitter being cleared, a population growing – the solution is an exponential.

## Definition and properties
$$f(x) = a \cdot b^{x} \qquad (b > 0,\ b \neq 1)$$
The **natural exponential function** uses Euler's number $e = \lim_{n\to\infty}\left(1 + \frac1n\right)^n \approx 2.71828$:
$$f(x) = e^x = \exp(x)$$

| Property | $e^x$ |
|---|---|
| Domain / range | $\mathbb R$ / $(0, \infty)$ – **always positive** |
| Special values | $e^0 = 1$, $e^1 = e$ |
| Monotonic | strictly increasing; $e^{-x}$ strictly decreasing |
| Limits | $e^x \to \infty$ for $x \to \infty$; $e^x \to 0$ for $x \to -\infty$ (asymptote $y = 0$) |
| Derivative | $(e^x)' = e^x$ – the only function equal to its own derivative (up to a factor) |
| Inverse | $\ln x$ → [[B3 Logarithmic Functions]] |

Every exponential can be written with base $e$: $\;b^x = e^{x\ln b}$. Rules are the [[A1 Exponent Rules]]: $e^{a}e^{b} = e^{a+b}$, $(e^a)^b = e^{ab}$.

## Growth and decay
$$N(t) = N_0\, e^{t/\tau} \;(\text{growth}), \qquad N(t) = N_0\, e^{-t/\tau} \;(\text{decay})$$
- **Time constant $\tau$:** after $t = \tau$, decay has reached $e^{-1} \approx 37\%$ of the start value (63 % of the way to zero); after $3\tau$ ≈ 5 %, after $5\tau$ < 1 %.
- **Half-life:** $e^{-t_{1/2}/\tau} = \tfrac12 \Rightarrow t_{1/2} = \tau\ln 2 \approx 0.69\,\tau$.
- Rate formulation: $N(t) = N_0 e^{-kt}$ with $k = 1/\tau$.

**Approach to a steady state** (the shape you'll see most often):
$$V(t) = V_\infty + (V_0 - V_\infty)\, e^{-t/\tau}$$
Starts at $V_0$, ends at $V_\infty$, covers 63 % of the gap after one $\tau$. It solves the differential equation $\tau\,\frac{dV}{dt} = -(V - V_\infty)$.

## In neuroscience #neuro
- **Passive membrane (RC circuit):** after a current step, $V(t) = V_\text{rest} + IR\left(1 - e^{-t/\tau_m}\right)$ with $\tau_m = R_m C_m$ (typically 10–30 ms). Measuring the 63 % point is how $\tau_m$ is estimated.
- **Synaptic currents:** after a spike, conductance decays as $g(t) = \bar g\, e^{-t/\tau_\text{syn}}$ (AMPA ~2–5 ms, NMDA ~50–100 ms, GABA_A ~5–10 ms).
- **STDP window:** weight change $\Delta w = A_+ e^{-\Delta t/\tau_+}$ for pre-before-post timing.
- **Poisson spiking:** inter-spike intervals are exponentially distributed, $p(t) = \lambda e^{-\lambda t}$; probability of no spike for time $t$: $e^{-\lambda t}$.
- **Pharmacokinetics / clearance:** drug and transmitter concentrations decay exponentially.

## Connections
- Exponentials as solutions of $\dot x = -x/\tau$ → [[B10 Differential Equations]]
- Exponent rules → [[A1 Exponent Rules]]
- Inverse function, solving for $t$ → [[B3 Logarithmic Functions]], [[A3 Logarithms]], [[A8 Solving Equations]]
- Derivative $e^x$, chain rule for $e^{-t/\tau}$ → [[B6 Differentiation Rules]]
- Integral of a decaying current = charge → [[B7 Antiderivatives and Integration]]
- Series $e^x = \sum x^k/k!$ → [[B9 Taylor Series]]
- $e^{i\varphi}$ → [[E2 Complex Numbers]]

## Where this is used in the vault
**Most important applications:** Membrane charging and decay ([[Ph05 Capacitance and RC Circuits]]), Boltzmann factors ([[Ph08 Thermodynamics and Statistics]]), cable decay ([[Ph10 Signal Propagation and Cable Theory]]), radioactive decay in PET and PCR growth ([[Meth04 In Vivo Imaging]], [[Meth05 Molecular Biology Tools]]), softmax and GLMs ([[CS08 Deep Neural Networks]], [[CS09 Probabilistic and Bayesian Models]]).

**All notes that build on this topic:**
- *Physics:* [[Ph05 Capacitance and RC Circuits]] · [[Ph07 Diffusion and Transport]] · [[Ph08 Thermodynamics and Statistics]] · [[Ph10 Signal Propagation and Cable Theory]] · [[Ph11 Optics and Fluorescence]] · [[Ph12 Quantum Basics for Biophysics]]
- *Chemistry:* [[Ch02 Chemical Bonds]] · [[Ch05 Redox and Electrochemistry]]
- *Biology:* [[Bio02 Membranes and Transport]] · [[Bio03 Proteins and Enzymes]] · [[Bio04 Nucleic Acids and Gene Expression]] · [[Bio05 Neurons and Action Potentials]] · [[Bio06 Synapses and Neurotransmitters]] · [[Bio07 Neural Circuits and Systems]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth03 Electrophysiology]] · [[Meth04 In Vivo Imaging]] · [[Meth05 Molecular Biology Tools]]
- *Computer Science:* [[CS02 Probability and Statistics]] · [[CS08 Deep Neural Networks]] · [[CS09 Probabilistic and Bayesian Models]] · [[CS10 Dynamical and Computational Neuro Models]] · [[CS11 Time Series and Signal Processing]]
- *Programming:* [[Py08 SciPy Scientific Computing]] · [[Py09 Python Machine Learning Libraries]] · [[Py11 PsychoPy Experiment Control]] · [[Py13 Python Reproducible Projects and Testing]] · [[R06 ggplot2 Visualization]] · [[R07 R Statistical Modelling]] · [[MAT07 MATLAB Statistics Toolbox]] · [[MAT08 Psychtoolbox]] · [[Doc02 Math in Markdown]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $e^x > 0$ always; $e^{-t/\tau}$ decays to 37 % after one $\tau$.
- Half-life $= \tau\ln2$.
- "Rate proportional to amount" ⇒ exponential.
