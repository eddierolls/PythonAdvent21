# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 19:50:10 2021

@author: edwar
"""

# Part 1
f = open("input/day8.in")
totalCount = 0
for line in f:
    totalCount += len([x for x in line.strip().split(" | ")[1].split(" ") if len(x) in [2,3,4,7]])
print(totalCount)

# Part 2 - probably a more elegant solution with ERO and projection mappings
f = open("input/day8.in")
totalCount = 0
for line in f:
    puzzle,solution = map(lambda x: x.split(" "),line.strip().split(" | "))
    puzzle = [''.join(sorted(x)) for x in puzzle]
    puzzle.sort(key = lambda x:len(x))
    solution = [''.join(sorted(x)) for x in solution]
    correspondsTo = [1,7,4]+[-1]*6+[8]
    # 5 liners
    correspondsTo[[x for x in range(3,6) if len([y for y in range(len(puzzle[0])) if puzzle[0][y] in puzzle[x]])==2][0]]=3 # All of the lines in 1 are also in 3
    correspondsTo[[x for x in range(3,6) if len([y for y in range(len(puzzle[2])) if puzzle[2][y] in puzzle[x]])==2][0]]=2 # Two of the lines in 4 are also in 2
    correspondsTo[correspondsTo[:6].index(-1)]=5 # The other 5 liner
    # 6 liners
    correspondsTo[[x for x in range(6,9) if len([y for y in range(len(puzzle[2])) if puzzle[2][y] in puzzle[x]])==4][0]]=9 # All of the lines in 4 are also in 9
    correspondsTo[[x for x in range(6,9) if len([y for y in range(len(puzzle[1])) if puzzle[1][y] in puzzle[x]])==2][0]]=6 # Two of the lines in 6 are also in 7
    correspondsTo[correspondsTo.index(-1)]=0
    
    ans = [-1]*4
    for ii in range(4):
        ans[ii] = correspondsTo[puzzle.index(solution[ii])]*(10**(3-ii))
    totalCount+=sum(ans)
print(totalCount)