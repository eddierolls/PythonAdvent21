# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 13:59:47 2021

@author: edwar
"""
from math import floor,ceil

def parseLine(line):
    out = []
    for s in line:
        try:
            out.append(int(s))
        except ValueError:
            out.append(s)
    return out

def performAddition(line1,line2):
    return ["["]+line1+[","]+line2+["]"]

def explode(line):
    currentDepth=0
    lastNumber = -1
    operationMade = False
    for ii in range(len(line)):
        if line[ii]=='[':
            currentDepth+=1
        elif line[ii]==']':
            currentDepth-=1
        if currentDepth==5:
            assert line[ii]=='[' and type(line[ii+1])==int and line[ii+2]==',' and type(line[ii+3])==int and line[ii+4]==']'
            if lastNumber>=0:
                line[lastNumber]+=line[ii+1]
            try:
                nextNumber = min([x for x in range(ii+5,len(line)) if type(line[x])==int])
                line[nextNumber]+=line[ii+3]
            except ValueError:
                pass
            line = line[:ii]+[0]+line[ii+5:]
            operationMade = True
            break
        elif type(line[ii])==int:
            lastNumber=ii
    return line,operationMade

def split(line):
    operationMade=False
    for ii in range(len(line)):
        if type(line[ii])==int and line[ii]>=10:
            line = line[:ii]+["[",floor(line[ii]/2),',',ceil(line[ii]/2),']']+line[ii+1:]
            operationMade=True
            break
    return line,operationMade

def calculateMagnitude(line):
    while len(line)>1:
        ii = 0
        while ii<len(line):
            if line[ii]=='[' and type(line[ii+1])==int and line[ii+2]==',' and type(line[ii+3])==int and line[ii+4]==']':
                line = line[:ii] + [3*line[ii+1]+2*line[ii+3]] + line[ii+5:]
            else:
                ii+=1
    return line[0]

f = open("input/day18.in")
currentLine = parseLine(f.readline().strip())
for line in f:
    currentLine = performAddition(currentLine,parseLine(line.strip()))
    operationMade = True
    while operationMade:
        operationMade=False
        currentLine,operationMade = explode(currentLine)
        if not operationMade:
            currentLine,operationMade = split(currentLine)
print(calculateMagnitude(currentLine))

# Got a bit lazy here
f = open("input/day18.test")
lines = [parseLine(s.strip()) for s in f]
topScore = 0
for ii in range(len(lines)):
    for jj in range(len(lines)):
        if ii!=jj:
            currentLine = performAddition(lines[ii],lines[jj])
            operationMade = True
            while operationMade:
                operationMade=False
                currentLine,operationMade = explode(currentLine)
                if not operationMade:
                    currentLine,operationMade = split(currentLine)
            topScore = max(topScore,calculateMagnitude(currentLine))
print(topScore)