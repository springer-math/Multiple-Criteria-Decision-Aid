# Filename: PYOMO_example_2.py
# Description: An example of solving a binary
# linear programming problem with Pyomo
# Authors: Papathanasiou, J. & Ploskas, N.

from pyomo.environ import *
from pyomo.opt import SolverFactory
import matplotlib.pyplot as plt
import numpy as np

# Create an object to perform optimization
opt = SolverFactory('cplex')

# Create an object of a concrete model
model = ConcreteModel()

# Define the decision variables
model.x1 = Var(within=Binary)
model.x2 = Var(within=Binary)
model.x3 = Var(within=Binary)
model.x4 = Var(within=Binary)
model.x5 = Var(within=Binary)
model.x6 = Var(within=Binary)

# Define the objective function
model.obj = Objective(expr = model.x1 +
    model.x2 + model.x3 + model.x4 + model.x5 +
    model.x6)

# Define the constraints
model.con1 = Constraint(expr = model.x1 +
    model.x3 >= 2)
model.con2 = Constraint(expr = model.x1 +
    model.x2 + model.x5 >= 2)
model.con3 = Constraint(expr = model.x3 +
    model.x4 >= 1)
model.con4 = Constraint(expr = model.x1 +
    model.x4 + model.x5 >= 1)
model.con5 = Constraint(expr = model.x4 +
    model.x5 + model.x6 >= 1)

# Solve the binary linear programming problem
results = opt.solve(model)

# Print the results
print ("Status: ",
    results.solver.termination_condition)

print("x1 = ", model.x1.value)
print("x2 = ", model.x2.value)
print("x3 = ", model.x3.value)
print("x4 = ", model.x4.value)
print("x5 = ", model.x5.value)
print("x6 = ", model.x6.value)

print ("The optimal value of the objective function "
    "is = ", model.obj())