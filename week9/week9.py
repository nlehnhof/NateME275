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

# n_men = 17
# n_female = 17
# mean_men = 3.882
# mean_female = 5.353
# variance_men = 2.985
# variance_female = 2.743
# std_men = np.sqrt(variance_men)
# std_female = np.sqrt(variance_female)

# stats.t.interval(0.95, n_men-1, loc=mean_men, scale=std_men/np.sqrt(n_men))
# stats.t.interval(0.95, n_female-1, loc=mean_female, scale=std_female/np.sqrt(n_female))

# df = n_men + n_female - 2
# xbar = mean_female - mean_men
# se = np.sqrt(variance_men/n_men + variance_female/n_female)

# print(stats.t.interval(0.95, df, loc=xbar, scale=se))
# print(stats.norm.interval(0.95, xbar, se))

# mean = 1000
# tail = 1000.6
# std_dev = 2

# tail = 1 - stats.norm.cdf(tail, loc=mean, scale=std_dev/np.sqrt(60))
# p_value = 2 * tail
# print(p_value)

# alpha = 5 % (since p_value < alpha, we reject H0 -- scale is calibrated with a true mean of 1000g. All we have left is the alt hypothesis that the mean is not 1000g, Ha: mu != 1000g)

# mean = 80
# coating = 74
# std = 18
# n = 60
# std_err = std / np.sqrt(n)

# # H0: mu >= 80 (nothing changed)
# p_value = stats.norm.cdf(coating, loc=mean, scale=std_err)
# print(p_value)

# 1. Define null and alt hypotheses
# 2. assume null to be true
# 3. collect data. Compute p-value. Choose alpha.
# 4. if p-value < alpha, reject H0

mean = 39
n = 6
thickness = [39.030, 38.997, 39.012, 39.008, 39.019, 39.002]
std_dev = np.std(thickness, ddof=1)
std_err = std_dev / np.sqrt(n)
sample_mean = np.mean(thickness)

# H0: mu = 39
# Ha: mu != 39
interval = 2* (1 - stats.t.cdf(sample_mean, df= n-1, loc=mean, scale=std_err)) * 100
print(interval)
# p_value = 6.7424 %
# alpha = 5% (since p-value > alpha, we fail to reject H0 -- there is not enough evidence to suggest that the mean thickness differs from 39 micrometers)