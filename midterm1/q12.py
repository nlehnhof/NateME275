import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc

def f(x):
    return np.sin(x**2)

x = np.linspace(0, 2*np.pi, 200)

def integral(f, x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        sol = sc.quad(f, 0, x[i])
        y[i] = sol[0]
    return y

y = integral(f, x)

plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Integral of f(x)')
plt.title('Cumulative Integral of sin(x^2)')
plt.show()

