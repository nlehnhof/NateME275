import numpy as np

## Average function for np.array(x)

array = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
w = np.array([1.0, 1.0, 1.0, 1.0, 5.0])

# a
def avg(x):
    l = len(x)
    total = np.sum(x)
    avg = total/l
    return avg

# b
def mavg(x, c = 1):
    mavg = avg(x) * c
    return mavg

# c
def wavg(x, w):
    wavg = np.sum(x * w) / np.sum(w)
    return wavg

# d
def tavg(filename):
    data = np.loadtxt(filename)
    n_rows = data.shape[0]
    sumcols = np.sum(data, axis=0)
    avgcolumns = sumcols / n_rows
    return avgcolumns

# e
def favg(x, f):
    avgf = np.sum(f(x))/len(x)
    return avgf


