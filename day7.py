# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:55:24 2021

@author: edwar
"""
from math import floor,ceil

f = open("input/day7.in")
# Part 1
x = list(sorted(map(int,f.readline().split(','))))
median = x[len(x)//2]
out = sum([abs(y-median) for y in x])
print(out)
# Part 2
# x = list(sorted(map(int,"16,1,2,0,4,2,7,1,2,14".split(','))))
mean1 = floor(sum(x)/len(x))
mean2 = ceil(sum(x)/len(x))
# The calculation isn't exact y = mean(x) + 1/n * sum(numbers less than mean minus numbers greater than mean) so try numbers +/-1
out1 = sum([abs(y-mean1)*(abs(y-mean1)+1)/2 for y in x])
out2 = sum([abs(y-mean2)*(abs(y-mean2)+1)/2 for y in x])
print(min(out1,out2))
