# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 16:03:50 2021

@author: edwar
"""
from collections import defaultdict
# A bit more question-specific than the general last attempt
letterMap = {'w':0,'x':1,'y':2,'z':3}

f = open("input/day24.in")
zScores = defaultdict(int)
zScores[0] = 0
divRemaining = 7
for t in range(14):
    newZ = defaultdict(int)
    for _ in range(4):
        f.readline()
    A = int(f.readline().strip().split(' ')[2])
    B = int(f.readline().strip().split(' ')[2])
    for _ in range(9):
        f.readline()
    C = int(f.readline().strip().split(' ')[2])
    divRemaining -= (A==26)
    for _ in range(2):
        f.readline()
    for w in range(1,10):
        for z in zScores.keys():
            x = ((z%26)+B)!=w
            y = 25*x+1
            z2 = (z//A)*y
            z2 += (w+C)*x
            if z2<=26**divRemaining:
                newZ[z2] = max(newZ[z2],zScores[z]*10+w)
    zScores = newZ
    print(t,divRemaining,len(zScores))
print(zScores)

# Part 2 - annoyingly the defaultdict doesn't quite work for the min
f = open("input/day24.in")
zScores = dict()
zScores[0] = 0
divRemaining = 7
for t in range(14):
    newZ = dict()
    for _ in range(4):
        f.readline()
    A = int(f.readline().strip().split(' ')[2])
    B = int(f.readline().strip().split(' ')[2])
    for _ in range(9):
        f.readline()
    C = int(f.readline().strip().split(' ')[2])
    divRemaining -= (A==26)
    for _ in range(2):
        f.readline()
    for w in range(1,10):
        for z in zScores.keys():
            x = ((z%26)+B)!=w
            y = 25*x+1
            z2 = (z//A)*y
            z2 += (w+C)*x
            if z2<=26**divRemaining and (z2 not in newZ.keys() or newZ[z2]>zScores[z]*10+w):
                newZ[z2] = zScores[z]*10+w
    zScores = newZ
    print(t,divRemaining,len(zScores))
print(zScores)
    