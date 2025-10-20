import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

######## QUESTION 1 ############

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

h_values = [0.5, 0.1, 0.01]

# euler_sol = [euler(df, y0, h, t0, tf) for h in h_values]
euler_sol = euler(df, y0, h_values[2], steps=200, t0=t0)

sol_default = sc.solve_ivp(df, [t0, tf], [y0])

t_eval = np.linspace(t0, tf, 200)
sol_smooth = sc.solve_ivp(df, [t0, tf], [y0], t_eval=t_eval)

plt.figure()
# RK45 default
plt.plot(sol_default.t, sol_default.y[0], 'k--', label='RK45 (default)')
# RK45 smooth
plt.plot(sol_smooth.t, sol_smooth.y[0], 'r', linewidth=2, label='RK45 (smooth)')
# plt.plot(euler_sol[0], euler_sol[1], '--', label='My euler')
# Graph styling
plt.title("Comparison of Default RK45 and Smotth RK45")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
# plt.grid(True)
plt.show()

######### QUESTION 2 ############

def system(t, states):
    mu = 2
    x, dx = states
    dx2 = mu * (1 - x**2) * dx - x 
    dx1 = dx
    return [dx1, dx2]

t0 = 0
tf = 10
t = np.linspace(t0, tf, 100)
y0 = [1, 2]

sol = sc.solve_ivp(system, (t0, tf), y0, t_eval = t)

plt.figure()
plt.plot(sol.t, sol.y[0], label='x')
plt.plot(sol.t, sol.y[1], label='dx')
plt.legend()
plt.show()

########### QUESTION 3 #############

def system(t, states):
    m = 0.0027 # kg 
    f = 0.0007 # kg/m
    b = 0.01 # kg/s
    k = 200 # N/m
    g = 9.81 # m/s**2    
    x, y, dx, dy = states
    dx1 = dx
    dy1 = dy

    if y <= 0:
        dxx = (-f * dx * np.sqrt(dx**2 + dy**2)) / m
        dyy = (-f * dy * np.sqrt(dx**2 + dy**2) - m * g - b * dy - k * y) / m
    else:
        dxx = (1/m) * (-f * dx * np.sqrt(dx**2 + dy**2))
        dyy = (1/m) * (-f * dy * np.sqrt(dx**2 + dy**2) - m * g)
    return [dx1, dy1, dxx, dyy]

y0 = [0.0, 0.2, 1.0, 0.4]

t0, tf = 0, 2
t_eval = np.linspace(t0, tf, 1000)

sol = sc.solve_ivp(system, (t0, tf), y0, t_eval = t_eval)

plt.figure()
plt.plot(sol.y[0], sol.y[1], label="Ping Pong Ball Position")
plt.xlim(0.0, 1.0)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.legend()
plt.title("2D Motion with Drag and Ground Contact")
plt.show()