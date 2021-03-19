import numpy as np
from numpy.core.fromnumeric import argmax
from sigmoid import *


def lr_cost_function(theta, X, y, lmd):
    m = y.size

    # You need to return the following values correctly
    cost = 0
    grad = np.zeros(theta.shape)

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta
    #                You should set cost and grad correctly.
    #

    h = sigmoid(np.dot(X, theta))

    reg_theta = theta[1:]
    cost = np.sum(-y * np.log(h) - (1 - y) * np.log(1 - h),
                  axis=0) / m + lmd / (2 * m) * np.sum(reg_theta * reg_theta)

    grad = np.dot(X.T, h - y) / m
    grad[1:] += lmd * reg_theta / m

    # =========================================================

    return cost, grad
