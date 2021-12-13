# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:24:34 2021

@author: edwar
"""

import numpy as np

def foldPaper(paper,direction,position):
    dims = paper.shape
    if direction=="y":
        if 2*position-dims[0]+1>0:
            paperFold = np.concatenate((np.full((2*position-dims[0]+1,dims[1]),False),paper[range(dims[0]-1,position,-1),:]),axis=0)
        else:
            paperFold = paper[range(dims[0]-1,position,-1),:]
        paper = np.logical_or(paper[range(position),:],paperFold)
    else:
        if 2*position-dims[1]+1>0:
            paperFold = np.concatenate((np.full((dims[0],2*position-dims[1]+1),False),paper[:,range(dims[1]-1,position,-1)]),axis=0)
        else:
            paperFold = paper[:,range(dims[1]-1,position,-1)]
        paper = np.logical_or(paper[:,range(position)],paperFold)
    return paper

charMap = {True:"#",False:"."}

f = open("input/day13.in")
coordinates = []
folds = []
for line in f:
    if "," in line:
        coordinates.append(tuple(map(int,line.strip().split(',')))) 
    elif "fold" in line:
        direction,position = line.strip().strip("fold along ").split("=")
        folds.append((direction,int(position)))
f.close()
    
dims = (max([x[1] for x in coordinates])+1,max([x[0] for x in coordinates])+1) # coordinates are reversed in input

paper = np.full(dims,False)
paper[np.array([x[1] for x in coordinates]),np.array([x[0] for x in coordinates])] = True # coordinates are reversed in input

direction,position = folds.pop(0)
paper = foldPaper(paper,direction,position)
print(np.sum(paper))

for direction,position in folds:
    paper = foldPaper(paper,direction,position)

g = open("input/day13.out",'w')
for ii in range(paper.shape[0]):
    line = list(paper[ii,:])
    line = [charMap[x] for x in line]
    g.write(''.join(line)+"\n")

g.close()
    
    