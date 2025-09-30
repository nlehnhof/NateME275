import numpy as np
import scipy
from scipy.optimize import fsolve

def y_goat(x, r=1):
    return np.sqrt(r**2 - x**2)

def y_pen(x):
    return -1 * (np.sqrt(1 - (x - 1)**2) + 1)

def point(r=1):
    return np.sqrt(r**2 - (r)**4 / 4)

def goat_area(r=1):
    def integrand(x):
        return y_goat(x, r) - y_pen(x)

    x0 = point(r)
    area_value, _ = scipy.integrate.quad(integrand, 0, x0)
    return area_value

# Target: half of pen area (pen radius = 1)
target_area = 0.5 * np.pi

# Function to find root: area(r) - target_area = 0
def area_difference(r):
    return goat_area(r) - target_area

# Solve for r
r_solution = fsolve(area_difference, 1.0)[0]
print(f"Goat rope length r for half the pen area: {r_solution:.4f}")

# Optional: check the area
print(f"Corresponding area: {goat_area(r_solution):.4f}")