import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt
import statistics as stats

def system(t, states, b):
    m = 20
    k = 20
    x, dx = states
    x1 = dx
    x2 = (-b * dx - k * x) / m
    return [x1, x2]

y0 = [1, 0]
t0 = 0
tf = 15
t_eval = np.linspace(t0, tf, 200)
b = [5, 40, 200]

plt.figure()

for i in b:
    sol = sc.solve_ivp(system, (t0, tf), y0, t_eval = t_eval, args = (i,))
    plt.plot(sol.t, sol.y[0], label = f'Damping Coefficient of {i}')

plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Mass-Spring-Damper Response for Different Damping")
plt.legend()
plt.grid(False)
plt.show()