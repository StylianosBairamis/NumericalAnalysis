import numpy as np

def gauss_seidel(n):
    A = np.zeros((n, n), dtype='double')

    b = list(np.ones(n - 2, dtype='double'))

    b.append(3)
    b.insert(0, 3)

    for i in range(n):  # Αρχικοποίηση του πίνακα συντελεστών.
        for j in range(n):
            if i == j:
                A[i, i] = 5
                if i != n - 1:
                    A[i + 1, i] = -2
                    A[i, i + 1] = -2

    x = np.random.rand(n)
    x_old = x.copy()

    max_iter = 100

    counter = 0

    for k in range(max_iter):
        for i in range(n):
            if i != 0 and i != n - 1:
                sum = b[i]
                sum -= x[i - 1] * A[i, i - 1] + x[i + 1] * A[i, i + 1]
                x[i] = sum / A[i, i]
            elif i == 0:
                sum = b[i]
                sum -= x[i + 1] * A[i, i + 1]
                x[i] = sum / A[i, i]
            else:
                sum = b[i]
                sum -= x[i - 1] * A[i, i - 1]
                x[i] = sum / A[i, i]

        temp = x - x_old
        maxel = temp[0]

        for j in range(len(temp)):
            if abs(maxel) < abs(temp[j]):
                maxel = temp[j]

        if maxel < 0.5 * 10 ** -4:
            break

        x_old = x.copy()
        counter += 1

    print(x)