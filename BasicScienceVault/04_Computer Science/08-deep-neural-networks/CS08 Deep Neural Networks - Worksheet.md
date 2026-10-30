---
tags: [computer-science, deep-learning, type/worksheet]
---
# CS08 Deep Neural Networks – Worksheet

> Theory: [[CS08 Deep Neural Networks]] · Solutions: [[CS08 Deep Neural Networks - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮. $\ln2\approx0.69$.

## Level 1 – MLPs and activations
1. Count the parameters of an MLP with layer sizes 784 → 100 → 10 (weights + biases).
2. Forward pass: $\mathbf x = (1, 2)$, $W = \begin{pmatrix}1&-1\\2&0\end{pmatrix}$, $\mathbf b = (0, -3)$, ReLU. Compute $\mathbf h$.
3. Compute softmax of the logits $(0, 0, \ln2)$. What happens if you add 5 to every logit?
4. Why does an MLP without nonlinear activation functions not gain anything from extra layers?

## Level 2 – Backpropagation
5. A single neuron: $z = wx$, $y = \sigma(z)$, $L = \tfrac12(y - t)^2$. With $w = 0$, $x = 2$, $t = 1$: compute $y$, $L$, $\partial L/\partial w$, and one gradient-descent step with $\eta = 1$.
6. A network has 10 sigmoid layers. Estimate the maximum factor by which the gradient can shrink from output to input. Name two remedies.
7. Why is the derivative of ReLU at $z < 0$ a potential problem ("dying ReLU")?

## Level 3 – CNNs, RNNs, attention
8. A 28 × 28 greyscale image goes through a conv layer with 16 kernels of size 3 × 3 (stride 1, no padding). Output shape? Number of parameters? Compare with a fully connected layer from 784 inputs to $26\cdot26\cdot16$ outputs.
9. Why do CNNs need far fewer parameters than fully connected networks for images?
10. In a simple RNN, the hidden state is multiplied by $W$ at each step. What happens to gradients over 100 steps if the largest eigenvalue of $W$ has magnitude 0.9? 1.1?
11. Attention with one query and two keys: the scaled scores are $(0, 0)$, with values $\mathbf v_1 = (1, 0)$ and $\mathbf v_2 = (0, 1)$. Compute the output. What if the scores were $(0, \ln3)$?

## Level 4 – Latents, regularisation, neuro
12. What two terms make up the VAE objective, and what does each do?
13. Explain dropout and why it acts as a regulariser.
14. A CNN predicts IT neuron responses well. Name two reasons why this does not mean the CNN "works like" the visual cortex.
15. 🧮 Softmax with temperature: $p_k = \frac{e^{z_k/T}}{\sum_je^{z_j/T}}$. For logits $(2, 1, 0)$, compute the probabilities for $T = 1$ and $T = 0.5$. What does lowering $T$ do?
