import numpy as np
import matplotlib.pyplot as plt

# Load (downward 1000 lb at C)
P = 1000.0  # lb

def get_angles(p1, p2):
    """Return cosθ, sinθ for the vector from p1 to p2."""
    r = p2 - p1
    L = np.linalg.norm(r)
    return r[0] / L, r[1] / L

def solve_truss(xC, yC=1.0, F=1000):
    # Node coordinates
    A = np.array([0.0, 0.0])
    B = np.array([1.0, 0.0])
    C = np.array([xC, yC])

    # Compute direction cosines
    cosAB, sinAB = get_angles(A, B)
    cosAC, sinAC = get_angles(A, C)
    cosBC, sinBC = get_angles(B, C)

    # Build equilibrium matrix (6 equations, 6 unknowns)
    A_matrix = np.array([
        [ cosAB,  cosAC,   0,  1,  0,  0],   # Node A, x
        [ sinAB,  sinAC,   0,  0,  1,  0],   # Node A, y
        [-cosAB,     0, cosBC,  0,  0,  0],   # Node B, x
        [-sinAB,     0, sinBC,  0,  0,  1],   # Node B, y
        [     0, -cosAC, -cosBC, 0,  0,  0],   # Node C, x
        [     0, -sinAC, -sinBC, 0,  0,  0]    # Node C, y
    ])

    # Right-hand side vector
    b_matrix = np.array([0, 0, 0, 0, 0, P], dtype=float)

    # Solve for unknowns
    x = np.linalg.solve(A_matrix, b_matrix)

    # # Display results
    # labels = ["F_AB", "F_AC", "F_BC", "A_x", "A_y", "B_y"]
    # for name, value in zip(labels, x):
    #     print(f"{name:>5s} = {value:10.2f} lb")
    F_AB, F_AC, F_BC, A_x, A_y, B_y = x
    return F_AC, F_BC

# xC_values = np.linspace(1.01, 3.0, 100)
# F_AC_values, FBC_values = [solve_truss(xC) for xC in xC_values]

fac, fbc = solve_truss(2)

print('F_BC: ', fbc)

# plot
# plt.plot(xC_values, F_AC_values, label="F_AC (lb)")
# plt.xlabel("xC (ft)")
# plt.ylabel("Force in AC (lb)")
# plt.title("Force in Truss Member AC vs. xC")
# plt.grid(False)
# plt.legend()
# plt.show()
