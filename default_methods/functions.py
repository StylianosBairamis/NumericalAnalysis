import numpy as np


def f(z):
    return np.exp(np.sin(z) ** 3) + z ** 6 - 2 * z ** 4 - z ** 3 - 1


def f(z):
    return np.exp(np.sin(z) ** 3) + z ** 6 - 2 * z ** 4 - z ** 3 - 1


def first(z):
    return 3 * np.exp(np.sin(z) ** 3) * np.cos(z) * (np.sin(z) ** 2) + 6 * z ** 5 - 8 * z ** 3 - 3 * z ** 2


def second(z):
    return 9 * np.exp(np.sin(z) ** 3) * (np.cos(z) ** 2) * (np.sin(z) ** 4) - 3 * np.exp(np.sin(z) ** 3) * (np.sin(z) ** 3) + 6 * np.exp(np.sin(z) ** 3) * (np.cos(z) ** 2) * (np.sin(z)) + 30 * z ** 4 - 24 * z ** 2 - 6 * z


