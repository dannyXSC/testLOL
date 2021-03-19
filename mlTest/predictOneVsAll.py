import numpy as np


def predict_one_vs_all(all_theta, X):
    m = X.shape[0]
    num_labels = all_theta.shape[0]

    # You need to return the following variable correctly;
    p = np.zeros(m)

    # Add ones to the X data matrix
    X = np.c_[np.ones(m), X]

    # ===================== Your Code Here =====================
    # Instructions : Complete the following code to make predictions using
    #                your learned logistic regression parameters (one vs all).
    #                You should set p to a vector of predictions (from 1 to
    #                num_labels)
    #
    # Hint : This code can be done all vectorized using the max function
    #        In particular, the max function can also return the index of the
    #        max element, for more information see 'np.argmax' function.
    #
    tRes = np.dot(X, all_theta.T)
    tRes = np.roll(tRes, -1, axis=1)
    tRes = np.hstack((np.zeros((m, 1)), tRes))
    p = np.argmax(tRes, axis=1)

    return p
