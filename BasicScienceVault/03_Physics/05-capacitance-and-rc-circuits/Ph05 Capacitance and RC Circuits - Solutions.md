---
tags: [physics, capacitance, rc-circuit, type/solution]
---
# Ph05 Capacitance and RC Circuits – Solutions

> Worksheet: [[Ph05 Capacitance and RC Circuits - Worksheet]] · Theory: [[Ph05 Capacitance and RC Circuits]] · Wrong? → [[Mistakes - Physics]]

## Level 1
1. $Q = CV = 10^{-5}\cdot5 = 5\times10^{-5}\,\text{C}$; $E = \tfrac12CV^2 = \tfrac12\cdot10^{-5}\cdot25 = 1.25\times10^{-4}\,\text{J}$
2. a) doubles b) halves
3. $C = 2\times10^{-4}\cdot10^{-6} = 2\times10^{-10}\,\text{F} = 200\,\text{pF}$
4. Only while the voltage across it **changes** ($I = C\,dV/dt$). At constant voltage, no current flows (in steady state, a capacitor acts as an open circuit).

## Level 2
5. $\tau = 10^8\cdot2\times10^{-10} = 2\times10^{-2}\,\text{s} = 20\,\text{ms}$
6. $V_\infty = IR = 10^{-10}\cdot10^8 = 10^{-2}\,\text{V} = 10\,\text{mV}$. After τ: 63 % = 6.3 mV. After 2τ: 86 % = 8.6 mV.
7. $25\cdot e^{-2}\approx25\cdot0.14 = 3.4\,\text{mV}$
8. $t_{1/2} = \tau\ln2\approx20\cdot0.69\approx13.9\,\text{ms}$
9. $\frac{I}{C} = \frac{10^{-10}}{2\times10^{-10}} = 0.5\,\text{V/s} = 0.5\,\text{mV/ms}$. (Check: the tangent at $t = 0$ would reach $V_\infty = 10$ mV after $\tau = 20$ ms, since $0.5\cdot20 = 10$ ✓.)

## Level 3
10. $R_\text{in} = \frac{R_m}{A}$ (more area means more channels in parallel, so lower resistance) and $C = c_m\cdot A$, so $\tau = R_\text{in}C = \frac{R_m}{A}c_mA = R_mc_m$, and $A$ cancels. $\tau_m = 5\times10^4\,\Omega\text{cm}^2\cdot10^{-6}\,\text{F/cm}^2 = 5\times10^{-2}\,\text{s} = 50\,\text{ms}$.
11. In the τ = 30 ms neuron, the first EPSP has decayed only to $e^{-1/3}\approx72\%$ when the second arrives, so they summate strongly. In the τ = 2 ms neuron, the first EPSP is gone ($e^{-5}<1\%$), so there is practically no summation. The τ = 2 ms cell is a **coincidence detector** (it only fires if inputs arrive almost simultaneously).
12. Series: $\frac{1}{C_\text{total}} = 40\cdot\frac{1}{C_1}$, so $C_\text{total} = C_1/40$: 40 times smaller.
13. $\tau = RC$ halves too, because $C$ stays the same. The neuron becomes faster but integrates over a shorter time.

## Level 4
14. $T = 20\ln\frac{30 - 0}{30 - 15} = 20\ln2\approx13.9\,\text{ms}$; $f\approx\frac{1}{13.9\,\text{ms}}\approx72\,\text{Hz}$.
15. $V_\infty = 15$ mV: the denominator becomes 0, so $T\to\infty$; the voltage approaches threshold but never reaches it (exactly rheobase). $V_\infty = 10$ mV: the argument of ln is negative, so there is no solution; the neuron never fires (subthreshold input).
16. $r = 20\,\text{nm} = 2\times10^{-8}\,\text{m}$; $A = 4\pi(2\times10^{-8})^2\approx5.0\times10^{-15}\,\text{m}^2$; $\Delta C = 10^{-2}\cdot5.0\times10^{-15}\approx5\times10^{-17}\,\text{F} = 0.05\,\text{fF}$. Single small synaptic vesicles are hard to resolve. In secretory cells with large dense-core vesicles (≈ 200–300 nm), the steps are ~1–3 fF, which is measurable.
