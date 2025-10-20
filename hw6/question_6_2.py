import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

def system(t, states):
    mu = 2
    x, dx = states
    dx2 = mu * (1 - x**2) * dx - x 
    dx1 = dx
    return [dx1, dx2]

t0 = 0
tf = 10
t = np.linspace(t0, tf, 100)
y0 = [1, 2]

sol = sc.solve_ivp(system, (t0, tf), y0, t_eval = t)

plt.figure()
# plt.plot(sol.y[0], sol.y[1])
plt.plot(sol.t, sol.y[0], label='x')
plt.plot(sol.t, sol.y[1], label='dx')
plt.xlabel("Time (s)")
plt.ylabel("Displacement / Velocity Amplitudes")
plt.title("Van der Pol Oscillator: Position and Velocity vs. Time")
plt.legend()
plt.show()