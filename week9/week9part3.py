import numpy as np
from scipy.stats import norm, t

# mean = 250
# std = np.sqrt( 200**2 / 16 + 800**2 / 16)

# probability of failure = t.cdf(0, 30, mean, std)

n = 10
# one-sided since we are only interested in whether the new tire is better.
df = 9
alpha = 0.05

diff = [0.16, 0.38, 0.17, 0.31, 0.19, 0.35, 0.43, -0.21, 0.34, 0.2]

mean_diff = np.mean(diff)
std = np.std(diff, ddof=1)
se = std / np.sqrt(n)

pvalue = 1 - t.cdf(mean_diff, df, 0, se)
print("P-value:", pvalue)

# Since it's a one-sided test, we only need the lower bound.
# The lower bound of the 95% confidence interval is at 0.05
point = t.ppf(0.05, df, mean_diff, se)
print("Lower Bound:", point)

# null: difference <= 0
# alternative: difference > 0

# Since p-value is 0.0015, which is less than 0.05, we reject the null hypothesis.
# The new tire is significantly better than the old tire.

### Summary
# Confidence interval or hypothesis test
# 1 sample group or 2 sample group (1: mean, std/sqrt(n) 2: mean1 - mean2, sqrt(std1^2/n1 + std2^2/n2))
# 1-sided or 2-sided (1: + or -, 2 with either lower or upper bound (using ppf) care about improvement: do both with lower bound and upper bound (using interval) are we looking at a deviation or an improvement)
# Large or small sample size (norm or t)
# Independent or paired samples (if paired, think about subtracting and treating as one sample)