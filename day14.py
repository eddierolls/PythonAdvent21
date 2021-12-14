# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:18:36 2021

@author: edwar
"""
from collections import Counter

f = open("input/day14.in")

initial = f.readline().strip()
f.readline() # Empty
pairsMap = {}
allElements = set()
for line in f:
    mapFrom,mapTo = line.strip().split(" -> ")
    allElements.add(mapFrom[0])
    pairsMap[mapFrom] = (mapFrom[0]+mapTo,mapTo+mapFrom[1])

pairsCount = {x:0 for x in pairsMap.keys()}
for ii in range(len(initial)-1):
    pairsCount[initial[ii:ii+2]] +=1

for t in range(40):
    newPairs = {x:0 for x in pairsMap.keys()}
    for mapFrom in pairsCount.keys():
        newPairs[pairsMap[mapFrom][0]] += pairsCount[mapFrom]
        newPairs[pairsMap[mapFrom][1]] += pairsCount[mapFrom]
    pairsCount = newPairs

allElements = Counter()
allElements[initial[0]]+=1
allElements[initial[-1]]+=1
for pair in pairsCount.keys():
    allElements[pair[0]]+=pairsCount[pair]
    allElements[pair[1]]+=pairsCount[pair]
print((allElements.most_common(1)[0][1]-allElements.most_common()[-1][1])//2)
    


