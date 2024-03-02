import os
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
import rampwf as rw

problem_title = "Fire detection"
_event_label_names = [
    "No Fire",
    "Fire"
]

# Correspondence between categories and int8 categories
# Mapping int to categories
int_to_cat = {
    0: "No Fire",
    1: "Fire"
}
# Mapping categories to int
cat_to_int = {v: k for k, v in int_to_cat.items()}

_event_label_int = list(int_to_cat)
Predictions = rw.prediction_types.make_multiclass(label_names=_event_label_int)
workflow = rw.workflows.Classifier()


score_types = [
    rw.score_types.Accuracy(name='accuracy', precision=3),
    rw.score_types.ROCAUC(name='Roc_auc',precision=3)
]



def _get_data(path=".", split="train"):
    # Load data from npy and csv files.
    # Data: raw images .npy format
    # Labels: .csv file
    #
    # returns X (input) and y (output) arrays
    # X: array (n_samples, n_fetaures)
    # y: array of shape (n_samples,)

    # data
    path_ = 'data/'+'X_'+split+'.csv'
    data = pd.read_csv(path_)
    X = data.values

    path_ = 'data/'+'/Y_'+split+'.csv'
    # labels
    y_df = pd.read_csv(path_)
    y = y_df.values.ravel().astype(int)
    return X, y


def get_train_data(path="."):
    return _get_data(path, "train")


def get_test_data(path="."):
    return _get_data(path, "test_private")


def get_cv(X, y):
    cv = TimeSeriesSplit(n_splits=5)
    return cv.split(X)