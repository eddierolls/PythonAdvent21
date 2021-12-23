# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:30:56 2021

@author: edwar
"""
from math import ceil,floor
from copy import deepcopy

roomMap = {0:'A',1:'A',2:'B',3:'B',4:'C',5:'C',6:'D',7:'D'}
revMap = {'A':[0,1],
          'B':[2,3],
          'C':[4,5],
          'D':[6,7]}
costMap = {'A':1,
           'B':10,
           'C':100,
           'D':1000}

class GameBoard:
    def __init__(self,state):
        self.state = state
        self.score = 0
        
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
    
def moveCost(a,b):
    if b<8:
        a,b=b,a
    cost = 1+(a%2) # To the end of the row
    roomExit = a//2+9.5
    if b>roomExit:
        cost+= (b-floor(roomExit))
    else:
        cost+= (ceil(roomExit)-b)
    return cost
            

f = open("input/day23.test")
f.readline()
f.readline()
p =  f.readline().strip().strip("#").split("#")
p += f.readline().strip().strip("#").split("#")
board = [p[y+4*x] for y in range(4) for x in range(2)] + [None]*7
allBoards = [GameBoard(board)]
minScore=99999999999999
i=0
allStates = set()
while len(allBoards)>0:
    thisBoard = allBoards.pop()
    allMoves = thisBoard.identifyMoves()
    for a in allMoves.keys():
        for b in allMoves[a]:
            newBoard = deepcopy(thisBoard)
            newBoard.score += moveCost(a,b)*costMap[newBoard.state[a]]
            newBoard.state[b],newBoard.state[a] = newBoard.state[a],newBoard.state[b]
            if newBoard.isComplete():
                minScore = min(minScore,newBoard.score)
            elif newBoard.score<minScore:
                allBoards.append(newBoard)
                allStates.add(tuple(newBoard.state))
    i+=1
    print(i,len(allBoards),minScore)
            

