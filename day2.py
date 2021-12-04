# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:10:38 2021

@author: edwar
"""

pos = [0,0]
directions = {"forward":(0,1),
              "down"   :(1,1),
              "up"     :(1,-1)} # The axes then the multiplier

f = open("input/day2.in")
for line in f:
    commands = line.split()
    pos[directions[commands[0]][0]] += directions[commands[0]][1]*int(commands[1])

print(pos[0]*pos[1])

# Part 2
pos = [0,0,0] # Aim,position,depth
f = open("input/day2.in")
for line in f:
    commands = line.split()
    if commands[0]=="down":
        pos[0]+=int(commands[1])
    elif commands[0]=="up":
        pos[0]-=int(commands[1])
    elif commands[0]=="forward":
        pos[1]+=int(commands[1])
        pos[2]+=int(commands[1])*pos[0]

print(pos[2]*pos[1])