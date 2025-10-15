import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def system(t, y):
    g = 9.81
    m = 80
    k = 10
    c = 20
    x, x1 = y
    dx1 = x1
    dx2 = (m*g - k*x - c*x1) / m
    return [dx1, dx2]

t0 = 0
tf = 20
t = np.linspace(t0, tf, 1000)
y0 = [0, 20]

sol = solve_ivp(system, (t0, tf), y0, t_eval = t)

dx1 = sol.y[0, :]
dx2 = sol.y[1, :]

plt.figure()
plt.plot(sol.t, dx1, label='dx1')
plt.plot(sol.t, dx2, label='dx2')
plt.xlabel('t')
plt.ylabel('h')
plt.show()
