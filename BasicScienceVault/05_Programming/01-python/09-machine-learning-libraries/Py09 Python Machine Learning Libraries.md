---
aliases: [scikit-learn, sklearn, PyTorch, Pipeline, Cross-Validation in Python, Autograd, Training Loop]
tags: [programming, python, machine-learning, deep-learning, cross-validation, type/overview, neuro]
---
# Py09 Python Machine Learning Libraries

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py09 Python Machine Learning Libraries - Worksheet|✏️ Worksheet]] · [[Py09 Python Machine Learning Libraries - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
Decoding stimuli from brain activity, classifying cell types, predicting behaviour, fitting deep models of the visual system – this is done with **scikit-learn** (classical ML) and **PyTorch** (deep learning). The concepts are in [[CS07 Machine Learning Fundamentals]] and [[CS08 Deep Neural Networks]]; this note is how to write them correctly, above all **without leakage** ([[CS06 Data Science Workflow]]).

## scikit-learn: one API for everything
Every model ("estimator") has the same methods:
```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(C=1.0, max_iter=1000)   # hyperparameters in the constructor
clf.fit(X_train, y_train)                        # learn parameters
y_pred = clf.predict(X_test)                     # labels
p = clf.predict_proba(X_test)[:, 1]              # probabilities
clf.score(X_test, y_test)                        # default metric (accuracy)
clf.coef_                                        # learned parameters end with _
```
- `X` has shape **(n_samples, n_features)** – trials × (channels·times) or trials × voxels. Not features × samples!
- Transformers (`StandardScaler`, `PCA`) have `fit`, `transform` and `fit_transform`.

### Pipelines: preprocessing inside the CV loop
```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
pipe = make_pipeline(StandardScaler(), PCA(n_components=20), SVC(kernel="linear", C=1))
```
A pipeline is one estimator: in cross-validation, **every step is fitted on the training fold only** and applied to the test fold. Scaling, PCA or feature selection on all data before CV is leakage.

### Cross-validation
```python
from sklearn.model_selection import cross_val_score, StratifiedKFold, GroupKFold, LeaveOneGroupOut, GridSearchCV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(pipe, X, y, cv=cv, scoring="balanced_accuracy")
scores.mean(), scores.std()
# independent units: split by subject / run / session
scores = cross_val_score(pipe, X, y, groups=runs, cv=LeaveOneGroupOut())
# hyperparameters with nested CV
inner = GridSearchCV(pipe, {"svc__C": [0.01, 0.1, 1, 10]}, cv=3)
outer_scores = cross_val_score(inner, X, y, cv=cv)
```
- Parameter names in a pipeline: `stepname__param` (`svc__C`).
- **Grouped CV** whenever samples aren't independent (trials of the same run, cells of the same animal); **TimeSeriesSplit** for forward-in-time prediction.
- Chance level: permutation test with `sklearn.model_selection.permutation_test_score`.

### Metrics
```python
from sklearn.metrics import accuracy_score, balanced_accuracy_score, roc_auc_score, confusion_matrix, r2_score, f1_score
```
| Task | Metric |
|---|---|
| balanced classes | accuracy |
| imbalanced classes | balanced accuracy, ROC-AUC, F1 |
| decoder ranking quality | ROC-AUC (0.5 = chance) |
| regression (predicting RT, firing rate) | $R^2$ on held-out data, explained variance |
| errors by class | confusion matrix |

## PyTorch basics
### Tensors
```python
import torch
x = torch.tensor([[1., 2.], [3., 4.]])
x.shape, x.dtype                            # torch.Size([2, 2]), torch.float32
t = torch.from_numpy(np_array).float()      # NumPy → torch (float32!)
x @ x.T, x.mean(dim=0)                      # dim instead of axis
device = "cuda" if torch.cuda.is_available() else "cpu"
x = x.to(device)                            # move to GPU
x.detach().cpu().numpy()                    # back to NumPy
```
Tensors are NumPy-like arrays that can live on a **GPU** and record operations for **automatic differentiation** ([[CS14 Hardware Essentials]]).

### Autograd
```python
w = torch.tensor(2.0, requires_grad=True)
loss = (3 * w - 1) ** 2
loss.backward()          # computes d loss / d w by the chain rule (backpropagation)
w.grad                   # tensor(30.)  = 2·(3w − 1)·3 at w = 2
```
PyTorch builds a graph of operations during the forward pass and applies the **chain rule** backwards ([[B6 Differentiation Rules]], [[B11 Multivariable Calculus]], [[CS08 Deep Neural Networks]]).

### nn.Module
```python
import torch.nn as nn
class MLP(nn.Module):
    def __init__(self, n_in, n_hidden, n_out):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(n_in, n_hidden), nn.ReLU(), nn.Linear(n_hidden, n_out))
    def forward(self, x):
        return self.net(x)          # logits; CrossEntropyLoss applies softmax itself
model = MLP(64, 32, 2).to(device)
```
`nn.Module` is a class ([[Py12 Python Object-Oriented Programming]]) whose layers' parameters are registered automatically (`model.parameters()`).

## The training loop and evaluation
```python
from torch.utils.data import TensorDataset, DataLoader
train_dl = DataLoader(TensorDataset(X_tr, y_tr), batch_size=64, shuffle=True)
val_dl = DataLoader(TensorDataset(X_va, y_va), batch_size=256)
opt = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
loss_fn = nn.CrossEntropyLoss()
for epoch in range(50):
    model.train()
    for xb, yb in train_dl:
        xb, yb = xb.to(device), yb.to(device)
        opt.zero_grad()                 # 1. reset gradients (they accumulate!)
        loss = loss_fn(model(xb), yb)   # 2. forward pass + loss
        loss.backward()                 # 3. backpropagation
        opt.step()                      # 4. update parameters
    model.eval()                        # dropout/batch-norm in inference mode
    with torch.no_grad():               # no graph, saves memory
        acc = sum((model(xb.to(device)).argmax(1) == yb.to(device)).sum().item()
                  for xb, yb in val_dl) / len(y_va)
    print(f"epoch {epoch}: val acc {acc:.3f}")
```
- The four steps `zero_grad → forward/loss → backward → step` are always the same.
- **Train / validation / test:** pick the epoch and hyperparameters on validation data (early stopping), report the test set **once** ([[CS06 Data Science Workflow]]).
- **Reproducibility:** `torch.manual_seed(0)`; full GPU determinism needs extra flags (`torch.use_deterministic_algorithms(True)`).

## Same idea in R and MATLAB
R: `tidymodels`/`caret`, `glmnet`, `torch` for R ([[R07 R Statistical Modelling]]). MATLAB: `fitcsvm`, `fitclinear`, `crossval`, Deep Learning Toolbox. Most research deep learning is in Python.

## In neuroscience #neuro
- **MVPA decoding** of stimulus category from fMRI patterns or MEG sensor data: `make_pipeline(StandardScaler(), LogisticRegression())` + `LeaveOneGroupOut` over runs ([[CS12 Neuroimaging Data Analysis]]). MNE's `mne.decoding.SlidingEstimator` decodes at every time point.
- **Encoding models:** ridge regression (`RidgeCV`) from stimulus features (e.g. CNN activations) to voxel responses; evaluate with held-out $R^2$.
- **Spike-sorting and cell-type classifiers**, pose estimation (DeepLabCut) and calcium-imaging segmentation are PyTorch/TensorFlow models.
- **Deep networks as brain models:** compare network layers to neural responses with RSA ([[CS08 Deep Neural Networks]], [[CS12 Neuroimaging Data Analysis]]).

## Math links #math-link
- Linear models $\hat y = Xw + b$, matrix shapes → [[C1 Matrices]], [[CS01 Mathematical Foundations]]
- Gradients and the chain rule (autograd) → [[B6 Differentiation Rules]], [[B11 Multivariable Calculus]]
- Logistic/softmax, cross-entropy → [[B2 Exponential Functions]], [[CS03 Information Theory]]
- Gradient descent → [[CS04 Optimization]]

## Connections
- Concepts: [[CS07 Machine Learning Fundamentals]], [[CS08 Deep Neural Networks]], [[CS04 Optimization]]
- Validation and leakage → [[CS06 Data Science Workflow]]
- Classes (`nn.Module`) → [[Py12 Python Object-Oriented Programming]]
- Arrays → [[Py05 NumPy and Arrays]]; GPUs → [[CS14 Hardware Essentials]]

## Key takeaways
- scikit-learn: `fit` / `predict` / `transform`; `X` is samples × features.
- Put all preprocessing in a **Pipeline**; use grouped/nested CV; report balanced accuracy or AUC.
- PyTorch: tensors + autograd + `nn.Module`; loop = `zero_grad`, forward, `backward`, `step`.
- `model.eval()` and `torch.no_grad()` for evaluation; test set once.
