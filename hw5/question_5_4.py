import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sc

x = np.array([-2.0000, -1.7895, -1.5789, -1.3684, -1.1579, -0.9474, -0.7368, -0.5263, -0.3158, -0.1053, 0.1053, 0.3158, 0.5263, 0.7368, 0.9474, 1.1579, 1.3684, 1.5789, 1.7895, 2.0000])
y = np.array([7.7859, 5.9142, 5.3145, 5.4135, 1.9367, 2.1692, 0.9295, 1.8957, -0.4215, 0.8553, 1.7963, 3.0314, 4.4279, 4.1884, 4.0957, 6.5956, 8.2930, 13.9876, 13.5700, 17.7481])

M = np.column_stack((np.ones_like(x), x, x**2))

p, res, rnk, s = sc.lstsq(M, y)


# print(p[2])

plt.figure()
plt.scatter(x, y, marker='o')
xx = np.linspace(-2, 2, 101)
yy = p[0] + p[1]*xx + p[2]*xx**2
plt.plot(xx, yy, label='Least Squares Fit, $y = a + bx^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Least Squares fit for Data')
plt.grid(False)
plt.show()
