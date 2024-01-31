import sympy as sp

x = sp.Symbol('x')

f = 94 * (sp.cos(x) ** 3) - 24 * sp.cos(x) + 177 * (sp.sin(x) ** 2) - 108 * (sp.sin(x) ** 4) - 72 * (sp.cos(x) ** 3) * (sp.sin(x) ** 2) -65

fun = sp.lambdify(x, f)

first = f.diff(x)
second = first.diff(x)

first_derivative = sp.lambdify(x, first)
second_derivative = sp.lambdify(x, second)