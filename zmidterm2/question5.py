import scipy.stats as stats

data = [0, 0, 1, 3, 4, 0, 0, 5, 5, 1, 1, 1, 13]

mean = sum(data) / len(data)
median = sorted(data)[len(data) // 2]
# 80 percentile
percentile_80 = stats.scoreatpercentile(data, 80)

stndev = stats.tstd(data)
variance = stats.tvar(data)
print("Mean:", mean)
print("Median:", median)
print("80th Percentile:", percentile_80)
print("Standard Deviation:", stndev)
print("Variance:", variance)

# Mean: 2.6153846153846154
# Median: 1
# 80th Percentile: 4.600000000000001
# Standard Deviation: 3.640935354604673
# Variance: 13.256410256410257