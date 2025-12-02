import numpy as np
from scipy.stats import norm, t

##### QUESTION 1 #####
# mean = 15

# n = 87 # use norm since n > 30
# mean_sample = 15.2
# std = 1.8
# se = std / np.sqrt(n)

# # Null Hypothesis: mu = 15 
# # Alternative Hypothesis: mu != 15
# # Find p-value for two-sided test

# tail = 1 - norm.cdf(mean_sample, loc=mean, scale=se)
# p_value = 2 * tail
# print("P-value:", p_value)

##### QUESTION 2 #####
# mean = 16
# n = 10  # use t since n < 30
# data = np.array([15.87, 16.02, 15.78, 15.83, 15.69, 15.81, 16.04, 15.81, 15.92, 16.10])
# mean_sample = np.mean(data)
# print(mean_sample)
# std = np.std(data, ddof=1)
# se = std / np.sqrt(n)
# df = n - 1

# # Find a 95% confidence interval for the upper bound on the fill weight
# conf_int = 0.95
# upper_bound = t.ppf(conf_int, df, mean_sample, se)
# print("95% Confidence Interval Upper Bound:", upper_bound)

# tail = t.cdf(mean_sample, df, mean, se)
# print("P-value:", tail)  # one-sided test   

##### QUESTION 3 #####
# n = 110 # presence
# mean = 169.9
# std = 24.8
# se = std / np.sqrt(n)

# n2 = 225 # absence
# mean2 = 163.3
# std2 = 25.8
# se2 = std2 / np.sqrt(n2)

# # Null Hypothesis: mu1 - mu2 = 0
# # Alternative Hypothesis: mu1 - mu2 != 0
# diff_mean = mean - mean2
# se_diff = np.sqrt(se**2 + se2**2)
# tail = 1 - norm.cdf(diff_mean, loc=0, scale=se_diff)
# p_value = 2 * tail
# print("P-value:", p_value)

# # Find 95% confidence interval for the difference in means
# conf_int = 0.95
# lower_bound = norm.ppf(0.025, diff_mean, se_diff)
# upper_bound = norm.ppf(0.975, diff_mean, se_diff)
# print("95% Confidence Interval:", (lower_bound, upper_bound))

##### QUESTION 4 #####
# nd = 6
# no = 8

# disk = np.array([269.0, 249.3, 255.2, 252.7, 247.0, 261.6])
# oval = np.array([268.8, 260.0, 273.5, 253.9, 278.5, 289.4, 261.6, 280.2])

# meand = np.mean(disk)
# stdd = np.std(disk, ddof=1)
# sed = stdd / np.sqrt(nd)

# meano = np.mean(oval)
# stdo = np.std(oval, ddof=1)
# seo = stdo / np.sqrt(no)

# diff = meano - meand
# se = np.sqrt(seo**2 + sed**2)

# pvalue = 2 * (1 - t.cdf(diff, df=12, loc=0, scale=se))
# print(pvalue)

##### QUESTION 5 #####
# n = 10
# rest = np.array([15, 16, 21, 17, 18, 15, 19, 21, 18, 14])
# exercise = np.array([30, 37, 39, 37, 40, 39, 34, 40, 38, 34])

# conf = 0.95

# # since paired, we can subtract and treat as one sample
# diff = exercise - rest
# mean_diff = np.mean(diff)
# std_diff = np.std(diff, ddof=1)
# se_diff = std_diff / np.sqrt(n)

# interval = t.interval(0.95, df=9, loc=mean_diff, scale=se_diff)
# print(interval)

############################################################33

"""
==============================================================
SUMMARY OF HYPOTHESIS TESTING PRINCIPLES USED IN THIS SCRIPT
==============================================================

This script performs several classical statistical inference tasks:
- One-sample hypothesis tests
- Two-sample hypothesis tests (independent and paired)
- Confidence intervals using normal and t distributions

Below is a consolidated summary of the principles, vocabulary, and cases used.


-----------------------------
1. Population Mean (μ)
-----------------------------
The *population mean* is the true average of the entire population.
A *sample mean* (x̄) is our estimate based on data.

We test hypotheses such as:
    H0: μ = μ0       (null hypothesis)
    Ha: μ ≠ μ0       (alternative hypothesis, two-sided)
Or sometimes:
    Ha: μ > μ0       (one-sided)
    Ha: μ < μ0


---------------------------------------------
2. Standard Deviation (σ) and Sample Std (s)
---------------------------------------------
- Population standard deviation (σ) is usually unknown.
- We estimate it using the sample standard deviation (s).

For unbiased estimation we use:
    s = np.std(data, ddof=1)
where ddof=1 applies the Bessel correction.


------------------------------
3. Standard Error (SE)
------------------------------
The standard error of the sample mean estimates the variability of x̄:

    SE = s / sqrt(n)

For two-sample tests (independent groups):

    SE_diff = sqrt( SE1^2 + SE2^2 )


-------------------------------------------------
4. Normal Distribution vs. t Distribution
-------------------------------------------------
A major decision in hypothesis testing:

Use **normal distribution (Z-test)** when:
    - Sample size n > 30 (Central Limit Theorem)
    - OR population standard deviation σ is known (rare)

Use **t distribution (t-test)** when:
    - Sample size n < 30
    - σ is unknown and must be estimated from the sample
    - Data are reasonably normal

Degrees of freedom (df):
    - One-sample t-test: df = n - 1
    - Two-sample t-test (unequal variances): df ≈ Satterthwaite approx.
    - Paired test: df = n - 1


---------------------------------------------------------
5. p-values
---------------------------------------------------------
A p-value measures how extreme the sample result is assuming H0 is true.

Two-sided test:
    p = 2 * (1 - CDF(|test statistic|))

One-sided test:
    p = 1 - CDF(test statistic)
or
    p = CDF(test statistic)
depending on direction.

If p < α (typically 0.05):
    Reject H0 → statistically significant difference.

If p ≥ α:
    Fail to reject H0 → not enough evidence to claim a difference.


---------------------------------------------------------
6. Confidence Intervals (CI)
---------------------------------------------------------
A 95% CI for a mean:
    mean ± t* * SE

For a *difference in means*:
    (x̄1 - x̄2) ± t* * SE_diff

For a *paired test*:
    - Compute differences first: d = x_exercise - x_rest
    - Treat d as a one-sample t-test problem


---------------------------------------------------------
7. Two-Sample Tests: Independent vs Paired
---------------------------------------------------------

Case A — Independent Samples:
--------------------------------
Used when two groups have no natural pairing (Tablet shapes, presence vs absence group).

Key assumptions:
    - Groups independent
    - Often assume unequal variances
    - SE_diff uses both groups’ standard errors

Case B — Paired Samples:
-------------------------
Used when each observation in group A corresponds directly to group B.
Examples:
    - Before/after measurements
    - Rest vs exercise heart rate for same subject

Method:
    diff = group2 - group1
    Test mean(diff) using a one-sample t-test.


---------------------------------------------------------
8. Normal CDF vs. t CDF
---------------------------------------------------------
scipy.stats.norm.cdf   → Normal CDF
scipy.stats.t.cdf       → t distribution CDF

pdf: probability density function  
cdf: cumulative distribution function  
ppf: inverse CDF (“percent point function”) used to find critical values.


---------------------------------------------------------
9. Summary of What Each Question Demonstrates
---------------------------------------------------------
Q1 — One-sample Z-test (large n)  
Q2 — One-sample t-test + upper confidence bound  
Q3 — Two-sample Z-test (large samples, independent groups)  
Q4 — Two-sample t-test (small samples, independent groups)  
Q5 — Paired t-test (small sample, paired design)


---------------------------------------------------------
10. Key Vocabulary
---------------------------------------------------------
- **Null hypothesis (H0):** Default assumption, “no difference.”
- **Alternative hypothesis (Ha):** Claim we seek evidence for.
- **Test statistic:** Standardized value describing how far sample result
  is from H0 prediction (z or t value).
- **p-value:** Probability of observing a result as extreme as ours if H0 is true.
- **Significance level (α):** Threshold for rejecting H0 (commonly 0.05).
- **Confidence interval:** Range of plausible values for a parameter.
- **Degrees of freedom (df):** Adjusts t-distribution based on sample size.
- **Paired data:** Data where observations are naturally linked.
- **Independent samples:** No natural pairing between groups.
- **Standard error (SE):** Estimated standard deviation of a statistic.


==============================================================
END OF SUMMARY
==============================================================
"""
