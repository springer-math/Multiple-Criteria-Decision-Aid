# Filename: weightedGP.py
# Description: Weighted Goal Programming method
# Authors: Papathanasiou, J. & Ploskas, N.

from pyomo.environ import *
from pyomo.opt import SolverFactory

# Create an object to perform optimization
opt = SolverFactory('cplex')

# Create an object of a concrete model
model = ConcreteModel()

# Define the decision variables
model.x1 = Var(within = NonNegativeIntegers)
model.x2 = Var(within = NonNegativeIntegers)

# Define the deviational variables
model.n1 = Var(within = NonNegativeIntegers)
model.p1 = Var(within = NonNegativeIntegers)
model.n2 = Var(within = NonNegativeIntegers)
model.p2 = Var(within = NonNegativeIntegers)
model.n3 = Var(within = NonNegativeIntegers)
model.p3 = Var(within = NonNegativeIntegers)
model.n4 = Var(within = NonNegativeIntegers)
model.p4 = Var(within = NonNegativeIntegers)

# Define the objective function with the
# associated weights (percentage normalization)
model.obj = Objective(expr = (1 / 600) * model.p1 +
    (1 / 700) * model.p2 + (2 / 18000) * model.n3 +
    (3 / 380) * model.p4)

# Define the constraints
model.con1 = Constraint(expr = 2 * model.x1 +
    4 * model.x2 + model.n1 - model.p1 == 600)
model.con2 = Constraint(expr = 5 * model.x1 +
    3 * model.x2 + model.n2 - model.p2 == 700)
model.con3 = Constraint(expr = 100 * model.x1 +
    90 * model.x2 + model.n3 - model.p3 == 18000)
model.con4 = Constraint(expr = 2 * model.x1 +
    2 * model.x2 + model.n4 - model.p4 == 380)
model.con5 = Constraint(expr = model.x1 +
    model.x2 <= 200)
model.con6 = Constraint(expr = model.x1 >= 60)
model.con7 = Constraint(expr = model.x2 >= 60)

# Solve the Goal Programming problem
opt.solve(model)

# Print the values of the decision variables
print("x1 = ", model.x1.value)
print("x2 = ", model.x2.value)

# Print the achieved values for each goal
if model.n1.value > 0:
    print("The first goal is underachieved by ",
          model.n1.value)
elif model.p1.value > 0:
    print("The first goal is overachieved by ",
          model.p1.value)
else:
    print("The first goal is fully satisfied")

if model.n2.value > 0:
    print("The second goal is underachieved by ",
          model.n2.value)
elif model.p2.value > 0:
    print("The second goal is overachieved by ",
          model.p2.value)
else:
    print("The second goal is fully satisfied")

if model.n3.value > 0:
    print("The third goal is underachieved by ",
          model.n3.value)
elif model.p3.value > 0:
    print("The third goal is overachieved by ",
          model.p3.value)
else:
    print("The third goal is fully satisfied")

if model.n4.value > 0:
    print("The fourth goal is underachieved by ",
          model.n4.value)
elif model.p4.value > 0:
    print("The fourth goal is overachieved by ",
          model.p4.value)
else:
    print("The fourth goal is fully satisfied")