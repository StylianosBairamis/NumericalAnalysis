from functions import fun, first_derivative, second_derivative
import random


def bisection():
    a = 0.9
    b = 1.5
    i = 0
    approx = []

    while True:
        m = random.uniform(a, b)
        approx.append(m)
        if fun(a) * fun(m) < 0:
            b = m
        elif fun(b) * fun(m) < 0:
            a = m
        if i >= 1:
            if abs(approx[i - 1] - approx[i]) < 0.5 * 10 ** -5:
                break
        if i == 50:
            print(approx)
        i += 1

    print(f"Root is {m}, number of iterations {i}")


def secant(x0, x1, x2):
    x = [x0, x1, x2]

    i = 0

    q = fun(x[i]) / fun(x[i + 1])

    r = fun(x[i + 2]) / fun(x[i + 1])

    s = fun(x[i + 2]) / fun(x[i])

    i = 3
    j = 0
    roots = []
    while True:

        q = fun(x[0]) / fun(x[1])

        r = fun(x[2]) / fun(x[1])

        s = fun(x[2]) / fun(x[0])

        temp = x[2] - (r * (r - q) * (x[2] - x[1]) + (1 - r) * s * (x[2] - x[0])) / ((q - 1) * (r - 1) * (s - 1))

        x[0] = x[1]
        x[1] = x[2]  # Μια ολίσθηση των στοιχείων προς τα αριστερά.
        x[2] = temp

        roots.append(temp)

        if j >= 1:
            if abs(roots[j] - roots[j - 1]) < 0.5 * 10 ** -5:
                break

        j += 1

    print(f"Root is {roots[len(roots) - 1]}, number of iterations {j}")


def newton(x):

    approx = []
    i = 0

    while True:
        x = x - 1 / (first_derivative(x) / fun(x) - (second_derivative(x) / (2 * first_derivative(x))))
        approx.append(x)
        if i >= 1:

            if abs(approx[i - 1] - approx[i]) < 0.5 * 10 ** -5:
                break
        i += 1

    print(f"Root is {x}, number of iterations {i}")
