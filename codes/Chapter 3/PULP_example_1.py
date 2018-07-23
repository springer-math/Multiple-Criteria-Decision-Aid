# Filename: PULP_example_1.py
# Description: An example of solving a linear
# programming problem with PuLP 
# Authors: Papathanasiou, J. & Ploskas, N.

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("LP example with 2 decision "
    "variables", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)

# Define the objective function
prob += 60*x1 + 40*x2

# Define the constraints
prob += 4*x1 + 4*x2 >= 10.0, "1st constraint"
prob += 2*x1 + x2 >= 4.0, "2nd constraint"
prob += 6*x1 + 2*x2 <= 12.0, "3rd constraint"

# Solve the linear programming problem
prob.solve()

# Print the results
print ("Status: ", LpStatus[prob.status])

for v in prob.variables():
    print (v.name, "=", v.varValue)

print ("The optimal value of the objective function "
    "is = ", value(prob.objective))

# Plot the optimal solution
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