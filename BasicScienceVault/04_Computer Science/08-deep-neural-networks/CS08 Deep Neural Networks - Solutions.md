---
tags: [computer-science, deep-learning, type/solution]
---
# CS08 Deep Neural Networks – Solutions

> Worksheet: [[CS08 Deep Neural Networks - Worksheet]] · Theory: [[CS08 Deep Neural Networks]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. $784\cdot100 + 100 = 78{,}500$ and $100\cdot10 + 10 = 1{,}010$, total **79,510**.
2. $W\mathbf x = (1 - 2,\ 2 + 0) = (-1, 2)$; $+\mathbf b = (-1, -1)$; ReLU gives $(0, 0)$. Both units are inactive for this input.
3. $e^0 = 1$, $e^0 = 1$, $e^{\ln2} = 2$, so softmax $= (\tfrac14, \tfrac14, \tfrac12)$. Adding 5 multiplies every term by $e^5$, which cancels: the probabilities are **unchanged**.
4. A composition of linear maps is linear: $W_3W_2W_1\mathbf x = W'\mathbf x$. The network can still only represent linear functions.

## Level 2
5. $z = 0$, so $y = 0.5$ and $L = \tfrac12(0.5 - 1)^2 = 0.125$. $\frac{\partial L}{\partial w} = (y - t)\,\sigma'(z)\,x = (-0.5)\cdot0.25\cdot2 = -0.25$. Update: $w = 0 - 1\cdot(-0.25) = 0.25$, which moves the output towards the target.
6. $\sigma'\le0.25$ per layer (times the weights), so up to about $0.25^{10}\approx10^{-6}$. Remedies: ReLU activations, residual connections, careful initialisation, batch/layer normalisation.
7. For $z < 0$ the gradient is 0, so the weights feeding that unit get no updates. If a unit is negative for **all** inputs, it never recovers ("dead"). Leaky ReLU and GELU have non-zero slopes for $z < 0$.

## Level 3
8. Output 26 × 26 × 16. Parameters: $3\cdot3\cdot1\cdot16 + 16 = 160$. Fully connected: $784\cdot10{,}816 + 10{,}816\approx8.5$ million, about 50,000 times more.
9. **Weight sharing** (the same kernel at every position) and **local connectivity** (each output looks only at a small patch). Images have local structure, and the same feature can appear anywhere.
10. The gradient contains roughly $\lambda^{100}$: $0.9^{100}\approx2.7\times10^{-5}$ (**vanishing**) and $1.1^{100}\approx1.4\times10^4$ (**exploding**). Fixes: LSTM/GRU gating, gradient clipping, orthogonal initialisation.
11. Scores (0, 0) give weights (0.5, 0.5) and output $(0.5, 0.5)$. Scores $(0, \ln3)$ give weights $(\tfrac14, \tfrac34)$ and output $(0.25, 0.75)$.

## Level 4
12. (1) **Reconstruction** term $\mathbb E_q[\log p(\mathbf x\mid\mathbf z)]$: the decoder must reproduce the data from the latent code. (2) **KL** term $D_{KL}(q(\mathbf z\mid\mathbf x)\|p(\mathbf z))$: keeps the encoded distributions close to the prior (e.g. a standard normal), which makes the latent space smooth, regular and usable for sampling.
13. During training, each unit is randomly switched off with probability $p$, so the network can't rely on specific co-adapted units and must learn redundant, robust features. It approximates averaging over an ensemble of thinned networks. At test time all units are used (with rescaled activations).
14. Any two: (1) Predictive accuracy of one response measure is **compatible with many mechanisms**; different architectures can predict similarly well. (2) CNNs lack features of the brain (spikes, recurrent and feedback connections, Dale's law, learning rules, development). (3) CNNs differ in behaviour: susceptibility to adversarial examples, texture bias, different errors from humans. (4) They are trained with backprop on labelled images, unlike the brain's learning.
15. $T = 1$: $e^2 = 7.39$, $e^1 = 2.72$, $e^0 = 1$, sum 11.11, so $(0.665, 0.245, 0.090)$. $T = 0.5$: logits $(4, 2, 0)$, $e^4 = 54.6$, $e^2 = 7.39$, $1$, sum 63.0, so $(0.867, 0.117, 0.016)$. Lowering $T$ makes the distribution **sharper** (more confident, closer to argmax); raising $T$ flattens it.
