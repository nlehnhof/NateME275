import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt
import statistics as stats


def system(t, states, i, r):
    rho = 0.03
    S, I, R = states
    dSdt = -i * S * I + rho * R
    dIdt = i * S * I - r * I
    dRdt = r * I - rho * R
    return [dSdt, dIdt, dRdt]

# Parameters
i = 0.002 / 7
r = 0.15

# Initial Conditions
S0 = 10000
I0 = 1
R0 = 0
state0 = [S0, I0, R0]

# Time span
t0 = 0
tf = 80  # long enough for I to reach 10
t_eval = np.linspace(t0, tf, 500)

# Solve
sol = sc.solve_ivp(system, (t0, tf), state0, t_eval=t_eval, args=(i, r))

S = sol.y[0]
I = sol.y[1]
R = sol.y[2]

# Find when I reaches 10
# idx_reach_10 = np.argmax(I >= 10)  # first index where I >= 10
# t_limit = sol.t[idx_reach_10]

# Trim data up to that moment
# S1 = S[:idx_reach_10]
# I1 = I[:idx_reach_10]
# R1 = R[:idx_reach_10]
# t1 = sol.t[:idx_reach_10]

# Plot
plt.figure()
plt.plot(sol.t, S, label="Susceptible (S)")
plt.plot(sol.t, I, label="Infected (I)")
plt.plot(sol.t, R, label="Recovered (R)")
plt.xlabel("Time (days)")
plt.ylabel("Population (log scale)")
# plt.yscale("log")
plt.title("Epidemic Progression with Reinfection")
plt.grid(True)
plt.legend()
plt.show()