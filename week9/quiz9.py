import numpy as np
from scipy.stats import norm

# area under normal curve to the right of z = -0.85
# z = -0.85
# area = 1 - norm.cdf(z)
# print(area)

mean = 2
variance = 9
std = 3

# x between 1 and 7
prob = norm.cdf(7, mean, std) - norm.cdf(1, mean, std)
print(prob)