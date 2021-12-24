# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:30:56 2021

@author: edwar
"""
from math import ceil,floor
from copy import deepcopy
import heapq
from random import randint

roomMap = {0:'A',1:'A',2:'B',3:'B',4:'C',5:'C',6:'D',7:'D'}
revMap = {'A':[0,1],
          'B':[2,3],
          'C':[4,5],
          'D':[6,7]}
costMap = {'A':1,
           'B':10,
           'C':100,
           'D':1000}
roomEnds = [8,9,9.5,10,10.5,11,11.5,12,12.5,13,14]

class GameBoard:
    def __init__(self,state):
        self.state = state
        self.score = 0
        self.minScore = self.potentialScore()
        
    def identifyMoves(self):
        toMove = [ii for ii in range(15) if self.state[ii] is not None]
        allMoves = dict()
        for amp in toMove:
            if amp<8:
                if amp%2==1 and (self.state[amp-1] is not None or roomMap[amp]==self.state[amp]):
                    continue
                elif amp%2==0 and roomMap[amp]==self.state[amp] and roomMap[amp]==self.state[amp+1]:
                    continue
                roomExit = amp//2+9.5
                lowerBlock = max([ii for ii in range(8,ceil(roomExit)) if self.state[ii] is not None]+[7])
                upperBlock = min([ii for ii in range(ceil(roomExit),15) if self.state[ii] is not None]+[15])
                finishSlots = list(range(lowerBlock+1,upperBlock))
            else:
                targetRoom = revMap[self.state[amp]]
                roomExit = targetRoom[0]//2+9.5
                if amp>roomExit and any([self.state[ii] for ii in range(ceil(roomExit),amp)]):
                    continue
                elif amp<roomExit and any([self.state[ii] for ii in range(amp+1,ceil(roomExit))]):
                    continue
                elif self.state[targetRoom[1]] is None:
                    finishSlots = [targetRoom[1]]
                elif self.state[targetRoom[0]] is None and self.state[targetRoom[1]]==self.state[amp]:
                    finishSlots = [targetRoom[0]]
                else:
                    continue
                
            allMoves[amp] = finishSlots
        return allMoves
    
    def isComplete(self):
        return self.state==['A','A','B','B','C','C','D','D']+[None]*7
    
    def potentialScore(self):
        toMove = [ii for ii in range(15) if self.state[ii] is not None]
        totalScore = self.score
        for amp in toMove:
            ampName = self.state[amp]
            if amp<8:
                if amp%2==1 and roomMap[amp]==ampName:
                    continue
                elif amp%2==1 and self.state[revMap[ampName][1]]!=ampName: # If the deepest member of the room isn't correct
                    totalScore += costMap[ampName]*(min([moveCost(amp,x)+moveCost(x,revMap[ampName][0]) for x in range(10,13)])+0.5)
                elif amp%2==1:
                    totalScore += costMap[ampName]*min([moveCost(amp,x)+moveCost(x,revMap[ampName][0]) for x in range(10,13)])
                elif roomMap[amp]==ampName and self.state[amp+1]==ampName: # In correct place and so is other room member
                    continue
                elif roomMap[amp]==ampName: # Correct place but other is not correct
                    totalScore += costMap[ampName]*4.5
                elif self.state[revMap[ampName][1]]!=ampName:
                    totalScore += costMap[ampName]*(min([moveCost(amp,x)+moveCost(x,revMap[ampName][0]) for x in range(10,13)])+0.5)
                else:
                    totalScore += costMap[ampName]*min([moveCost(amp,x)+moveCost(x,revMap[ampName][0]) for x in range(10,13)])
            else:
                if self.state[revMap[ampName][1]]==ampName:
                    totalScore += costMap[ampName]*moveCost(amp,revMap[ampName][0])
                else:
                    totalScore += costMap[ampName]*(moveCost(amp,revMap[ampName][0])+0.5)
        return totalScore
    
    def __lt__(self,other):
        return self.minScore<other.minScore
    
    def __gt__(self,other):
        return self.minScore>other.minScore
    
def moveCost(a,b):
    if b<8:
        a,b=b,a
    assert a<8 and b>=8
    cost = 1+(a%2) # To the end of the row
    roomExit = a//2+9.5
    if b>roomExit:
        cost+= len([x for x in roomEnds if x>roomExit and x<=b])
    else:
        cost+= len([x for x in roomEnds if x<roomExit and x>=b])
    return cost
            

f = open("input/day23.in")
f.readline()
f.readline()
p =  f.readline().strip().strip("#").split("#")
p += f.readline().strip().strip("#").split("#")
board = [p[y+4*x] for y in range(4) for x in range(2)] + [None]*7
allBoards = []
heapq.heappush(allBoards,GameBoard(board))
visitedBoards = set(tuple(allBoards[0].state))
minScore=99999999999999
i=0
while len(allBoards)>0:
    thisBoard = heapq.heappop(allBoards)
    if thisBoard.minScore>minScore:
        continue
    allMoves = thisBoard.identifyMoves()
    for a in allMoves.keys():
        for b in allMoves[a]:
            newBoard = deepcopy(thisBoard)
            newBoard.score += moveCost(a,b)*costMap[newBoard.state[a]]
            newBoard.state[b],newBoard.state[a] = newBoard.state[a],newBoard.state[b]
            newBoard.minScore = newBoard.potentialScore()
            tupleState = tuple(newBoard.state)
            if newBoard.isComplete():
                minScore = min(minScore,newBoard.score)
            elif newBoard.minScore<minScore and tupleState not in visitedBoards:
                heapq.heappush(allBoards,newBoard)
                visitedBoards.add(tupleState)
print(minScore)

