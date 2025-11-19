import numpy as np
from scipy.stats import norm

# Tabe lists the probability mass function associated 
# with the number of widgets a random customer orders.
# x   1   2    3  4    5
# p(x) 0.4 0.25 0.2 0.1 0.05

# find mean number of widgets a customer ordered
x = np.array([1, 2, 3, 4, 5])
p = np.array([0.4, 0.25, 0.2, 0.1, 0.05])
mean = np.sum(x * p)
print(mean)

# find variance
variance = np.sum(p * (x - mean)**2)
print(variance)

# 2.15
# 1.4275