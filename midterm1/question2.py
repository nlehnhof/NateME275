import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc

def m(x):
    return x - 0.4 * np.sin(x) - np.pi / 2

def dm(x):
    return 1 -0.4 * np.cos(x)

# def m(x):
#     return x**3 - x

# def dm(x):
#     return 3*x**2 - 1

x = np.linspace(-10.0, 10.0, 1000)

sol = sc.root_scalar(m, bracket=[-3.0, 3.0], method = 'bisect')
print(sol.root)

def newtons(f, df, x0, max_iter=2, tol=1e-6):
    x = x0
    for i in range(1, max_iter+1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return x, False, i
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new, True, i
        x = x_new
    return x, False, max_iter
    
root, converged, iter = newtons(m, dm, x0=1.0)
print("Root = ", root)
print("Converged = ", converged)
print("Iterations = ", iter)

error = 100 * ((root - 1.9433558226260175) / 1.9433558226260175)
print("Relative Error: ", error)

# number = 1 * 2 **3 + 1 * 2 **2 + 1 * 2 **1 + 0 * 2**0 + 1 * 2**-1 + 1 * 2**-2
# print(number)
