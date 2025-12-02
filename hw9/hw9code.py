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

import numpy as np
from scipy.stats import norm, t

n = 123
mean = 136.9
std = 22.6
se = std / np.sqrt(n)

# Find a 95% confidence interval for the mean surgery time
z_95 = norm.pdf(0.975)
z_952 = norm.interval(0.95, loc=mean, scale=se)
margin_of_error = z_95 * se
ci = (mean + margin_of_error, mean - margin_of_error)
print(ci)
print(z_952)

# Confidence that the mean is between 133.9 and 139.9?
lower_bound = 133.9
upper_bound = 139.9
z = ((upper_bound - lower_bound) / 2) / se
confidence = 2*norm.cdf(z) - 1
print(confidence)

# Approximately how many surgeries must be sampled so that a 
# 95 % confidence interval will specify the mean to within +- 3 minutes?
std = 22.6
margin_of_error = 3

z = norm.ppf(0.975)  # 1.96

required_n = (z * std / margin_of_error) ** 2
print(required_n)

# Find a 98% lower confidence bound for the mean time
lower_bound_98 = norm.ppf(0.02, loc=mean, scale=se)
print(lower_bound_98)

# (132.9060375776225, 140.8939624223775)
# 0.8590318028563106
# 218.00705636197017
# 132.71492515231745

import numpy as np
import scipy.stats as stats

n = 5
results = np.array([
    87.0, 86.0, 86.5, 88.0, 85.3,
])

mean = np.mean(results)
std_dev = np.std(results, ddof=1)
std_err = std_dev / np.sqrt(n)
conf_int = 0.99

print(stats.t.interval(conf_int, n-1, loc=mean, scale=std_err))
# (84.45718330626976, 88.66281669373025)

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('hw9/knee.csv')
heights = data['kneeheightmidpatella'].dropna()

mean_height = np.mean(heights)
std_height = np.std(heights, ddof=1)
sample_size = len(heights)
std_err = std_height / np.sqrt(sample_size)

# # Histogram
# plt.figure()
# plt.hist(heights, bins=20, alpha=0.6)
# plt.title('Histogram of Heights')
# plt.xlabel('Height')
# plt.ylabel('Density')
# plt.show()

# # CDF
# plt.figure()
# plt.hist(heights, bins=20, alpha=0.6, density=True, cumulative=True)
# plt.title('Cumulative Distribution Function of Height')
# plt.xlabel('Height')
# plt.ylabel('Cumulative Probability')
# plt.show()

# Normal Distribution using norm.pdf
# Normal PDF
plt.figure()
plt.hist(heights, bins=25, alpha=0.6, density=True)
plt.title('Probabilty Distribution Function of Height')
plt.xlabel('Height')
plt.ylabel('Density')
# plt.show()


x = np.linspace(mean_height - 4*std_height, mean_height + 4*std_height, 1000)
pdf_values = stats.norm.pdf(x, mean_height, std_height)
# plt.figure()
plt.plot(x, pdf_values, 'k', linewidth=2, label='Normal PDF')
plt.legend()
# plt.title('Normal Distribution PDF')
# plt.xlabel('Height')
# plt.ylabel('Density')
plt.show()