import numpy as np
from statistics import mean, stdev

# Values and frequencies
occupants = [1, 2, 3, 4, 5]
cars = [70, 15, 10, 3, 2]

# Expand the dataset
data = []
for x, f in zip(occupants, cars):
    data.extend([x] * f)

# a) Sample mean
mean_value = mean(data)

# b) Sample standard deviation
std_value = stdev(data)

# c) Median
median_value = np.median(data)

# d) Quartiles
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

# e) Proportion above mean
count_above_mean = sum(1 for x in data if x > mean_value)
prop_above_mean = count_above_mean / len(data)

print("Mean:", mean_value)
print("Standard Deviation:", std_value)
print("Median:", median_value)
print("Q1:", Q1)
print("Q3:", Q3)
print("Proportion above mean:", prop_above_mean)
