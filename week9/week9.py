import scipy.stats as stats
import numpy as np

# sample_size = 30
# mean = 10
# std_dev = 1.3

# std_err = std_dev / np.sqrt(sample_size)

# conf_int = 0.9 # for lower bound

# # Confidence interval calculation
# # mean + z * (std_dev / sqrt(n))

# # Lower Bound
# print(stats.norm.ppf(0.1, mean, std_err))
# # Upper Bound
# print(stats.norm.ppf(0.9, mean, std_err))

# sample = [580, 400, 428, 825, 875, 550, 575, 750]
# sample_size = len(sample)
# mean = np.mean(sample)
# std_dev = np.std(sample, ddof=1)
# std_err = std_dev / np.sqrt(sample_size)

# print(stats.t.interval(0.99, sample_size-1, loc=mean, scale=std_err))

n_men = 17
n_female = 17
mean_men = 3.882
mean_female = 5.353
variance_men = 2.985
variance_female = 2.743
std_men = np.sqrt(variance_men)
std_female = np.sqrt(variance_female)

# stats.t.interval(0.95, n_men-1, loc=mean_men, scale=std_men/np.sqrt(n_men))
# stats.t.interval(0.95, n_female-1, loc=mean_female, scale=std_female/np.sqrt(n_female))

df = n_men + n_female - 2
xbar = mean_female - mean_men
se = np.sqrt(variance_men/n_men + variance_female/n_female)

print(stats.t.interval(0.95, df, loc=xbar, scale=se))
print(stats.norm.interval(0.95, xbar, se))