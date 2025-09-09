# Make a function polar2cart(r, theta)
# that converts from polar coordinates to Cartesian where the inputs
# r and theta are scalars and theta is in degrees

# Then create the inverse function cart2polar(x, y) (theta is in degrees)

import numpy as np

def polar2cart(r, theta):
    thetar = np.deg2rad(theta)
    print(thetar)
    xt = np.cos(thetar)
    yt = np.sin(thetar)
    x = r * xt
    y = r * yt
    return x, y

print(polar2cart(1, 30))

def cart2polar(x, y):
    thetar = np.arctan2(y, x)
    theta = np.rad2deg(thetar)
    r = np.sqrt(x**2 + y**2)
    return r, theta

print(cart2polar(0, 5))

# Now create the same two functions 
# but for numpy array inputs. 
# Let’s call them polar2cart_np(r, theta) 
# and cart2polar_np(x, y)

array = np.array([[0.0, 1.0], [1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [8.0, 0.0]])

def cart2polar_np(array):
    # Assuming array of [[x, y]...]
    x = array[:, 0]
    y = array[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.rad2deg(np.arctan2(y, x))
    return np.column_stack((r, theta))

print(cart2polar_np(array))

pol_array = np.array([[2.0, 30.0],
                      [4.0, 60.0],
                      [10.0, 90]])

def polar2cart_np(array):
    # assuming array of [[r, theta]...]
    r = array[:, 0]
    theta = array[:, 1]
    thetar = np.deg2rad(theta)
    x = np.cos(thetar) * r
    y = np.sin(thetar) * r
    return np.column_stack((x, y))

print(np.round(polar2cart_np(pol_array), 5))
