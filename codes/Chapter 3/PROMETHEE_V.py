# Filename: PROMETHEE_V.py
# Description: PROMETHEE V method
# Authors: Papathanasiou, J. & Ploskas, N.

from pulp import *
from PROMETHEE import promethee, main

# Call PROMETHEE II to calculate the flows
flows = main('n', 'n')

# Create an object of a model
prob = LpProblem("Promethee V", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0, 1, LpBinary)
x2 = LpVariable("x2", 0, 1, LpBinary)
x3 = LpVariable("x3", 0, 1, LpBinary)
x4 = LpVariable("x4", 0, 1, LpBinary)
x5 = LpVariable("x5", 0, 1, LpBinary)
x6 = LpVariable("x6", 0, 1, LpBinary)

# Define the objective function
prob += flows[0] * x1 + flows[1] * x2 + flows[2] \
    + flows[3] * x4 + flows[4] * x5 + flows[5] * x6

# Define the constraints
prob += x1 + x2 + x3 + x4 + x5 + x6 == 3
prob += x1 + x4 <= 1
prob += x2 + x4 <= 1
prob += 8 * x1 + 5 * x2 + 7 * x3 + 9 * x4 + \
    11 * x5 + 6 * x6 <= 18

# Solve the linear programming problem
prob.solve()

# Print the results
print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("The optimal value of the objective function is = ", 
	value(prob.objective))