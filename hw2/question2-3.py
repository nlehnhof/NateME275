import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar

'''
Use the x and y position equations for a projectile
Solve for t and plug in to get a single equation for height
based on distance x initial velocity V.

x = lambda Sx: V * np.cos(theta) * t 
y = lambda Sy: V * np.sin(theta) * t
'''
def Sy(theta, x, V=100, g=9.81): 
    y = V * np.sin(theta) * (x / (V * np.cos(theta))) - 0.5 * g * (x / (V * np.cos(theta)))**2
    return y

'''
Bisection, root-finding function:

a : left endpoint
b : right endpoint
f : function to evaluate

on [a, b], finds root where f(c) = 0,
returns c.
'''
def bisect(a, b, f, tol=1e-6, max_iter=100):
    fa, fb = f(a), f(b)
    eval = fa * fb
    if (eval > 0):
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(max_iter):
        # compute midpoint
        c = (a + b) / 2
        fc = f(c)
        if (abs(fc) < tol or (b-a) / 2 < tol):
            return c
        elif fa * fc < 0:
            b = c
        else:
            a = c

# Target position
x_target = 400
y_target = 50

# My function (calculated height - target height)
f = lambda theta: Sy(theta, x_target) - y_target

# scipy function for confirmation
low = root_scalar(f, bracket=[0, 0.4], method='bisect')
theta_deg_low = np.rad2deg(low.root)

high = root_scalar(f, bracket=[1.2, 1.4], method='bisect')
theta_deg_high = np.rad2deg(high.root)

print(theta_deg_low)
print(theta_deg_high)

# Find the low angle
theta_low = np.rad2deg(bisect(np.deg2rad(0), np.deg2rad(45), f))
print(theta_low)
# Find the high angle
theta_high = np.rad2deg(bisect(np.deg2rad(45), np.deg2rad(90), f))
print(theta_high)

# Set up plotting 
xs = np.linspace(0, x_target, 200)
ys = [Sy(np.deg2rad(theta_low), xi) for xi in xs]
yh = [Sy(np.deg2rad(theta_high), xi) for xi in xs]

# PLOT
plt.figure()
plt.plot(xs, ys, label=f"Low Trajectory\n ({theta_low:.2f}°)")
plt.plot(xs, yh, label=f"High Trajectory\n ({theta_high:.2f}°)")
plt.plot(x_target, y_target, "ro", label="Target")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile trajectory with bisection-solved launch angle")
plt.legend(loc="upper right")
plt.show()