---
tags: [physics, circuit, resistance, type/solution]
---
# Ph04 Circuits and Resistance – Solutions

> Worksheet: [[Ph04 Circuits and Resistance - Worksheet]] · Theory: [[Ph04 Circuits and Resistance]] · Wrong? → [[Mistakes - Physics]]

## Level 1
1. $V = 100\cdot0.2 = 20\,\text{V}$
2. $\Delta V = 2\times10^8\cdot5\times10^{-11} = 10^{-2}\,\text{V} = 10\,\text{mV}$
3. $\frac{1}{2\times10^{-11}} = 5\times10^{10}\,\Omega = 50\,\text{G}\Omega$; $\frac{1}{10^8} = 10^{-8}\,\text{S} = 10\,\text{nS}$
4. $I = 10\,\text{pS}\cdot(-80\,\text{mV}) = -800\times10^{-15}\,\text{A} = -0.8\,\text{pA}$ (inward)

## Level 2
5. Series: 400 Ω. Parallel: $\frac{100\cdot300}{400} = 75\,\Omega$.
6. $G = 1000\cdot10\,\text{pS} = 10\,\text{nS}$, so $R = 100\,\text{M}\Omega$.
7. $\frac1R = \frac1{300} + \frac1{300} + \frac2{300} = \frac4{300}$, so $R = 75\,\text{M}\Omega$.
8. $\Delta V = 10^7\cdot10^{-9} = 10\,\text{mV}$. The real membrane potential deviates by 10 mV from the command voltage, so I–V curves and kinetics are distorted. Use series-resistance compensation and low-resistance pipettes, and keep currents small.

## Level 3
9. $2 - 0.5 + I_3 = 0\Rightarrow I_3 = -1.5\,\text{nA}$ (i.e. 1.5 nA flowing out of the node).
10. KCL: $g_\text{K}(V - E_\text{K}) + g_\text{Na}(V - E_\text{Na}) = 0\Rightarrow V = \frac{10\cdot(-90) + 1\cdot60}{11} = \frac{-840}{11}\approx-76.4\,\text{mV}$
11. $V = \frac{-900 + 60 + 0}{15} = \frac{-840}{15} = -56\,\text{mV}$ (depolarised by about 20 mV)
12. $V = \frac{-900 + 60 + 5\cdot(-76)}{16} = \frac{-1220}{16} = -76.25\,\text{mV}$, almost unchanged. Input resistance: before $\frac{1}{11\,\text{nS}}\approx91\,\text{M}\Omega$; after $\frac{1}{16\,\text{nS}} = 62.5\,\text{M}\Omega$.

## Level 4
13. Small neurons have a small membrane area, so they have fewer channels and a **higher input resistance**. The same synaptic current $I$ produces a larger $\Delta V = I\cdot R_\text{in}$, which reaches threshold earlier. Large motor neurons need more current and are recruited only for strong contractions.
14. **Shunting:** the input resistance falls (task 12: from 91 to 62.5 MΩ), so every excitatory current produces a **smaller** voltage change ($\Delta V = I\cdot R_\text{in}$). Mathematically, inhibition increases the denominator of the weighted average and pulls $V$ towards $E_\text{inh}$, so excitation is divided.
15. Each neuron has its own membrane circuit (batteries + conductances + capacitor between its inside and outside). The **inside nodes of the two cells** are connected by a **resistor** (conductance $g_\text{gap}$). Current flows through it in proportion to the voltage difference between the cells, $I = g_\text{gap}(V_1 - V_2)$.
