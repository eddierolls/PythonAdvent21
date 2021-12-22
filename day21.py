# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:25:07 2021

@author: edwar
"""
from collections import Counter

f = open("input/day21.in")
p1 = int(f.readline().strip().strip("Player 1 starting position: "))
p2 = int(f.readline().strip().strip("Player 2 starting position: "))

scores = [0,0]
pos = [p1,p2]
dice = 0
p = 0
totalRolls=0
while max(scores)<1000:
    dice = ((dice+3-1)%100)+1
    pos[p] = ((pos[p] + dice + (dice-1) + (dice-2) - 1)%10)+1
    scores[p]+=pos[p]
    p = (p+1)%2
    totalRolls+=3
print(min(scores)*totalRolls)
    
# Part 2
scorePaths = {3:1,
              4:3,
              5:6,
              6:7,
              7:6,
              8:3,
              9:1}
stateCounter = Counter([(p1,p2,0,0)])
p = 0 # player number
wins = [0,0]
while len(stateCounter)>0:
    nextCounter = Counter()
    for gameState in stateCounter.keys():
        for roll in scorePaths.keys():
            nextGameState = list(gameState)
            nextGameState[p] = ((nextGameState[p]-1+roll)%10)+1
            nextGameState[p+2] += nextGameState[p]
            if nextGameState[p+2]>=21:
                wins[p]+=stateCounter[gameState]*scorePaths[roll]
            else:
                nextCounter[tuple(nextGameState)] += stateCounter[gameState]*scorePaths[roll]
    p = (p+1)%2
    stateCounter = nextCounter
print(max(wins))


