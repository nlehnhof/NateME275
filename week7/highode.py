import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt

# Pendulum
# Sum M = -mg sin(theta) L
#       = I alpha = I ddw
# I = mL**2

def system(t, y):
    g = 9.81
    L = 5
    theta = 30
    theta, w = y
    dww = -g * np.sin(np.deg2rad(theta)) / L
    dtheta = w
    return [dtheta, dww]
    
t0 = 0
tf = 100
t = np.linspace(t0, tf, 100)
y0 = [10, 0]

sol = itg.solve_ivp(system, (t0, tf), y0, t_eval = t)

dx1 = sol.y[0, :]
dx2 = sol.y[1, :]

plt.figure()
plt.plot(sol.t, dx1, label='theta')
plt.plot(sol.t, dx2, label='omega')
plt.xlabel('t')
plt.title('Pendulum')
plt.show()
