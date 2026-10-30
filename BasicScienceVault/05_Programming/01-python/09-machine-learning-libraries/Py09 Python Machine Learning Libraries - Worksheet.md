---
tags: [programming, python, machine-learning, type/worksheet]
---
# Py09 Python Machine Learning Libraries – Worksheet

> Theory: [[Py09 Python Machine Learning Libraries]] · Solutions: [[Py09 Python Machine Learning Libraries - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Recall
1. Which methods do scikit-learn estimators and transformers have? What does a trailing underscore (`coef_`) mean?
2. EEG epochs: 300 trials, 32 channels, 50 time points, flattened for a classifier. What shape must `X` have?
3. Name the four steps inside a PyTorch training iteration in order.
4. What do `model.eval()` and `torch.no_grad()` each do?

## Level 2 – Leakage detective
5. Is there leakage? Fix it if so.
   ```python
   X = StandardScaler().fit_transform(X)
   scores = cross_val_score(SVC(), X, y, cv=5)
   ```
6. fMRI data with 8 runs, 20 trials per run. Why is `KFold(5, shuffle=True)` over trials a bad choice? What do you use?
7. You choose `C` with `GridSearchCV(cv=5)` and report `grid.best_score_` as decoding accuracy. What's the problem?
8. 90 % of trials are "no-go". A decoder reaches 90 % accuracy. Is it good? Which metric would you report?

## Level 3 – Autograd and code
9. $L(w) = (2w - 4)^2$. Compute $dL/dw$ at $w = 3$ by hand. What does `w.grad` contain after `L.backward()`?
10. What happens if you forget `opt.zero_grad()`?
11. Write a scikit-learn pipeline: standardise → PCA with 10 components → logistic regression; evaluate with leave-one-run-out CV and balanced accuracy.

## Level 4 – Neuro transfer
12. You want to know whether a decoder trained on subjects 1–19 works on a new subject. Which CV splitter? What would within-subject CV measure instead?
13. An encoding model predicts voxel responses from CNN features with ridge regression. Which metric, and computed on which data?
14. 💻 Generate a toy dataset (`sklearn.datasets.make_classification`, 200 samples, 50 features, 5 informative), and compare 5-fold CV accuracy with a leaky pipeline (feature selection `SelectKBest(k=5)` on all data first) versus a correct pipeline – using **random labels** (`rng.permutation(y)`). What do you observe?
