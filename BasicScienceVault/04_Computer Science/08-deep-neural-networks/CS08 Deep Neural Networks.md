---
aliases: [Deep Neural Networks, Deep Learning, Backpropagation, CNN, RNN, LSTM, Transformer, Attention, Autoencoder, VAE]
tags: [computer-science, deep-learning, backpropagation, cnn, transformer, type/overview, neuro]
---
# CS08 Deep Neural Networks

> [[MOC-computer-science|↑ CS MOC]] · [[CS08 Deep Neural Networks - Worksheet|✏️ Worksheet]] · [[CS08 Deep Neural Networks - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Deep learning has changed neuroscience in two ways. It is a **tool**: cell segmentation, pose tracking, spike sorting, decoding. It is also a **model**: networks trained on tasks develop representations that resemble those in the brain. Under the hood, every deep network is just linear algebra ([[CS01 Mathematical Foundations]]), nonlinearities, a loss ([[CS03 Information Theory]]), and gradient descent with the chain rule ([[CS04 Optimization]]).

## Perceptron and multilayer perceptron
- **Perceptron** (Rosenblatt 1958): $y = \text{step}(\mathbf w^T\mathbf x + b)$, a linear threshold unit (McCulloch–Pitts neuron). It can only separate classes with a hyperplane, so it can't learn XOR.
- **Multilayer perceptron (MLP):** layers of units, each computing
  $$\mathbf h^{(l)} = \sigma\!\left(W^{(l)}\mathbf h^{(l-1)} + \mathbf b^{(l)}\right),\qquad\mathbf h^{(0)} = \mathbf x$$
  The **nonlinearity** σ is essential; without it, the whole network collapses into one linear map.
- **Universal approximation:** one hidden layer with enough units can approximate any continuous function. Depth makes this far more efficient (hierarchical features).
- **Parameter count** of a layer $n_\text{in}\to n_\text{out}$: $n_\text{in}n_\text{out} + n_\text{out}$.

## Activation functions
| Function | Formula | Derivative | Notes |
|---|---|---|---|
| **Sigmoid** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | $\sigma(1 - \sigma)\le0.25$ | output (0, 1); saturates, causing **vanishing gradients** in deep nets |
| **tanh** | $\tanh z$ | $1 - \tanh^2z$ | output (−1, 1), zero-centred; also saturates |
| **ReLU** | $\max(0, z)$ | 0 for $z < 0$, 1 for $z > 0$ | default in hidden layers; cheap; no saturation for $z > 0$; units can "die" |
| Leaky ReLU / GELU | small slope for $z < 0$ / smooth ReLU | – | GELU is used in transformers |
| **Softmax** (output) | $\text{softmax}(\mathbf z)_k = \frac{e^{z_k}}{\sum_je^{z_j}}$ | – | turns scores (logits) into class probabilities; invariant to adding a constant to all $z_k$ |

The ReLU is a rough analogue of a neuron's f–I curve (rectification above threshold, [[Bio05 Neurons and Action Potentials]]).

## Backpropagation as an application of the chain rule
1. **Forward pass:** compute the activations layer by layer and the loss $L$.
2. **Backward pass:** compute $\boldsymbol\delta^{(l)} = \frac{\partial L}{\partial\mathbf z^{(l)}}$ from the output back to the input using the chain rule:
   $$\boldsymbol\delta^{(l)} = \left(W^{(l+1)T}\boldsymbol\delta^{(l+1)}\right)\odot\sigma'(\mathbf z^{(l)}),\qquad\frac{\partial L}{\partial W^{(l)}} = \boldsymbol\delta^{(l)}\,\mathbf h^{(l-1)T}$$
3. **Update** all weights by gradient descent (SGD/Adam).

- Backprop computes **all** gradients at about the cost of two forward passes (reverse-mode automatic differentiation). Frameworks (PyTorch, JAX) do it automatically.
- **Vanishing/exploding gradients:** the gradient is a product of many Jacobians. With sigmoid derivatives ≤ 0.25, after 10 layers the factor is $\le0.25^{10}\approx10^{-6}$. Remedies: ReLU, careful initialisation, residual connections ($\mathbf h + f(\mathbf h)$), normalisation layers.
- For one sigmoid neuron with squared loss: $\frac{\partial L}{\partial w} = (y - t)\,\sigma'(z)\,x$ ([[CS01 Mathematical Foundations]]).

## Convolutional neural networks (CNNs)
- **Convolution layers:** small learned **kernels** (e.g. 3×3) slide across the image. **Weight sharing** (the same kernel everywhere) gives **translation equivariance** and far fewer parameters than fully connected layers.
- **Output size:** $\frac{n - k + 2p}{s} + 1$ (input $n$, kernel $k$, padding $p$, stride $s$). Parameters per layer: $k\cdot k\cdot C_\text{in}\cdot C_\text{out} + C_\text{out}$.
- **Pooling** (max/average) downsamples. Deeper layers have larger **receptive fields** and respond to more complex features (edges → textures → parts → objects).
- **Neuro as model:** CNNs trained on object recognition predict responses in the **ventral visual stream** (V4, IT) better than hand-crafted models (Yamins & DiCarlo). Early layers resemble Gabor-like V1 receptive fields. Hubel & Wiesel's simple and complex cells inspired the design.
- **Neuro as tool:**
  - cell and nucleus segmentation (U-Net, **Cellpose**, StarDist)
  - **pose estimation** (DeepLabCut, SLEAP)
  - EM connectome segmentation
  - denoising (DeepInterpolation)

## Recurrent neural networks (RNNs, LSTMs)
- **RNN:** a hidden state carries memory over time,
  $$\mathbf h_t = \tanh(W\mathbf h_{t-1} + U\mathbf x_t + \mathbf b),\qquad\mathbf y_t = V\mathbf h_t$$
  It is trained with **backpropagation through time** (BPTT). Long sequences make gradients vanish or explode (products of $W$ over many steps, governed by its eigenvalues; [[C4 Eigenvalues and Eigenvectors]]).
- **LSTM / GRU:** gated cells (input, forget, output gates) with a memory cell that can keep information over long times.
- **Neuro:**
  - RNNs trained on cognitive tasks reproduce the population dynamics of prefrontal and motor cortex, and can then be reverse-engineered (fixed points, line attractors; Mante, Sussillo et al. 2013)
  - models of working memory and timing ([[CS10 Dynamical and Computational Neuro Models]])
  - decoding speech from cortical activity in BCIs

## Transformers and attention
$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
- Each token (input element) is projected into a **query** $\mathbf q = W_Q\mathbf x$, a **key** $\mathbf k = W_K\mathbf x$ and a **value** $\mathbf v = W_V\mathbf x$.
- Query–key dot products measure relevance (similarity, [[D2 Dot and Cross Product]]). Softmax turns them into weights. The output is a **weighted average of the values**.
- **Scaling** by $\sqrt{d_k}$ keeps the dot products from growing with dimension (otherwise softmax saturates).
- **Multi-head attention** runs several attention mechanisms in parallel. **Positional encodings** add order information, because attention itself is permutation-invariant.
- **Self-attention** relates every element to every other: global context, but **quadratic cost** in sequence length.
- The basis of large language models, vision transformers and **foundation models for neural data** (pretrained on many sessions and animals, then adapted to new recordings).
- Neuro analogies (attention as gain modulation, transformers and hippocampal memory) are suggestive but loose.

## Autoencoders and variational autoencoders
- **Autoencoder:** encoder $\mathbf z = f(\mathbf x)$ into a low-dimensional **latent** code (bottleneck), decoder $\hat{\mathbf x} = g(\mathbf z)$; minimise reconstruction error. A linear autoencoder with MSE learns the PCA subspace; nonlinear ones learn curved manifolds.
- **Variational autoencoder (VAE):** the encoder outputs a **distribution** $q(\mathbf z\mid\mathbf x)$ (mean and variance). Training maximises the **ELBO**:
  $$\text{ELBO} = \mathbb E_q[\log p(\mathbf x\mid\mathbf z)] - D_{KL}\big(q(\mathbf z\mid\mathbf x)\,\|\,p(\mathbf z)\big)$$
  This is reconstruction minus a KL penalty keeping latents close to a prior ([[CS03 Information Theory]], [[CS09 Probabilistic and Bayesian Models]]). The **reparameterisation trick** $\mathbf z = \boldsymbol\mu + \boldsymbol\sigma\odot\boldsymbol\epsilon$ makes sampling differentiable. Latent spaces are smooth, and new samples can be generated.
- **Neuro:** **LFADS** (sequential VAE with RNNs) infers single-trial latent dynamics from population spikes; behavioural embeddings from video; CEBRA (contrastive) joint neural–behavioural latent spaces.

## Regularisation in deep learning
| Method | How | Why it helps |
|---|---|---|
| **Dropout** | randomly zero a fraction $p$ of units during training | prevents co-adaptation; like an ensemble of subnetworks |
| **Batch normalisation** | normalise layer inputs to zero mean, unit variance per mini-batch (+ learned scale and shift) | stabilises and speeds up training; mild regularisation |
| **Weight decay** | L2 penalty on weights ([[CS04 Optimization]]) | smaller weights, smoother functions |
| Data augmentation | rotations, flips, noise, crops | invariances; effectively more data |
| Early stopping | stop when the validation loss rises | limits effective complexity |

## Interpretability
- **Saliency maps:** gradient of the output with respect to the input, $\frac{\partial y}{\partial\mathbf x}$: which pixels or time points matter locally. They are noisy and can be misleading.
- **Feature attribution:** integrated gradients, SHAP, occlusion analysis.
- **Probing:** train simple (linear) classifiers on hidden layers to see what information is linearly available there, which is the same logic as neural decoding.
- **In-silico neurophysiology:** "record" artificial units, find preferred stimuli (feature visualisation), lesion units, which uses neuroscience methods on networks.
- **Caveat:** explanations are hypotheses about the model, not about the brain. Validate them causally.

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Matrix products, Jacobians, chain rule → [[CS01 Mathematical Foundations]], [[B6 Differentiation Rules]]
- Sigmoid derivative $\sigma(1 - \sigma)$ → [[B6 Differentiation Rules - Solutions]] (task 16)
- Convolution → [[CS11 Time Series and Signal Processing]], [[B7 Antiderivatives and Integration]]
- Exponentials in softmax, powers in vanishing gradients → [[B2 Exponential Functions]], [[A1 Exponent Rules]]
- Eigenvalues of recurrent weights and stability → [[C4 Eigenvalues and Eigenvectors]]
- KL and ELBO → [[CS03 Information Theory]]

## Connections
- In code → [[Py09 Python Machine Learning Libraries]] (PyTorch: tensors, autograd, training loop)
- Optimisation (SGD, Adam) → [[CS04 Optimization]]
- ML basics and evaluation → [[CS07 Machine Learning Fundamentals]]
- Biological networks and where the analogy breaks → [[CS10 Dynamical and Computational Neuro Models]]
- Segmentation and microscopy → [[Meth01 Microscopy]]
- GPUs → [[CS14 Hardware Essentials]]

## Key takeaways
- MLP: $\mathbf h = \sigma(W\mathbf x + \mathbf b)$ stacked; nonlinearity is essential; softmax for class probabilities.
- Backprop = chain rule from output to input; beware vanishing gradients (sigmoid ≤ 0.25 per layer).
- CNNs: shared kernels, receptive fields, a good model of the ventral stream. RNNs/LSTMs: recurrent state over time.
- Attention: softmax($QK^T/\sqrt{d_k}$)$V$, a learned weighted average.
- Autoencoders learn latent codes; VAEs maximise the ELBO (reconstruction − KL).
- Regularise (dropout, batch norm, weight decay, augmentation, early stopping); treat interpretability methods with caution.
