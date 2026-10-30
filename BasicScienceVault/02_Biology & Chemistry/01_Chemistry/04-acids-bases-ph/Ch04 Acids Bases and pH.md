---
aliases: [Acids Bases and pH, pH, Henderson-Hasselbalch, Buffers, Säuren und Basen]
tags: [chemistry, ph, buffer, type/overview, neuro]
---
# Ch04 Acids, Bases and pH

> [[MOC-chemistry|↑ Chemistry MOC]] · [[Ch04 Acids Bases and pH - Worksheet|✏️ Worksheet]] · [[Ch04 Acids Bases and pH - Solutions|✅ Solutions]] · [[Mistakes - Chemistry|⚠️ Mistake log]]

## Why this matters
The charge of amino acids, neurotransmitters and drugs depends on pH. Protein function, receptor gating, vesicle filling and drug uptake all change with protonation. Brain pH is tightly regulated. Even small shifts change excitability, which is why hyperventilation can trigger seizures.

## Definitions
- **Acid** (Brønsted): proton donor, $\text{HA}\rightleftharpoons\text{H}^+ + \text{A}^-$
- **Base:** proton acceptor, $\text{B} + \text{H}^+\rightleftharpoons\text{BH}^+$
- An acid and the base it forms after losing H⁺ are a **conjugate pair** (HA/A⁻, BH⁺/B).

$$\text{pH} = -\log_{10}[\text{H}^+], \qquad [\text{H}^+] = 10^{-\text{pH}}\ \text{mol/L}$$
- Water: $K_w = [\text{H}^+][\text{OH}^-] = 10^{-14}$, so $\text{pH} + \text{pOH} = 14$ (at 25 °C).
- pH 7 is neutral; below 7 is acidic, above 7 is basic.
- **One pH unit = a factor of 10** in [H⁺]. Blood at pH 7.4 has $[\text{H}^+] = 10^{-7.4}\approx4\times10^{-8}\,\text{M}$ = 40 nM.

**Acid strength** is given by the dissociation constant
$$K_a = \frac{[\text{H}^+][\text{A}^-]}{[\text{HA}]},\qquad \text{p}K_a = -\log_{10}K_a$$
A smaller $\text{p}K_a$ means a stronger acid. Strong acids (HCl) dissociate completely; weak acids (acetic acid, $\text{p}K_a = 4.76$) only partly.

## Henderson–Hasselbalch equation
Take the log of the $K_a$ expression and rearrange:
$$\boxed{\text{pH} = \text{p}K_a + \log_{10}\frac{[\text{A}^-]}{[\text{HA}]}}$$
| pH relative to p$K_a$ | ratio [A⁻]/[HA] | mostly … |
|---|---|---|
| pH = p$K_a$ − 2 | 1 : 100 | protonated (HA) |
| pH = p$K_a$ − 1 | 1 : 10 | protonated |
| pH = p$K_a$ | 1 : 1 | half and half |
| pH = p$K_a$ + 1 | 10 : 1 | deprotonated (A⁻) |
| pH = p$K_a$ + 2 | 100 : 1 | deprotonated |

**Rule of thumb:** if the pH is below the p$K_a$, the group carries its proton; if the pH is above the p$K_a$, it has lost it.

At pH 7.4:
- **carboxyl groups** (p$K_a$ ≈ 2–4) are **–COO⁻**
- **amino groups** (p$K_a$ ≈ 9–10.5) are **–NH₃⁺**
- **phosphates** are negatively charged
- **histidine** (p$K_a$ ≈ 6) is partly protonated, which makes it a perfect pH sensor in proteins

## Buffers
A **buffer** is a mixture of a weak acid and its conjugate base. Added H⁺ is taken up by A⁻, and added OH⁻ is neutralised by HA, so the pH changes only slightly.
- It buffers best at **pH = p$K_a$**. The useful range is about **p$K_a$ ± 1**.
- Buffer capacity grows with the total concentration of the buffer.
- Lab buffers include HEPES (p$K_a$ ≈ 7.5), Tris (≈ 8.1) and phosphate (p$K_{a2}$ ≈ 7.2).

### The bicarbonate buffer (blood and brain)
$$\text{CO}_2 + \text{H}_2\text{O}\ \underset{\text{carbonic anhydrase}}{\rightleftharpoons}\ \text{H}_2\text{CO}_3\rightleftharpoons\text{H}^+ + \text{HCO}_3^-$$
$$\text{pH} = 6.1 + \log_{10}\frac{[\text{HCO}_3^-]}{0.03\cdot p\text{CO}_2}$$
($[\text{HCO}_3^-]$ in mM, $p\text{CO}_2$ in mmHg; 0.03 is the solubility of CO₂.)
- Normal values: $[\text{HCO}_3^-] = 24\,\text{mM}$ and $p\text{CO}_2 = 40\,\text{mmHg}$, giving a ratio of $24/1.2 = 20$ and pH $= 6.1 + \log_{10}20 \approx 6.1 + 1.3 = 7.4$.
- Although the p$K_a$ (6.1) is far from 7.4, the buffer is very effective because it is an **open system**. The **lungs** adjust pCO₂ within minutes, and the **kidneys** adjust HCO₃⁻ over hours to days.
- **Hyperventilation** lowers pCO₂, which raises pH (respiratory alkalosis). **Hypoventilation** raises pCO₂ and lowers pH (respiratory acidosis).

## In neuroscience #neuro
- **Brain pH and excitability:** alkalosis increases neuronal excitability, partly through relief of the proton block of NMDA receptors. Acidosis decreases excitability. Clinicians use **hyperventilation** during EEG to provoke absence seizures. Acidosis at the end of a seizure helps terminate it.
- **Cerebral blood flow:** CO₂ is a strong vasodilator in the brain. Hyperventilation causes vasoconstriction (light-headedness) and was used acutely to lower intracranial pressure. CO₂ inhalation is used as a vascular challenge in BOLD fMRI.
- **Central chemoreceptors** in the brainstem sense CSF pH, which is driven by CO₂ because CO₂ crosses the BBB but HCO₃⁻ does so only slowly, and they control breathing.
- **Acidic compartments:**
  - Synaptic vesicles have pH ≈ 5.5, set by the V-ATPase proton pump. The proton gradient drives transmitter loading (e.g. VGLUT, VMAT).
  - Lysosomes have pH ≈ 4.5–5.
- **pHluorin:** a pH-sensitive GFP variant. Its fluorescence is quenched in the acidic vesicle and turns on at exocytosis when the vesicle opens to pH 7.4. It is used to image transmitter release and recycling.
- **Acid-sensing ion channels (ASICs)** open at low pH and are involved in pain, fear and ischaemia.
- **Local anaesthetics** (lidocaine, p$K_a$ ≈ 7.9) are weak bases.
  - The **uncharged** form crosses membranes.
  - The **charged** form blocks the Na⁺ channel from the inside.
  - In inflamed, acidic tissue, more drug is protonated and less reaches the nerve, so they work less well.

## Math links #math-link
- pH, p$K_a$ and Henderson–Hasselbalch are all logarithms → [[A3 Logarithms]], [[B3 Logarithmic Functions]]
- Converting pH to [H⁺] uses powers of ten → [[A1 Exponent Rules]]
- The fraction protonated, $\frac{1}{1 + 10^{\text{pH}-\text{p}K_a}}$, is a **sigmoid** in pH → [[B1 Properties of Functions]], [[B8 Curve Sketching]]

## Connections
- Functional groups and their charges → [[Ch07 Organic Chemistry Essentials]]
- Amino acids as zwitterions → [[Ch08 Biomolecules]]
- Electrochemical gradients (H⁺ gradient in mitochondria and vesicles) → [[Ch05 Redox and Electrochemistry]]
- Vesicle filling → [[Bio06 Synapses and Neurotransmitters]]

## Key takeaways
- pH = −log[H⁺]; one unit is a tenfold change.
- pH = p$K_a$ + log([A⁻]/[HA]); below the p$K_a$ the group is protonated, above it deprotonated.
- Buffers work best at their p$K_a$ ± 1. The bicarbonate system is regulated by the lungs and kidneys.
- Brain pH affects excitability, blood flow and drug action.
