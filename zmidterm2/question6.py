import scipy.stats as stats

data = [0, 0, 1, 3, 4, 0, 0, 5, 5, 1, 1, 1, 13]

# Plot a histogram of the data with 10 bins
import matplotlib.pyplot as plt
plt.hist(data, bins=10, edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()