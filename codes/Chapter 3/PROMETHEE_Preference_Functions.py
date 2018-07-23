# Filename: PROMETHEE_Preference_Functions.py
# Description: This module calculates the
# unicriterion preference degrees of the actions
# for a specific criterion
# Authors: Papathanasiou, J. & Ploskas, N.

from numpy import *

# Calculate the unicriterion preference degrees
def uni_cal(x, p, c, f):
    """ x is the action performances array, p is the
    array with the preference parameters of all 
	criteria, c is the criteria min (0) or max (1) 
	optimization array, and f is the preference 
	function array for a specific criterion ('u' 
	for usual, 'us' for u-shape, 'vs' for v-shape, 
	'le' for level, 'li' for linear, and 'g' for 
	Gaussian)
    """
    uni = zeros((x.shape[0], x.shape[0]))
    for i in range(size(uni, 0)):
        for j in range(size(uni, 1)):
            if i == j:
                uni[i, j] = 0
            elif f == 'u':  # Usual preference function
                if x[j] - x[i] > 0:
                    uni[i, j] = 1
                else:
                    uni[i, j] = 0
            elif f == 'us': # U-shape preference function
                if x[j] - x[i] > x[0]:
                    uni[i, j] = 1
                elif x[j] - x[i] <= p[0]:
                    uni[i, j] = 0
            elif f == 'vs': # V-shape preference function
                if x[j] - x[i] > p[1]:
                    uni[i, j] = 1
                elif x[j] - x[i] <= 0:
                    uni[i, j] = 0
                else:
                    uni[i, j] = (x[j] - x[i]) / p[1]
            elif f == 'le': # Level preference function
                if x[j] - x[i] > p[1]:
                    uni[i, j] = 1
                elif x[j] - x[i] <= p[0]:
                    uni[i, j] = 0
                else:
                    uni[i, j] = 0.5
            elif f == 'li': # Linear preference function
                if x[j] - x[i] > p[1]:
                    uni[i, j] = 1
                elif x[j] - x[i] <= p[0]:
                    uni[i, j] = 0
                else:
                    uni[i, j] = ((x[j] - x[i]) -
                        p[0]) / (p[1] - p[0])
            elif f == 'g':  # Gaussian preference function
                if x[j] - x[i] > 0:
                    uni[i, j] = 1 - math.exp(-(math.pow(x[j]
                        - x[i], 2) / (2 * p[1] ** 2)))
                else:
                    uni[i, j] = 0
    if c == 0:
        uni = uni
    elif c == 1:
        uni = uni.T
    # positive, negative and net flows
    pos_flows = sum(uni, 1) / (uni.shape[0] - 1)
    neg_flows = sum(uni, 0) / (uni.shape[0] - 1)
    net_flows = pos_flows - neg_flows
    return net_flows