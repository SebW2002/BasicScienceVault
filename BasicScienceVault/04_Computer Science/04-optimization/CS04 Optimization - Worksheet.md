---
tags: [computer-science, optimization, type/worksheet]
---
# CS04 Optimization – Worksheet

> Theory: [[CS04 Optimization]] · Solutions: [[CS04 Optimization - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮.

## Level 1 – Losses and gradient descent
1. Predictions $\hat y = (2, 4, 5)$, targets $y = (1, 4, 7)$. Compute the MSE and MAE.
2. Perform two gradient-descent steps on $J(w) = (w - 3)^2$ from $w_0 = 0$ with $\eta = 0.1$.
3. For the same $J$, by what factor does the distance to the optimum shrink per step with $\eta = 0.1$? What happens with $\eta = 1.1$? Find the range of $\eta$ that converges.
4. What is the difference between batch gradient descent and stochastic gradient descent? One advantage of each?

## Level 2 – Convexity
5. Which functions are convex: $x^2$, $x^3$, $\lvert x\rvert$, $e^x$, $\sin x$, $-\ln x$ (for $x > 0$)?
6. Why can't gradient descent get stuck in a bad local minimum when fitting a logistic regression?
7. $f(x, y) = x^2 - y^2$ has $\nabla f = 0$ at the origin. Compute the Hessian and classify the point.

## Level 3 – Regularisation
8. 1D ridge regression without intercept: minimise $\sum_i(y_i - wx_i)^2 + \lambda w^2$. Derive $\hat w$. Compute it for $x = (1, 2)$, $y = (2, 4)$ with $\lambda = 0$ and $\lambda = 5$.
9. Why does L1 regularisation produce exactly zero weights, while L2 only shrinks them?
10. A model has training error 2 % and test error 25 %. Another has training error 20 % and test error 21 %. Diagnose each (bias/variance) and suggest a fix.
11. Which corresponds to a Gaussian prior on weights, and which to a Laplace prior?

## Level 4 – Constraints & neuro transfer
12. Use a Lagrange multiplier to maximise $f(x, y) = xy$ subject to $x + y = 10$.
13. Show that the delta rule $\Delta w = \eta(t - wx)x$ is gradient descent on $L = \tfrac12(t - wx)^2$.
14. A fitted biophysical neuron model gives very different parameters depending on the starting values, but each fit reproduces the data equally well. What does this tell you about the optimisation problem and about parameter interpretation?
15. 🧮 Momentum: with $\beta = 0.9$ and a constant gradient $g = 1$, the velocity follows $v_t = \beta v_{t-1} + g$ with $v_0 = 0$. Compute $v_1, v_2, v_3$ and the limit $v_\infty$. What is the effective step size multiplier?
