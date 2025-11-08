import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

# T varies with the distance from the exterior wall, x, according to
# k d2Tdx2 + dTdx + T = 0
# outer sheathing has a conductivity of k = 0.1
# Insulated region 0.05 <= x <- 0.2 has a k of 0.2.
# Exterior surface of the wall x=0, the temperature is T = 0, and DTdx = 100.
# What is the temperature of the interior surface of the wall (to at least 2 decimal places)?

### DEFINE THE MODEL ###
def system(x, states):
    if x >= 0.05:
        k = 0.2
    else:
        k = 0.1
    T, dT = states
    dT1 = dT
    dT2 = (-T - dT) / k
    return [dT1, dT2]

### INITIAL CONDITIONS AND PARAMETERS ###
x0 = 0
xf = 0.2
y0 = [0.0, 100.0]  # T(0) = 0, dT/dx(0) = 100
x_eval = np.linspace(x0, xf, 1000)
### SOLVE THE ODE ###
sol = sc.solve_ivp(system, (x0, xf), y0, t_eval=x_eval)
### OUTPUT THE INTERIOR SURFACE TEMPERATURE ###
interior_temp = sol.y[0][-1]
print(f"Interior surface temperature at x={xf} m: {interior_temp:.4}")

### PLOT RESULTS ###
# plt.figure()
# plt.plot(sol.t, sol.y[0], label='y(t)', color='blue')
# plt.plot(sol.t, sol.y[1], label='z(t)', color='orange')
# plt.xlabel('x')
# plt.ylim(0, 10.5)
# plt.ylabel('Temperature')
# plt.title('Solution of Coupled ODEs')
# plt.legend()
# plt.show()