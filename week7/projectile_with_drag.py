import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt

#  v = sqrt(dx**2 + dy**2)

# dx2 = (-C * dx * sqrt(dx**2 + dy**2)) / m
# dy2 = (-C * dy * sqrt(dx**2 + dy**2) - mg) / m

V0=45.0
theta=np.radians(25.0)

def system(t, states):
    C = 1.0
    m = 1.0
    g = 9.81
    dx, dy, x, y = states
    dxx = (-C * dx * np.sqrt(dx**2 + dy**2)) / m
    dxdt = dx
    dyy = (-C * dy * np.sqrt(dx**2 + dy**2) - m * g) / m
    dydt = dy
    return [dxx, dyy, dx, dy]

t0 = 0
tf = 6
t = np.linspace(t0, tf, 1000)
y0 = [V0*np.cos(theta), V0*np.sin(theta), 0.0, 0.0]

sol = itg.solve_ivp(system, (t0, tf), y0, t_eval = t)

plt.figure()
plt.plot(sol.t, sol.y[0], label='dx')
plt.plot(sol.t, sol.y[1], label='dy')
plt.plot(sol.t, sol.y[2], label='x')
plt.plot(sol.t, sol.y[3], label='y')
plt.legend()
plt.show()
