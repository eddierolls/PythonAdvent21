# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 18:28:58 2021

@author: edwar
"""
from copy import copy

def findIntersection(b1,b2):
    overlap = []
    for x in range(3):
        c1,c2 = max(b1[x][0],b2[x][0]),min(b1[x][1],b2[x][1])
        if c1>c2:
            return None
        else:
            overlap.append((c1,c2))
    return tuple(overlap)

def boxSize(b):
    dims = [b[x][1]-b[x][0]+1 for x in range(3)]
    return dims[0]*dims[1]*dims[2]

f = open("input/day22.in")
onBoxes = [] # represent a box as [(xMin,xMax),(yMin,yMax),(zMin,zMax)]
offBoxes = []
part1=False
for line in f:
    isOn,line = line.strip().split(' ')
    line = map(lambda x:x.split('=')[1],line.split(','))
    box = tuple([tuple(map(int,x.split('..'))) for x in line])
    
    if (abs(box[0][0])>50 or abs(box[0][1])>50) and part1:
        continue
    
    newOnBoxes = copy(onBoxes)
    newOffBoxes = copy(offBoxes)
    
    if isOn == 'on':
        newOnBoxes.append(box)
    
    for b2 in onBoxes:
        overlap = findIntersection(box,b2)
        if overlap is not None:
            newOffBoxes.append(overlap)
    for b2 in offBoxes:
        overlap = findIntersection(box,b2)
        if overlap is not None:
            newOnBoxes.append(overlap)
    
    onBoxes = newOnBoxes
    offBoxes = newOffBoxes

score = sum([boxSize(b) for b in onBoxes]) - sum([boxSize(b) for b in offBoxes])
print(score)
    