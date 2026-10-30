---
aliases: [Information Theory, Entropy, Mutual Information, KL Divergence, Cross-Entropy, Neural Coding]
tags: [computer-science, information-theory, entropy, neural-coding, type/overview, neuro]
---
# CS03 Information Theory

> [[MOC-computer-science|↑ CS MOC]] · [[CS03 Information Theory - Worksheet|✏️ Worksheet]] · [[CS03 Information Theory - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
How much does a spike train tell you about a stimulus? Is information carried by the spike count or by precise timing? Information theory (Shannon, 1948) gives exact, model-free answers in **bits**. The same quantities (entropy, KL divergence, cross-entropy) are also the loss functions of machine learning and the core of variational inference and the free-energy principle.

## Entropy
$$H(X) = -\sum_xp(x)\log_2p(x)\qquad[\text{bits}]$$
- It measures **uncertainty**, i.e. the average **surprise** $-\log_2p(x)$ of outcomes (with natural log, the unit is **nats**; 1 nat ≈ 1.44 bits).
- $H\ge0$; $H = 0$ for a certain outcome. $H$ is maximal for a **uniform** distribution: $H = \log_2N$ for $N$ outcomes. A fair coin has 1 bit; 8 equally likely stimuli have 3 bits.
- **Binary entropy:** $H_b(p) = -p\log_2p - (1-p)\log_2(1-p)$, maximal (1 bit) at $p = 0.5$.
- **Joint entropy** $H(X, Y)$; **conditional entropy** $H(Y\mid X) = \sum_xp(x)H(Y\mid X = x)$ (remaining uncertainty about $Y$ once $X$ is known). Chain rule: $H(X, Y) = H(X) + H(Y\mid X)$.
- **Continuous variables:** differential entropy $h(X) = -\int p\log p$; a Gaussian has $h = \frac12\log_2(2\pi e\sigma^2)$ (it can be negative, and only differences are meaningful).
- **Link to physics:** Boltzmann's entropy $S = k\ln W$ is the same concept. For $W$ equally likely microstates, Shannon gives $\log_2W$ bits ([[Ph08 Thermodynamics and Statistics]]).

## Mutual information
$$I(X;Y) = H(Y) - H(Y\mid X) = H(X) - H(X\mid Y) = \sum_{x,y}p(x,y)\log_2\frac{p(x,y)}{p(x)p(y)}$$
- It measures how much knowing one variable **reduces uncertainty** about the other.
- **Symmetric**; $I\ge0$; $I = 0$ **if and only if** $X$ and $Y$ are independent. It captures **any** dependency, not only linear ones (unlike correlation).
- Bounded by $I(X;Y)\le\min(H(X), H(Y))$. A neuron can't convey more about the stimulus than the stimulus entropy.
- **Data processing inequality:** processing can't create information. For a chain $S\to R_1\to R_2$, $I(S;R_2)\le I(S;R_1)$.
- **Neural coding:** $I(S;R)$ between stimulus $S$ and response $R$ quantifies how much a neuron "tells" about the stimulus. **Information rate** (bits/s) and **information per spike** compare codes.

## Kullback–Leibler divergence
$$D_{KL}(P\,\|\,Q) = \sum_xp(x)\log\frac{p(x)}{q(x)}$$
- It measures how different an approximating distribution $Q$ is from the true distribution $P$: the extra bits needed if you code data from $P$ with a code optimised for $Q$.
- $D_{KL}\ge0$ (Gibbs' inequality), $= 0$ only if $P = Q$.
- **Not symmetric**: $D_{KL}(P\|Q)\neq D_{KL}(Q\|P)$, so it is not a distance. It is infinite if $Q$ assigns zero probability where $P$ has mass.
- Mutual information **is** a KL divergence: $I(X;Y) = D_{KL}(p(x, y)\,\|\,p(x)p(y))$.
- **Variational methods:** approximate an intractable posterior $p(z\mid x)$ with a simpler $q(z)$ by minimising $D_{KL}(q\|p)$, which is equivalent to maximising the **evidence lower bound (ELBO)** ([[CS09 Probabilistic and Bayesian Models]], VAEs in [[CS08 Deep Neural Networks]]).
- **Free-energy principle** (Friston): brains minimise "variational free energy", an upper bound on surprise built from exactly this KL term. It is an ambitious and debated unifying theory linked to predictive coding.

## Cross-entropy and classification loss
$$H(P, Q) = -\sum_xp(x)\log q(x) = H(P) + D_{KL}(P\,\|\,Q)$$
- For classification, $P$ is the true label (one-hot) and $Q$ is the model's predicted probabilities (softmax output). The loss for one sample is simply $-\log q(\text{correct class})$.
- Minimising cross-entropy = minimising KL to the true labels = **maximising likelihood** of a categorical model ([[CS02 Probability and Statistics]]).
- Binary version (logistic regression): $L = -[t\log\hat p + (1 - t)\log(1 - \hat p)]$.
- Confident wrong predictions are punished heavily: $-\log(0.01)\approx4.6$ nats, compared with $-\log(0.5)\approx0.69$ nats.

## Information-theoretic analysis of neural codes
| Code | Information carried by | Example | How to test |
|---|---|---|---|
| **Rate code** | spike counts in a window (tens–hundreds of ms) | motor cortex, many sensory neurons | compute $I(S; N)$ from counts |
| **Temporal code** | precise spike timing, latency, patterns, phase relative to oscillations | auditory brainstem (µs), first-spike latency in touch/retina, hippocampal **phase precession** | compare $I(S;\text{word})$ for fine vs. coarse time bins: if information grows with finer bins, timing matters |
| Population code | joint activity of many neurons | direction in motor cortex, place-cell ensembles | decoding, MI of populations (noise correlations!) |

**Practical issues:**
- **Limited-sampling bias:** plug-in estimates of entropy and MI from few trials are **biased upwards** (spurious information). Use bias corrections (Panzeri–Treves, shuffling) or decoding-based lower bounds.
- MI needs many trials per stimulus, and joint distributions of many neurons quickly become impossible to estimate (the curse of dimensionality).

**Efficient coding hypothesis** (Barlow, 1961): sensory systems maximise the information they transmit under constraints such as limited spikes, energy and noise. Its predictions include decorrelated (whitened) codes in the retina, sparse codes in V1 (Olshausen & Field 1996), and contrast responses matched to natural statistics (Laughlin 1981, histogram equalisation in the fly eye).

## In neuroscience #neuro
- A neuron firing up to 100 Hz with 1 ms resolution has a maximum entropy rate of several hundred bits/s, but the measured information about stimuli is typically **~1–3 bits per spike** and often lower.
- MI between neurons or brain areas (and transfer entropy for directed influence) is used for functional connectivity.
- **Surprise and prediction error:** $-\log p(x)$ appears in models of novelty responses, mismatch negativity and dopamine.

## Math links #math-link
- Logarithms in different bases, change of base → [[A3 Logarithms]]
- Sums over distributions → [[A7 Sums Products and Factorials]]
- Concavity of entropy, maximum at the uniform distribution (by Lagrange multipliers) → [[CS04 Optimization]], [[B8 Curve Sketching]]
- Bits per stimulus: $\log_2N$ → [[B3 Logarithmic Functions]]

## Connections
- In code → [[Py05 NumPy and Arrays]] (histograms, probabilities), [[Py08 SciPy Scientific Computing]] (`scipy.stats.entropy`)
- Distributions and Bayes → [[CS02 Probability and Statistics]]
- Entropy in physics → [[Ph08 Thermodynamics and Statistics]]
- Cross-entropy loss → [[CS07 Machine Learning Fundamentals]], [[CS08 Deep Neural Networks]]
- Variational inference → [[CS09 Probabilistic and Bayesian Models]]
- Spike timing, phase → [[Ph09 Waves and Oscillations]], [[CS11 Time Series and Signal Processing]]

## Key takeaways
- $H = -\sum p\log_2p$ is uncertainty in bits, maximal at uniform ($\log_2N$).
- $I(X;Y) = H(Y) - H(Y\mid X)$ is the uncertainty reduction. It is 0 iff independent and captures nonlinear dependencies.
- $D_{KL}(P\|Q)\ge0$ and is asymmetric; minimising it is the basis of variational inference.
- Cross-entropy $= H(P) + D_{KL}(P\|Q)$; the classification loss is $-\log q(\text{correct})$.
- Rate vs. temporal codes are distinguished by how information depends on time resolution. Beware sampling bias.
