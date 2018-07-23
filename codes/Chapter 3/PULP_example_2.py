# Filename: PULP_example_1.py
# Description: An example of solving a binary
# linear programming problem with Pulp
# Authors: Papathanasiou, J. & Ploskas, N.

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Binary LP example with 6 decision "
    "variables", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", 0, 1, LpBinary)
x2 = LpVariable("x2", 0, 1, LpBinary)
x3 = LpVariable("x3", 0, 1, LpBinary)
x4 = LpVariable("x4", 0, 1, LpBinary)
x5 = LpVariable("x5", 0, 1, LpBinary)
x6 = LpVariable("x6", 0, 1, LpBinary)

# Define the objective function
prob += x1 + x2 + x3 + x4 + x5 + x6

# Define the constraints
prob += x1 + x3 >= 2
prob += x1 + x2 + x5 >= 2
prob += x3 + x4 >= 1
prob += x1 + x4 + x5 >= 1
prob += x4 + x5 + x6 >= 1

# Solve the linear programming problem
prob.solve()

# Print the results
print ("Status: ", LpStatus[prob.status])

for v in prob.variables():
    print (v.name, "=", v.varValue)

print ("The optimal value of the objective function "
    "is = ", value(prob.objective))
