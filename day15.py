# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:39:49 2021

@author: edwar
"""

import numpy as np
import heapq

f = open("input/day15.in")

line = list(map(int,list(f.readline().strip())))
scores = [[sum(line[:x]) for x in range(1,len(line)+1)]]
for line in f:
    line = list(map(int,list(line.strip())))
    newScores = [scores[-1][0]+line[0]]
    for jj in range(1,len(line)):
        newScores.append(min(newScores[-1],scores[-1][jj])+line[jj])
    scores.append(newScores)

print(scores[-1][-1]-scores[0][0])
f.close()

# Part 2
f = open("input/day15.in")

cave = []
for line in f:
    cave.append(list(map(int,list(line.strip()))))
cave = np.array(cave)

origCave = cave
for ii in range(1,5):
    cave = np.concatenate((cave,origCave+ii),axis=0)
origCave = cave
for ii in range(1,5):
    cave = np.concatenate((cave,origCave+ii),axis=1)

cave = ((cave-1)%9)+1

currentPath = []
heapq.heappush(currentPath,(0,0,0))
scoreAt = np.zeros(cave.shape,dtype="int32")
while len(currentPath)>0 and scoreAt[cave.shape[0]-1,cave.shape[1]-1]==0:
    score,x,y = heapq.heappop(currentPath)
    for ii,jj in [(1,0),(0,1),(-1,0),(0,-1)]:
        if x+ii>=0 and y+jj>=0 and x+ii<cave.shape[0] and y+jj<cave.shape[1] and scoreAt[x+ii,y+jj]==0:
            scoreAt[x+ii,y+jj] = scoreAt[x,y]+cave[x+ii,y+jj]
            heapq.heappush(currentPath,(scoreAt[x+ii,y+jj],x+ii,y+jj))
    
print(scoreAt[cave.shape[0]-1,cave.shape[1]-1])
            
