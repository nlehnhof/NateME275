from scipy.optimize import root_scalar

def f(x): 
    return x**3 - 1

sol = root_scalar(f, bracket=(-3, 8), method='bisect')

print(sol)