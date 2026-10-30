---
tags: [computer-science, machine-learning, type/worksheet]
---
# CS07 Machine Learning Fundamentals – Worksheet

> Theory: [[CS07 Machine Learning Fundamentals]] · Solutions: [[CS07 Machine Learning Fundamentals - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮. $\sigma(0) = 0.5$, $\sigma(2)\approx0.88$, $\sigma(-2)\approx0.12$.

## Level 1 – Task types
1. Supervised or unsupervised? Regression, classification, clustering or dimensionality reduction? a) predict reaction time from EEG power, b) group 500 neurons by waveform shape, c) decide from fMRI whether a face or a house was shown, d) find the main axes of variation in population activity.
2. Fit a line by OLS to the points (1, 2), (2, 3), (3, 5). Compute slope and intercept.
3. A logistic regression has $w = 2$, $b = -4$. Compute $P(y = 1)$ for $x = 1$, 2 and 3. Where is the decision boundary?

## Level 2 – Trees and clustering
4. A node contains 8 samples of class A and 2 of class B. Compute the Gini impurity. What would a pure node have?
5. Why does a random forest generalise better than a single deep decision tree?
6. One iteration of k-means in 1D: data 1, 2, 3, 10, 11, 12; initial centroids $\mu_1 = 1$, $\mu_2 = 3.5$. Assign the points and update the centroids. Do one more iteration.
7. What is the key difference between k-means and a Gaussian mixture model?

## Level 3 – Metrics
8. A seizure detector: TP = 40, FN = 10, FP = 20, TN = 930. Compute accuracy, precision, recall, specificity and F1.
9. A dataset has 95 % class A. A model always predicts A. What are its accuracy and balanced accuracy? What does that teach you?
10. What does an AUC of 0.5 mean? An AUC of 0.9? Can a model with AUC 0.9 be badly calibrated?

## Level 4 – Neuro transfer
11. A decoder trained on day 1 achieves 90 % accuracy on day 1 test trials but 60 % on day 2. Name two possible reasons and one remedy.
12. You decode the animal's running speed from V1 activity with high accuracy. Can you conclude that V1 computes running speed?
13. Explain the kernel trick in two sentences. Why is an RBF-SVM sometimes worse than a linear one on fMRI data with 50,000 voxels and 100 trials?
14. 🧮 Compute the ROC-AUC from these scores. Positives: 0.9, 0.8, 0.4; negatives: 0.7, 0.3, 0.2. (Use: AUC = fraction of positive–negative pairs in which the positive has the higher score.)
