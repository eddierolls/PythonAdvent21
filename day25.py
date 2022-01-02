# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:06:51 2021

@author: edwar
"""
from copy import deepcopy

charMap = {'.':None,'>':"r",'v':"d"}

f = open("input/day25.in")
board = []
for line in f:
    line = [charMap[s] for s in line.strip()]
    board.append(line)
dims = (len(board),len(board[0]))

t = 0
movesMade = True
while movesMade:
    movesMade = False
    t+=1
    newBoard = deepcopy(board)
    for y in range(dims[1]):
        for x in [x for x in range(dims[0]) if board[x][y]=='r' and board[x][(y+1)%dims[1]] is None]:
            newBoard[x][y] = None
            newBoard[x][(y+1)%dims[1]] = 'r'
            movesMade = True
    board = deepcopy(newBoard)
    
    for x in range(dims[0]):
        for y in [y for y in range(dims[1]) if board[x][y]=='d' and board[(x+1)%dims[0]][y] is None]:
            newBoard[x][y] = None
            newBoard[(x+1)%dims[0]][y] = 'd'
            movesMade = True
    board = deepcopy(newBoard)
    print(t)