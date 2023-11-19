# This is a sample Python script.
from AmericanOptionSolver import *
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r = 0.02  # risk free
    q = 0.02  # dividend yield
    K = 100.0  # strike
    S = 100  # underlying spot
    sigma = 0.25  # volatility
    T = 1  # maturity
    option_type = qd.OptionType.Put
    solver = AmericanOptionSolver(r, q, sigma, K, T, option_type)
    solver.use_derivative = False
    solver.iter_tol = 1e-5
    solver.max_iters = 20
    price = solver.solve(0.0, S)
    print(price)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
