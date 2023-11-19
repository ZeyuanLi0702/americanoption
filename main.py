# This is a sample Python script.
from AmericanOptionSolver import *
import time
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst = [[5,1,4,15], [7,2,5,20],[11,2,5,31],[15,2,6,41],[15,3,7,41],[25,4,9,51],[25,5,12,61],
           [25,6,15,61],[35,8,16,81],[51,8,24,101],[65,8,32,101]]
    r = 0.05  # risk free
    q = 0.05  # dividend yield
    K = 100.0  # strike
    S = 100  # underlying spot
    sigma = 0.25  # volatility
    T = 1  # maturity
    option_type = qd.OptionType.Put
    solver = AmericanOptionSolver(r, q, sigma, K, T, option_type)
    solver.assign_par(201, 16, 64, 201)
    # accurate = solver.solve(0,S)

    solver.use_derivative = False
    # for ls in lst:
    #     solver.assign_par(ls[0],ls[1],ls[2],ls[3])
    #     start = time.process_time()
    #     price = solver.solve(0,S)
    #     error = price - accurate
    #
    #     print("total time cost = ", time.process_time() - start)

    n = [2, 4, 6, 8, 10, 12, 16]  # the number of collocation nodes
    p = [5, 8, 15, 25, 50, 65, 81]  # the number of quadrature nodes
    l = [3, 5, 7, 12, 20, 33, 41]  # the number of integration nodes
    m = [1, 1, 2, 3, 4, 5, 6]  # the number of iterations
    n_bench = 64
    p_bench = 131
    l_bench = 131
    m_bench = 16
    american_premium_benchmark = 0.10695270125432899

    error_n = []
    for n_i in n:
        solver = AmericanOptionSolver(r, q, sigma, K, T, option_type)
        solver.assign_par(l_bench, m_bench, n_i, p_bench)
        solver.use_derivative = False
        solver.iter_tol = 0
        solver.max_iters = 10
        price = solver.solve(0.0, S)  # t and S
        american_premium = price - solver.european_price
        # print("european price = ", solver.european_price)
        # print("american price = ", price)
        print("american price = ", price - solver.european_price)
        error_n.append(american_premium_benchmark - american_premium)

    error_p = []
    for p_i in p:
        solver = AmericanOptionSolver(r, q, sigma, K, T, option_type)
        solver.assign_par(l_bench,m_bench,n_bench,p_i)
        solver.use_derivative = False
        solver.iter_tol = 0
        solver.max_iters = 10
        price = solver.solve(0.0, S)  # t and S
        # print("european price = ", solver.european_price)
        # print("american price = ", price)
        american_premium = price - solver.european_price
        print("american price = ", american_premium)
        error_p.append(american_premium_benchmark - american_premium)

    error_m = []
    for m_i in m:
        solver = AmericanOptionSolver(r, q, sigma, K, T, option_type)
        solver.assign_par(l_bench, m_i, n_bench, p_bench)
        solver.use_derivative = False
        solver.iter_tol = 0
        solver.max_iters = m_i
        price = solver.solve(0.0, S)  # t and S
        # print("european price = ", solver.european_price)
        # print("american price = ", price)
        american_premium = price - solver.european_price
        print("american price = ", american_premium)
        error_m.append(american_premium_benchmark - american_premium)

    print(error_p, error_n, error_m)
    print(american_premium_benchmark)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
