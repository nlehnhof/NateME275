import numpy as np
import scipy.optimize as opt
import scipy.integrate as int
import matplotlib.pyplot as plt

# --- Given Data ---
time = np.array([0.0, 0.24489796, 0.44897959, 0.65306122, 0.85714286, 1.06122449, 1.26530612, 1.46938776, 1.67346939, 1.87755102, 2.08163265, 2.28571429, 2.48979592, 2.69387755, 2.89795918, 3.10204082, 3.30612245, 3.51020408, 3.71428571, 3.91836735, 4.12244898, 4.32653061, 4.53061224, 4.73469388, 4.93877551, 5.14285714, 5.34693878, 5.55102041, 5.75510204, 5.95918367, 6.16326531, 6.36734694, 6.57142857, 6.7755102 , 6.97959184, 7.18367347, 7.3877551 , 7.59183673, 7.79591837, 8.0])
position = np.array([0.16326531, 0.97959184, 1.79591837, 2.6122449,  3.42857143, 4.24489796, 5.06122449, 5.87755102, 6.69387755, 7.51020408, 8.32653061, 9.14285714, 9.95918367, 10.7755102, 11.59183673, 12.40816327, 13.2244898, 14.04081633, 14.85714286, 15.67346939, 16.46730529, 17.14618909, 17.70012495, 18.12911287, 18.43315285, 18.6122449, 18.666389, 18.59558517, 18.3998334, 18.07913369, 17.63348605, 17.06289046, 16.36734694, 15.54685548, 14.60141608, 13.53102874, 12.33569346, 11.01541025, 9.57017909, 8.0])

# --- Use Central Diff ---
dt = np.diff(time)

velocity = np.zeros_like(position)
velocity[1:-1] = (position[2:] - position[:-2]) / (time[2:] - time[:-2])
velocity[0] = (position[1] - position[0]) / (time[1] - time[0])
velocity[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])

# --- Plot Position and Velocity ---
plt.figure()
plt.plot(time, position, 'o-', label='Position (m)')
plt.plot(time, velocity, 'x-', label='Velocity (m/s)')
plt.xlabel('Time (s)')
plt.legend(loc='upper left')
plt.title("RC Car Position and Velocity (m/s) vs Time (s)")
plt.show()
