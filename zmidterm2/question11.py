import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

# Accelerated life test
# 12 motors were operated under high temperature conditions
# The lifetimes (in hours) were measured at ambient temperatures (in deg C)
# ranging from 40 to 95 in steps of 5 (i.e. first lifetime measurement was taken at 40 C, second at 45, and so on):

temperature = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
lifetime = [851, 635, 764, 708, 469, 661, 586, 371, 337, 245, 129, 158]

# Plot the data
# Fit a least squares regression line to the data
# Find the correlation coefficient

plt.figure()
plt.scatter(temperature, lifetime, color='blue', label='Data Points')

A = np.column_stack((temperature, np.ones_like(temperature)))
coeff = np.linalg.lstsq(A, lifetime)[0]
# print(coeff)
# [ -12.61118881 1344.08857809]

coeffs = sc.linregress(temperature, lifetime)
# print(coeffs)
# slope=-12.611188811188812, intercept=1344.088578088578

correlation_matrix = np.corrcoef(temperature, lifetime)
correlation_coefficient = correlation_matrix[0, 1]
print("Correlation Coefficient:", correlation_coefficient)
# -0.9346328250899916

#### SANITY PLOT ####
# line = coeffs.slope * np.array(temperature) + coeffs.intercept
# plt.figure()
# plt.plot(temperature, line, color='red', label='Least Squares Fit')
# plt.scatter(temperature, lifetime, color='blue', label='Data Points')
# plt.xlabel('Temperature (deg C)')
# plt.ylabel('Lifetime (hours)')
# plt.title('Lifetime vs Temperature with Least Squares Fit')
# plt.legend()
# plt.annotate(f'Correlation Coefficient: {correlation_coefficient:.2f}', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, verticalalignment='top')
# plt.show()
