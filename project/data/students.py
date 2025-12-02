import pandas as pd
from scipy.stats import t
import numpy as np

# Load your dataset
df = pd.read_csv("C:\\Users\\nlehn\\NateME275\\project\\data\\Student_performance_data _.csv")

# Filter groups
low_abs = df[df["Absences"] <= 5]      # Group 1
high_abs = df[df["Absences"] > 5]      # Group 2

# Randomly select 25 students from each group
g1 = low_abs.sample(n=25, random_state=42)["GPA"]
g2 = high_abs.sample(n=25, random_state=42)["GPA"]

# Calculate means and standard deviations
n1 = len(g1)
n2 = len(g2)

mean1 = g1.mean()
mean2 = g2.mean()

std1 = g1.std(ddof=1)
std2 = g2.std(ddof=1)

# Difference in means
diff = mean1 - mean2

# Standard error calculation
SE = np.sqrt((std1**2 / n1) + (std2**2 / n2))

# Degrees of freedom
df = n1 + n2 - 2

# Null: mean1 - mean2 = 0
# Alternative: mean1 - mean2 != 0
# alpha = 0.05

# Two-tailed p-value (must be abs(diff))
p_value = 2 * (1 - t.cdf(abs(diff), df=df, loc=0, scale=SE))

print("Mean (≤5 absences):", mean1)
print("Mean (>5 absences):", mean2)
print("Difference in means:", diff)
print("t-test df:", df)
print("p-value:", p_value)

# Mean (≤5 absences): 3.21297597
# Mean (>5 absences): 1.71087134
# Difference in means: 1.5021046
# t-test df: 48
# p-value: 4.33164e-12

# Since p-value << alpha, we reject the null hypothesis.
# There is a significant difference in GPA between students with ≤5 absences and those with >5 absences.

import matplotlib.pyplot as plt

############# Histogram
# plt.figure(figsize=(8,5))
# plt.hist(g1, bins=10, alpha=0.6, density=True, label="≤5 Absences")
# plt.hist(g2, bins=10, alpha=0.6, density=True, label=">5 Absences")

# plt.xlabel("GPA")
# plt.ylabel("Density")
# plt.title("Histogram of GPA by Absence Group")
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.show()

############## CDF Plot
plt.figure(figsize=(8,5))

# Sort and compute CDF for each group
g1_sorted = np.sort(g1)
g2_sorted = np.sort(g2)

g1_cdf = np.arange(1, len(g1_sorted)+1) / len(g1_sorted)
g2_cdf = np.arange(1, len(g2_sorted)+1) / len(g2_sorted)

# Plot both CDFs
plt.plot(g1_sorted, g1_cdf, label="≤5 Absences", linewidth=2)
plt.plot(g2_sorted, g2_cdf, label=">5 Absences", linewidth=2)

plt.xlabel("GPA")
plt.ylabel("CDF (Proportion ≤ GPA)")
plt.grid(False)
plt.legend()
plt.show()

# from scipy.stats import gaussian_kde

# # --- Compute KDEs ---
# kde1 = gaussian_kde(g1)
# kde2 = gaussian_kde(g2)

# # Generate smooth range of GPA values
# x_vals = np.linspace(min(g1.min(), g2.min()), max(g1.max(), g2.max()), 500)

# # --- Create Figure ---
# plt.figure(figsize=(8,5))

# # Histograms (normalized to density)
# plt.hist(g1, bins=10, density=True, alpha=0.4, label="≤ 5 Absences")
# plt.hist(g2, bins=10, density=True, alpha=0.4, label="> 5 Absences")

# # PDF curves overlaid
# plt.plot(x_vals, kde1(x_vals), linewidth=2, label="PDF ≤ 5 Absences")
# plt.plot(x_vals, kde2(x_vals), linewidth=2, label="PDF > 5 Absences")

# # Formatting
# plt.xlabel("GPA")
# plt.ylabel("Density")
# # plt.title("Histogram and Probability Density Function of GPA by Absence Group")
# plt.legend()
# plt.grid(False)

# # Display plot
# plt.show()

