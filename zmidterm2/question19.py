import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

"""
In a certain type of automobile engine, 
the cylinder head is fastened to the block by 10 bolts, 
each of which should be torqued to 60 Nm. 
Assume that the torques of the bolts are independent. 

If each bolt is torqued correctly with probability 0.99, 
what is the probability that all the bolts on a 
cylinder head are torqued correctly? 

Report to at least 3 decimal places 
(probability in fractional form).
"""

n = 10
pcorrect = 0.99
p_all_correct = sc.binom.pmf(n, n, pcorrect)
print(f"Probability that all bolts are torqued correctly: {p_all_correct:.3f}")
# Output: Probability that all bolts are torqued correctly: 0.904
# The probability that all 10 bolts are torqued correctly is approximately 0.904
p_one_incorrect = 1 - (pcorrect**n)
print(f"Probability that at least one bolt is torqued incorrectly: {p_one_incorrect:.3f}")
# Output: Probability that at least one bolt is torqued incorrectly: 0.096

