---
tags: [programming, python, machine-learning, type/solution]
---
# Py09 Python Machine Learning Libraries – Solutions

> Worksheet: [[Py09 Python Machine Learning Libraries - Worksheet]] · Theory: [[Py09 Python Machine Learning Libraries]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. Estimators: `fit`, `predict` (classifiers also `predict_proba`, `score`); transformers: `fit`, `transform`, `fit_transform`. A trailing underscore marks attributes **learned** during `fit`.
2. `(300, 1600)`: samples × features, 32 · 50 = 1600.
3. `opt.zero_grad()` → forward pass and loss → `loss.backward()` → `opt.step()`.
4. `model.eval()` switches layers like dropout and batch-norm to inference behaviour; `torch.no_grad()` stops recording the computation graph (faster, less memory). They're independent – use both for evaluation.

## Level 2
5. **Yes**: the scaler saw the test folds (means and SDs). Fix: `cross_val_score(make_pipeline(StandardScaler(), SVC()), X, y, cv=5)`.
6. Trials from the same run share slow drifts and noise, and in fMRI neighbouring trials overlap in the BOLD response, so test trials are not independent of training trials → inflated accuracy. Use `LeaveOneGroupOut()` with `groups=run`.
7. `best_score_` is the best of several CV scores on the same data → optimistically biased. Use nested CV (`cross_val_score(GridSearchCV(...), X, y, cv=outer)`) or an untouched test set.
8. No – always predicting "no-go" gives 90 %. Report balanced accuracy (here it would be 50 %) or ROC-AUC, plus the confusion matrix.

## Level 3
9. $dL/dw = 2(2w - 4)\cdot2 = 4(2w - 4)$; at $w = 3$: $4\cdot2 = 8$. `w.grad` = `tensor(8.)`.
10. Gradients **accumulate** across iterations (PyTorch adds to `.grad`), so each step uses the sum of all past gradients → wrong, growing updates.
11. ```python
    pipe = make_pipeline(StandardScaler(), PCA(n_components=10), LogisticRegression(max_iter=1000))
    scores = cross_val_score(pipe, X, y, groups=runs, cv=LeaveOneGroupOut(), scoring="balanced_accuracy")
    print(scores.mean())
    ```

## Level 4
12. `LeaveOneGroupOut()` (or `GroupKFold`) with `groups=subject`. Within-subject CV measures how well it generalises to new trials of **known** subjects – usually much higher.
13. Correlation or $R^2$ between predicted and measured responses on **held-out** data (stimuli not used for fitting, ideally a separate run), often divided by a noise ceiling.
14. ```python
    import numpy as np
    from sklearn.datasets import make_classification
    from sklearn.feature_selection import SelectKBest
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score
    from sklearn.pipeline import make_pipeline
    rng = np.random.default_rng(0)
    X, y = make_classification(n_samples=200, n_features=50, n_informative=5, random_state=0)
    y_rand = rng.permutation(y)
    X_sel = SelectKBest(k=5).fit_transform(X, y_rand)                     # leaky
    leaky = cross_val_score(LogisticRegression(), X_sel, y_rand, cv=5).mean()
    clean = cross_val_score(make_pipeline(SelectKBest(k=5), LogisticRegression()), X, y_rand, cv=5).mean()
    print(leaky, clean)
    ```
    With random labels the true accuracy is 50 %. With seed 0 the leaky version gives ≈ 0.59, the correct pipeline ≈ 0.46 (chance level ± noise). The leaky version picked the features that happen to correlate with the random labels in *all* data, test folds included. The bias grows with more features and fewer samples – try `n_features=5000`, which is typical for voxels.
