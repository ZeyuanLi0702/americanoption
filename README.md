# americanoption

Classes:
For the project we have four files with five abstract classes. We will introduce our project by classes and a code walk through.

EuropeanOption: 
The usage of this class is to calculate the initial B value for the fix point problem for B, this class has different methods for different option types.

Interpolation: 
The usage of this class is mainly to accomplish the part of Chebyshev interpolation, initialize the tau, create ak based on q and evaluate q(z) given q and z.

QDPlus:
 The usage of this class is to calculate the first exercise boundary B0

AmericanOptionSolver: 
This part is the main part of our project. The main function”solver”, solves the American Premium using given parameters. We will illustrate the utility in detail in the scenario walkthrough! And I will firstly introduce some important method:
Solver: the most important method which solves for the American premium and works the whole process.
compute_exercise_boundary, iterate_once, iterate_for_eachtau: these are a series of methods that solve for the fix point problem for B0 it lead the iteration and use imported method from Interpolation
quadrature_sum: This method use quadrature estimate to estimate for the integral of the american premium and k1, k2, k3
compute_integration_term: This method is important to save complexity because it is used for the integral of both the american premium and k1,k2,k3. The role it plays is to set appropriate u and Bu for the quadrature sum. When we calculate k1,k2,k3, we need u = tau - tau(1+ y**2)/4 and B(u) for it. When we calculate for the final premium, we need u = tau






Scenario Walkthrough

We initialize the AmericanOptionSolver, we set the interest rate, dividend rate, expiry, spot price, volatility and strike price for the class. 
we call {solver} to solve for the American premium.
It uses the call {set_collocation_points} to initialize the tau values using Chebyshev interpolation
it assigns the tau value to the attribute {shared_tau}.
it calls {compute exercise_boundary} to compute the boundary value Bn with given stopping criterions
The {compute_exercise_boundary} call {set initial guess} to get B0 using QD+ approximation and starts an iteration to solve the fix point problem
For each Bi( ) it compute the Bi( - (1+y**2)/4) by {compute_integration_term} and integrate
It integrate  k1, k2, k3 with {quadrature_sum} with k1,k2,k3
We write a function to compute the value of N,D,N’,D’.
After having all the Boundary values, we can compute for the integral using {quadrature_sum}.
