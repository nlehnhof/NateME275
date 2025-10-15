import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

# T = [10, -2, -15, -30]
# t = [0, 1.2, 4.8, 7.9]

# f1_t1 = (-15 - 10) / (4.8 - 0)
# print(f1_t1)

# plt.figure()
# plt.plot(t, T)
# plt.show()

def f(x):
    return x**2 * np.sin(x) + np.log(x)

def forward(f, xj, step=1e-6):
    return (f(xj+step) - f(xj)) / (xj+step - xj)

def central(f, xj, step=1e-4):
    return (f(xj+step)-f(xj-step)) / (xj+step - (xj-step))

# x = np.linspace(0.0, 2.5, (2.5/1e-6))

fwd = forward(f, 2)
ctr = central(f, 2)

error = 100 * (ctr - fwd) / fwd

print(fwd)
print(ctr)
print(error)