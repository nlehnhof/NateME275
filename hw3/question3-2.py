import numpy as np

def f(x):
    return x**3 - 3*x**2 + x -1

def df(x):
    return 3*x**2 - 6*x + 1

def newtons(f, df, x0, max_iter=100, tol=1e-6):
    x = x0
    for i in range(1, max_iter+1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return x, False, i
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new, True, i
        x = x_new
    return x, False, max_iter
    
root, converged, iter = newtons(f, df, x0=100.0)
print("Root = ", root)
print("Converged = ", converged)
print("Iterations = ", iter)

# Root =  2.7692923542386314
# Converged =  True
# Iterations =  15