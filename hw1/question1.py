import numpy as np
import matplotlib.pyplot as plt

#################
#### GIVENS #####
#################

def find_inaccuracy(total_in_hours, missile_speed, binary):
    # total time elapsed in seconds
    # time_in_seconds = total_in_hours * 60 * 60
    # number of times incremented (number of tenths of a seconds in 100 hours)
    time_in_tenths = total_in_hours * 60 * 60 * 10

    ###############################
    #### COMPUTE REAL DECIMAL ##### 
    ####### VALUE OF BINARY #######
    ###############################
    '''
    Since our binary number is root 2, 
    every point after the decimal point is b[i] * (2)^-i
    with i being the index of that place after the decimal point.
    To find the true decimal value of the binary, I need to sum b[i].
    '''
    decimal_value_of_binary = sum(
        int(b) * # use int to convert the string to int
        2**-(i+1)  # use i+1 because python starts at 0th index
        for i, b in enumerate(binary) # use enumerate since it returns both the value and index
        )

    ###########################
    #### COMPUTE THE ERROR ####
    ###########################

    ideal = 0.1
    error_per_increment = ideal - decimal_value_of_binary # True Error
    total_time_error = error_per_increment * time_in_tenths
    distance_error = missile_speed * total_time_error

    return total_time_error, distance_error

#### FROM THE REPORT ####
hours = [0, 1, 8, 20, 48, 72, 100]
inaccuracy = [0, 0.0034, 0.0275, 0.0687, 0.1648, 0.2473, 0.3433]
shift = [0, 7, 55, 137, 330, 494, 687]

#### MY VALUES ####
total_in_hours = 100
missile_speed = 1670
binary = "00011001100110011001100"

##### MY ANSWER FOR MY VALUES #####
distance_error = find_inaccuracy(total_in_hours, missile_speed, binary)[1]
print(distance_error)

##########
## PLOT ##
##########

#### Initialize ####
i = np.ones(7)
j = np.ones(7)
for g, each in enumerate(hours):
    i[g], j[g] = find_inaccuracy(each, missile_speed, binary)

plt.figure()
plt.plot(inaccuracy, shift, '-o', label = "Report Estimates")
plt.plot(i, j, '-o', label = "My Estimates")
plt.xlabel("Inaccuracy (s)")
plt.ylabel("Shift (m)")
plt.title("Inaccuracy vs. Missile Distance Error")
plt.legend()
plt.show()