import numpy as np
import matplotlib as pyplot
from scipy import optimize

# tan(theta) = \frac{2}{tan(\beta)} * (M**2 * sin(\beta)**2 - 1)/(M**2 * [1.4 + cos(2\beta)] + 2)))

# \beta_min = inverse_sin(1/M)
# \beta_max = 64^circ

# If theta = 15 degrees and M = 2, find \beta using scipy.root_scalar

M = 2
theta = np.deg2rad(15)

def f(beta):
    return 2 * (M**2 * np.sin(beta)**2 -1) / (M**2 * (1.4 + np.cos(2 * beta)) + 2 * np.tan(beta)) - np.tan(theta)

min = np.arcsin(1/M)
max = np.deg2rad(64)

sol = optimize.root_scalar(f, bracket=[min, max])

print("beta(rad) = ", sol.root)
print("beta(deg) = ", np.rad2deg(sol.root))
print(sol.converged)

# beta(rad) =  0.7894140910022259
# beta(deg) =  45.23009570258384
# True