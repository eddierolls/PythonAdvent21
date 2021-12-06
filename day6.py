# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:16:09 2021

@author: edwar
"""

f = open("input/day6.in")
numbers = list(map(int,f.readline().split(',')))
numbers = [numbers.count(x) for x in range(9)]
for _ in range(80):
    numbers = numbers[1:7] + [numbers[0]+numbers[7]] + [numbers[8]] + [numbers[0]]

print(sum(numbers))

f = open("input/day6.in")
numbers = list(map(int,f.readline().split(',')))
numbers = [numbers.count(x) for x in range(9)]
for _ in range(256):
    numbers = numbers[1:7] + [numbers[0]+numbers[7]] + [numbers[8]] + [numbers[0]]

print(sum(numbers))