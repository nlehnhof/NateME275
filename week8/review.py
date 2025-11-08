import numpy as np
from scipy.integrate import solve_ivp

# def func(t, states):
#     x, y = states
#     dydt = -x
#     dxdt = y
#     return [dxdt, dydt]

# y0 = [1, 0]
# t0 = 0.0
# tf = 3.0

# t_eval = np.linspace(t0, tf, 100)

# sol = solve_ivp(func, (t0, tf), y0, t_eval=t_eval)

# import matplotlib.pyplot as plt

# plt.figure()
# plt.plot(sol.t, sol.y[0, :], label='x(t)')
# plt.plot(sol.t, sol.y[1, :], label='y(t)')
# plt.legend()
# plt.show()

# dyy = -2 * dy - 5 * y
# x1 = y
# x2 = dy

# def func(t, states):
#     x1, x2 = states
#     dy = x2
#     dyy = -2 * x2 - 5 * x1
#     return [dy, dyy]

# y0 = [1, 0]
# t0 = 0.0
# tf = 10
# t_eval = np.linspace(t0, tf, 300)
# sol = solve_ivp(func, (t0, tf), y0, t_eval=t_eval)

# def func(t, states):
#     x1, x2, x1p, x2p = states
#     dx = x1p
#     dx2 = x2p
#     dxx1 = -2 * (x1 - x2)
#     dxx2 = 2 * (x1 - x2)
#     return [dx, dx2, dxx1, dxx2]

# y0 = [1, 0, 0, 0]
# t0 = 0.0
# tf = 4.0
# t_eval = np.linspace(t0, tf, 100)
# sol = solve_ivp(func, (t0, tf), y0, t_eval=t_eval)

# import matplotlib.pyplot as plt

# plt.figure()
# plt.plot(sol.t, sol.y[0, :], label='x1(t)')
# plt.plot(sol.t, sol.y[1, :], label='x2(t)')
# plt.legend()
# plt.show()

hours = [2, 4, 6, 8, 10]
score = [65, 70, 75, 85, 95]

x = hours; y = score

A = np.column_stack((x, np.ones_like(x)))
coeff = np.linalg.lstsq(A, y)[0]
print(coeff)