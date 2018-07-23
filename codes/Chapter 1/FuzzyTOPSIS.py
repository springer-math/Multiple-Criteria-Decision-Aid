# Filename: FuzzyTOPSIS.py
# Description: Fuzzy TOPSIS method
# Authors: Papathanasiou, J. & Ploskas, N.

from numpy import *
import matplotlib.pyplot as plt
import timeit

# Convert the linguistic variables for the criteria weights
# or the ratings into fuzzy weights and fuzzy decision
# matrix, respectively
def cal(a, b, k):
    """ a is the dictionary with the linguistic variables 
	for the criteria weights (or the linguistic 
	variables for the ratings), b is the matrix with 
	the criteria weights (or the ratings), and k is 
	the number of the decision makers. The output is 
	the fuzzy decision matrix or the fuzzy weights 
	of the criteria 
	"""
    f = []
    for i in range(len(b)):
        c = []
        for z in range(3):
            x = 0
            for j in range (k):
                x = x + a[b[i][j]][z]
            c.append(round(x / k, 3))
        f.append(c)
    return asarray(f)

# Calculate the fuzzy normalized decision matrix
def fndm(a, n, m):
    """ a is the fuzzy decision matrix, n is the number of
    criteria, and m is the number of the alternatives.
    The output is the fuzzy normalized decision matrix 
	"""
    x = amax(a[:, 2:3])
    f = zeros((n * m, 3))
    for i in range(n * m):
        for j in range(3):
            f[i][j] = round(a[i][j] / x, 3)
    return f

# Calculate the fuzzy weighted normalized decision matrix
def weighted_fndm(a, b, n, m):
    """ a is the fuzzy normalized decision matrix, b is the
    criteria weights, n is the number of criteria, and m
    is the number of the alternatives. The output is
    the fuzzy weighted normalized decision matrix 
	"""
    f = zeros((n * m, 3))
    z = 0
    for i in range(n * m):
        if i % len(b) == 0:
            z = 0
        else:
            z = z + 1
        for j in range(3):
            f[i][j] = round(a[i][j] * b[z][j], 3)
    return f

# Calculate the distance between two fuzzy triangular 
# numbers
def distance(a, b):
    """ a and b are fuzzy triangular numbers. The output is
    their distance 
	"""
    return sqrt(1/3 * ((a[0] - b[0])**2 + (a[1] - b[1])**2
        + (a[2] - b[2])**2))

# Determine the fuzzy positive ideal solution (FPIS)
def func_dist_fpis(a, n, m):
    """ a is the fuzzy weighted normalized decision matrix,
    n is the number of criteria, and m is the number of
    the alternatives. The output is the ideal
    solution of each criterion 
	"""
    fpis = ones((3, 1))
    dist_pis = zeros(m)
    p = 0
    for i in range(m):
        for j in range(n):
            dist_pis[i] = dist_pis[i] + distance(a[p + j],
                fpis)
        p = p + n
    return dist_pis

# Determine the fuzzy negative ideal solution (FNIS)
def func_dist_fnis(a, n, m):
    """ a is the fuzzy weighted normalized decision matrix,
    n is the number of criteria, and m is the number of
    the alternatives. The output is the anti-ideal
    solution of each criterion 
	"""
    fnis = zeros((3, 1))
    dist_nis = zeros(m)
    p = 0
    for i in range(m):
        for j in range(n):
            dist_nis[i] = dist_nis[i] + distance(a[p + j],
                fnis)
        p = p + n
    return dist_nis

# Fuzzy TOPSIS method: it calls the other functions
def f_topsis(a, b, c, d, n, m, k, pl):
    """ a is the dictionary with the linguistic variables
    for the criteria weights, b is the matrix with the
    importance weights of the criteria, c is a 
	dictionary with the linguistic variables for the 
	ratings, d is the matrix with all the ratings, n 
	is the number of criteria, m is the number of the 
	alternatives, and k is the number of the decision 
	makers 
	"""

    # Steps 3 and 4
    fuzzy_weights = cal(a, b, k)
    fuzzy_decision_matrix = cal(c, d, k)
    fuzzy_norm_decision_matrix = fndm(fuzzy_decision_matrix,
        n, m)

    # Step 5
    weighted_fuzzy_norm_decision_matrix = \
        weighted_fndm(fuzzy_norm_decision_matrix,
        fuzzy_weights, n, m)

    # Steps 6 and 7
    a_plus = func_dist_fpis(
		weighted_fuzzy_norm_decision_matrix, n, m)
    a_minus = func_dist_fnis(
		weighted_fuzzy_norm_decision_matrix, n, m)

    # Step 8
    CC = [] # closeness coefficient
    for i in range(m):
        CC.append(round(a_minus[i] / (a_plus[i] +
            a_minus[i]), 3))

    if pl == 'y':
        q = [i + 1 for i in range(m)]
        plt.plot(q, a_plus, 'p--', color = 'red',
            markeredgewidth = 2, markersize = 8)
        plt.plot(q, a_minus, '*--',  color = 'blue',
            markeredgewidth = 2, markersize = 8)
        plt.plot(q, CC, 'o--', color = 'green',
            markeredgewidth = 2, markersize = 8)
        plt.title('Fuzzy TOPSIS results')
        plt.legend(['Distance from the ideal',
            'Distance from the anti-ideal',
            'Closeness coeficient'])
        plt.xticks(range(m + 2))
        plt.axis([0, m + 1, 0, 3])
        plt.xlabel('Alternatives')
        plt.legend()
        plt.grid(True)
        plt.show()
    return CC

m = 6 # the number of the alternatives
n = 4 # the number of the criteria
k = 3 # the number of the decision makers

# Steps 1 and 2
# Define a dictionary with the linguistic variables for the
# criteria weights
cw = {'VL':[0, 0, 0.1], 'L':[0, 0.1, 0.3],
      'ML':[0.1, 0.3, 0.5], 'M':[0.3, 0.5, 0.7],
      'MH':[0.5, 0.7, 0.9], 'H':[0.7, 0.9, 1],
      'VH':[0.9, 1, 1]}

# Define a dictionary with the linguistic variables for the
# ratings
r = {'VP':[0, 0, 1], 'P':[0, 1, 3], 'MP':[1, 3, 5],
     'F':[3, 5, 7], 'MG':[5, 7, 9], 'G':[7, 9, 10],
     'VG':[9, 10, 10]}

# The matrix with the criteria weights
cdw = [['H', 'VH', 'VH'], ['M', 'H', 'VH'],
       ['M', 'MH', 'ML'], ['H', 'VH', 'MH']]

# The ratings of the six candidate sites by the decision
# makers under all criteria
c1 = [['VG', 'G', 'MG'], ['F', 'MG', 'MG'],
      ['P', 'P', 'MP'], ['G', 'VG', 'G']]
c2 = [['MP', 'F', 'F'], ['F', 'VG', 'G'],
      ['MG', 'VG', 'G'], ['MG', 'F', 'MP']]
c3 = [['MG', 'MP', 'F'], ['MG', 'MG', 'VG'],
      ['MP', 'F', 'F'], ['MP', 'P', 'P']]
c4 = [['MG', 'VG', 'VG'], ['G', 'G', 'VG'],
      ['MG', 'VG', 'G'], ['VP', 'F', 'P']]
c5 = [['VP', 'P', 'G'], ['P', 'VP', 'MP'],
      ['G', 'G', 'VG'], ['G', 'MG', 'MG']]
c6 = [['F', 'G', 'G'], ['F', 'MP', 'MG'],
      ['VG', 'MG', 'F'], ['P', 'MP', 'F']]

all_ratings = vstack((c1, c2, c3, c4, c5, c6))

# final results
start = timeit.default_timer()
f_topsis(cw, cdw, r, all_ratings, n, m, k, 'n')
stop = timeit.default_timer()
print(stop - start)
print("Closeness coefficient = ", 
	f_topsis(cw, cdw, r, all_ratings, n, m, k, 'y'))
