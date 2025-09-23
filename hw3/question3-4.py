import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

file = "hw3/accel.dat"

data = np.loadtxt(file)
t = data[:, 0]
a = data[:, 1]

vel = integrate.cumulative_trapezoid(a, t, initial = 0)

# def v(t, a):
#     v = []
#     for i in np.arange(len(t)):
#         v.append(integrate.trapezoid(a[:i+1], t[:i+1]))
#     return v

# vel = v(t, a)

# Plot results in two stacked subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8,6))
ax1.plot(t, a)
ax1.set_ylabel("Acceleration (m/s²)")
ax1.legend()

ax2.plot(t, vel)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Velocity (m/s)")
ax2.legend()

plt.suptitle("Acceleration and Velocity vs Time")
plt.tight_layout()
plt.show()