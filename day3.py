# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:22:50 2021

@author: edwar
"""
import numpy as np

f = open("input/day3.in")
scores = np.array([int(s) for s in f.readline().strip()])
totalLines = 1
for line in f:
    scores += np.array([int(s) for s in line.strip()])
    totalLines+=1

scores = np.array([int(x>(totalLines/2)) for x in scores])
binaryMultiplier = np.array([2**x for x in range(len(scores)-1,-1,-1)])

gamma = sum(scores*binaryMultiplier)
epsilon = sum((1-scores)*binaryMultiplier)

print(gamma*epsilon)

# Part 2
f = open("input/day3.in")
allRows = []
for line in f:
    allRows.append([int(s) for s in line.strip()])

oxygenKeep = list(range(len(allRows)))
co2Keep = list(range(len(allRows)))
for idx in range(len(allRows[0])):
    if len(oxygenKeep)>1:
        mostCommon = round((sum([allRows[x][idx] for x in oxygenKeep])+0.25)/len(oxygenKeep))
        oxygenKeep = [x for x in oxygenKeep if allRows[x][idx]==mostCommon]
    if len(co2Keep)>1:
        mostCommon = round((sum([allRows[x][idx] for x in co2Keep])+0.25)/len(co2Keep))
        co2Keep = [x for x in co2Keep if allRows[x][idx]!=mostCommon]

oxygenScore = sum(np.array(allRows[oxygenKeep[0]])*binaryMultiplier)
co2Score = sum(np.array(allRows[co2Keep[0]])*binaryMultiplier)

print(oxygenScore*co2Score)