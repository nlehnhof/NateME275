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

h_values = 0.001

# euler_sol = [euler(df, y0, h, t0, tf) for h in h_values]
euler_sol = euler(df, y0, h_values, steps=(int(tf//h_values + 1)), t0=t0)

# print(euler_sol)


# Define parameters
f = lambda t, s: s * t**2 - 1.1*s # ODE
# h = 0.0001 # Step size
h = 0.5
t = np.arange(0, 2 + h, h) # Numerical grid
s0 = 1 # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

print(s)

#([0, 0.5, 1.0, 1.5, 2.0], 
# [1, 0.44999999999999996, 0.2587499999999999, 
# 0.2458124999999999, 0.3871546874999998])

# sol_default = sc.solve_ivp(df, [t0, tf], [y0])
# 
# t_eval = np.linspace(t0, tf, 200)
# sol_smooth = sc.solve_ivp(df, [t0, tf], [y0], t_eval=t_eval)