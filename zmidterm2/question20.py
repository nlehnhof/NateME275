import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

"""
A system consists of four components connected as shown below.  
Assume each component functions independently 
and that the probabilities of failure are 
0.05 for A, 0.03 for B, 0.07 for C, and 0.14 for D.  

Find the probability that the system functions.  

Report to at least 3 decimal places 
(probability in fractional form)
"""

# Since we know the probabilities of failure for each component,
# we can calculate the probability that the system functions.
# Prob that A fails = 0.05
# Prob that B fails = 0.03
# Prob that C fails = 0.07
# Prob that D fails = 0.14

# For success of the system, we need both A and B to work,
# and at least one of C or D to work.

# So we can calculate the probability that A and B both work,
# and the probability that C or D works.

probAandBwork = (1 - 0.05) * (1 - 0.03)
probCorDwork = ((1-0.07) + (1-0.14) - (1-0.07) * (1-0.14))
probsuccess = probAandBwork * probCorDwork
print(f"P(system functions) = {probsuccess:.3f}")
# 0.912