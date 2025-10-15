import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc

def f(x):
    return 5 * np.exp(-0.5 * x) * np.cos(2*x)

x = np.linspace(-2, 1, 50)

sol = sc.trapezoid(f(x), x)
gaus = sc.quad(f, -2, 1)

print(sol)
print(gaus[0])

error = abs(sol - gaus[0])
print(error)