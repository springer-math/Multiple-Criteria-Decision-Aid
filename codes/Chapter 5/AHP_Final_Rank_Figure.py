# Filename: AHP_Final_Rank_Figure.py
# Description: Optional module to plot the
# results of AHP method
# Authors: Papathanasiou, J. & Ploskas, N.

import matplotlib.pyplot as plt
from graphviz import Digraph
from numpy import *

# Plot final rank figure
def graph(scores, b):
    """ scores is the matrix with the scores, and b
    is a string describing the score
    """
    s = Digraph('Actions', node_attr = {'shape':
        'plaintext'})
    s.body.extend(['rankdir = LR'])
    x = sort(scores)
    y = argsort(scores)
    l = []
    for i in y:
        s.node('action' + str(i), '''<
        <TABLE BORDER="0" CELLBORDER="1"
            CELLSPACING="0" CELLPADDING="4">
          <TR>
            <TD COLSPAN="2" bgcolor="grey" >Action
                ''' + str(y[i] + 1) + '''</TD>
          </TR>
          <TR>
            <TD>'''+ b +'''</TD>
            <TD>''' + str(x[i]) + '''</TD>
          </TR>
        </TABLE>>''')
    k = []
    for q in range(len(scores) - 1):
        k.append(['action' + str(q + 1), 'action'
            + str(q)])
    print(k)
    s.edges(k)
    s.view()

# Plot final rank
def plot(a, b):
    """ a is the matrix with the scores, and b
    is a string describing the method
    """
    scores = a
    yaxes_list = [0.2] * size(scores, 0)
    plt.plot(yaxes_list, scores, 'ro')
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    plt.axis([0, 0.7, min(scores) - 0.05,
        max(scores) + 0.05])
    plt.title(b + " results")
    plt.ylabel("Scores")
    plt.legend()
    plt.grid(True)
    z1 = []
    for i in range(size(scores, 0)):
        z1.append('   (Action ' + str(i + 1) + ')')
    z = [str(a) + b for a, b in zip(scores, z1)]
    for X, Y, Z in zip(yaxes_list, scores, z):
        plt.annotate('{}'.format(Z), xy = (X, Y),
            xytext=(10, -4), ha = 'left',
            textcoords = 'offset points')
    plt.show()