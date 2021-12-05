# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:20:37 2021

@author: edwar
"""
import numpy as np

f = open("input/day5.in")
lines = []
diagonals = []
dims = [0,0]
for line in f:
    start,end = line.strip().split(" -> ")
    start = tuple(map(int,start.split(',')))
    end = tuple(map(int,end.split(',')))
    if (start[0]==end[0] or start[1]==end[1]) and sum(start)<sum(end):
        lines.append([start,end])
    elif (start[0]==end[0] or start[1]==end[1]): # Switch the order
        lines.append([end,start])
    else:
        diagonals.append([start,end])

dims = (1000,1000)
upDown = np.zeros(dims)
leftRight = np.zeros(dims)
for start,end in lines:
    if start[0]==end[0]:
        leftRight[start] += 1
        leftRight[(end[0],end[1]+1)] -= 1
    elif start[1]==end[1]:
        upDown[start] += 1
        upDown[(end[0]+1,end[1])] -= 1

totalCounts = np.cumsum(upDown,0) + np.cumsum(leftRight,1)
print(np.sum(totalCounts>1))

# Moving into hack, quick code, could probably do this with repeated matrix transformations
for start,end in diagonals:
    signs = [(start[x]<end[x])*2-1 for x in range(2)]
    jj = start[1]
    for ii in range(start[0],end[0]+signs[0],signs[0]):
        totalCounts[(ii,jj)]+=1
        jj = jj + signs[1]

print(np.sum(totalCounts>1))
