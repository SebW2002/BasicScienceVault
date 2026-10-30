---
aliases: [Machine Learning Fundamentals, Regression, Logistic Regression, SVM, Random Forest, k-means, ROC AUC, Maschinelles Lernen]
tags: [computer-science, machine-learning, classification, clustering, type/overview, neuro]
---
# CS07 Machine Learning Fundamentals

> [[MOC-computer-science|↑ CS MOC]] · [[CS07 Machine Learning Fundamentals - Worksheet|✏️ Worksheet]] · [[CS07 Machine Learning Fundamentals - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Machine learning (ML) is now part of almost every neuroscience pipeline:
- decoding stimuli and choices from activity
- classifying cell types
- sorting spikes
- segmenting images
- predicting diagnoses

Most of the time, simple models (linear and logistic regression, random forests, k-means) are the right first choice. You need to understand what they assume, how to evaluate them, and when they fail.

## Supervised vs. unsupervised learning
| | **Supervised** | **Unsupervised** |
|---|---|---|
| Data | inputs $\mathbf x$ **with** targets $y$ | inputs only |
| Goal | predict $y$ for new $\mathbf x$ | find structure |
| Tasks | **regression** ($y$ continuous), **classification** ($y$ categorical) | **clustering**, **dimensionality reduction**, density estimation |
| Neuro examples | predict reaching direction from M1 activity; classify the stimulus from fMRI patterns | group neurons into cell types; find low-dimensional population dynamics |

Also: **semi-supervised**, **self-supervised** (predict parts of the data from other parts, the basis of foundation models) and **reinforcement learning** ([[CS10 Dynamical and Computational Neuro Models]]).

## Linear regression and logistic regression
**Linear regression:** $\hat y = \mathbf w^T\mathbf x + b$; minimise the MSE.
- **Closed form (OLS):** $\hat{\mathbf w} = (X^TX)^{-1}X^T\mathbf y$ (the normal equations; [[C3 Linear Systems and Gaussian Elimination]]).
- In 1D: slope $= \frac{\sum(x_i - \bar x)(y_i - \bar y)}{\sum(x_i - \bar x)^2} = \frac{\text{Cov}(x, y)}{\text{Var}(x)}$; intercept $= \bar y - \text{slope}\cdot\bar x$.
- $R^2 = 1 - \frac{SS_\text{res}}{SS_\text{tot}}$: fraction of variance explained (evaluate it on held-out data).
- **Assumptions:** linearity, independent errors with constant variance. Probabilistically, OLS is the MLE under Gaussian noise.
- **Extensions:** ridge/lasso ([[CS04 Optimization]]); polynomial or basis-function features; GLMs ([[CS09 Probabilistic and Bayesian Models]]). This is the same model as the fMRI GLM ([[CS12 Neuroimaging Data Analysis]]).

**Logistic regression** (binary classification):
$$P(y = 1\mid\mathbf x) = \sigma(\mathbf w^T\mathbf x + b) = \frac{1}{1 + e^{-(\mathbf w^T\mathbf x + b)}}$$
- The **log-odds** are linear: $\log\frac{p}{1-p} = \mathbf w^T\mathbf x + b$. The decision boundary ($p = 0.5$) is the hyperplane $\mathbf w^T\mathbf x + b = 0$ ([[D3 Lines and Planes]]).
- Loss: binary cross-entropy (convex, so a unique optimum; [[CS03 Information Theory]]).
- Multiclass: **softmax regression**, $P(y = k\mid\mathbf x) = \frac{e^{\mathbf w_k^T\mathbf x}}{\sum_je^{\mathbf w_j^T\mathbf x}}$.
- Workhorse for **neural decoding**: interpretable weights, probability outputs, fast.

## Support vector machines and kernel methods (conceptual)
- **Linear SVM:** finds the separating hyperplane with the **maximum margin** (the largest distance to the nearest training points, the **support vectors**). Soft margin: hinge loss $\max(0, 1 - y_i(\mathbf w^T\mathbf x_i + b))$ + L2 penalty; $C$ controls the trade-off between margin width and training errors.
- **Kernel trick:** replace the dot products $\mathbf x_i^T\mathbf x_j$ with a **kernel** $k(\mathbf x_i,\mathbf x_j)$, which corresponds to an implicit (possibly infinite-dimensional) feature map. A linear separation in feature space is a **nonlinear** boundary in input space.
  - **RBF kernel** $k(\mathbf x,\mathbf x') = e^{-\gamma\lVert\mathbf x - \mathbf x'\rVert^2}$: similarity decays with distance.
  - Polynomial kernels.
- Kernels also underlie Gaussian processes ([[CS09 Probabilistic and Bayesian Models]]).
- **Neuro:** linear SVMs were long the default for fMRI MVPA ([[CS12 Neuroimaging Data Analysis]]).

## Decision trees, random forests, gradient boosting
- **Decision tree:** recursively splits the data with simple rules ("firing rate > 10 Hz?") chosen to make the child nodes as **pure** as possible.
  - **Gini impurity** $G = 1 - \sum_kp_k^2$, or entropy $-\sum p_k\log p_k$.
  - Interpretable, handles mixed feature types and nonlinearities, but deep trees overfit badly (high variance).
- **Random forest:** many deep trees, each trained on a **bootstrap sample** (bagging) with a **random subset of features** at each split. Averaging their votes reduces variance strongly. Robust, little tuning; **feature importances** (interpret with care: correlated features share importance).
- **Gradient boosting** (XGBoost, LightGBM): trees are added **sequentially**, each one fitting the residual errors (negative gradients of the loss) of the current ensemble, with a small learning rate. Often the best performer on tabular data.
- **Neuro:** cell-type classification from electrophysiological and morphological features; predicting clinical outcomes from tabular data.

## Clustering: k-means, hierarchical, Gaussian mixture models
| Method | Idea | Pros / cons |
|---|---|---|
| **k-means** | minimise within-cluster squared distances $\sum_k\sum_{i\in k}\lVert\mathbf x_i - \boldsymbol\mu_k\rVert^2$. Lloyd's algorithm alternates (1) assign each point to the nearest centroid, (2) recompute each centroid as the mean | fast. Needs $k$; assumes roughly spherical, equal-sized clusters; depends on initialisation (use k-means++ and multiple restarts) |
| **Hierarchical** (agglomerative) | start with each point as a cluster and repeatedly merge the closest pair. **Linkage**: single (nearest points), complete (farthest), average, **Ward** (smallest variance increase) | produces a **dendrogram**; cut at any level; no $k$ needed upfront; $O(n^2)$ memory |
| **Gaussian mixture model (GMM)** | data come from $K$ Gaussians with means, covariances and weights; fitted with **EM** (E-step: soft assignment probabilities; M-step: update the parameters) | **soft** (probabilistic) assignments; elliptical clusters; choose $K$ via BIC; k-means is a limiting case |
| Density-based (DBSCAN, HDBSCAN) | clusters = dense regions; points in sparse regions are noise | arbitrary shapes; no $k$; used in spike sorting |

**Choosing $k$:** elbow plot, silhouette score, BIC (for GMMs), stability across subsamples, and above all **biological validation**. Clustering always returns clusters, even in structureless data.

## Evaluation metrics
**Confusion matrix** (binary):
| | predicted + | predicted − |
|---|---|---|
| actual + | TP | FN |
| actual − | FP | TN |

| Metric | Formula | Question it answers |
|---|---|---|
| Accuracy | $\frac{TP + TN}{\text{all}}$ | fraction correct; **misleading with class imbalance** |
| Balanced accuracy | mean of per-class recalls | robust to imbalance |
| **Precision** (PPV) | $\frac{TP}{TP + FP}$ | of the predicted positives, how many are real? |
| **Recall** (sensitivity, TPR) | $\frac{TP}{TP + FN}$ | of the real positives, how many were found? |
| Specificity (TNR) | $\frac{TN}{TN + FP}$ | of the real negatives, how many were correctly rejected? |
| **F1** | $2\cdot\frac{\text{precision}\cdot\text{recall}}{\text{precision} + \text{recall}}$ | harmonic mean of precision and recall |
| **ROC curve / AUC** | TPR vs. FPR for all thresholds; AUC = area | threshold-independent separability; AUC = P(random positive scored higher than random negative); 0.5 = chance, 1 = perfect |
| PR curve / AP | precision vs. recall | better than ROC for rare positives |
| **Calibration** | reliability diagram: predicted probability vs. observed frequency | does "70 % confidence" mean right 70 % of the time? Essential for clinical use |

Regression metrics: MSE/RMSE, MAE, $R^2$ (out of sample).

## Generalisation, overfitting, underfitting
- **Generalisation** = performance on **new** data from the same distribution. Training performance alone means nothing.
- **Overfitting:** the model learns noise (low training error, high test error). **Underfitting:** too simple (both errors high). See bias–variance in [[CS04 Optimization]].
- **Remedies:** more data, regularisation, simpler models, feature selection, ensembling, early stopping, data augmentation.
- **Learning curves** (performance vs. training set size) show whether more data would help.
- **Distribution shift:** models trained on one scanner, lab, species or session can fail on another, so test across sites and sessions.

## In neuroscience #neuro
- **Decoding:**
  - linear decoders of population activity (what information is linearly readable?)
  - **brain–computer interfaces** (velocity decoding from motor cortex)
  - classification of mental states from fMRI and EEG
- **Encoding models:** predict neural responses from stimulus features (linearised encoding models of fMRI voxels).
- **Unsupervised:** cell types from scRNA-seq (clustering after PCA, [[Meth06 Omics and Sequencing]]); spike sorting (clustering of waveform features, [[CS11 Time Series and Signal Processing]]); behavioural "syllables" from video.
- **Caution:** decoding a variable from a brain area shows the information is **present**, not that the brain **uses** it.

## Math links #math-link
- Normal equations, matrix inverse → [[C1 Matrices]], [[C3 Linear Systems and Gaussian Elimination]]
- Sigmoid, logit (log-odds) → [[B1 Properties of Functions]], [[A3 Logarithms]]
- Hyperplanes and margins → [[D3 Lines and Planes]]
- Distances for clustering → [[CS01 Mathematical Foundations]]
- Covariance in 1D regression → [[CS02 Probability and Statistics]]

## Connections
- In code → [[Py09 Python Machine Learning Libraries]] (scikit-learn), [[R07 R Statistical Modelling]] (GLMs)
- Losses and regularisation → [[CS04 Optimization]]
- Workflow, CV, leakage → [[CS06 Data Science Workflow]]
- Deep networks → [[CS08 Deep Neural Networks]]
- GLMs and GMMs probabilistically → [[CS09 Probabilistic and Bayesian Models]]
- MVPA → [[CS12 Neuroimaging Data Analysis]]

## Key takeaways
- Supervised (regression, classification) vs. unsupervised (clustering, dimensionality reduction).
- OLS: $\hat{\mathbf w} = (X^TX)^{-1}X^T\mathbf y$. Logistic: $\sigma(\mathbf w^T\mathbf x + b)$, log-odds linear, convex cross-entropy.
- SVM: maximum margin, kernels for nonlinear boundaries. Trees → forests (bagging) → boosting (sequential residuals).
- k-means (hard, spherical), hierarchical (dendrogram), GMM (soft, elliptical, EM).
- Accuracy can mislead. Use precision, recall, F1, ROC-AUC and calibration, always on held-out data.
