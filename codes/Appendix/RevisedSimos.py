# Filename: RevisedSimos.py
# Description: Revised Simos method
# Authors: Papathanasiou, J. & Ploskas, N.

from numpy import *

# placement of cards ('w' represents a white card)
subsets = array([['b','d'], ['c'], ['w'], 
	['e', 'f', 'h'], ['w'], ['w'], ['a', 'g']])

# parameter z
z = 6.5

# calculate number of cards, positions, and vector c
noOfcards = 0
positions = 0
c = []
for i in range(subsets.shape[0]):
    if subsets[i][0] != 'w':
        noOfcards = noOfcards + len(subsets[i][:])
        positions = positions + 1
        c.append(len(subsets[i][:]))

# calculate u
u = round((z - 1) / positions, 6)

# calculate vector e
e = ones(positions)
counter = -1
for i in range(subsets.shape[0]):
    if subsets[i][0] != 'w':
        counter = counter + 1
    else:
        e[counter] = e[counter] + 1

# calculate the non-normalized weights k
k = ones(positions)
totalk = k[0] * c[0]
for i in range(1, positions):
    k[i] = 1 + u * sum(e[0:i])
    totalk = totalk + k[i] * c[i]

# calculate the normalized weights
normalizedWeights = zeros(positions)
for i in range(0, positions):
    normalizedWeights[i] = (100 / totalk) * k[i]

# print the criteria weights
counter = -1
for i in range(subsets.shape[0]):
    if subsets[i][0] != 'w':
        counter = counter + 1
    else:
        continue
    for j in range(len(subsets[i][:])):
        print("Weight of criterion ", subsets[i][j], 
			" = ", normalizedWeights[counter])
