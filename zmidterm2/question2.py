import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

t0=0
tf=2
y0=1
t_eval = np.linspace(t0, tf, 200)

def df(t, y):
    return y * t**2 - 1.1 * y

sol_smooth = sc.solve_ivp(df, (t0, tf), [y0], t_eval=t_eval)
print(f"y({tf}) = {sol_smooth.y[0][-1]:.3f}")
# y(2) = 1.594
#### DOUBLE CHECKED WITH FINER h-VALUE IN EULER ####

# plt.figure()
# plt.plot(sol_smooth.t, sol_smooth.y[0], 'r', linewidth=2, label='RK45 (smooth)')
# plt.show()