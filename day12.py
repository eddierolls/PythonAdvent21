# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 08:55:20 2021

@author: edwar
"""
from copy import copy

class Cave:
    def __init__(self,name):
        self.adjacent = []
        self.name = name
        self.isBig = name.upper()==name
        
f = open("input/day12.in")
caves = dict()
for line in f:
    x,y = line.strip().split("-")
    if x not in caves:
        caves[x]=Cave(x)
    if y not in caves:
        caves[y]=Cave(y)
    caves[x].adjacent.append(y)
    caves[y].adjacent.append(x)

stack = [[c,set([c])] for c in caves["start"].adjacent]

totalPaths = 0
while len(stack)>0:
    cave,visited = stack.pop()
    for nextCave in caves[cave].adjacent:
        if nextCave=="end":
            totalPaths+=1
        elif nextCave!="start" and (caves[nextCave].isBig or nextCave not in visited):
            thisVisited = copy(visited)
            thisVisited.add(nextCave)
            stack.append([nextCave,thisVisited])

print(totalPaths)

# Part b works very similar
stack = [[c,set([c]),False] for c in caves["start"].adjacent]
caves["start"].adjacent = []

totalPaths = 0
while len(stack)>0:
    cave,visited,visitedTwice = stack.pop()
    for nextCave in caves[cave].adjacent:
        if nextCave=="end":
            totalPaths+=1
        elif caves[nextCave].isBig or nextCave not in visited:
            thisVisited = copy(visited)
            thisVisited.add(nextCave)
            stack.append([nextCave,thisVisited,visitedTwice])
        elif not visitedTwice:
            stack.append([nextCave,visited,True])

print(totalPaths)


    