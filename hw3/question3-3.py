import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def integrand(x):
    return 4 * np.sqrt(1 - 4*x**2)

min = -0.5
max = 0.5

# x2 = np.arange(-0.5, 0.5, 50)

N = np.arange(20, 400, 10)

def f(N):
    y = []
    for n in N:
        x = np.linspace(-0.5, 0.5, num=n)
        y.append(integrate.trapezoid(integrand(x), x))
    return y

def g(N):
    y = []
    for n in N:
        val, _ = integrate.quad(integrand, -0.5, 0.5)
        y.append(val)
    return y

sol = f(N)
sol2 = g(N)

plt.figure()
plt.plot(N, sol, marker="o", linestyle='-', label = "Trapezoid")
plt.plot(N, sol2, linestyle="--", label = "Quad")
plt.legend(loc="lower right")
plt.xlabel("Number of Discretization Points")
plt.ylabel("Integral Solution")
plt.title("Discretization Points Demonstrating Convergence for Integral")
plt.show()

# sol_trap = integrate.trapezoid(integrand(x), x)
# sol_quad = integrate.quad(lambda x: 4 * np.sqrt(1 - 4*x**2), -0.5, 0.5)[0]
# print(sol_trap)
# print(sol_quad)