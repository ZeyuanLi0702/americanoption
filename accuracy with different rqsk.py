from AmericanOptionSolver import *
from multiprocessing import Pool

if __name__ == '__main__':
    # unit test one for valuing American option
    r = [0.02, 0.04, 0.06, 0.08, 0.1]  # risk free
    q = [0.02, 0.04, 0.06, 0.08, 0.1]  # dividend yield
    K = 100.0  # strike
    S = [25, 50, 80, 90, 100, 110, 120, 150, 175, 200]  # underlying spot
    sigma = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]  # volatility
    T = [1 / 12, 0.25, 0.5, 0.75, 1, 2, 3]  # maturity
    option_type = qd.OptionType.Put
    n = 2  # the number of collocation nodes
    p = 5  # the number of quadrature nodes
    l = 3  # the number of integration nodes
    m = 1  # the number of iterations
    n_benchmark = 64
    p_benchmark = 131
    l_benchmark = 131
    m_benchmark = 16

    solver = AmericanOptionSolver(r, q, sigma, K, T, option_type)
    solver.assign_par(n_benchmark, p_benchmark, l_benchmark, m_benchmark)
    solver.use_derivative = False
    solver.iter_tol = 0
    solver.max_iters = 30
    price = solver.solve(0.0, S)  # t and S
    print("european price = ", solver.european_price)
    print("american price = ", price)
    print("american price = ", price - solver.european_price)
    american_premium_benchmark = price - solver.european_price
    american_premium_benchmark = 0.10695270125432899

    error_r = []
    for r_i in r:
        solver = AmericanOptionSolver(r_i, q[0], sigma[0], K, T[0], option_type)
        solver.assign_par(n,p, l,m)
        solver_benchmark = AmericanOptionSolver(r_i, q[0], sigma[0], K, T[0], option_type)
        solver_benchmark.assign_par(n_benchmark, p_benchmark, l_benchmark, m_benchmark)
        solver.use_derivative = False
        solver_benchmark.use_derivative = False
        solver.iter_tol = 0
        solver_benchmark.iter_tol = 0
        solver.max_iters = 5
        solver_benchmark.max_iter = 5
        price = solver.solve(0.0, S[0])  # t and S
        price_benchmark = solver_benchmark.solve(0.0, S[0])
        american_premium = price - solver.european_price
        american_premium_benchmark = price_benchmark - solver.european_price
        error_r.append(american_premium_benchmark - american_premium)
    print(error_r)

    # error_r = []

    error_q = []
    for q_i in q:
        solver = AmericanOptionSolver(r[0], q_i, sigma[0], K, T[0], option_type)
        solver_benchmark = AmericanOptionSolver(r[0], q_i, sigma[0], K, T[0], option_type)
        solver.assign_par(n, p, l, m)
        solver_benchmark.assign_par( n_benchmark, p_benchmark, l_benchmark, m_benchmark)
        solver.use_derivative = False
        solver_benchmark.use_derivative = False
        solver.iter_tol = 0
        solver_benchmark.iter_tol = 0
        solver.max_iters = 5
        solver_benchmark.max_iter = 5
        price = solver.solve(0.0, S[0])  # t and S
        price_benchmark = solver_benchmark.solve(0.0, S[0])
        american_premium = price - solver.european_price
        american_premium_benchmark = price_benchmark - solver.european_price
        print("european price = ", solver.european_price)
        print("american price = ", price)
        print("american price = ", price - solver.european_price)

    error_sigma = []
    for sigma_i in sigma:
        solver = AmericanOptionSolver(r[0], q[0], sigma_i, K, T[0], option_type)
        solver_benchmark = AmericanOptionSolver(r[0], q[0], sigma_i, K, T[0], option_type)
        solver.assign_par(n, p, l, m)
        solver_benchmark.assign_par(n_benchmark, p_benchmark, l_benchmark, m_benchmark)
        solver.use_derivative = False
        solver_benchmark.use_derivative = False
        solver.iter_tol = 0
        solver_benchmark.iter_tol = 0
        solver.max_iters = 5
        solver_benchmark.max_iter = 5
        price = solver.solve(0.0, S[0])  # t and S
        price_benchmark = solver_benchmark.solve(0.0, S[0])
        american_premium = price - solver.european_price
        american_premium_benchmark = price_benchmark - solver.european_price
        # print("european price = ", solver.european_price)
        # print("american price = ", price)
        print("american price = ", price - solver.european_price)
        error_sigma.append(american_premium_benchmark - american_premium)
    print(error_sigma)

    # Compute the error of different r, q, s, k and observe their differences.
    error_T = []
    for T_i in T:
        solver = AmericanOptionSolver(r[0], q[0], sigma[0], K, T_i, option_type)
        solver_benchmark = AmericanOptionSolver(r[0], q[0], sigma[0], K, T_i, option_type)
        solver.assign_par(n, p, l, m)
        solver_benchmark.assign_par(n_benchmark, p_benchmark, l_benchmark, m_benchmark)
        solver.use_derivative = False
        solver_benchmark.use_derivative = False
        solver.iter_tol = 0
        solver_benchmark.iter_tol = 0
        solver.max_iters = 5
        solver_benchmark.max_iter = 5
        price = solver.solve(0.0, S[0])  # t and S
        price_benchmark = solver_benchmark.solve(0.0, S[0])
        american_premium = price - solver.european_price
        american_premium_benchmark = price_benchmark - solver.european_price
        # print("european price = ", solver.european_price)
        # print("american price = ", price)
        print("american price = ", price - solver.european_price)
        error_T.append(american_premium_benchmark - american_premium)
    print(error_T)
