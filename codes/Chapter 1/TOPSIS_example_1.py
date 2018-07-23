# Filename: TOPSIS_example_1.py
# Description: Application of TOPSIS in the first facility
# location problem of Chapter 1
# Authors: Papathanasiou, J. & Ploskas, N.

from numpy import *

# performances of the alternatives
x = array([[8, 7, 2, 1], [5, 3, 7, 5], [7, 5, 6, 4],
           [9, 9, 7, 3], [11, 10, 3, 7], [6, 9, 5, 4]])

# weights of the criteria
weights = array([0.4, 0.3, 0.1, 0.2])

# Step 1 (vector normalization): cumsum() produces the
# cumulative sum of the values in the array and can also
# be used with a second argument to indicate the axis to use
col_sums = array(cumsum(x**2, 0))
norm_x = array([[round(x[i, j] / sqrt(col_sums[x.shape[0]
	- 1, j]), 3) for j in range(4)] for i in range(6)])

# Step 2 (Multiply each evaluation by the associated weight):
# wnx is the weighted normalized x matrix
wnx = array([[round(weights[i] * norm_x[j, i], 3)
    for i in range(4)] for j in range(6)])

# Step 3 (positive and negative ideal solution)
pis = array([amax(wnx[:, :1]), amax(wnx[:, 1:2]),
    amax(wnx[:, 2:3]), amax(wnx[:, 3:4])])
nis = array([amin(wnx[:, :1]), amin(wnx[:, 1:2]),
    amin(wnx[:, 2:3]), amin(wnx[:, 3:4])])

# Step 4a: determine the distance to the positive ideal
# solution (dpis)
b1 = array([[(wnx[j, i] - pis[i])**2 for i in range(4)]
    for j in range(6)])
dpis = sqrt(sum(b1, 1))

# Step 4b: determine the distance to the negative ideal
# solution (dnis)
b2 = array([[(wnx[j, i] - nis[i])**2 for i in range(4)]
    for j in range(6)])
dnis = sqrt(sum(b2, 1))

# Step 5: calculate the relative closeness to the ideal
# solution
final_solution = array([round(dnis[i] / (dpis[i] + dnis[i]),
    3) for i in range(6)])
print("Closeness coefficient = ", final_solution)