import numpy as np
from scipy.stats import norm, t

# # Using Argon
# n_a = 544
# mean_a = 0.37
# std_a = 0.25

# # Using CO2
# n_c = 581
# mean_c = 0.4
# std_c = 0.26

# # Null: mean_a - mean_c = 0
# # Alt: mean_a - mean_c != 0

# alpha = 0.05

# diff = mean_a - mean_c
# std_diff = np.sqrt((std_a**2 / n_a + std_c**2 / n_c))

# print("Difference in means:", diff)
# print("Standard error of difference:", std_diff)

# # How likely is it that we get 0.03 or -0.03 if null is true?
# tail = norm.cdf(diff, 0, std_diff)
# print(tail)
# p_value = 2 * tail
# # print("P-value:", p_value)
# # Since p_value is 0.048, we reject the null hypothesis at alpha = 0.05 level since Argon seems to produce smaller inclusions.

# # 95 % CI for difference in means
# interval = norm.interval(0.95, diff, std_diff)
# print(interval)

# # null: mean_a - mean_c >= -0.015
# tail2 = norm.cdf(diff, -0.015, std_diff)
# print("P-value for H0:", tail2)
# # 0.162 > 0.05, we fail to reject the null hypothesis that the difference in means is 0.015

# structured
n_s = 10
mean_s = 44.1
std_s = 10.09

# conventional
n_c = 10
mean_c = 32.3
std_c = 8.56

diff = mean_s - mean_c
std_diff = np.sqrt((std_s**2 / n_s + std_c**2 / n_c))
print("Difference in means:", diff)
print("Standard error of difference:", std_diff)

# null: mean_s - mean_c <= 0
# alt: mean_s - mean_c > 0 IMPROVMENT 
# alpha = 0.05

tail = 1 - t.cdf(11.8, df=18, loc=0, scale=4.18)
print("P-value:", tail)

# Since we want structured better at 5% significance level,
# We only want the positive tail.

# Since p_value is 0.0024, which is less than 0.05,
# we reject the null hypothesis and conclude that
# the difference in means is 
# statistically significant and the structured is better.

# 95% CI for difference in means
# interval = t.interval(0.95, df=18, loc=diff, scale=std_diff)
# print("95% CI for difference in means:", interval)

low = t.ppf(0.05, df=18, loc=diff, scale=std_diff)
print(low)
# Since the entire interval is positive,
# we are 95% confident that the structured method
# leads to higher scores than the conventional method.

### t.interval is for two-tailed only
### t.ppf() lower or upper bound for one-tailed
### t.cdf() to compute p_value for one-tailed
### norm.interval() for two-tailed when n > 30 or we know std deviance of population
### norm.ppf() lower or upper bound for one-tailed when n > 30 or we know std deviance of population
### norm.cdf() to compute p_value for one-tailed when n > 30 or we know std deviance of population
