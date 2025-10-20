import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt

# J * dw + b * w - KI * i = 0
# Kb * w + L * di + R * i = vs

R, L, kb, ki, J, b = 2.0, 0.5, 0.1, 0.1, 0.01, 0.02
Vs = 12.0

# dw = (K1 * i - bw) / J
# di = (Vs - K w - Ri) / L

def dw(i, w):
    return (ki * i - b * w) / J

def di(i, w):
    return (Vs - kb * w - R * i) / L

def motor_rhs(t, x):
    i, w = x
    dw = (ki * i - b * w) / J
    di = (Vs - kb * w - R * i) / L
    return [di, dw]

t0 = 0
tf = 2
t_eval = np.linspace(t0, tf, 100)
y0 = [0, 0]

sol = itg.solve_ivp(motor_rhs, (t0, tf), y0, t_eval = t_eval)
di = sol.y[0, :]
dw = sol.y[1, :]

plt.figure()
plt.plot(sol.t, di, label='Current i(t)')
plt.plot(sol.t, dw, label='Angular velocity w(t)')
plt.xlabel('Time (s)'); plt.legend()
plt.title('DC Motor Dynamics')
plt.show()
