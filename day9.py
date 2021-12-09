# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 19:25:28 2021

@author: edwar
"""
import numpy as np
from collections import Counter

# Part 1
f = open("input/day9.in")
heights = []
for line in f:
    heights.append(list(map(int,list(line.strip()))))
heights = np.array(heights)
dims = heights.shape
vertDiff = np.diff(heights,axis=0)
horzDiff = np.diff(heights,axis=1)
vertLowest = np.logical_and(np.concatenate((vertDiff>0,np.full((1,dims[1]),True))),
                            np.concatenate((np.full((1,dims[1]),True),vertDiff<0)))
horzLowest = np.logical_and(np.concatenate((horzDiff>0,np.full((dims[0],1),True)),axis=1),
                            np.concatenate((np.full((dims[0],1),True),horzDiff<0),axis=1))
lowPoint = np.logical_and(vertLowest,horzLowest)
riskLevels = heights+1
print(np.sum(lowPoint*riskLevels))

# Part 2
heights = np.concatenate((np.full((1,dims[1]),9),heights,np.full((1,dims[1]),9)))
heights = np.concatenate((np.full((dims[0]+2,1),9),heights,np.full((dims[0]+2,1),9)),axis=1)
points = [(x,y) for x in range(dims[0]+2) for y in range(dims[1]+2) if heights[(x,y)]<9]
for _ in range(9): # 9 turns
    nextPoints = []
    for x,y in points:
        if heights[(x-1,y)]<heights[(x,y)]:
            nextPoints.append((x-1,y))
        elif heights[(x+1,y)]<heights[(x,y)]:
            nextPoints.append((x+1,y))
        elif heights[(x,y-1)]<heights[(x,y)]:
            nextPoints.append((x,y-1))
        elif heights[(x,y+1)]<heights[(x,y)]:
            nextPoints.append((x,y+1))
        else:
            nextPoints.append((x,y))
    points = nextPoints
pointsCount = Counter(points)
print(np.prod([x[1] for x in pointsCount.most_common(3)]))

