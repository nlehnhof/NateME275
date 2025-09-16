import matplotlib.pyplot as plt
import numpy as np

n = np.logspace(1, 6, num=6, base=10, dtype=int)

'''
The Function we want to evaluate.
'''
def f(n):
    s= 0.0
    for i in range(n):
        s += 0.1
    return abs(n/10 -s)

# error = [f(each) for each in n]
error = []
for i in n:
    error.append(f(i))

plt.figure()
plt.loglog(n, error, marker='o')
plt.xlabel("n (number of terms)")
plt.ylabel("Absolute Roundoff Error")
plt.title("Roundoff Error as we Sum 0.1")
plt.show()