import numpy as np


def cholesky(n):
    A = np.array([[1, 1, 2], [1, 3, 0], [2, 0, 7]])

    L = np.zeros(A.shape)

    for i in range(A.shape[0]):
        L[i, i] = np.sqrt(A[i, i])
        u = A[i, i + 1:n] / L[i, i]
        L[i, i + 1:n] = u
        b = np.matrix(u).T
        temp = b * u
        A[i + 1:n, i + 1:n] = A[i + 1:n, i + 1:n] - temp[0:temp.shape[0], 0:temp.shape[0]]

    print("L matrix is: ")
    print(L.T)
