---
tags: [physics, cable-theory, conduction, type/solution]
---
# Ph10 Signal Propagation and Cable Theory – Solutions

> Worksheet: [[Ph10 Signal Propagation and Cable Theory - Worksheet]] · Theory: [[Ph10 Signal Propagation and Cable Theory]] · Wrong? → [[Mistakes - Physics]]

## Level 1
1. Axial (internal) resistance $r_i$, membrane resistance $r_m$, membrane capacitance $c_m$.
2. The distance over which a steady-state passive voltage decays to $1/e$ (37 %). After 2 λ, 14 % remains.
3. **Passive** spread is purely electrotonic: the voltage decays with distance (and is filtered in time). **Active** propagation regenerates the signal at each location through voltage-gated channels (an AP), so it travels without decrement.
4. Myelin increases $R_m$ and decreases $C_m$, so current along the internode leaks very little and charges the membrane quickly. The AP only needs to be regenerated at the nodes, and the slow step of local charging and channel opening happens only every ~1 mm instead of continuously.

## Level 2
5. $10e^{-1}\approx3.7\,\text{mV}$. With λ = 1 mm: $10e^{-0.5}\approx6.1\,\text{mV}$.
6. $\lambda = \sqrt{\frac{20\,000\cdot4\times10^{-4}}{400}} = \sqrt{\frac{8}{400}} = \sqrt{0.02}\approx0.141\,\text{cm} = 1.41\,\text{mm}$
7. a) $\sqrt4 = 2$: λ doubles. b) $\sqrt{1/2}\approx0.71$: λ shrinks by about 29 %.
8. $L = 1/0.5 = 2$. Not compact: the far end is attenuated to $e^{-2}\approx14\%$ (in an infinite cable; a sealed end gives somewhat less attenuation).

## Level 3
9. $15\cdot6 = 90\,\text{m/s}$; 1 m takes about 11 ms.
10. $v\propto\sqrt d$: $\sqrt4 = 2$, so 2 m/s. For 10 m/s: $(10)^2 = 100$ times thicker, i.e. $d = 100\,\mu\text{m}$.
11. Myelinated: $30/6 = 5\,\mu\text{m}$. Unmyelinated: $v = 1\cdot\sqrt{d/1\,\mu\text{m}} = 30\Rightarrow d = 900\,\mu\text{m}$, almost 1 mm, 180 times thicker. That's why vertebrates use myelin and squid use giant axons.
12. Without a spatial gradient, $\frac{\partial^2V}{\partial x^2} = 0$, so $0 = \tau\frac{\partial V}{\partial t} + V$, i.e. $\tau\frac{dV}{dt} = -V$, the equation of a discharging RC circuit with solution $V_0e^{-t/\tau}$ ✓.

## Level 4
13. The cable acts as a **low-pass filter** that becomes stronger with distance: high-frequency components (the fast rise) are attenuated more than slow ones. Along the way, charge has to fill the capacitance of each segment. The EPSP arrives at the soma with a slower rise and broader shape (and later peak).
14. Without myelin, an internode has a low $R_m$ (current leaks out) and a high $C_m$ (more charge needed to change voltage). The current arriving from the last node is lost along the way and may not depolarise the next node to threshold, so conduction is blocked. The bare internodal membrane also has few Na⁺ channels, so it can't generate an AP itself.
15. The positive Na⁺ feedback **amplifies** the depolarisation at each new location back to full size. Passive losses are compensated, so the AP travels at constant amplitude, and the threshold ensures all-or-none behaviour. A linear (passive) system can only attenuate signals.
16. $e^{-1.2/0.8} = e^{-1.5}\approx0.22$ (22 %); $e^{-0.2/0.8} = e^{-0.25}\approx0.78$ (78 %). The distal input reaches the soma at less than a third of the efficacy of the proximal one, which is a strong reason for active dendritic conductances.
