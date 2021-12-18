# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 09:39:32 2021

@author: edwar
"""
f = open("input/day17.in")
line = f.readline()
#line = "target area: x=20..30, y=-10..-5"
line = line.strip().strip("target area: ").split(', ')
x,y = list(map(lambda x: x[2:].split(".."),line))
xBox = list(map(int,x))
yBox = list(map(int,y))

# From the input it's clear that a value of x exists provided as eventually fall in straight line
# For a velocity of -min(y)-1, we go through x axis at velocity -min(y)-1 then 1 step later is min(y)
yVel = -min(yBox)-1
print(yVel*(yVel+1)//2)

# Part 2
yInit = list(range(min(yBox),-min(yBox)))
yPaths = {t:[] for t in range(yVel*2+2)}
for y in yInit:
    totalYdist = 0
    for t in range(yVel*2+2):
        totalYdist+=(y-t)
        if totalYdist>=min(yBox) and totalYdist<=max(yBox):
            yPaths[t].append(y)

xInit = [x for x in range(max(xBox)+1) if x*(x+1)//2>=min(xBox)]
allPaths = set()
for x in xInit:
    totalXdist = 0
    for t in range(max(yPaths.keys())+1):
        totalXdist+=max(x-t,0)
        if totalXdist>=min(xBox) and totalXdist<=max(xBox):
            allPaths=allPaths.union(set([(x,y) for y in yPaths[t]]))

print(len(allPaths))
