# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:45:03 2021

@author: edwar
"""
from collections import deque

# Part A
f = open("input/day1.in")
reading = int(f.readline())
increases = 0
for line in f:
    newReading = int(line)
    increases += (reading<newReading)
    reading = newReading

print(increases)

# Part B
f = open("input/day1.in")
increases = 0
queue = deque([int(f.readline()) for _ in range(3)])
for line in f:
    oldVal = queue.popleft()
    queue.append(int(line))
    increases+=(oldVal<queue[-1])
print(increases)
    
