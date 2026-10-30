---
tags: [computer-science, optimization, type/solution]
---
# CS04 Optimization – Solutions

> Worksheet: [[CS04 Optimization - Worksheet]] · Theory: [[CS04 Optimization]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. Errors: 1, 0, −2. MSE $= \frac{1 + 0 + 4}{3} = \frac53\approx1.67$; MAE $= \frac{1 + 0 + 2}{3} = 1$.
2. $J' = 2(w - 3)$. $w_1 = 0 - 0.1\cdot2(-3) = 0.6$; $w_2 = 0.6 - 0.1\cdot2(-2.4) = 0.6 + 0.48 = 1.08$.
3. $w_{t+1} - 3 = (1 - 2\eta)(w_t - 3)$. With η = 0.1 the factor is 0.8 (shrinks by 20 % per step). With η = 1.1 it is −1.2: the error flips sign and grows, so it **diverges**. Convergence needs $\lvert1 - 2\eta\rvert < 1$, i.e. $0 < \eta < 1$.
4. Batch GD uses all data per step: exact gradient, smooth convergence, but expensive per step. SGD uses a mini-batch: cheap, many updates per epoch, and the noise can help escape saddles; the cost is noisy convergence.

## Level 2
5. Convex: $x^2$, $\lvert x\rvert$, $e^x$, $-\ln x$. Not convex: $x^3$ (concave for $x < 0$), $\sin x$.
6. The negative log-likelihood of logistic regression is **convex** in the weights, so every local minimum is global (unless the data are perfectly separable, where weights grow without bound; regularisation fixes this).
7. $H = \begin{pmatrix}2&0\\0&-2\end{pmatrix}$: eigenvalues of opposite sign, so a **saddle point**.

## Level 3
8. $\frac{dJ}{dw} = -2\sum x_i(y_i - wx_i) + 2\lambda w = 0\Rightarrow\hat w = \frac{\sum x_iy_i}{\sum x_i^2 + \lambda}$. Here $\sum xy = 2 + 8 = 10$ and $\sum x^2 = 5$. With λ = 0: $\hat w = 2$. With λ = 5: $\hat w = 10/10 = 1$ (shrunk towards 0).
9. The L1 penalty has a **constant** slope (±λ) even close to 0, so it keeps pushing small weights all the way to zero. Geometrically, the L1 constraint region has corners on the axes, where the loss contours touch first. The L2 penalty's slope $2\lambda w$ vanishes near 0, so weights get small but rarely exactly zero.
10. Model 1: low training error, large gap, so **high variance (overfitting)**. Fix with more regularisation, a simpler model, more data, data augmentation or early stopping. Model 2: both errors high, small gap, so **high bias (underfitting)**. Fix with a more flexible model, better features or less regularisation.
11. Gaussian prior gives L2 (ridge). Laplace prior gives L1 (lasso).

## Level 4
12. $\mathcal L = xy - \mu(x + y - 10)$: $y = \mu$, $x = \mu$, $x + y = 10$, so $x = y = 5$ and $f_\text{max} = 25$.
13. $\frac{\partial L}{\partial w} = -(t - wx)x$, so gradient descent gives $\Delta w = -\eta\frac{\partial L}{\partial w} = \eta(t - wx)x$ ✓.
14. The loss landscape has many equally good minima (or flat valleys): the parameters are **not identifiable** from these data. Different parameter combinations compensate each other (degeneracy, e.g. several channel densities producing the same firing pattern, Prinz et al. 2004). Interpret individual parameter values cautiously; report parameter ranges or posterior distributions; constrain with additional data.
15. $v_1 = 1$, $v_2 = 1.9$, $v_3 = 2.71$; $v_\infty = \frac{g}{1 - \beta} = 10$. With a consistent gradient, momentum multiplies the effective step size by up to $\frac{1}{1-\beta} = 10$.
