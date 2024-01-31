from default_methods.functions import f, first


def bisection(a, b):
    i = 0
    an = [a]
    bn = [b]
    mn = []

    while (b - a) / 2 > 0.5 * 10 ** -5:
        m = (b + a) / 2
        mn.append(m)
        if f(m) == 0:
            break
        if f(m) * f(a) < 0:
            b = m
            bn.append(b)
        else:
            a = m
            an.append(a)
        i += 1

    print(f"Root is {m}, number of iterations {i}")
    print("a: ", an, len(an))
    print("b: ", bn, len(bn))
    print("m:", mn, len(mn))


def newton(x):
    xr = []
    i = 0

    while True:
        x = x - f(x) / first(x)
        xr.append(x)
        if i >= 1:
            if abs(xr[i] - xr[i - 1]) < 0.5 * 10 ** -5:
                break

        i += 1

    print(f"Root is {x}, number of iterations {i}")


def secant(a, b):
    x = [a, b]
    counter = 1

    while True:
        temp = x[counter] - (f(x[counter]) * (x[counter] - x[counter - 1])) / (f(x[counter]) - f(x[counter - 1]))
        x.append(temp)
        counter += 1

        if counter >= 3:
            if abs(x[counter] - x[counter - 1]) < 0.5 * 10 ** -5:
                break

    print(f"Root is {x[counter]}, number of iterations {counter}")
