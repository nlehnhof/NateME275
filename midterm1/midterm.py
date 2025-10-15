import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc

# def m(x):
#     return x - 0.4 * np.sin(x) - np.pi / 2

# def dm(x):
#     return 1 -0.4 * np.cos(x)

def m(x):
    return x**3 - x

def dm(x):
    return 3*x**2 - 1

x = np.linspace(-10.0, 10.0, 1000)

sol = sc.root_scalar(m, bracket=[-3.0, -0.5], method = 'bisect')
print(sol.root)

# def newtons(f, df, x0, max_iter=2, tol=1e-6):
#     x = x0
#     for i in range(1, max_iter+1):
#         fx = f(x)
#         dfx = df(x)
#         if dfx == 0:
#             return x, False, i
#         x_new = x - fx/dfx
#         if abs(x_new - x) < tol:
#             return x_new, True, i
#         x = x_new
#     return x, False, max_iter
    
# root, converged, iter = newtons(m, dm, x0=1.0)
# print("Root = ", root)
# print("Converged = ", converged)
# print("Iterations = ", iter)

# error = 100 * ((root - 1.9433558226260175) / 1.9433558226260175)
# print("Relative Error: ", error)

# number = 1 * 2 **3 + 1 * 2 **2 + 1 * 2 **1 + 0 * 2**0 + 1 * 2**-1 + 1 * 2**-2
# print(number)

def f(x):
    return 5 * np.exp(-0.5 * x) * np.cos(2*x)

x = np.linspace(-2, 1, 50)

sol = sc.trapezoid(f(x), x)
gaus = sc.quad(f, -2, 1)

print(sol)
print(gaus[0])

error = abs(sol - gaus[0])
print(error)

# def sqrt_iterate(y0, x, tol=1e-6):
#     y0 = y0
#     while abs(x - y0**2) > tol:
#         y0 = 0.5 * (y0 + x / y0)
#     return y0

# y = sqrt_iterate(12, 9)

# print(y)

A = np.array([
    [1, 2, 3],
    [3, 3, 3],
    [4, 5, 1],
])

B = np.array([
    [2, 2, 2],
    [5, 4, 3],
    [2, 2, 23],
])

a = A*B
b = B*A

print(a)
print(B)

def f(x):
    return np.sin(x**2)

x = np.linspace(0, 2*np.pi, 200)

def integral(f, x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        sol = sc.cumulative_trapezoid(f, 0, x[i])
        y[i] = sol[0]
    return y

# y = np.sin(x**2)
# F = sc.cumulative_trapezoid(y, x, initial=0)

y = integral(f, x)

plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Integral of f(x)')
plt.title('Cumulative Integral of sin(x^2)')
plt.show()

# T = [10, -2, -15, -30]
# t = [0, 1.2, 4.8, 7.9]

# f1_t1 = (-15 - 10) / (4.8 - 0)
# print(f1_t1)

# plt.figure()
# plt.plot(t, T)
# plt.show()

def f(x):
    return x**2 * np.sin(x) + np.log(x)

def forward(f, xj, step=1e-6):
    return (f(xj+step) - f(xj)) / (xj+step - xj)

def central(f, xj, step=1e-4):
    return (f(xj+step)-f(xj-step)) / (xj+step - (xj-step))

# x = np.linspace(0.0, 2.5, (2.5/1e-6))

fwd = forward(f, 2)
ctr = central(f, 2)

error = 100 * (ctr - fwd) / fwd

print(fwd)
print(ctr)
print(error)

# def m(x):
#     return x - 0.4 * np.sin(x) - np.pi / 2

# def dm(x):
#     return 1 -0.4 * np.cos(x)

def m(x):
    return x**3 - x

def dm(x):
    return 3*x**2 - 1

x = np.linspace(-10.0, 10.0, 1000)

sol = sc.root_scalar(m, bracket=[-3.0, -0.5], method = 'bisect')
print(sol.root)

# def newtons(f, df, x0, max_iter=2, tol=1e-6):
#     x = x0
#     for i in range(1, max_iter+1):
#         fx = f(x)
#         dfx = df(x)
#         if dfx == 0:
#             return x, False, i
#         x_new = x - fx/dfx
#         if abs(x_new - x) < tol:
#             return x_new, True, i
#         x = x_new
#     return x, False, max_iter
    
# root, converged, iter = newtons(m, dm, x0=1.0)
# print("Root = ", root)
# print("Converged = ", converged)
# print("Iterations = ", iter)

# error = 100 * ((root - 1.9433558226260175) / 1.9433558226260175)
# print("Relative Error: ", error)

# number = 1 * 2 **3 + 1 * 2 **2 + 1 * 2 **1 + 0 * 2**0 + 1 * 2**-1 + 1 * 2**-2
# print(number)

R1 = R2 = R3 = 1
R4 = R5 = 2

Vs = 15

A = np.array([
    [R2+R4, -R2, -R4],
    [-R2, R1+R2+R3, -R3],
    [-R4, -R3, R3+R4+R5],
])

b = np.array([15, 0, 0])

x = np.linalg.solve(A, b)

print(x)

A = np.array([
    [0, 3, 0, 6],
    [1, 0, 2, 0],
    [0, 5, 5, 0],
    [0, 0, 7, 1],
])

b = np.array([18, -5, -25, -17], dtype=float)

x = np.linalg.solve(A, b)

# print(x[1])

c = A @ x

print(c)

xvec = np.array([0.0, 0.06411414, 0.12822827, 0.19234241, 0.25645654, 0.32057068, 0.38468481, 0.44879895, 0.51291309, 0.57702722, 0.64114136, 0.70525549, 0.76936963, 0.83348377, 0.8975979, 0.96171204, 1.02582617, 1.08994031, 1.15405444, 1.21816858, 1.28228272, 1.34639685, 1.41051099, 1.47462512, 1.53873926, 1.60285339, 1.66696753, 1.73108167, 1.7951958, 1.85930994, 1.92342407, 1.98753821, 2.05165235, 2.11576648, 2.17988062, 2.24399475, 2.30810889, 2.37222302, 2.43633716, 2.5004513, 2.56456543, 2.62867957, 2.6927937, 2.75690784, 2.82102197, 2.88513611, 2.94925025, 3.01336438, 3.07747852, 3.14159265])
yvec = np.array([-1.33420675, -1.10031441, -1.70601521, -0.44700296, 0.30883201, 0.01610921, 0.81291503, 0.95636478, 1.03921739, 0.99634815, 1.26036554, 1.52465377, 0.24763214, 0.99063965, 0.29047526, 0.067633, -1.06786088, -0.77228815, -0.41577237, -1.97700207, -2.65033565, -2.68936338, -1.76184177, -0.69284902, -1.22291395, -0.75623781, -1.26228219, -0.25055401, -0.65165001, 0.28173528, 0.37392696, 0.78813861, 1.68701433, 1.92216713, 3.314706, 3.19845057, 3.66274494, 3.55980745, 4.51291657, 3.55387125, 4.1570019, 3.42706402, 2.77786829, 2.52253828, 1.76818801, 1.36396786, 0.51341986, -0.01626634, -0.79174608, -2.07371013])

# y = a sin(x) + b sin(2x) + c sin(3x) + d
A = np.vstack([np.array(np.sin(xvec)), np.array(np.sin(2*xvec)), np.array(np.sin(3*xvec)), np.ones(len(xvec))]).T
b = np.array(yvec)

coeffs, residuals, rank, s = np.linalg.lstsq(A, b)
a, b, c, d = coeffs
print(f"a={a}, b={b}, c={c}, d={d}")

z = np.arange(0.0, np.pi, 0.001)

plt.figure()
plt.plot(xvec, yvec, 'o', label='data points')
plt.plot(z, a*np.sin(z) + b*np.sin(2*z) + c * np.sin(3*z) + d, 'r-', label='fitted curve')
plt.legend()
plt.show()