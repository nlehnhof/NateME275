import numpy as np
import matplotlib.pyplot as plt

x = [-1 , 0, 1.5, 3]
y = [3, 1, 3, 8]

# fit y= a*x**2 + b*x + c

A = np.vstack([np.array(x)**2, np.array(x), np.ones(len(x))]).T
b = np.array(y)
coeffs, residuals, rank, s = np.linalg.lstsq(A, b)
a, b, c = coeffs
print(f"a={a}, b={b}, c={c}")

z = np.arange(-1, 3, 0.01)

plt.figure()
plt.plot(x, y, 'o', label='data points')
plt.plot(z, a*z**2 + b*z + c, 'r-', label='fitted curve')
plt.legend()
plt.show()
