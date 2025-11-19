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