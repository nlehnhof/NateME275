import matplotlib.pyplot as plt
import scipy.integrate as sc
import numpy as np

t = [1, 2, 3.25, 4.5, 6, 7, 8, 8.5, 9, 10]
v = [5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5]

# Calculate the area under the curve using the trapezoidal rule
area = np.trapz(v, t)
print(area)

# Find average velocity, though velocity is given at unequally spaced values of time
average_velocity = area / (t[-1] - t[0])
print(average_velocity)

# 60.125
# 6.680555555555555

# To find a unique solution to an nth order initial value problem,
# we need n initial conditions. For example, for a second order ODE,
# we need two initial conditions, typically the value of the function
# and its first derivative at a given point.
# For a 5th order ODE, we need five initial conditions.

# Which of the following parameters most strongly affects the stability of solving an ODE (stability is not the same as accuracy, can be stable and inaccurate, but an unstable solution will blow up).

# A.
# initial condition

# B.
# number of states

# C.
# time step size

# D.
# order of differentiation

# The answer is C. time step size because a smaller time step size can lead to a more stable solution, while a larger time step size can cause instability and numerical errors.
# A and B also play a role in stability, but to a lesser extent than time step size because A affects the starting point of the solution and B affects the complexity of the system being modeled.
# D affects the numerical methods used to solve the ODE and can impact stability, but it is generally less significant than time step size.

# The default algorithm in solve_ivp uses fixed width time steps. True or False.
# False. The default algorithm in solve_ivp uses adaptive time stepping.

# Which of these options is the least sensitive to outliers?

# A.
# mean

# B.
# median

# C.
# standard deviation

# D.
# correlation coefficient

# The correlation coefficient is a measure of the strength and direction of the linear 
# relationship between two variables. It is not affected 
# by outliers in the same way that the mean and standard 
# deviation are, making it the least sensitive to outliers 
# among the options listed.
# The median and mean are both sensitive to outliers, but the median is generally more robust in the presence of extreme values.
# The standard deviation is also sensitive to outliers, as it is based on the mean.

# If A and B are mutually exclusive is P(A and B) = 0? The answer is 
# True because mutually exclusive events cannot occur at the same time.

# If A and B are mutually exclusive then P(A or B) = P(A) + P(B). 
# The answer is True because mutually exclusive events cannot occur at the same time, so the probability of either event occurring is simply the sum of their individual probabilities.

