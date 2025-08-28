import math
import numpy as np


def learn(x, y):
    return x.T.dot(y)


def learn_op(x, y):
    return np.sum([np.outer(x, y) for x, y in zip(x, y)], axis=0)


def recall(w, x, d='out'):
    end_of_recall = False; \
            y_pred = None;
    x_eval = y_pred

    while end_of_recall == False:
        y_pred = activate(w.T.dot(x) \
                              if d == 'out' else w.dot(x))

        x_eval = activate(w.dot(y_pred) \
                              if d == 'out' else w.T.dot(y_pred))

        x, end_of_recall = x_eval, np.all(np.equal(x, x_eval))

    return y_pred


def bipolar_th(x):
    return 1 if x >= 0 else -1


def activate(x):
    return np.vectorize(bipolar_th)(x)


patterns = 20;
neurons = 8000;
mm_cells = 5500

X = np.array([1 if x > 0.5 else -1 for x in np.random.rand(patterns * neurons)], dtype=np.int8)

Y = np.array(-X[:patterns * mm_cells], dtype=np.int8)

X = np.reshape(X, (patterns, neurons))
Y = np.reshape(Y, (patterns, mm_cells))

W = learn_op(X, Y)  # W - the correlation weights matrix (i.e., the BAM's memory storage space)

print("Recalling the associations (Y) for the input patterns (X):\n")

for x, y in zip(X, Y):
    y_pred = recall(W, x, 'out')  # y_pred - the predicted pattern Y
    # Check if the target and predicted patterns (Y) are identical, and display the results
    print("x =", x, "target =", y, "y =", -y_pred, " :", np.any(-y_pred != y))

print("\r\nRecalling the associations (X) for the output patterns (Y):\n")

for x, y in zip(X, Y):
    x_pred = recall(W, y, d='in')  # x_pred - the predicted pattern X

    print("y =", y, "target =", x, "x =", -x_pred, " :", np.any(-x_pred != x))