######### PROBLEM 1 #############################3

import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt
import statistics as stats

def system(t, states, b):
    m = 20
    k = 20
    x, dx = states
    x1 = dx
    x2 = (-b * dx - k * x) / m
    return [x1, x2]

y0 = [1, 0]
t0 = 0
tf = 15
t_eval = np.linspace(t0, tf, 200)
b = [5, 40, 200]

plt.figure()

for i in b:
    sol = sc.solve_ivp(system, (t0, tf), y0, t_eval = t_eval, args = (i,))
    plt.plot(sol.t, sol.y[0], label = f'Damping Coefficient of {i}')

plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Mass-Spring-Damper Response for Different Damping")
plt.legend()
plt.grid(False)
plt.show()

####### PROBLEM 2 ###############################3

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

######### PROBLEM 3 ######################################33

import numpy as np
from statistics import mean, stdev

# Values and frequencies
occupants = [1, 2, 3, 4, 5]
cars = [70, 15, 10, 3, 2]

# Expand the dataset
data = []
for x, f in zip(occupants, cars):
    data.extend([x] * f)

# a) Sample mean
mean_value = mean(data)

# b) Sample standard deviation
std_value = stdev(data)

# c) Median
median_value = np.median(data)

# d) Quartiles
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

# e) Proportion above mean
count_above_mean = sum(1 for x in data if x > mean_value)
prop_above_mean = count_above_mean / len(data)

print("Mean:", mean_value)
print("Standard Deviation:", std_value)
print("Median:", median_value)
print("Q1:", Q1)
print("Q3:", Q3)
print("Proportion above mean:", prop_above_mean)
