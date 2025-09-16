import matplotlib.pyplot as plt
import numpy as np
import math

k = np.arange(0, 21, 1)

def Leibniz(k):
    s = 0.0
    for i in range(k):
        s += (-1)**i / (2 * i + 1)
    return 4 * s

error = []
for i in k:
    error.append(abs((Leibniz(i) - math.pi) / math.pi) * 100)

plt.figure()
plt.plot(k, error, marker="o")
plt.xlabel("Number of Terms")
plt.xticks(range(0, 21, 2))
plt.ylabel("Relative Percent Error (%)")
plt.title("Relative Percent Error of Leibniz Formula for $\pi$")
plt.show()