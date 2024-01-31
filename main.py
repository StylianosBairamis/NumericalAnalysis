from default_methods.root_finding import bisection, newton, secant
from modified_methods.root_finding import modified_bisection, modified_newton, modified_secant
from matrix_operations.gauss_elimination import  gauss_elimination
from matrix_operations.cholesky import cholesky
from matrix_operations.gauss_seidel import gauss_seidel


# def graph():
#     x = np.linspace(-2, 2, 1000)
#     plt.plot(x, f(x), first(x), second(x))
#     plt.grid()
#     plt.show()


if __name__ == "__main__":
    #### First part

    # graph()
    bisection(-1.5, 1)
    newton(-2)
    secant(1.4, 1.8)

    #### Second Part

    modified_secant(1, 1.05, 1.2)
    modified_bisection()
    modified_newton(1)

    ### Thrid part
    cholesky(3)
    gauss_elimination(3)
    gauss_seidel(10000)
