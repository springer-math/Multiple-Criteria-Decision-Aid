# Filename: PROMETHEE_II.py
# Description: PROMETHEE II method
# Authors: Papathanasiou, J. & Ploskas, N.

import matplotlib.pyplot as plt
from numpy import *
from PROMETHEE_Preference_Functions import uni_cal
from PROMETHEE_Final_Rank_Figure import graph, plot

# PROMETHEE method: it calls the other functions
def promethee(x, p, c, d, w):
    """ x is the action performances array, b is the
    array with the preference parameters of all 
	criteria, c is the criteria min (0) or max (1) 
	optimization array, d is the preference 
	function array ('u' for usual, 'us' for 
	u-shape, 'vs' for v-shape, 'le' for level, 
	'li' for linear, and 'g' for Gaussian), and w
    is the weights array
    """
    weighted_uni_net_flows = []
    total_net_flows = []
    for i in range(x.shape[1]):
        weighted_uni_net_flows.append(w[i] *
            uni_cal(x[:, i:i + 1], p[:,
            i:i + 1], c[i], d[i]))
	
    # print the weighted unicriterion preference
    # net flows
    for i in range(size(weighted_uni_net_flows, 1)):
        k = 0
        for j in range(size(weighted_uni_net_flows, 0)):
            k = k + round(weighted_uni_net_flows[j][i], 5)
        total_net_flows.append(k)
    return around(total_net_flows, decimals = 4)

# main function
def main(a, b):
    """ a and b are flags; if they are set to 'y' they do
    print the results, anything else does not print
    the results
	"""

    # action performances array
    x = array([[8, 7, 2, 1], [5, 3, 7, 5], [7, 5, 6, 4],
        [9, 9, 7, 3], [11, 10, 3, 7], [6, 9, 5, 4]])

    # preference parameters of all criteria array
    p = array([[1, 1, 1, 1], [2, 2, 2, 2]])

    # criteria min (0) or max (1) optimization array
    c = ([1, 1, 1, 1])

    # preference function array
    d = (['li', 'li', 'li', 'li'])

    # weights of criteria
    w = array([0.4, 0.3, 0.1, 0.2])

    # final results
    final_net_flows = promethee(x, p, c, d, w)
    print("Global preference flows = ", final_net_flows)
    if a == 'y':
        graph(final_net_flows, "Phi")
    if b == 'y':
        plot(final_net_flows, "PROMETHEE II")
    return final_net_flows

if __name__ == '__main__':
    main('n','y')