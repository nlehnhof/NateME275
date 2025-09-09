### COMPLETE ###

import numpy as np
import matplotlib.pyplot as plt

h = [[0, 11], [11, 20], [20, 32], [32, 47]]

h1 = np.linspace(0, 11, 100)
h2 = np.linspace(11, 20, 100)
h3 = np.linspace(20, 32, 100)
h4 = np.linspace(32, 47, 100)

T1 = 288.15 - 6.5*h1
T2 = np.ones(100) * 216.65
T3 = 216.65 + (h3 - 20)
T4 = 228.65 + 2.8 * (h4 - 32)

plt.figure()
plt.plot(T1, h1)
plt.plot(T2, h2)
plt.plot(T3, h3)
plt.plot(T4, h4)
plt.xlabel("Temperature (K)")
plt.ylabel("Altitude (km)")
plt.title("Temperature (K) as a function of Altitude (km)")
plt.legend(["0 - 11 km", "11 - 20 km", "20 - 32 km", "32 - 47 km"], loc="center right")
plt.show()