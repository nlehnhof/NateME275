import numpy as np
from scipy import integrate

x = np.linspace(0, np.pi, num=50)
x2 = np.arange(0, np.pi)
y = np.sin(x**2)

# print(integrate.trapezoid(y, x))
# print(integrate.simpson(y, x=x))
# print(integrate.quad(lambda x: np.sin(x**2), 0, np.pi)[0])
