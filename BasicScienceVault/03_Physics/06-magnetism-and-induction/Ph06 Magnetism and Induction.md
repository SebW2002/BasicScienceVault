---
aliases: [Magnetism and Induction, Faraday's Law, TMS, Magnetic Field, Magnetismus und Induktion]
tags: [physics, magnetism, induction, tms, meg, type/overview, neuro]
---
# Ph06 Magnetism and Induction

> [[MOC-physics|↑ Physics MOC]] · [[Ph06 Magnetism and Induction - Worksheet|✏️ Worksheet]] · [[Ph06 Magnetism and Induction - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
Electricity and magnetism are two sides of one phenomenon. **Moving charges (currents) create magnetic fields**, which is why the brain's own currents can be measured by **MEG**. **Changing magnetic fields create electric fields**, which is how **TMS** stimulates the cortex through the intact skull. Both principles, plus magnetic resonance, are also behind **MRI**.

## Magnetic fields and currents
- The magnetic field $\vec B$ is measured in **tesla (T)**. Typical values:
  - Earth: ≈ 50 µT
  - fridge magnet: ≈ 5 mT
  - clinical MRI: 1.5–3 T (research: 7–11.7 T)
  - TMS coil peak: ≈ 1–2.5 T
  - brain (MEG): **10–1000 fT** (1 fT = 10⁻¹⁵ T)
- **Oersted / Biot–Savart:** every current produces a magnetic field around it. For a long straight wire,
  $$B = \frac{\mu_0I}{2\pi r},\qquad \mu_0 = 4\pi\times10^{-7}\,\text{T·m/A}$$
  Field lines form circles around the wire. **Right-hand rule:** thumb along the current, fingers curl in the direction of $\vec B$.
- **Coils** (solenoids) concentrate the field: $B = \mu_0nI$ inside ($n$ = turns per length).
- **Lorentz force** on moving charges: $\vec F = q\,\vec v\times\vec B$ (perpendicular to both; [[D2 Dot and Cross Product]]). It acts on current-carrying wires and makes ions in flowing blood generate tiny voltages in an MRI scanner.

## Faraday's law of induction
A **changing magnetic flux** induces an electric field and therefore a voltage (EMF) in any loop around it:
$$\mathcal E = -\frac{d\Phi}{dt},\qquad \Phi = B\cdot A\ (\text{flux} = \text{field}\times\text{area, for a perpendicular field})$$
- It is the **rate of change** that matters, not the field strength itself. A static MRI field induces nothing in a stationary body; switching gradients do.
- **Lenz's rule** (the minus sign): the induced current opposes the change that caused it.
- With $N$ turns: $\mathcal E = -N\frac{d\Phi}{dt}$, which is the principle of generators, transformers and pick-up coils.
- **Induced field in a conducting medium** (tissue): for a loop of radius $r$ in a field that changes uniformly, $E = \frac{r}{2}\frac{dB}{dt}$.

## Transcranial magnetic stimulation (TMS)
1. A capacitor discharges a brief, strong current pulse (several kA, ~0.1 ms rise time) through a coil held on the scalp.
2. The coil produces a rapidly changing magnetic field (≈ 1–2 T), which passes the skull and scalp unattenuated.
3. Faraday's law: the changing field **induces an electric field** in the brain (on the order of 100 V/m in superficial cortex), and **induced currents** flow in the conducting tissue.
4. The induced field depolarises axons, mostly at bends and terminals, which triggers action potentials in the cortex beneath the coil.

- **Figure-of-eight coils** focus stimulation under their centre (a few cm²). Depth is limited to about 2–3 cm because fields fall off with distance from the coil.
- **Uses:**
  - Over motor cortex, a single pulse gives a muscle twitch, the **motor evoked potential (MEP)**, which defines the motor threshold.
  - "Virtual lesions" test causality in cognitive studies.
  - **Repetitive TMS (rTMS)**: high frequency (e.g. 10 Hz, theta-burst) tends to increase excitability; low frequency (1 Hz) tends to decrease it.
  - rTMS of the left dorsolateral prefrontal cortex is an approved treatment for **depression**.
- **Safety:** risk of seizures at high intensities and frequencies; no metal implants near the coil; noise (hearing protection).

## Magnetic fields of neural currents: the basis of MEG
- Synchronous postsynaptic currents in tens of thousands of parallel **pyramidal cells** form a current dipole (≈ 10 nA·m), whose magnetic field outside the head is about **10–1000 fT**.
- This is **about 50 million to 5 billion times smaller than the Earth's field** (50 µT). MEG therefore needs:
  - **SQUIDs** (superconducting quantum interference devices, cooled with liquid helium) or newer **optically pumped magnetometers (OPMs)**, which can sit directly on the scalp
  - **magnetically shielded rooms**
  - gradiometers that cancel distant noise
- **Advantages over EEG:** magnetic fields pass through the skull without distortion (good source localisation); reference-free.
- **Limitation:** in a spherical head model, **radial** dipoles produce no external field (cross product with the radial direction is zero), so MEG mainly sees **tangential** sources in sulcal walls ([[Meth03 Electrophysiology]], [[D2 Dot and Cross Product]]).

## Related: MRI in one paragraph
Hydrogen nuclei (spins) align in a strong static field $B_0$ and precess at the Larmor frequency $f = \frac{\gamma}{2\pi}B_0$ (≈ 128 MHz at 3 T). An RF pulse tips them; their relaxation induces a signal in receiver coils (**Faraday's law**). Switched **gradient fields** encode position. Rapid gradient switching induces electric fields in the body and can cause peripheral nerve stimulation (tingling), a direct application of induction. See [[Meth04 In Vivo Imaging]] and [[Meth02 Structural Biology]].

## In neuroscience #neuro
- TMS + EEG measures cortical reactivity and connectivity. TMS + MEP measures cortical excitability (e.g. after drugs, in stroke).
- Deep TMS (H-coils) is approved for OCD and smoking cessation in some countries.
- MEG gives millisecond-resolved, millimetre-to-centimetre source maps, used clinically to localise epileptic spikes and eloquent cortex before surgery.

## Math links #math-link
- $B\propto1/r$ (wire) vs. dipole fields $\propto1/r^3$: power laws → [[A1 Exponent Rules]]
- Faraday's law as a derivative of flux, $\mathcal E = -d\Phi/dt$ → [[B6 Differentiation Rules]]
- Lorentz force and dipole fields: cross product, right-hand rule → [[D2 Dot and Cross Product]]
- MEG source localisation: inverse problem with a lead-field matrix → [[C3 Linear Systems and Gaussian Elimination]]

## Connections
- Currents → [[Ph02 Electricity and Charge]]; induced fields → [[Ph03 Electric Fields and Potential]]
- MEG and EEG → [[Meth03 Electrophysiology]]
- MRI → [[Meth04 In Vivo Imaging]]
- Larmor/NMR → [[Meth02 Structural Biology]]
- What TMS triggers → [[Bio05 Neurons and Action Potentials]]

## Key takeaways
- Currents create magnetic fields ($B = \mu_0I/2\pi r$ for a wire). Neural currents produce fT fields, which is MEG.
- Changing magnetic flux induces an electric field ($\mathcal E = -d\Phi/dt$). Fast-changing coil fields induce ~100 V/m in cortex, which is TMS.
- MEG sees tangential, not radial, dipoles and needs SQUIDs/OPMs and shielding.
