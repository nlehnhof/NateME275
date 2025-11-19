import numpy as np
from scipy import integrate

# Resistors labeled 100 ohms have true resistances that are between 80 and 120.
# Let X be the resistance of a randomly chosen resistor. 
# Probability desnity function of X is given by:
#  f(x) = (x-80) / 800 for 80< x< 120
# f(x) = 0 otherwise
# 
# What proportion of resistors have resistances less than 90 ohms?
def f(x):
    if 80 < x < 120:
        return (x - 80) / 800
    else:
        return 0

# Find the mean resistance
mean = integrate.quad(lambda x: x * f(x), 80, 120)[0]
print("Mean resistance:", mean)
# Find the variance of the resistance
variance = integrate.quad(lambda x: (x - mean) ** 2 * f(x), 80, 120)[0]
print("Variance of resistance:", variance)
std = np.sqrt(variance)
print("Standard deviation of resistance:", std)
# x less than 90
prob = integrate.quad(f, 80, 90)[0]
print("Proportion of resistors with resistance less than 90 ohms:", prob)

# Mean resistance: 106.66666666666666
# Variance of resistance: 88.88888888888887
# Standard deviation of resistance: 9.428090415820632
# Proportion of resistors with resistance less than 90 ohms: 0.06250000000000001