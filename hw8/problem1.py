import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data_f = np.recfromcsv('hw8/female.csv', encoding='ISO-8859-1')
knee_f = data_f['kneeheightmidpatella']

data_m = np.recfromcsv('hw8/male.csv', encoding='ISO-8859-1')
knee_m = data_m['kneeheightmidpatella']

knee = np.concatenate((knee_f, knee_m))

########### A ##############

# Plot histogram
# plt.figure()
# plt.hist(knee, bins=30, density=True, alpha=0.6, color='g')
# plt.xlabel('Knee Height (mid patella)')
# plt.ylabel('Density')
# plt.title('Histogram of Knee Height (mid patella)')
# plt.show()

########### B ##############
# sizes = []
# for entry in knee:
#     if entry >= 425 | entry <= 550:
#         sizes.append(entry)

# # Get percentiles of sizes
# percentiles = np.percentile(sizes, [25, 50, 75])
# print("25th, 50th, 75th percentiles of knee heights >= 425 mm:", percentiles)

# First Sizes
# 425 mm - 443 mm: 25th percentile
# 443 mm - 491 mm: 50th percentile
# 491 mm - 495 mm: 75th percentile
# 495 mm - 550 mm: 100th percentile

########### C ##############

stat_f = data_f['stature']
stat_m = data_m['stature']
stat = np.concatenate((stat_f, stat_m))

# Plot Scatter Plot
plt.figure()
plt.scatter(knee, stat, alpha=0.5)
plt.xlabel('Knee Height (mid patella) [mm]')
plt.ylabel('Stature [cm]')
plt.title('Scatter Plot of Knee Height vs Stature')
# Plot least squares fit
slope, intercept, r_value, p_value, std_err = stats.linregress(knee, stat)
line = slope * knee + intercept
plt.plot(knee, line, color='red', label='Least Squares Fit')
# Find correlation coefficient
correlation_matrix = np.corrcoef(knee, stat)
correlation_coefficient = correlation_matrix[0, 1]
print("Correlation Coefficient between Knee Height and Stature:", correlation_coefficient)
plt.annotate(f'Correlation Coefficient: {correlation_coefficient:.2f}', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, verticalalignment='top')
plt.show()