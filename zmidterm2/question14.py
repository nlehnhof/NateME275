import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

"""
Human blood may contain neither, either, or both of two antigens,
A and B. At a certain blood bank, 40% of the blood donors have the 
A antigen (and may also have the B antigen), 15% have the B antigen 
(and may also have the A antigen), 5% have both the A and B antigens, 
and the rest have neither antigen. 

Blood that contains only the A antigen is called type A, 
blood that contains only the B antigen is called type B, 
blood that contains both antigens is called type AB, 
and blood that contains neither antigen is called type O.

Report all probabilities as fractions to at least 2 decimal places.

14.
What is the probability that a randomly chosen blood donor 
is type A, type B, or type AB?
"""
##### A     ~ A
decision_matrix = np.array([
    [0.05, 0.10],    # B
    [0.35,  0.5]     # ~ B
])

total_A = 0.35 + 0.10 + 0.05
print("total A", total_A)

notB = decision_matrix[1,0] + decision_matrix[1,1]
print("not B", notB)
notBcheck = 0.35 + 0.50
print("not B check", notBcheck)

AgivenB = decision_matrix[0,0] / (decision_matrix[0,0] + decision_matrix[0,1])
print("A given B", AgivenB)
AgivenBcheck = 0.05 / 0.15
print("A given B check", AgivenBcheck)

BgivenA = decision_matrix[0,0] / (decision_matrix[0,0] + decision_matrix[1,0])
print("B given A", BgivenA)
BgivenAcheck = 0.05 / 0.40
print("B given A check", BgivenAcheck)

