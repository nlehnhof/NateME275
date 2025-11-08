import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

# dydt = -2y + 4 * exp(-t)
# dzdt = - y * z **2 / 3

# y(0) = 2
# z(0) = 4
# simulated in time from t = 0 to t = 4

### SOLVE ODEs ###
def model(t, states):
    y, z = states
    dydt = -2 * y + 4 * np.exp(-t)
    dzdt = - (y * z**2) / 3
    return [dydt, dzdt]

tspan = (0, 4)
y0 = [2, 4]
sol = sc.solve_ivp(model, tspan, y0, t_eval=np.linspace(0, 4, 100))

### PLOT RESULTS ###
plt.figure()
plt.plot(sol.t, sol.y[0], label='y(t)', color='blue')
plt.plot(sol.t, sol.y[1], label='z(t)', color='orange')
plt.xlabel('Time t')
plt.ylabel('States y and z')
plt.title('Solution of Coupled ODEs')
plt.legend()
plt.show()