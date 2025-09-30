import numpy as np

def f(x):
    return np.exp(x) * np.sin(x)

def df(x):
    return np.exp(x) * (np.sin(x) + np.cos(x))

def trapz(f, x0, x1, n):
    x = np.linspace(x0, x1, n+1)
    y = f(x)
    h = (x1 - x0) / n
    integral = (h/2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

area = trapz(f, 0, 1, 19)

exact_area = 0.5 * (np.exp(1) * (np.sin(1) - np.cos(1)) + 1)
print(f"Exact area: {exact_area:.8f}")

print(area)