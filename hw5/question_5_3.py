import numpy as np

m1 = 5
m2 = 3
m3 = 2

g = 9.81 

k1 = 100
k2 = 150
k3 = 100

K = np.array([[k1+k2, -k2,   0.0],
              [-k2,   k2+k3, -k3],
              [0.0,   -k3,    k3]])

f = np.array([m1*g, m2*g, m3*g])

x = np.linalg.solve(K, f)

print("x1: ", x[0])
print("x2: ", x[1])
print("x3: ", x[2])