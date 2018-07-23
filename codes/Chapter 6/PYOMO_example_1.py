# Filename: PYOMO_example_1.py
# Description: An example of solving a linear
# programming problem with Pyomo
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
model.x1 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeReals)

# Define the objective function
model.obj = Objective(expr = 60 * model.x1 +
    40 * model.x2)

# Define the constraints
model.con1 = Constraint(expr = 4 * model.x1 +
    4 * model.x2 >= 10)
model.con2 = Constraint(expr = 2 * model.x1 +
    model.x2 >= 4)
model.con3 = Constraint(expr = 6 * model.x1 +
    2 * model.x2 <= 12)

# Solve the linear programming problem
results = opt.solve(model)

# Print the results
print ("Status: ",
    results.solver.termination_condition)

print("x1 = ", model.x1.value)
print("x2 = ", model.x2.value)

print ("The optimal value of the objective function "
    "is = ", model.obj())

# Plot the results
x = np.arange(0, 5)

plt.plot(x, 2.5 - x, label = '4x1 + 4x2 >= 10')
plt.plot(x, 4 - 2 * x, label= ' 2x1 + x2 >= 4')
plt.plot(x, 6 - 3 * x, label = '6x1 + 2x2 <= 12')
plt.plot(x, 2 - 2/3*x, '--')
plt.annotate('Objective\n function', xy = (0.6, 1.6),
    xytext = (0.3, 0.8), arrowprops =
    dict(facecolor = 'black', width = 1.5, headwidth = 7))
plt.annotate('Optimal\n solution\n(1.5, 1)', 
    xy = (1.48, 0.98), xytext = (1, 0.5), arrowprops =
    dict(facecolor = 'black', width = 1.5, headwidth = 7))
plt.plot(1.5, 1, 'wo')
plt.text(0.1, 4, 'Feasible area', size = '12')

# Define the boundaries of the feasible area in the plot
a = [0, 1.5, 1.75, 0, 0]
b = [4, 1, 0.75, 6, 4]
plt.fill(a, b, 'grey')

plt.xlabel("x1")
plt.ylabel("x2")
plt.title('LP Example 1')
plt.axis([0, 3, 0, 6])
plt.grid(True)
plt.legend()
plt.show()