# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 09:49:55 2021

@author: edwar
"""
import numpy as np

def getSurrounding(idx,dims):
    out = [(idx[0]+x,idx[1]+y) for x in range(-1,2) for y in range(-1,2) if not (x==0 and y==0)]
    out = [(x,y) for (x,y) in out if x>=0 and y>=0 and x<dims[0] and y<dims[1]]
    return np.array([x[0] for x in out]),np.array([x[1] for x in out])

f = open("input/day11.in")
octopuses = []
for line in f:
    octopuses.append(list(map(int,list(line.strip()))))

octopuses = np.array(octopuses)
dims = octopuses.shape
flashCount=0
t = 0
while t<100 or totalFlashes<dims[0]*dims[1]:
    octopuses+=1
    totalFlashes=0
    while np.max(octopuses)>9:
        toFlash = np.argwhere(octopuses>9)
        for x,y in toFlash:
            adj = getSurrounding((x,y),dims)
            octopuses[adj]+=1
            octopuses[x,y] = -100
            if t<100:
                flashCount+=1
            totalFlashes+=1
    octopuses[octopuses<0] = 0
    t+=1

print(flashCount)
print(t)
