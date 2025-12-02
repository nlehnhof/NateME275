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

(132.9060375776225, 140.8939624223775)
0.8590318028563106
218.00705636197017
132.71492515231745