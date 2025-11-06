import scipy.stats as stats

# mu = 50
# sigma = 5

# stats.norm.cdf(52, mu, sigma)
# mid = stats.norm.cdf(52, mu, sigma) - stats.norm.cdf(42, mu, sigma)
# # print("Cumulative probability up to 52:", stats.norm.cdf(52, mu, sigma))
# # print("Probability between 42 and 52:", mid)

# stats.norm.ppf(0.4, mu, sigma)
# # print("40th percentile:", stats.norm.ppf(0.4, mu, sigma))

# mu = 0.66
# sigma = 0.5244

# sigma1 = 0.05244
# mu1 = 66

# print(stats.norm.cdf(0.5, 0.66, sigma1))

# n = 50
# s = 1.43
# mu = 4.46

# z = stats.norm.ppf(0.975)
# print(z)
# confidence = z * (s/(n**0.5))
# print(mu - confidence, mu + confidence)

n = 40
s = 6
mu = 67

z = stats.norm.ppf(0.95)
print(z)
confidence = z * (s/(n**0.5))
print(mu - confidence, mu + confidence)