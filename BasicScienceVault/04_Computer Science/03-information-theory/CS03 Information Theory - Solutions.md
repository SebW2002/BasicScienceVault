---
tags: [computer-science, information-theory, type/solution]
---
# CS03 Information Theory – Solutions

> Worksheet: [[CS03 Information Theory - Worksheet]] · Theory: [[CS03 Information Theory]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. a) 1 bit b) $\log_28 = 3$ bits c) 0 bits
2. $\tfrac12\cdot1 + \tfrac14\cdot2 + \tfrac18\cdot3 + \tfrac18\cdot3 = 0.5 + 0.5 + 0.375 + 0.375 = 1.75$ bits
3. $\log_216 = 4$ bits; at most 4 bits ($I\le H(S)$).
4. Maximum: uniform $(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$ with 2 bits. Minimum: a deterministic distribution (one outcome with probability 1) with 0 bits.

## Level 2
5. $P(r_1) = \tfrac12$, $P(r_2) = P(r_3) = \tfrac14$, so $H(R) = 1.5$ bits. $H(R\mid S) = \tfrac12\cdot0 + \tfrac12\cdot1 = 0.5$ bits. $I = 1.5 - 0.5 = 1$ bit, the full stimulus entropy, because the response always tells you which stimulus it was.
6. $I = 0$: $R$ is independent of $S$.
7. Yes. Example: $X$ uniform on $\{-1, 0, 1\}$ and $Y = X^2$. The correlation is 0 (symmetric), but $Y$ is completely determined by $X$, so $I(X;Y) = H(Y) > 0$ (≈ 0.92 bits).
8. No: **data processing inequality**. $I(S;R_\text{downstream})\le I(S;R_A)$. (It can, however, make the information more **accessible**, e.g. linearly decodable.)

## Level 3
9. $D_{KL}(P\|Q) = 2\cdot\tfrac12\log_2\frac{1/2}{1/4} = 1$ bit. $D_{KL}(Q\|P)$ contains terms $\tfrac14\log\frac{1/4}{0} = \infty$, so it is **infinite**. KL is asymmetric, and it blows up when the second distribution assigns zero probability to an outcome the first one allows.
10. $-\log_20.5 = 1$ bit ($= \ln2\approx0.69$ nats). For $q = (0.7, 0.1, 0.2)$: $-\log_20.1 = \log_210\approx3.32$ bits (≈ 2.3 nats). Confident wrong answers are penalised heavily.
11. $H(P, Q) = H(P) + D_{KL}(P\|Q)$. $H(P)$ doesn't depend on $Q$, so the $Q$ that minimises $H(P, Q)$ is the same one that minimises $D_{KL}(P\|Q)$.

## Level 4
12. Information **increases with finer time resolution**, so precise spike timing carries stimulus information beyond counts: a (partly) **temporal code**. (Check that this isn't sampling bias, which also grows with finer bins and more possible "words".)
13. With few trials, the estimated response distributions are noisy, which **overestimates** MI (limited-sampling bias), possibly entirely. Checks: shuffle stimulus labels and recompute (the shuffled MI estimates the bias); apply bias corrections; collect more trials; use decoding accuracy as a conservative lower bound.
14. Neural codes are adapted to the statistics of natural stimuli to transmit as much information as possible with limited resources (spikes, energy, neurons, noise). Confirmed predictions: retinal **centre-surround** receptive fields that decorrelate (whiten) natural images; **sparse, Gabor-like** V1 receptive fields that emerge from sparse coding of natural images; the contrast–response curve of fly interneurons that matches the cumulative distribution of natural contrasts (Laughlin 1981).
15. $H_b(0.1) = -0.1\log_20.1 - 0.9\log_20.9 = 0.1\cdot3.322 + 0.9\cdot0.152\approx0.332 + 0.137 = 0.469$ bits per bin.
