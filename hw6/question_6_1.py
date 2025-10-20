import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

# S(t_j+1) = S(tj) + h(dS(tj)/dt)
def euler(df, S0, h, steps, t0=0):
    S = [S0]
    t = [t0]

    for i in range(steps):
        tj = t[-1]
        Sj = S[-1]
        S2 = Sj + h * df(tj, Sj)
        tj += h
        S.append(S2)
        t.append(tj)
    return t, S 

def df(t, y):
    return y* t**2 - 1.1*y

y0 = 1
t0 = 0
tf = 2

h_values = [0.5, 0.1, 0.01]

# euler_sol = [euler(df, y0, h, t0, tf) for h in h_values]
euler_sol = euler(df, y0, h_values[2], steps=200, t0=t0)

sol_default = sc.solve_ivp(df, [t0, tf], [y0])

t_eval = np.linspace(t0, tf, 200)
sol_smooth = sc.solve_ivp(df, [t0, tf], [y0], t_eval=t_eval)

plt.figure()
# Euler plots
# for (t, y), h in zip(euler_sol, h_values):
    # plt.plot(t, y, marker='o', label=f"Euler h={h}")

# RK45 default
plt.plot(sol_default.t, sol_default.y[0], 'k--', label='RK45 (default)')

# RK45 smooth
plt.plot(sol_smooth.t, sol_smooth.y[0], 'r', linewidth=2, label='RK45 (smooth)')
# plt.plot(euler_sol[0], euler_sol[1], '--', label='My euler')
# Graph styling
plt.title("Comparison of Default RK45 and Smotth RK45")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
# plt.grid(True)
plt.show()