# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 10:59:50 2021

@author: edwar
"""
from math import ceil
from copy import deepcopy
import heapq
import string

BOARDSIZE = 4

roomMap = {x:string.ascii_uppercase[x//BOARDSIZE] for x in range(4*BOARDSIZE)}
revMap = {string.ascii_uppercase[x]:list(range(x*BOARDSIZE,(x+1)*BOARDSIZE)) for x in range(4)}
costMap = {'A':1,
           'B':10,
           'C':100,
           'D':1000}
roomEnds = list(sorted(list(range(BOARDSIZE*4,BOARDSIZE*4+7))+[x+0.5 for x in range(BOARDSIZE*4+1,BOARDSIZE*4+5)]))

class GameBoard:
    def __init__(self,state):
        self.state = state
        self.score = 0
        self.minScore = self.potentialScore()
        
    def canMove(self):
        toMove = [ii for ii in range(BOARDSIZE*4,BOARDSIZE*4+7) if self.state[ii] is not None] # Corridoors
        for room in string.ascii_uppercase[:4]:
            nextRoom = [x for x in revMap[room] if self.state[x] is not None]
            if len(nextRoom)==0:
                continue
            amp = min(nextRoom)
            if not all([self.state[x]==room for x in range(amp,max(revMap[room])+1)]):
                toMove.append(amp)
        return toMove
    
    def identifyMoves(self):
        toMove = self.canMove()
        allMoves = dict()
        for amp in toMove:
            if amp<BOARDSIZE*4:
                roomExit = amp//BOARDSIZE+1.5+BOARDSIZE*4
                lowerBlock = max([ii for ii in range(BOARDSIZE*4,ceil(roomExit)) if self.state[ii] is not None]+[BOARDSIZE*4-1])
                upperBlock = min([ii for ii in range(ceil(roomExit),BOARDSIZE*4+7) if self.state[ii] is not None]+[BOARDSIZE*4+7])
                finishSlots = list(range(lowerBlock+1,upperBlock))
            else:
                targetRoom = revMap[self.state[amp]]
                roomExit = targetRoom[0]//BOARDSIZE+1.5+BOARDSIZE*4
                if amp>roomExit and any([self.state[ii] for ii in range(ceil(roomExit),amp)]):
                    continue
                elif amp<roomExit and any([self.state[ii] for ii in range(amp+1,ceil(roomExit))]):
                    continue
                nextRoom = [x for x in targetRoom if self.state[x] is None]
                if len(nextRoom)==0:
                    continue
                roomSlot = max(nextRoom)
                if all([self.state[x]==self.state[amp] for x in range(roomSlot+1,max(targetRoom)+1)]):
                    finishSlots = [roomSlot]
                else:
                    continue
                
            allMoves[amp] = finishSlots
        return allMoves
    
    def isComplete(self):
        return self.state==['A']*BOARDSIZE+['B']*BOARDSIZE+['C']*BOARDSIZE+['D']*BOARDSIZE+[None]*7
    
    def potentialScore(self):
        toMove = [ii for ii in range(BOARDSIZE*4,BOARDSIZE*4+7) if self.state[ii] is not None]
        roomAdd = {x:0 for x in string.ascii_uppercase[:4]}
        for room in string.ascii_uppercase[:4]:
            spaces = [x for x in revMap[room] if self.state[x]!=room]
            if len(spaces)==0:
                continue
            toMove+=[x for x in range(min(revMap[room]),max(spaces)+1) if self.state[x] is not None]
            roomAdd[room] = (max(spaces)-min(revMap[room]))/2
            
        totalScore = self.score
        for amp in toMove:
            ampName = self.state[amp]
            if amp<BOARDSIZE*4:
                totalScore += costMap[ampName]*(min([moveCost(amp,x)+moveCost(x,revMap[ampName][0]) for x in range(BOARDSIZE*4+2,BOARDSIZE*4+5)])+roomAdd[ampName])
            else:
                totalScore += costMap[ampName]*(moveCost(amp,revMap[ampName][0])+roomAdd[ampName])
        return totalScore
    
    def __lt__(self,other):
        return self.minScore<other.minScore
    
    def __gt__(self,other):
        return self.minScore>other.minScore
    
def moveCost(a,b):
    if b<BOARDSIZE*4:
        a,b=b,a
    assert a<BOARDSIZE*4 and b>=BOARDSIZE*4
    cost = 1+(a%BOARDSIZE) # To the end of the row
    roomExit = a//BOARDSIZE+1.5+BOARDSIZE*4
    if b>roomExit:
        cost+= len([x for x in roomEnds if x>roomExit and x<=b])
    else:
        cost+= len([x for x in roomEnds if x<roomExit and x>=b])
    return cost

f = open("input/day23.in")
f.readline()
f.readline()
p =  f.readline().strip().strip("#").split("#")
if BOARDSIZE==4:
    p += ["D","C","B","A"]
    p += ["D","B","A","C"]
p += f.readline().strip().strip("#").split("#")
board = [p[y+4*x] for y in range(4) for x in range(BOARDSIZE)] + [None]*7
board = GameBoard(board)
allBoards = []
heapq.heappush(allBoards,board)
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
    if i%1000 == 0:
        print(i,minScore,len(allBoards),allBoards[0].minScore)
    i+=1
print(minScore)

