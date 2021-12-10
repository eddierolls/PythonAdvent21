# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:50:52 2021

@author: edwar
"""

partners = {"{":"}",
            "[":"]",
            "<":">",
            "(":")"}
scores = {"}":1197,
          "]":57,
          ">":25137,
          ")":3}

incompletePoints = {"}":3,
                    "]":2,
                    ">":4,
                    ")":1}


f = open("input/day10.in")
errorScore=0
incompleteScores=[]
for line in f:
    s = line.strip()
    stack = []
    found = False
    for c in s:
        if c in partners.keys():
            stack.append(c)
        elif len(stack)>0 and partners[stack[-1]]==c:
            stack.pop()
        else:
            errorScore+=scores[c]
            found = True
            break
    if not found:
        thisScore = 0
        while len(stack)>0:
            c = partners[stack.pop()]
            thisScore*=5
            thisScore+=incompletePoints[c]
        incompleteScores.append(thisScore)
print(errorScore)
incompleteScores.sort()
print(incompleteScores[len(incompleteScores)//2])