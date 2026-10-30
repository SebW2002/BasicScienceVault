---
tags: [computer-science, information-theory, type/worksheet]
---
# CS03 Information Theory – Worksheet

> Theory: [[CS03 Information Theory]] · Solutions: [[CS03 Information Theory - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮. Use log base 2 unless stated. $\ln2\approx0.69$.

## Level 1 – Entropy
1. Compute the entropy of a) a fair coin, b) a fair 8-sided die, c) a certain event.
2. Compute the entropy of $p = (\tfrac12, \tfrac14, \tfrac18, \tfrac18)$.
3. A neuron is shown one of 16 equally likely images. What is the stimulus entropy? What is the maximum information any response can carry about the stimulus?
4. Which distribution over 4 outcomes has maximum entropy? Minimum entropy?

## Level 2 – Mutual information
5. Two stimuli ($s_1$, $s_2$, each $p = \tfrac12$). Response: for $s_1$ always $r_1$; for $s_2$ either $r_2$ or $r_3$ with equal probability. Compute $H(R)$, $H(R\mid S)$ and $I(S;R)$.
6. What is $I(S;R)$ if the response distribution is the same for every stimulus?
7. Two variables have correlation $\rho = 0$. Can their mutual information be positive? Give an example.
8. A downstream neuron receives input only from neuron A. Can it carry more stimulus information than A? Which principle applies?

## Level 3 – KL and cross-entropy
9. Compute $D_{KL}(P\|Q)$ for $P = (\tfrac12, \tfrac12, 0, 0)$ and $Q = (\tfrac14, \tfrac14, \tfrac14, \tfrac14)$. Now compute $D_{KL}(Q\|P)$. What do you notice?
10. A classifier outputs $q = (0.25, 0.5, 0.25)$ and the true class is the second one. Compute the cross-entropy loss in bits and in nats. What if the output were $q = (0.7, 0.1, 0.2)$? (Use $\log_2 10\approx3.32$.)
11. Show that minimising cross-entropy $H(P, Q)$ over $Q$ is the same as minimising $D_{KL}(P\|Q)$.

## Level 4 – Neural coding
12. You compute information in spike trains with bin sizes of 100 ms, 10 ms and 1 ms and get 0.3, 0.9 and 1.4 bits. What does this suggest about the code?
13. With only 10 trials per stimulus, you find 0.5 bits of mutual information. Why could this be misleading, and how could you check it?
14. Explain the efficient coding hypothesis and give one prediction that has been confirmed.
15. 🧮 Compute the binary entropy $H_b(0.1)$ (a neuron that spikes in 10 % of bins).
