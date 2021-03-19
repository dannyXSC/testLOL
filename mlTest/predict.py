from matplotlib.pyplot import axis
import numpy as np
from sigmoid import *


def predict(theta1, theta2, x):
    # Useful values
    m = x.shape[0]
    num_labels = theta2.shape[0]

    # You need to return the following variable correctly
    p = np.zeros(m)

    # ===================== Your Code Here =====================
    # Instructions : Complete the following code to make predictions using
    #                your learned neural network. You should set p to a
    #                1-D array containing labels between 1 to num_labels.
    #
    # mid=

    x = np.c_[np.ones(m), x]
    mid = sigmoid(np.dot(x, theta1.T))
    mid = np.c_[np.ones(m), mid]
    res = sigmoid(np.dot(mid, theta2.T))
    p = np.argmax(res, axis=1) + 1

    return p
