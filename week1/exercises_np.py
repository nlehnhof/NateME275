import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# 1
# a = np.linspace(0, 3, 30)

# 2
# b = np.ones(10, dtype=np.int16) * 3

# 3
c = np.array([
    [4, 6, 6, 9],
    [7, 4, 10, 5],
    [1, 6, 4, 10]])

# 4
dim = np.shape(c)
nrows = np.shape(c)[0]
ncols = np.shape(c)[1]

# 5
e = c[2, 3]

# 6
f = c[:, 2]

# 7
g = c[2, :]

# 8
h = c * 2

# 9
i = c[c > 5]

# 10
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 11
# print(a.max())

# 12

# j = np.vstack([a, b])

# # 13
# k = j.T
# # print(k)

# # 14
# l = j[::-1]
# print(l)

print(np.average(np.square(a- b)))
