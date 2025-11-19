import numpy as np
import scipy.stats as stats

n = 123
mean = 136.9
std = 22.6
se = std / np.sqrt(n)

# Find a 95% confidence interval for the mean surgery time
ci = stats.t.interval(0.95, n-1, loc=mean, scale=se)
print(ci)


# Confidence that the mean is between 133.9 and 139.9?
lower_bound = 133.9
upper_bound = 139.9
p_lower = stats.t.cdf(lower_bound, n-1, loc=mean, scale=se)
p_upper = stats.t.cdf(upper_bound, n-1, loc=mean, scale=se)
confidence = p_upper - p_lower
print(confidence)

# Approximately how many surgeries must be sampled so that a 
# 95 % confidence interval will specify the mean to within +- 3 minutes?
std = 22.6
margin_of_error = 3

z = stats.norm.ppf(0.975)  # 1.96

required_n = (z * std / margin_of_error) ** 2
print(int(np.ceil(required_n)))

# Find a 98% lower confidence bound for the mean time
lower_bound_98 = stats.t.ppf(0.02, n-1, loc=mean, scale=se)
print(lower_bound_98)

# (132.86602407581225, 140.93397592418776)
# 0.8564567602381621
# 219
# 132.66970598487148