# Filename: SIR.py
# Description: SIR method
# Authors: Papathanasiou, J. & Ploskas, N.

from numpy import *
import matplotlib.pyplot as plt
from SIR_Final_Rank_Figure import graph, plot

# Calculate the preference degrees
def pref_func(a, b, c, d, e, m):
    """ a and b are action performances, c is q, d is p,
    e is the preference function ('u' for usual, 'us'
    for u-shape, 'vs' for v-shape, 'le' for level,
    'li' for linear, and 'g' for Gaussian), m is min/max
    """
    f = float(1.0)
    if m == 1:
        temp = a
        a = b
        b = temp
    if e == 'u': # Usual preference function
        if b - a > 0:
            f = 1
        else:
            f = 0
    elif e == 'us': # U-shape preference function
        if b - a > c:
            f = 1
        elif b - a <= c:
            f = 0
    elif e == 'vs': # V-shape preference function
        if b - a > d:
            f = 1
        elif b - a <= 0:
            f = 0
        else:
            f = (b - a) / d
    elif e == 'le': # Level preference function
        if b - a > d:
            f = 1
        elif b - a <= c:
            f = 0
        else:
            f = 0.5
    elif e == 'li': # Linear preference function
        if b - a > d:
            f = 1
        elif b - a <= c:
            f = 0
        else:
            f = ((b - a) - c) / (d - c)
    elif e == 'g': # Gaussian preference function
        if b - a > 0:
            f = 1 - math.exp(-(math.pow(b - a, 2)
                / (2 * d ** 2)))
        else:
            f = 0
    return f

# Calculate S and I matrices
def SImatrix(x, p, c, d):
    """ x is the action performances array, p is the
    array with the preference parameters of all criteria,
    c is the criteria min (0) or max (1) optimization
    array, and d is the preference function array for
    a specific criterion ('u' for usual, 'us' for u-shape,
    'vs' for v-shape, 'le' for level, 'li' for linear,
    and 'g' for Gaussian)
    """
    SI = zeros((size(x, 0), size(x, 1)))
    for i in range(size(x, 1)):
        for j in range(size(x, 0)):
            k = 0
            for h in range(size(x, 0)):
                k = k + pref_func(x[j, i], x[h, i],
                    p[0, i], p[1, i], d[i], c[i])
                SI[j, i] = k
    return SI

# Calculate S- and I-flow for SIR-SAW
def SIflowsSAW(w, SI):
    """ w is the weights array and SI is S or I matrix
    """
    k = zeros(size(SI, 0))
    for i in range(size(SI, 0)):
        for j in range(size(SI, 1)):
            k[i] = k[i] + w[j] * SI[i, j]
    return k

# Calculate SIplus and SIminus for SIR-TOPSIS
def SIRTOPSIS(w, SI, l):
    """ w is the weights array, SI is S or I matrix,
    and l is the distance metric
    """
    SIplus = zeros((size(SI, 0)))
    SIminus = zeros((size(SI, 0)))
    bb = []
    cc = []
    for i in range((size(w, 0))):
        bb.append(amax(SI[:, i:i + 1]))
        bbb = array(bb)
        cc.append(amin(SI[:, i:i + 1]))
        ccc = array(cc)
    for i in range((size(SI, 0))):
        for j in range((size(SI, 1))):
            SIplus[i] = SIplus[i] + math.pow(w[j]
                * abs(SI[i, j] - bbb[j]), l)
            SIminus[i] = SIminus[i] + math.pow(w[j]
                * abs(SI[i, j] - ccc[j]), l)
        SIplus[i] = math.pow(SIplus[i], 1 / l)
        SIminus[i] = math.pow(SIminus[i], 1 / l)
    return SIplus, SIminus

# Calculate the S- and I-flow for SIR-TOPSIS
def SIflowsTOPSIS(p, m):
    """ p is SIplus and m is SIminus
    """
    return m / (m + p)

# Calculate n-flow
def Nflow(s, i):
    """ s is S-flow and i is I-flow
    """
    return s - i

# Calculate r-flow
def Rflow(s, i):
    """ a is S-flow and b is I-flow
    """
    return s / (s + i)

# main function
def main(a, b, c):
    """ a, b, and c are flags; if a and b are set to 
	'y' they do print the results, anything else does 
	not print the results. If c equals 1, SIR-SAW is 
	used as the aggregation procedure; otherwise, 
	SIR-TOPSIS is used
	"""

    # action performances array
    x = array([[8, 7, 2, 1], [5, 3, 7, 5], [7, 5, 6, 4],
        [9, 9, 7, 3], [11, 10, 3, 7], [6, 9, 5, 4]])

    # preference parameters of all criteria array
    p = array([[1, 1, 1, 1], [2, 2, 2, 2]])

    # criteria min (0) or max (1) optimization array for
    # calculating S matrix
    c1 = ([1, 1, 1, 1])

    # criteria min (0) or max (1) optimization array for
    # calculating I matrix (the opposite of c1)
    c2 = ([0, 0, 0, 0])

    # preference function array
    d = (['li', 'li', 'li', 'li'])

    # weights of criteria
    w = array([0.4, 0.3, 0.1, 0.2])

    # calculate S matrix
    S = SImatrix(x, p, c1, d)
    print("S = ", S)

    # calculate I matrix
    I = SImatrix(x, p, c2, d)
    print("I = ", I)

    if c == 1: # SIR-SAW
        # calculate S-flow
        Sflow = SIflowsSAW(w, S)

        # calculate I-flow
        Iflow = SIflowsSAW(w, I)
    else: # SIR-TOPSIS
        # calculate S-flow
        Splus, Sminus = SIRTOPSIS(w, S, 2)
        Sflow = SIflowsTOPSIS(Splus, Sminus)

        # calculate I-flow
        Iplus, Iminus = SIRTOPSIS(w, I, 2)
        Iflow = SIflowsTOPSIS(Iplus, Iminus)

    # calculate n-flow
    nflow = Nflow(Sflow, Iflow)

    # calculate r-flow
    rflow = Rflow(Sflow, Iflow)

    # print flows
    print("S-flow = ", Sflow)
    print("I-flow = ", Iflow)
    print("n-flow = ", nflow)
    print("r-flow = ", rflow)
	
    # plot results
    if a == 'y':
        graph(around(rflow, 3), "Flow")
    if b == 'y':
        plot(around(rflow, 3), "SIR")

if __name__ == '__main__':
    main('n', 'y', 1)
