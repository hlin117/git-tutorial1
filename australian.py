#!/usr/bin/env python
#title          :australian.py
#description    :A classification task to show how to improve SVMs
#author         :Henry Lin
#version        :0.0.1
#python_version :2.7.6
#================================================================================

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv("data/australian.data", header=None, sep=" ")
X = dataset.drop(14, axis=1)        # Features
y = dataset[14]                     # Labels

# Produces a "one hot encoding" of the data
conv_X = pd.get_dummies(X, columns=[0, 3, 4, 5, 7, 8, 10, 11])

X_train, X_test, y_train, y_test = train_test_split(conv_X, y, test_size=0.25,
                                                    random_state=888)

reg = LogisticRegression()
reg.fit(X_train, y_train)
predictions = reg.predict(X_test)
print "Accuracy score for logreg: ", accuracy_score(y_test, predictions)

svm = SVC()
svm.fit(X_train, y_train)
predictions = svm.predict(X_test)
print "Accuracy score for svm: ", accuracy_score(y_test, predictions)
