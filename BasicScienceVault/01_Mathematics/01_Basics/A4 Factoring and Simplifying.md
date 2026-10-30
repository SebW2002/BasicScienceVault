---
aliases: [Factoring and Simplifying, Factoring, Ausklammern]
tags: [basics, factoring, algebra, type/overview, neuro]
---
# A4 Factoring and Simplifying

> [[A0 Basics MOC|↑ Basics MOC]] · [[A4 Factoring and Simplifying - Worksheet|✏️ Worksheet]] · [[A4 Factoring and Simplifying - Solutions|✅ Solutions]] · [[Mistakes - Basics|⚠️ Mistake log]]

## Why this matters
Factoring is the reverse of multiplying out. It lets you cancel fractions, find zeros (a product is zero iff a factor is zero) and reveal hidden structure in formulas – e.g. that the resting potential is a **weighted average** of reversal potentials.

## The tools
### 1. Distributive law (both directions)
$$a(b + c) = ab + ac \qquad\longleftrightarrow\qquad ab + ac = a(b + c)$$

### 2. Common factor
Find the largest factor shared by **all** terms: $6x^3 - 9x^2 = 3x^2(2x - 3)$.

### 3. Grouping
$ax + ay + bx + by = a(x+y) + b(x+y) = (a+b)(x+y)$

### 4. Binomial patterns (see [[A6 Binomial Formulas and Theorem]])
$a^2 + 2ab + b^2 = (a+b)^2$, $\;a^2 - 2ab + b^2 = (a-b)^2$, $\;a^2 - b^2 = (a-b)(a+b)$

### 5. Quadratics $x^2 + px + q$
If $x_1, x_2$ are the zeros, then $x^2 + px + q = (x - x_1)(x - x_2)$, with $x_1 + x_2 = -p$ and $x_1 \cdot x_2 = q$ (Vieta).
Example: $x^2 + 5x + 6$: two numbers with product 6 and sum 5 → 2 and 3 → $(x+2)(x+3)$.
For $ax^2 + bx + c$ with $a \neq 1$: $a(x - x_1)(x - x_2)$, zeros via the quadratic formula ([[A8 Solving Equations]]).

## Simplifying = factor first, then cancel
$$\frac{x^2 - 9}{x^2 + 3x} = \frac{(x-3)(x+3)}{x(x+3)} = \frac{x-3}{x} \quad (x \neq 0,\ x \neq -3)$$

> [!important] Golden rule
> **Only factors can be cancelled, never summands.** $\dfrac{x + 2}{2} \neq x + 1$, but $\dfrac{2x+4}{2} = \dfrac{2(x+2)}{2} = x + 2$.
> Note the excluded values: cancelling does not remove the original domain restriction.

## In neuroscience #neuro
**Steady-state membrane potential.** With several conductances, the total ionic current is
$$I = g_L(V - E_L) + g_K(V - E_K) + g_{Na}(V - E_{Na})$$
At steady state $I = 0$. Multiply out and **factor out $V$**:
$$V(g_L + g_K + g_{Na}) = g_L E_L + g_K E_K + g_{Na} E_{Na} \;\Rightarrow\; V = \frac{g_L E_L + g_K E_K + g_{Na} E_{Na}}{g_L + g_K + g_{Na}}$$
The membrane potential is a **conductance-weighted average** of the reversal potentials. Opening more Na⁺ channels pulls $V$ towards $E_{Na}$ – the idea behind the action potential and the GHK equation.

**Shunting inhibition** falls out of the same formula: a synapse with $E_\text{syn} \approx V_\text{rest}$ doesn't change the numerator much but increases the denominator, "dividing down" excitatory effects.

## Connections
- Patterns used here → [[A6 Binomial Formulas and Theorem]]
- Cancelling in fractions → [[A5 Fractions]]
- Factored form shows zeros directly → [[A8 Solving Equations]], [[B1 Properties of Functions]]
- Removable discontinuities after cancelling → [[B5 Limits and Continuity]]

## Where this is used in the vault
**Most important applications:** Steady-state membrane potential as a conductance-weighted average and shunting inhibition ([[Ph04 Circuits and Resistance]], [[Bio06 Synapses and Neurotransmitters]]).

**All notes that build on this topic:**
- *Physics:* [[Ph04 Circuits and Resistance]]
- *Chemistry:* [[Ch05 Redox and Electrochemistry]]
- *Biology:* [[Bio06 Synapses and Neurotransmitters]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Look for: common factor → binomial pattern → quadratic → grouping.
- Cancel factors, never summands.
- Factoring out a variable is how you solve for it when it appears in several terms.
