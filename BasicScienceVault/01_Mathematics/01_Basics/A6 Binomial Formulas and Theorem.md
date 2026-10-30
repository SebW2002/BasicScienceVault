---
aliases: [Binomial Formulas, Binomial Theorem, Binomische Formeln]
tags: [basics, binomial, algebra, type/overview, neuro]
---
# A6 Binomial Formulas and Binomial Theorem

> [[A0 Basics MOC|↑ Basics MOC]] · [[A6 Binomial Formulas and Theorem - Worksheet|✏️ Worksheet]] · [[A6 Binomial Formulas and Theorem - Solutions|✅ Solutions]] · [[Mistakes - Basics|⚠️ Mistake log]]

## Why this matters
The three binomial formulas are shortcuts you'll use for factoring, completing the square and rationalising roots. The binomial theorem generalises them to $(a+b)^n$ – and its coefficients are exactly the probabilities of the **binomial distribution**, the classic model of quantal transmitter release.

## The three binomial formulas
| # | Formula |
|---|---|
| 1 | $(a + b)^2 = a^2 + 2ab + b^2$ |
| 2 | $(a - b)^2 = a^2 - 2ab + b^2$ |
| 3 | $(a + b)(a - b) = a^2 - b^2$ |

> [!warning] The #1 algebra error
> $(a + b)^2 \neq a^2 + b^2$ – you forget the mixed term $2ab$. Check with $a = b = 1$: $4 \neq 2$.

**Uses**
- Mental arithmetic: $49^2 = (50 - 1)^2 = 2500 - 100 + 1 = 2401$; $\;19 \cdot 21 = 20^2 - 1 = 399$
- Factoring: $x^2 - 6x + 9 = (x - 3)^2$; $\;4y^2 - 25 = (2y-5)(2y+5)$
- **Completing the square:** $x^2 + 6x + 2 = (x + 3)^2 - 9 + 2 = (x+3)^2 - 7$ → vertex form of a parabola, derivation of the quadratic formula ([[A8 Solving Equations]]), and of Gaussians.

## The binomial theorem
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{\,n-k} b^{\,k}, \qquad \binom nk = \frac{n!}{k!\,(n-k)!}$$
(See [[A7 Sums Products and Factorials]] for $\Sigma$ and $!$.)

**Pascal's triangle** gives the coefficients – each entry is the sum of the two above:
```
n=0:          1
n=1:        1   1
n=2:      1   2   1
n=3:    1   3   3   1
n=4:  1   4   6   4   1
```
Example: $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$; $\;(x - 2)^3 = x^3 - 6x^2 + 12x - 8$ (signs alternate because $b = -2$).

**Interpretation:** $\binom nk$ = number of ways to choose $k$ of $n$ objects ("n choose k").

**Approximation for small $x$:** $(1 + x)^n \approx 1 + nx$ – the first two terms of the theorem (and of the Taylor series → [[B9 Taylor Series]]).

## In neuroscience #neuro
**Quantal release (del Castillo & Katz):** a synapse has $n$ release sites, each releasing a vesicle independently with probability $p$. The probability that exactly $k$ vesicles are released is
$$P(k) = \binom nk p^k (1-p)^{n-k}$$
These are exactly the terms of $(p + (1-p))^n = 1^n = 1$ – which proves that all probabilities sum to 1. Mean release $= np$, variance $= np(1-p)$; fitting these to EPSC amplitudes ("variance–mean analysis") estimates $n$ and $p$.

**Variance formula:** $\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - \mu^2$ follows from expanding with binomial formula 2.

**Gaussians:** completing the square in the exponent is how products of Gaussian likelihoods (e.g. cue combination in Bayesian perception) are simplified.

## Connections
- Factoring patterns → [[A4 Factoring and Simplifying]]
- Rationalising roots via formula 3 → [[A2 Root Rules]]
- $\Sigma$, factorial → [[A7 Sums Products and Factorials]]
- Quadratic formula via completing the square → [[A8 Solving Equations]]
- $(1+x)^n \approx 1 + nx$ → [[B9 Taylor Series]]

## Where this is used in the vault
**Most important applications:** Quantal transmitter release $\binom nk p^k(1-p)^{n-k}$ ([[Bio06 Synapses and Neurotransmitters]], [[CS02 Probability and Statistics]]); counting microstates for entropy ([[Ph08 Thermodynamics and Statistics]]).

**All notes that build on this topic:**
- *Physics:* [[Ph08 Thermodynamics and Statistics]]
- *Biology:* [[Bio02 Membranes and Transport]] · [[Bio06 Synapses and Neurotransmitters]]
- *Computer Science:* [[CS02 Probability and Statistics]]
- *Programming:* [[MAT07 MATLAB Statistics Toolbox]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Never forget the mixed term $2ab$.
- Pascal's triangle / $\binom nk$ give the coefficients of $(a+b)^n$.
- Binomial theorem = binomial distribution = quantal release.
