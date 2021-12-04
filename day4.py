# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:51:54 2021

@author: edwar
"""
import copy

def sub2ind(size,rows,cols):
    return rows+(cols*size[0])

def ind2sub(size,ind):
    return (ind%size[0],ind//size[0])

class Board:
    def __init__(self,board):
        self.rows = [len(board[0])]*len(board) # Numbers to be found per row
        self.cols = [len(board)]*len(board[0]) # numbers to be found per col
        self.numbers = [board[x][y] for x,y in [ind2sub([5,5],x) for x in range(25)]]
        self.numberSet = set(self.numbers)
        self.boardSize = (len(self.rows),len(self.cols))
    

f = open("input/day4.in")
numbers = list(map(int,f.readline().split(',')))
boards = []
currentBoard = []
f.readline()

for line in f:
    if line=='\n':
        boards.append(Board(currentBoard))
        currentBoard = []
    else:
        currentBoard.append([int(x) for x in line.split(' ') if x!=''])
        
score = -1
for ix in range(len(numbers)):
    x = numbers[ix]
    for ixBoard in range(len(boards)):
        board = boards[ixBoard]
        if x in board.numberSet:
            row,col = ind2sub(board.boardSize,board.numbers.index(x))
            board.rows[row]-=1
            board.cols[col]-=1
            if board.rows[row]==0 or board.cols[col]==0:
                score = sum(board.numberSet-set(numbers[:ix+1]))*x
    if score>0:
        break

print(score)
                
# Part 2
f = open("input/day4.in")
numbers = list(map(int,f.readline().split(',')))
boards = []
currentBoard = []
f.readline()

for line in f:
    if line=='\n':
        boards.append(Board(currentBoard))
        currentBoard = []
    else:
        currentBoard.append([int(x) for x in line.split(' ') if x!=''])
        
unfinishedBoards = set(range(len(boards)))
score = -1
for ix in range(len(numbers)):
    toRemove = set()
    x = numbers[ix]
    for ixBoard in unfinishedBoards:
        board = boards[ixBoard]
        if x in board.numberSet:
            row,col = ind2sub(board.boardSize,board.numbers.index(x))
            board.rows[row]-=1
            board.cols[col]-=1
            if board.rows[row]==0 or board.cols[col]==0:
                toRemove.add(ixBoard)
                if len(unfinishedBoards)-len(toRemove)==0:
                    score = sum(board.numberSet-set(numbers[:ix+1]))*x
                    break
    if score>0:
        break
    unfinishedBoards = unfinishedBoards-toRemove

print(score)


        