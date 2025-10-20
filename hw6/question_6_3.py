import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

def system(t, states):
    m = 0.0027 # kg 
    f = 0.0007 # kg/m
    b = 0.01 # kg/s
    k = 200 # N/m
    g = 9.81 # m/s**2    
    x, y, dx, dy = states
    dx1 = dx
    dy1 = dy

    if y <= 0:
        dxx = (-f * dx * np.sqrt(dx**2 + dy**2)) / m
        dyy = (-f * dy * np.sqrt(dx**2 + dy**2) - m * g - b * dy - k * y) / m
    else:
        dxx = (1/m) * (-f * dx * np.sqrt(dx**2 + dy**2))
        dyy = (1/m) * (-f * dy * np.sqrt(dx**2 + dy**2) - m * g)
    return [dx1, dy1, dxx, dyy]

y0 = [0.0, 0.2, 1.0, 0.4]

t0, tf = 0, 2
t_eval = np.linspace(t0, tf, 1000)

sol = sc.solve_ivp(system, (t0, tf), y0, t_eval = t_eval)

plt.figure()
plt.plot(sol.y[0], sol.y[1], label="Ping Pong Ball Position")
plt.xlim(0.0, 1.0)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.legend()
plt.title("2D Motion with Drag and Ground Contact")
plt.show()