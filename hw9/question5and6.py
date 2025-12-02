import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('hw9/knee.csv')
heights = data['kneeheightmidpatella'].dropna()

mean_height = np.mean(heights)
std_height = np.std(heights, ddof=1)
sample_size = len(heights)
std_err = std_height / np.sqrt(sample_size)

# # Histogram
# plt.figure()
# plt.hist(heights, bins=20, alpha=0.6)
# plt.title('Histogram of Heights')
# plt.xlabel('Height')
# plt.ylabel('Density')
# plt.show()

# # CDF
# plt.figure()
# plt.hist(heights, bins=20, alpha=0.6, density=True, cumulative=True)
# plt.title('Cumulative Distribution Function of Height')
# plt.xlabel('Height')
# plt.ylabel('Cumulative Probability')
# plt.show()

# Normal Distribution using norm.pdf
# Normal PDF
plt.figure()
plt.hist(heights, bins=25, alpha=0.6, density=True)
plt.title('Probabilty Distribution Function of Height')
plt.xlabel('Height')
plt.ylabel('Density')
# plt.show()


x = np.linspace(mean_height - 4*std_height, mean_height + 4*std_height, 1000)
pdf_values = stats.norm.pdf(x, mean_height, std_height)
# plt.figure()
plt.plot(x, pdf_values, 'k', linewidth=2, label='Normal PDF')
plt.legend()
# plt.title('Normal Distribution PDF')
# plt.xlabel('Height')
# plt.ylabel('Density')
plt.show()