import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

##### Question 1 ######
# S(t_j+1) = S(tj) + h(dS(tj)/dt)
def euler(df, S0, h, steps, t0=0):
    S = [S0]
    t = [t0]

    for i in range(steps):
        tj = t[-1]
        Sj = S[-1]
        S2 = Sj + h * df(tj, Sj)
        tj += h
        S.append(S2)
        t.append(tj)
    return t, S 

def df(t, y):
    return y* t**2 - 1.1*y

y0 = 1
t0 = 0
tf = 2

h_values = 0.001

# euler_sol = [euler(df, y0, h, t0, tf) for h in h_values]
euler_sol = euler(df, y0, h_values, steps=(int(tf//h_values + 1)), t0=t0)

# print(euler_sol)

# Define parameters
f = lambda t, s: s * t**2 - 1.1*s # ODE
# h = 0.0001 # Step size
h = 0.5
t = np.arange(0, 2 + h, h) # Numerical grid
s0 = 1 # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

print(s)

#([0, 0.5, 1.0, 1.5, 2.0], 
# [1, 0.44999999999999996, 0.2587499999999999, 
# 0.2458124999999999, 0.3871546874999998])

# sol_default = sc.solve_ivp(df, [t0, tf], [y0])
# 
# t_eval = np.linspace(t0, tf, 200)
# sol_smooth = sc.solve_ivp(df, [t0, tf], [y0], t_eval=t_eval)

######  Question 2 ######
t0=0
tf=2
y0=1
t_eval = np.linspace(t0, tf, 200)

def df(t, y):
    return y * t**2 - 1.1 * y

sol_smooth = sc.solve_ivp(df, (t0, tf), [y0], t_eval=t_eval)
print(f"y({tf}) = {sol_smooth.y[0][-1]:.3f}")
# y(2) = 1.594
#### DOUBLE CHECKED WITH FINER h-VALUE IN EULER ####

# plt.figure()
# plt.plot(sol_smooth.t, sol_smooth.y[0], 'r', linewidth=2, label='RK45 (smooth)')
# plt.show()

###### Question 3 ######
# dydt = -2y + 4 * exp(-t)
# dzdt = - y * z **2 / 3

# y(0) = 2
# z(0) = 4
# simulated in time from t = 0 to t = 4

### SOLVE ODEs ###
def model(t, states):
    y, z = states
    dydt = -2 * y + 4 * np.exp(-t)
    dzdt = - (y * z**2) / 3
    return [dydt, dzdt]

tspan = (0, 4)
y0 = [2, 4]
sol = sc.solve_ivp(model, tspan, y0, t_eval=np.linspace(0, 4, 100))

### PLOT RESULTS ###
plt.figure()
plt.plot(sol.t, sol.y[0], label='y(t)', color='blue')
plt.plot(sol.t, sol.y[1], label='z(t)', color='orange')
plt.xlabel('Time t')
plt.ylabel('States y and z')
plt.title('Solution of Coupled ODEs')
plt.legend()
plt.show()

###### Question 4 ######
# T varies with the distance from the exterior wall, x, according to
# k d2Tdx2 + dTdx + T = 0
# outer sheathing has a conductivity of k = 0.1
# Insulated region 0.05 <= x <- 0.2 has a k of 0.2.
# Exterior surface of the wall x=0, the temperature is T = 0, and DTdx = 100.
# What is the temperature of the interior surface of the wall (to at least 2 decimal places)?

### DEFINE THE MODEL ###
def system(x, states):
    if x >= 0.05:
        k = 0.2
    else:
        k = 0.1
    T, dT = states
    dT1 = dT
    dT2 = (-T - dT) / k
    return [dT1, dT2]

### INITIAL CONDITIONS AND PARAMETERS ###
x0 = 0
xf = 0.2
y0 = [0.0, 100.0]  # T(0) = 0, dT/dx(0) = 100
x_eval = np.linspace(x0, xf, 1000)
### SOLVE THE ODE ###
sol = sc.solve_ivp(system, (x0, xf), y0, t_eval=x_eval)
### OUTPUT THE INTERIOR SURFACE TEMPERATURE ###
interior_temp = sol.y[0][-1]
print(f"Interior surface temperature at x={xf} m: {interior_temp:.4}")

### PLOT RESULTS ###
# plt.figure()
# plt.plot(sol.t, sol.y[0], label='y(t)', color='blue')
# plt.plot(sol.t, sol.y[1], label='z(t)', color='orange')
# plt.xlabel('x')
# plt.ylim(0, 10.5)
# plt.ylabel('Temperature')
# plt.title('Solution of Coupled ODEs')
# plt.legend()
# plt.show()

###### Question 5 - 9 ######
import scipy.stats as stats

data = [0, 0, 1, 3, 4, 0, 0, 5, 5, 1, 1, 1, 13]

mean = sum(data) / len(data)
median = sorted(data)[len(data) // 2]
# 80 percentile
percentile_80 = stats.scoreatpercentile(data, 80)

stndev = stats.tstd(data)
variance = stats.tvar(data)
print("Mean:", mean)
print("Median:", median)
print("80th Percentile:", percentile_80)
print("Standard Deviation:", stndev)
print("Variance:", variance)

# Mean: 2.6153846153846154
# Median: 1
# 80th Percentile: 4.600000000000001
# Standard Deviation: 3.640935354604673
# Variance: 13.256410256410257

###### Question 10 ######
import scipy.stats as stats

data = [0, 0, 1, 3, 4, 0, 0, 5, 5, 1, 1, 1, 13]

# Plot a histogram of the data with 10 bins
import matplotlib.pyplot as plt
plt.hist(data, bins=10, edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

###### Question 11 -13 ######
# Accelerated life test
# 12 motors were operated under high temperature conditions
# The lifetimes (in hours) were measured at ambient temperatures (in deg C)
# ranging from 40 to 95 in steps of 5 (i.e. first lifetime measurement was taken at 40 C, second at 45, and so on):

temperature = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
lifetime = [851, 635, 764, 708, 469, 661, 586, 371, 337, 245, 129, 158]

# Plot the data
# Fit a least squares regression line to the data
# Find the correlation coefficient

plt.figure()
plt.scatter(temperature, lifetime, color='blue', label='Data Points')

A = np.column_stack((temperature, np.ones_like(temperature)))
coeff = np.linalg.lstsq(A, lifetime)[0]
# print(coeff)
# [ -12.61118881 1344.08857809]

coeffs = sc.linregress(temperature, lifetime)
# print(coeffs)
# slope=-12.611188811188812, intercept=1344.088578088578

correlation_matrix = np.corrcoef(temperature, lifetime)
correlation_coefficient = correlation_matrix[0, 1]
print("Correlation Coefficient:", correlation_coefficient)
# -0.9346328250899916

#### SANITY PLOT ####
# line = coeffs.slope * np.array(temperature) + coeffs.intercept
# plt.figure()
# plt.plot(temperature, line, color='red', label='Least Squares Fit')
# plt.scatter(temperature, lifetime, color='blue', label='Data Points')
# plt.xlabel('Temperature (deg C)')
# plt.ylabel('Lifetime (hours)')
# plt.title('Lifetime vs Temperature with Least Squares Fit')
# plt.legend()
# plt.annotate(f'Correlation Coefficient: {correlation_coefficient:.2f}', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, verticalalignment='top')
# plt.show()

###### Question 14 - 18 ######
import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

"""
Human blood may contain neither, either, or both of two antigens,
A and B. At a certain blood bank, 40% of the blood donors have the 
A antigen (and may also have the B antigen), 15% have the B antigen 
(and may also have the A antigen), 5% have both the A and B antigens, 
and the rest have neither antigen. 

Blood that contains only the A antigen is called type A, 
blood that contains only the B antigen is called type B, 
blood that contains both antigens is called type AB, 
and blood that contains neither antigen is called type O.

Report all probabilities as fractions to at least 2 decimal places.

14.
What is the probability that a randomly chosen blood donor 
is type A, type B, or type AB?
"""
##### A     ~ A
decision_matrix = np.array([
    [0.05, 0.10],    # B
    [0.35,  0.5]     # ~ B
])

total_A = 0.35 + 0.10 + 0.05
print("total A", total_A)

notB = decision_matrix[1,0] + decision_matrix[1,1]
print("not B", notB)
notBcheck = 0.35 + 0.50
print("not B check", notBcheck)

AgivenB = decision_matrix[0,0] / (decision_matrix[0,0] + decision_matrix[0,1])
print("A given B", AgivenB)
AgivenBcheck = 0.05 / 0.15
print("A given B check", AgivenBcheck)

BgivenA = decision_matrix[0,0] / (decision_matrix[0,0] + decision_matrix[1,0])
print("B given A", BgivenA)
BgivenAcheck = 0.05 / 0.40
print("B given A check", BgivenAcheck)

####### Question 19 ######
"""
In a certain type of automobile engine, 
the cylinder head is fastened to the block by 10 bolts, 
each of which should be torqued to 60 Nm. 
Assume that the torques of the bolts are independent. 

If each bolt is torqued correctly with probability 0.99, 
what is the probability that all the bolts on a 
cylinder head are torqued correctly? 

Report to at least 3 decimal places 
(probability in fractional form).
"""

n = 10
pcorrect = 0.99
p_all_correct = sc.binom.pmf(n, n, pcorrect)
print(f"Probability that all bolts are torqued correctly: {p_all_correct:.3f}")
# Output: Probability that all bolts are torqued correctly: 0.904
# The probability that all 10 bolts are torqued correctly is approximately 0.904
p_one_incorrect = 1 - (pcorrect**n)
print(f"Probability that at least one bolt is torqued incorrectly: {p_one_incorrect:.3f}")
# Output: Probability that at least one bolt is torqued incorrectly: 0.096

###### Question 20 ######
"""
A system consists of four components connected as shown below.  
Assume each component functions independently 
and that the probabilities of failure are 
0.05 for A, 0.03 for B, 0.07 for C, and 0.14 for D.  

Find the probability that the system functions.  

Report to at least 3 decimal places 
(probability in fractional form)
"""

# Since we know the probabilities of failure for each component,
# we can calculate the probability that the system functions.
# Prob that A fails = 0.05
# Prob that B fails = 0.03
# Prob that C fails = 0.07
# Prob that D fails = 0.14

# For success of the system, we need both A and B to work,
# and at least one of C or D to work.

# So we can calculate the probability that A and B both work,
# and the probability that C or D works.

probAandBwork = (1 - 0.05) * (1 - 0.03)
probCorDwork = ((1-0.07) + (1-0.14) - (1-0.07) * (1-0.14))
probsuccess = probAandBwork * probCorDwork
print(f"P(system functions) = {probsuccess:.3f}")
# 0.912

###### Question 21 - 22 ######

# In a sample of 20 men the mean height was 178 cm.  
# In a sample of 30 women the mean height was 164 cm.  
# What was the mean height for both groups put together (in cm).

mean = (20 * 178 + 30 *164) / 50
# print(mean)
# 169.6 cm

# If P(A) = 0.5 and P(A and ~B) = 0.4, 
# for what value of P(B) will A and B be independent?
# ~B means not B

# If A and B are independent, then P(A and B) = P(A) * P(B)
Pa = 0.5
PAnotB = 0.4
PnotB = PAnotB / Pa
# print(PnotB)
# 0.8
PB = 1- PnotB
# print(PB)
#  0.2

# A    ~A
# 0.1  0.1    B
# 0.4  0.4   ~B

###### Question 23 - 24 ######

t = [1, 2, 3.25, 4.5, 6, 7, 8, 8.5, 9, 10]
v = [5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5]

# Calculate the area under the curve using the trapezoidal rule
area = np.trapz(v, t)
print(area)

# Find average velocity, though velocity is given at unequally spaced values of time
average_velocity = area / (t[-1] - t[0])
print(average_velocity)

# 60.125
# 6.680555555555555