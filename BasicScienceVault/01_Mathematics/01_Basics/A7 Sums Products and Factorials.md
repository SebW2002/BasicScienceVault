---
aliases: [Sums and Products, Sigma Notation, Factorial, Summenzeichen]
tags: [basics, summation, factorial, type/overview, neuro]
---
# A7 Sums, Products and Factorials

> [[A0 Basics MOC|↑ Basics MOC]] · [[A7 Sums Products and Factorials - Worksheet|✏️ Worksheet]] · [[A7 Sums Products and Factorials - Solutions|✅ Solutions]] · [[Mistakes - Basics|⚠️ Mistake log]]

## Why this matters
Every mean, variance, weighted input, likelihood and matrix product is written with $\Sigma$ or $\Pi$. Reading this notation fluently is essential for methods sections and computational neuroscience papers.

## Sum notation $\Sigma$
$$\sum_{i=1}^{n} a_i = a_1 + a_2 + \dots + a_n$$
$i$ = index (name doesn't matter), $1$ = lower bound, $n$ = upper bound.

| Rule | Formula |
|---|---|
| Constant | $\sum_{i=1}^{n} c = n \cdot c$ |
| Factor out constants | $\sum c\, a_i = c \sum a_i$ |
| Split sums | $\sum (a_i + b_i) = \sum a_i + \sum b_i$ |
| Index shift | $\sum_{i=1}^{n} a_i = \sum_{j=0}^{n-1} a_{j+1}$ |
| Gauss sum | $\sum_{i=1}^{n} i = \dfrac{n(n+1)}{2}$ |
| Sum of squares | $\sum_{i=1}^{n} i^2 = \dfrac{n(n+1)(2n+1)}{6}$ |
| Geometric sum ($q \neq 1$) | $\sum_{k=0}^{n} q^k = \dfrac{1 - q^{n+1}}{1 - q}$; for $\lvert q\rvert < 1$: $\sum_{k=0}^{\infty} q^k = \dfrac{1}{1-q}$ |

> [!warning] Not allowed
> $\sum a_i b_i \neq \left(\sum a_i\right)\left(\sum b_i\right)$ · $\;\sum a_i^2 \neq \left(\sum a_i\right)^2$

## Product notation $\Pi$
$$\prod_{i=1}^{n} a_i = a_1 \cdot a_2 \cdots a_n, \qquad \ln \prod_{i=1}^n a_i = \sum_{i=1}^n \ln a_i$$
The log turns products into sums ([[A3 Logarithms]]) – that's why we maximise **log**-likelihoods.

## Factorial
$$n! = \prod_{k=1}^{n} k = 1 \cdot 2 \cdots n, \qquad 0! = 1, \qquad n! = n \cdot (n-1)!$$
Simplify quotients by cancelling: $\dfrac{7!}{5!} = 7 \cdot 6 = 42$. Factorials grow faster than any exponential – $10! = 3\,628\,800$.
Used in $\binom nk$ ([[A6 Binomial Formulas and Theorem]]) and Taylor series ([[B9 Taylor Series]]).

## In neuroscience #neuro
- **Descriptive statistics:** mean $\bar x = \frac1n \sum x_i$, variance $s^2 = \frac{1}{n-1}\sum (x_i - \bar x)^2$.
- **Model neuron / perceptron:** the input is a weighted sum $u = \sum_{i=1}^{N} w_i x_i + b$; the neuron fires if $u$ exceeds a threshold. This is also a dot product ([[D2 Dot and Cross Product]]).
- **Poisson spike counts:** if a neuron fires at rate $\lambda$ spikes per window,
  $$P(k \text{ spikes}) = \frac{\lambda^k e^{-\lambda}}{k!}$$
- **Likelihood of independent trials:** $L = \prod_i P(k_i)$, log-likelihood $\ln L = \sum_i \ln P(k_i)$.
- **Matrix product** entries are sums: $(AB)_{ij} = \sum_k A_{ik}B_{kj}$ ([[C1 Matrices]]).
- **Synaptic depression / facilitation** with constant factor per spike leads to geometric sums.

## Connections
- $\binom nk$ and binomial theorem → [[A6 Binomial Formulas and Theorem]]
- Log of a product → [[A3 Logarithms]]
- Integral = limit of sums → [[B7 Antiderivatives and Integration]]
- Infinite sums → [[B9 Taylor Series]]
- Weighted sum = dot product → [[D2 Dot and Cross Product]], [[C1 Matrices]]

## Where this is used in the vault
**Most important applications:** Poisson spike counts, likelihoods as products ([[CS02 Probability and Statistics]]), entropy sums ([[CS03 Information Theory]]), discrete convolution ([[CS11 Time Series and Signal Processing]]), discounted returns in RL ([[CS10 Dynamical and Computational Neuro Models]]).

**All notes that build on this topic:**
- *Physics:* [[Ph04 Circuits and Resistance]] · [[Ph07 Diffusion and Transport]] · [[Ph08 Thermodynamics and Statistics]] · [[Ph09 Waves and Oscillations]] · [[Ph12 Quantum Basics for Biophysics]]
- *Chemistry:* [[Ch08 Biomolecules]]
- *Biology:* [[Bio01 Cell Biology]] · [[Bio03 Proteins and Enzymes]] · [[Bio04 Nucleic Acids and Gene Expression]] · [[Bio05 Neurons and Action Potentials]] · [[Bio06 Synapses and Neurotransmitters]]
- *Methods:* [[Meth04 In Vivo Imaging]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS02 Probability and Statistics]] · [[CS03 Information Theory]] · [[CS04 Optimization]] · [[CS06 Data Science Workflow]] · [[CS10 Dynamical and Computational Neuro Models]] · [[CS11 Time Series and Signal Processing]]
- *Programming:* [[Prog00 Shared Programming Concepts]] · [[Py05 NumPy and Arrays]] · [[Py06 pandas and Tabular Data]] · [[Py11 PsychoPy Experiment Control]] · [[R02 R Data Structures and Vectorization]] · [[R05 dplyr and tidyr]] · [[MAT07 MATLAB Statistics Toolbox]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Write out the first 2–3 terms when a sum looks confusing.
- Constants factor out, sums split – but products of sums don't.
- $0! = 1$; cancel factorials before multiplying.
