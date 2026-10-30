---
aliases: [Trigonometric Functions, Trigonometrische Funktionen, sine, cosine]
tags: [analysis, trigonometry, function, type/overview, neuro]
---
# B4 Trigonometric Functions

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B4 Trigonometric Functions - Worksheet|✏️ Worksheet]] · [[B4 Trigonometric Functions - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
The brain oscillates. Alpha, theta, gamma rhythms, phase locking, Fourier spectra, cosine-tuned motor neurons, head-direction cells – all described by sine and cosine. The geometric definition is in [[D4 Unit Circle Trigonometry]]; here we look at them as **functions of time or angle**.

## The three functions
| | $\sin x$ | $\cos x$ | $\tan x = \frac{\sin x}{\cos x}$ |
|---|---|---|---|
| Domain | $\mathbb R$ | $\mathbb R$ | $x \neq \frac\pi2 + k\pi$ (poles) |
| Range | $[-1, 1]$ | $[-1, 1]$ | $\mathbb R$ |
| Period | $2\pi$ | $2\pi$ | $\pi$ |
| Symmetry | odd | even | odd |
| Zeros | $k\pi$ | $\frac\pi2 + k\pi$ | $k\pi$ |
| Derivative | $\cos x$ | $-\sin x$ | $\frac{1}{\cos^2 x}$ |

**Always use radians in calculus:** $180° = \pi$, so $x_\text{rad} = x_\text{deg}\cdot\frac{\pi}{180}$.

## The general oscillation
$$y(t) = A \sin(2\pi f t + \varphi) + c$$
| Symbol | Meaning |
|---|---|
| $A$ | amplitude (half the peak-to-peak height) |
| $f$ | frequency in Hz (cycles per second); period $T = 1/f$ |
| $\omega = 2\pi f$ | angular frequency (rad/s) |
| $\varphi$ | phase shift (rad) |
| $c$ | offset / baseline |

For $y = \sin(bx)$ the period is $\frac{2\pi}{b}$.

## Key identities
- **Pythagoras:** $\sin^2 x + \cos^2 x = 1$
- **Shifts:** $\sin(x + \frac\pi2) = \cos x$, $\;\cos(x + \frac\pi2) = -\sin x$, $\;\sin(x + \pi) = -\sin x$, $\;\sin(\pi - x) = \sin x$
- **Addition theorems:** $\sin(a \pm b) = \sin a\cos b \pm \cos a\sin b$; $\;\cos(a \pm b) = \cos a\cos b \mp \sin a \sin b$
- **Double angle:** $\sin 2x = 2\sin x\cos x$; $\;\cos 2x = \cos^2 x - \sin^2 x$
- **Notation:** $\sin^2 x = (\sin x)^2$, but $\sin^{-1}x = \arcsin x$ (inverse function), **not** $\frac1{\sin x}$.

## Solving trig equations
$\sin x = \frac12$ has infinitely many solutions! On $[0, 2\pi)$: $x = \frac\pi6$ and $x = \pi - \frac\pi6 = \frac{5\pi}6$. Use the unit circle and symmetry ([[D4 Unit Circle Trigonometry]]).

## In neuroscience #neuro
- **Brain rhythms:** delta (1–4 Hz), theta (4–8), alpha (8–12), beta (13–30), gamma (30–100 Hz). A 10 Hz alpha wave with 5 µV amplitude: $y(t) = 5\sin(20\pi t)\,\mu\text{V}$.
- **Phase:** the angle $2\pi f t + \varphi$ tells *where in the cycle* we are. Hippocampal place cells fire at progressively earlier theta phases as an animal crosses the place field (**phase precession**).
- **Phase difference** between two signals of frequency $f$ with time lag $\Delta t$: $\Delta\varphi = 2\pi f\Delta t$.
- **Cosine tuning** (motor cortex, Georgopoulos): $r(\theta) = b_0 + b_1\cos(\theta - \theta_\text{pref})$ – maximum at the preferred movement direction, minimum opposite.
- **Fourier analysis:** every signal can be decomposed into sines and cosines of different frequencies – the basis of power spectra, filters and time–frequency analysis (complex form → [[E2 Complex Numbers]]).

## Connections
- Decomposing signals into sines → [[B12 Fourier Analysis]]; harmonic oscillator → [[B10 Differential Equations]]
- Geometric definition, special values → [[D4 Unit Circle Trigonometry]]
- Symmetry (even/odd) → [[B1 Properties of Functions]]
- Derivatives → [[B6 Differentiation Rules]]; series → [[B9 Taylor Series]]
- $e^{i\varphi} = \cos\varphi + i\sin\varphi$ → [[E2 Complex Numbers]]
- Rotations → [[C1 Matrices]]

## Where this is used in the vault
**Most important applications:** Oscillations and brain rhythms ([[Ph09 Waves and Oscillations]]), Fourier analysis ([[B12 Fourier Analysis]], [[CS11 Time Series and Signal Processing]]), cosine tuning ([[Bio07 Neural Circuits and Systems]]).

**All notes that build on this topic:**
- *Physics:* [[Ph09 Waves and Oscillations]] · [[Ph11 Optics and Fluorescence]]
- *Biology:* [[Bio07 Neural Circuits and Systems]]
- *Methods:* [[Meth03 Electrophysiology]]
- *Computer Science:* [[CS11 Time Series and Signal Processing]]
- *Programming:* [[Py11 PsychoPy Experiment Control]] · [[R07 R Statistical Modelling]] · [[MAT06 MATLAB Signal Processing Toolbox]] · [[MAT08 Psychtoolbox]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Radians! Period of $\sin(bx)$ is $2\pi/b$; of $\sin(2\pi f t)$ is $1/f$.
- $\sin$ odd, $\cos$ even, $\sin^2 + \cos^2 = 1$.
- Trig equations have infinitely many solutions – state the interval.
