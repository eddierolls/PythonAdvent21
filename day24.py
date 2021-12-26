# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:26:01 2021

@author: edwar
"""
letterMap = {'w':0,'x':1,'y':2,'z':3}

f = open("input/day24.in")
allVars = {(0,0,0,0):0}
i=0
for line in f:
    line = line.strip().split(' ')
    newVars = dict()
    if line[0]=="inp":
        for var in allVars.keys():
            for x in range(1,10):
                nVar = list(var)
                nVar[letterMap[line[1]]] = x
                nVar = tuple(nVar)
                if nVar not in newVars.keys():
                    newVars[nVar] = allVars[var]*10+x
                else:
                    newVars[nVar] = max(newVars[nVar],allVars[var]*10+x)
    elif line[0]=="add":
        for var in allVars.keys():
            nVar = list(var)
            try:
                nVar[letterMap[line[1]]] += int(line[2])
            except ValueError:
                nVar[letterMap[line[1]]] += nVar[letterMap[line[2]]]
            newVars[tuple(nVar)] = allVars[var]
    elif line[0]=="mul":
        for var in allVars.keys():
            nVar = list(var)
            try:
                nVar[letterMap[line[1]]] *= int(line[2])
            except ValueError:
                nVar[letterMap[line[1]]] *= nVar[letterMap[line[2]]]
            nVar = tuple(nVar)
            if nVar not in newVars.keys():
                newVars[nVar] = allVars[var]
            else:
                newVars[nVar] = max(newVars[nVar],allVars[var])
    elif line[0]=="div":
        for var in allVars.keys():
            nVar = list(var)
            try:
                divBy = int(line[2])
            except ValueError:
                divby = nVar[letterMap[line[2]]]
            if divBy==0:
                continue
            nVar[letterMap[line[1]]]//=divBy
            nVar = tuple(nVar)
            if nVar not in newVars.keys():
                newVars[nVar] = allVars[var]
            else:
                newVars[nVar] = max(newVars[nVar],allVars[var])
    elif line[0]=='mod':
        for var in allVars.keys():
            nVar = list(var)
            try:
                modBy = int(line[2])
            except ValueError:
                modby = nVar[letterMap[line[2]]]
            if modBy<=0 or nVar[letterMap[line[1]]]<0:
                continue
            nVar[letterMap[line[1]]]%=modBy
            nVar = tuple(nVar)
            if nVar not in newVars.keys():
                newVars[nVar] = allVars[var]
            else:
                newVars[nVar] = max(newVars[nVar],allVars[var])
    elif line[0]=='eql':
        for var in allVars.keys():
            nVar = list(var)
            try:
                eql = int(line[2])
            except ValueError:
                eql = nVar[letterMap[line[2]]]
            nVar[letterMap[line[1]]]=int(nVar[letterMap[line[1]]]==eql)
            nVar = tuple(nVar)
            if nVar not in newVars.keys():
                newVars[nVar] = allVars[var]
            else:
                newVars[nVar] = max(newVars[nVar],allVars[var])
    else:
        ValueError("Input not parsed")
    allVars = newVars
    i+=1
    print(i,len(allVars),[len(set([x[ii] for x in allVars.keys()])) for ii in range(4)],min([x[3] for x in allVars.keys()]),max([x[3] for x in allVars.keys()]))
