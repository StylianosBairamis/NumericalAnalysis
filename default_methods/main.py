import numpy as np
from matplotlib import pyplot as plt
from default_methods.functions import f, first, second
from root_finding import bisection, newton, secant


def graph():
    x = np.linspace(-2, 2, 1000)
    plt.plot(x, f(x), first(x), second(x) )
    plt.grid()
    plt.show()


if __name__ == "__main__":
    graph()
    bisection(-1.5, 1)
    newton(-2)
    secant(1.4, 1.8)
