---
aliases: [Membranes and Transport, Ion Channels, Membrane Transport, Na-K-ATPase, Membranen und Transport]
tags: [biology, membrane, transport, ion-channel, type/overview, neuro]
---
# Bio02 Membranes and Transport

> [[MOC-biology|↑ Biology MOC]] · [[Bio02 Membranes and Transport - Worksheet|✏️ Worksheet]] · [[Bio02 Membranes and Transport - Solutions|✅ Solutions]] · [[Mistakes - Biology|⚠️ Mistake log]]

## Why this matters
The membrane is where neuroscience happens. It separates two salt solutions, acts as a capacitor, and holds the pumps that build gradients and the channels that use them. Many drugs, toxins and genetic brain diseases act on membrane transport proteins.

## Lipid bilayer: structure and fluidity
- Two leaflets of phospholipids, about **5 nm** thick, with a hydrophobic core ([[Ch03 Intermolecular Forces and Solubility]]).
- **Fluid mosaic model:** lipids and many proteins diffuse laterally within the leaflet. Flipping between leaflets ("flip-flop") is rare and requires enzymes (flippases, scramblases).
- **Asymmetry:** phosphatidylserine (PS) sits on the inner leaflet. When PS appears on the outer leaflet, it signals "eat me" to microglia and macrophages, for example in apoptosis and synapse pruning.

**Fluidity increases with:**
- higher temperature
- shorter fatty acid tails
- more **unsaturated** (cis-kinked) tails

**Cholesterol** acts as a **buffer**. It stiffens fluid membranes and keeps rigid membranes from freezing.

**Lipid rafts** are microdomains rich in cholesterol and sphingolipids that cluster signalling proteins.

**Electrical properties:** the membrane is an insulator between two conductors, i.e. a **capacitor**.
- Specific capacitance $c_m\approx1\,\mu\text{F/cm}^2$.
- Charge needed for a voltage change: $Q = CV$.
- Together with membrane resistance, it sets the **time constant** $\tau_m = R_mC_m$.

## Permeability: who can cross?
| Freely permeable | Slowly | Practically impermeable (need proteins) |
|---|---|---|
| O₂, CO₂, N₂, small lipophilic molecules (steroids, ethanol, anaesthetics) | H₂O, urea, glycerol | ions (Na⁺, K⁺, Cl⁻, Ca²⁺), glucose, amino acids, charged and large molecules |

## Passive transport (down the electrochemical gradient, no energy)
1. **Simple diffusion** through the lipid bilayer: O₂, CO₂, steroids. The rate is proportional to the concentration difference (Fick's law, [[Ch06 Solutions and Concentration]]).
2. **Channels**: aqueous pores that open and close (gating).
   - Very fast: **10⁶–10⁸ ions/s** per channel.
   - Selective (K⁺, Na⁺, Ca²⁺, Cl⁻, or nonselective cation channels).
   - Aquaporins for water (AQP4 in astrocytes).
3. **Carriers** (facilitated diffusion): bind their substrate and change conformation.
   - Slower (about 10²–10⁴/s) and **saturable** (Michaelis–Menten-like, [[Bio03 Proteins and Enzymes]]).
   - Example: GLUT1 and GLUT3 for glucose.

## Active transport (against the gradient, needs energy)
**Primary active transport** uses ATP directly.
- **Na⁺/K⁺-ATPase:** per ATP, **3 Na⁺ out and 2 K⁺ in**.
  - It is **electrogenic**: it moves one net positive charge outward per cycle and contributes a few mV of hyperpolarisation.
  - It restores the gradients after activity and consumes a large share of the brain's ATP.
  - Blocked by ouabain and digoxin.
- **Ca²⁺-ATPases:** PMCA (plasma membrane) and SERCA (into the ER) keep cytosolic Ca²⁺ at about 100 nM.
- **V-ATPase:** pumps H⁺ into synaptic vesicles and lysosomes ([[Ch04 Acids Bases and pH]]).

**Secondary active transport** couples one solute moving downhill (usually Na⁺, sometimes H⁺) to another moving uphill.

| Transporter | Stoichiometry / function | Neuro relevance |
|---|---|---|
| NCX (Na⁺/Ca²⁺ exchanger) | 3 Na⁺ in : 1 Ca²⁺ out | removes Ca²⁺ after activity |
| **NKCC1** | Na⁺ + K⁺ + 2 Cl⁻ in | high in immature neurons → depolarising GABA |
| **KCC2** | K⁺ + Cl⁻ out | mature neurons → low Cl⁻, inhibitory GABA |
| EAAT1/2 (GLAST, GLT-1) | glutamate + 3 Na⁺ + H⁺ in, K⁺ out | astrocytic glutamate clearance; prevents excitotoxicity |
| **DAT, SERT, NET** | monoamine + Na⁺ + Cl⁻ in | reuptake; SSRIs block SERT; cocaine blocks DAT; amphetamine reverses DAT |
| VMAT2, VGLUT, VGAT | transmitter into vesicle in exchange for H⁺ | vesicle filling; reserpine blocks VMAT |

## Ion channels
**Basic properties**
- **Selectivity:** set by the selectivity filter ([[Ch01 Atomic Structure]]).
- **Gating:** what opens the channel.
- **Single-channel conductance** $\gamma$: about 1–300 pS.
- Single-channel current: $i = \gamma(V - E_\text{rev})$. Example: $\gamma = 20\,\text{pS}$ and $V - E = -100\,\text{mV}$ give $i = -2\,\text{pA}$.
- Macroscopic current: $I = N\cdot P_\text{open}\cdot i$.

| Gating type | Examples | Function |
|---|---|---|
| **Voltage-gated** | Nav (Na⁺), Kv (K⁺), Cav (Ca²⁺), HCN | action potentials, transmitter release (presynaptic Cav2.1/2.2), pacemaking |
| **Ligand-gated** (ionotropic receptors) | nAChR, AMPA, NMDA, kainate, GABA_A, glycine, 5-HT₃, P2X | fast synaptic transmission ([[Bio06 Synapses and Neurotransmitters]]) |
| **Mechanosensitive** | Piezo2 (touch, proprioception), Piezo1, TMC1/2 (hair cells, hearing), some K2P channels | somatosensation, hearing, baroreception |
| Other | TRP channels (TRPV1: heat and capsaicin; TRPM8: cold), Ca²⁺-activated K⁺ channels (BK, SK), leak K2P channels | temperature, pain, afterhyperpolarisation, resting potential |

**Structure of voltage-gated channels:** four domains or subunits, each with 6 transmembrane segments (S1–S6).
- **S4** carries positive charges (Arg/Lys) and moves in the electric field: it is the **voltage sensor**.
- S5–S6 and the pore loop form the pore.
- Nav channels **inactivate** within about 1 ms (the "ball-and-chain" / IFM motif), which underlies the refractory period ([[Bio05 Neurons and Action Potentials]]).

## In neuroscience #neuro
- **Channelopathies:**
  - **Dravet syndrome**: loss of Nav1.1 (*SCN1A*), mainly in inhibitory interneurons, causes severe epilepsy.
  - Loss of **Nav1.7** (*SCN9A*) causes congenital insensitivity to pain; gain-of-function causes erythromelalgia.
  - Episodic ataxia type 1 (Kv1.1).
  - Familial hemiplegic migraine (Cav2.1).
- **Toxins as tools:** tetrodotoxin (TTX, pufferfish) blocks Nav; tetraethylammonium (TEA) blocks K⁺ channels; ω-conotoxins block Cav2.2; α-bungarotoxin binds the nAChR.
- **Drugs:** local anaesthetics, many antiepileptics (carbamazepine, phenytoin) and lidocaine block Nav channels. Benzodiazepines enhance GABA_A. SSRIs block SERT.
- **Nobel prizes:**
  - Neher & Sakmann, 1991: single-channel recording with patch clamp ([[Meth03 Electrophysiology]]).
  - Agre and MacKinnon, 2003: aquaporins and the K⁺ channel structure ([[Meth02 Structural Biology]]).
  - Julius & Patapoutian, 2021: TRPV1 and Piezo.

## Math links #math-link
- $Q = CV$, $\tau = RC$, parallel conductances add → [[A5 Fractions]], [[B2 Exponential Functions]]
- $i = \gamma(V - E)$, a linear current–voltage (I–V) relation → [[B1 Properties of Functions]]
- Open probability of voltage-gated channels: Boltzmann sigmoid $P_\text{open} = \frac{1}{1 + e^{-(V - V_{1/2})/k}}$ → [[B8 Curve Sketching]]
- Carrier saturation: Michaelis–Menten → [[A5 Fractions]]
- Number of open channels out of $N$ (binomial) → [[A6 Binomial Formulas and Theorem]]

## Connections
- Lipids → [[Ch08 Biomolecules]]; solubility → [[Ch03 Intermolecular Forces and Solubility]]
- Gradients and equilibrium potentials → [[Ch05 Redox and Electrochemistry]]
- Channels in action potentials → [[Bio05 Neurons and Action Potentials]]
- Receptors → [[Bio06 Synapses and Neurotransmitters]]
- Recording channel currents → [[Meth03 Electrophysiology]]

## Key takeaways
- The bilayer is a fluid, asymmetric insulator and capacitor (≈ 1 µF/cm²). Cholesterol buffers its fluidity.
- Passive: diffusion, channels (fast, up to ~10⁸/s), carriers (saturable). Active: pumps (ATP) and secondary transporters (Na⁺ gradient).
- Na⁺/K⁺-ATPase: 3 Na⁺ out, 2 K⁺ in, 1 ATP.
- Channels are gated by voltage, ligands or mechanical force.
