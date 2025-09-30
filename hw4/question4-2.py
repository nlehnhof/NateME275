import numpy as np

def f(x):
    return np.exp(x) * np.sin(x)

def df(x):
    return np.exp(x) * (np.sin(x) + np.cos(x))

x0 = 1.5

h_values = [1e-1, 1e-6, 1e-11, 1e-17]

for h in h_values:
    forward_diff = (f(x0 + h) - f(x0)) / h
    exact = df(x0)
    percent_error = abs((forward_diff - exact) / exact) * 100
    print(f"h: {h:.1e}, Forward Diff: {forward_diff:.6f}, Exact: {exact:.6f}, Percent Error: {percent_error:.6f}%")