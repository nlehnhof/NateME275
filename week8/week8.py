import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

x = np.random.normal(0, 1, 100)

plt.figure()
plt.hist(x, bins=20, density=True)
plt.show()