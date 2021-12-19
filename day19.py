# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:52:01 2021

@author: edwar
"""
from collections import defaultdict
from itertools import combinations,permutations,product

def beaconDistance(b1,b2):
    x1,y1,z1 = b1
    x2,y2,z2 = b2
    return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

def manhattanDistance(b1,b2):
    return sum([abs(b1[x]-b2[x]) for x in range(3)])

def permuteBeacons(b,co,mult):
    return [tuple([y[x]*mult[x] for x in co]) for y in b]

def shiftBeacons(b,shift):
    return [tuple([y[x]+shift[x] for x in range(3)]) for y in b]

def findPosition(b1,b2,pos):
    b1 = set(b1)
    for co in permutations([0,1,2],3): # Looping over co-ordinate ordering
        for mult in product((1,-1),repeat=3): # Looping over multiplier
            theseBeacons = permuteBeacons(b2,co,mult)
            startBeacon = theseBeacons[0]
            for beacon in b1:
                shift = tuple([beacon[x]-startBeacon[x] for x in range(3)])
                shiftedBeacons = set(shiftBeacons(theseBeacons,shift))
                if len(shiftedBeacons.intersection(b1))>=12:
                    return shift,co,mult

        
f = open("input/day19.in")
scanners = []
thisScanner = []
for line in f:
    if line[:3]=='---':
        pass
    elif line.strip()=='':
        scanners.append(thisScanner)
        thisScanner=[]
    else:
        thisScanner.append(tuple(map(int,line.strip().split(','))))
scanners.append(thisScanner)

scanDistances = [] # Note these are all squared to stay in integers
for scan in scanners:
    theseScanners = defaultdict(list)
    for b1,b2 in combinations(range(len(scan)),2):
        theseScanners[beaconDistance(scan[b1],scan[b2])]+=[b1,b2]
    assert max([len(x) for x in theseScanners.values()])==2 # Not guaranteed by the question, but makes life easier if true
    scanDistances.append(theseScanners)

position = [(0,0,0)] + [None for _ in range(len(scanners)-1)]
toConsider = set([0])
while len(toConsider)>0:
    s1=toConsider.pop()
    otherScanners = [x for x in range(len(position)) if position[x] is None]
    for s2 in otherScanners:
        sharedDistances = set(scanDistances[s1].keys()).intersection(set(scanDistances[s2].keys()))
        b1 = set([scanDistances[s1][x][0] for x in sharedDistances] + [scanDistances[s1][x][1] for x in sharedDistances])
        b1 = [scanners[s1][x] for x in b1] # list of co-ordinates of beacons of first scanner
        b2 = set([scanDistances[s2][x][0] for x in sharedDistances] + [scanDistances[s2][x][1] for x in sharedDistances])
        b2 = [scanners[s2][x] for x in b2] # list of co-ordinates of beacons of second scanner
        if len(b1)>=12:
            shift,co,mult = findPosition(b1,b2,position[s1])
            scanners[s2] = shiftBeacons(permuteBeacons(scanners[s2],co,mult),shift)
            position[s2] = shift
            toConsider.add(s2)

allBeacons = set()
for s in scanners:
    allBeacons.update(s)
print(len(allBeacons))

print(max([manhattanDistance(s1,s2) for s1,s2 in combinations(position,2)]))


    
    
    