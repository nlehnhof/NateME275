import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

# In a sample of 20 men the mean height was 178 cm.  
# In a sample of 30 women the mean height was 164 cm.  
# What was the mean height for both groups put together (in cm).

mean = (20 * 178 + 30 *164) / 50
# print(mean)
# 169.6 cm

# If P(A) = 0.5 and P(A and ~B) = 0.4, 
# for what value of P(B) will A and B be independent?
# ~B means not B

# If A and B are independent, then P(A and B) = P(A) * P(B)
Pa = 0.5
PAnotB = 0.4
PnotB = PAnotB / Pa
# print(PnotB)
# 0.8
PB = 1- PnotB
# print(PB)
#  0.2

# A    ~A
# 0.1  0.1    B
# 0.4  0.4   ~B