---
aliases: [Capacitance and RC Circuits, Capacitor, Time Constant, Passive Membrane, Leaky Integrate-and-Fire, Kondensator]
tags: [physics, capacitance, rc-circuit, time-constant, type/overview, neuro]
---
# Ph05 Capacitance and RC Circuits

> [[MOC-physics|↑ Physics MOC]] · [[Ph05 Capacitance and RC Circuits - Worksheet|✏️ Worksheet]] · [[Ph05 Capacitance and RC Circuits - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
Because the membrane is a capacitor, a neuron can't change its voltage instantly. It **integrates** input over time with a time constant τ of about 10–30 ms. This explains temporal summation, why synaptic potentials are slower than the currents that cause them, and why the leaky integrate-and-fire model works.

## Capacitance
A **capacitor** consists of two conductors separated by an insulator. Applying a voltage $V$ stores charge $+Q$ on one side and $-Q$ on the other:
$$C = \frac{Q}{V}\qquad[\text{F} = \text{C/V}]$$
- **Parallel-plate capacitor:** $C = \varepsilon_0\varepsilon_r\frac{A}{d}$, with $\varepsilon_0 = 8.85\times10^{-12}$ F/m. Capacitance is larger for a larger area and a thinner, more polarisable insulator.
- **Capacitive current:** charge only changes if current flows onto the plates, so
  $$I_C = C\frac{dV}{dt}$$
  A capacitor passes current **only while the voltage changes**. At constant voltage, $I_C = 0$.
- **Stored energy:** $E = \tfrac12CV^2$.
- Capacitors in parallel add ($C = C_1 + C_2$), like areas of membrane.

## The lipid bilayer as a capacitor
- Two conducting solutions (cytoplasm, extracellular fluid) are separated by an insulating hydrophobic core about 2–4 nm thick, with $\varepsilon_r\approx2$.
- Estimate per area: $c_m = \frac{\varepsilon_0\varepsilon_r}{d}\approx\frac{8.85\times10^{-12}\cdot2}{2\times10^{-9}}\approx9\times10^{-3}\,\text{F/m}^2\approx0.9\,\mu\text{F/cm}^2$. This matches the measured **≈ 1 µF/cm²**, which is remarkably constant across cell types.
- Total capacitance is proportional to membrane area: a soma of 20 µm diameter has $A = 4\pi r^2\approx1.3\times10^{-5}$ cm², so $C\approx13$ pF. Whole neurons with dendrites have ~50–300 pF. Measuring $C$ is a way to estimate membrane area.
- **Myelin** stacks many membranes **in series**. Capacitances in series combine like resistances in parallel ($\frac{1}{C} = \sum\frac{1}{C_i}$), so 50 layers reduce capacitance about 50-fold ([[Ph10 Signal Propagation and Cable Theory]]).

## Charging and discharging (RC circuit)
A resistor and capacitor in parallel (the membrane) driven by a constant current step $I$:
$$C\frac{dV}{dt} = -\frac{V}{R} + I$$
(Here $V$ is measured relative to rest.)

**Charging** after the current turns on at $t = 0$:
$$V(t) = IR\left(1 - e^{-t/\tau}\right),\qquad \tau = RC$$
**Discharging** after the current turns off:
$$V(t) = V_0\,e^{-t/\tau}$$

| Time | Charging: fraction of final value | Discharging: fraction remaining |
|---|---|---|
| $t = \tau$ | 63 % | 37 % |
| $t = 2\tau$ | 86 % | 14 % |
| $t = 3\tau$ | 95 % | 5 % |
| $t = 5\tau$ | > 99 % | < 1 % |

- Steady state: $V_\infty = IR$ (Ohm's law, after the capacitor is "full").
- Initial slope: $\frac{dV}{dt}\big|_0 = \frac{I}{C}$. At first, all current goes into charging the capacitor.

## Time constant τ = R·C and its meaning
- **Membrane time constant:** $\tau_m = R_\text{in}C = R_mc_m$ (specific values). Because $R_m$ (Ω·cm²) times $c_m$ (F/cm²) has the areas cancel, **τ doesn't depend on cell size**, only on how leaky the membrane is. Example: $R_m = 20\,\text{k}\Omega\text{·cm}^2$ and $c_m = 1\,\mu\text{F/cm}^2$ give $\tau_m = 20$ ms.
- **Meaning:**
  - **Temporal integration (summation):** inputs arriving within about τ of each other add up.
  - **Low-pass filtering:** fast fluctuations are smoothed out ([[Ph09 Waves and Oscillations]]); the cutoff frequency is $f_c = \frac{1}{2\pi\tau}$.
  - **Synaptic potentials are slower than synaptic currents:** a 2 ms EPSC produces an EPSP lasting about τ.
  - A larger τ means a longer "memory" of inputs; a shorter τ means more precise timing (e.g. auditory brainstem neurons have τ < 1 ms for sound localisation).
  - In active cortex, many open synaptic channels lower $R$, so τ shrinks (the "high-conductance state").

## Passive membrane model as the basis for neuron models
**Leaky membrane (leaky capacitor):**
$$\tau_m\frac{dV}{dt} = -(V - E_L) + R_mI(t)$$

**Leaky integrate-and-fire (LIF) neuron:** the same equation plus a rule: when $V$ reaches the threshold $V_\theta$, a spike is registered and $V$ is reset to $V_\text{reset}$ (plus a refractory period). With constant input $V_\infty = E_L + RI$, the time to threshold is
$$T = \tau\ln\frac{V_\infty - V_\text{reset}}{V_\infty - V_\theta}$$
which gives the firing rate $f = \frac{1}{t_\text{ref} + T}$. If $V_\infty < V_\theta$, the neuron never fires (the current is below **rheobase**).

The **Hodgkin–Huxley model** adds voltage-dependent conductances in parallel to this RC circuit ([[Ph10 Signal Propagation and Cable Theory]], [[Bio05 Neurons and Action Potentials]]).

## In neuroscience #neuro
- **Measuring τ and C in patch clamp:** inject a small current step, fit an exponential to the voltage response to get τ, compute $R_\text{in} = \Delta V/I$, then $C = \tau/R_\text{in}$ ([[Meth03 Electrophysiology]]).
- **Capacitance measurements of exocytosis:** each fused vesicle adds its membrane to the cell surface, so $C$ increases in tiny steps (≈ 0.05 fF for a small synaptic vesicle, a few fF for large dense-core vesicles). This allows release to be measured electrically, for example at large synaptic terminals and in chromaffin cells.
- **Temporal coding:** neurons with short τ act as **coincidence detectors**; neurons with long τ act as **integrators**.

## Math links #math-link
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- Differential equation $\tau\frac{dV}{dt} = -V + RI$ and its exponential solution → [[B6 Differentiation Rules]], [[B2 Exponential Functions]]
- Time to threshold by taking the logarithm → [[A3 Logarithms]], [[A8 Solving Equations]]
- $I_C = C\,dV/dt$ is a derivative; charge $Q = \int I\,dt$ is an integral → [[B7 Antiderivatives and Integration]]
- Euler integration of the LIF model → [[B9 Taylor Series]]
- Series capacitance: reciprocals → [[A5 Fractions]]

## Connections
- Resistors and Kirchhoff → [[Ph04 Circuits and Resistance]]
- Membrane field and potential → [[Ph03 Electric Fields and Potential]]
- Filtering → [[Ph09 Waves and Oscillations]]
- Spatial spread → [[Ph10 Signal Propagation and Cable Theory]]
- Membrane structure → [[Bio02 Membranes and Transport]]

## Key takeaways
- $C = Q/V$; membrane $c_m\approx1\,\mu\text{F/cm}^2$; $I_C = C\,dV/dt$ (current only while V changes).
- RC charging: $V = IR(1 - e^{-t/\tau})$; discharging: $V_0e^{-t/\tau}$; 63 % / 37 % after one τ.
- $\tau = RC$ (10–30 ms), independent of cell size. It sets temporal summation and low-pass filtering.
- The leaky capacitor + threshold + reset is the LIF neuron.
