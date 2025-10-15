import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Set initial conditions
# Framework is du/dt = alpha u - beta u v
# dv/dt = - gamma v + delta u v
alpha = 1
beta = 0.01
gamma = 1
delta = 0.02
t0 = 0
tf = 15
t = np.linspace(t0, tf, 100)

u_0 = 50
v_0 = 10
y0 = [u_0, v_0]

# define functions 
def system(t, y):
    alpha = 1
    beta = 0.01
    gamma = 1
    delta = 0.02
    u, v = y
    du_dt = alpha * u -beta * u * v
    dv_dt = -gamma * v+ delta * u * v
    return [du_dt, dv_dt]

solution = solve_ivp(system, (t0, tf), y0, teval=t)

# Plot
plt.figure()
plt.plot(solution.t, solution.y[0, :], label='Prey')
plt.plot(solution.t, solution.y[1, :], label='Predators')
plt.xlabel('Time (s)')
plt.ylabel('Population')
plt.legend()
plt.show()
