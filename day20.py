# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 19:32:42 2021

@author: edwar
"""
def getDims(arr):
    return (len(arr),len(arr[0]))

def addImageBorders(image,border):
    dims = getDims(image)
    image.insert(0,[border]*dims[1])
    image.append([border]*dims[1])
    for line in image:
        line.insert(0,border)
        line.append(border)

def binToInt(b): # Specific to question format
    return sum([2**(len(b)-1-x) for x in range(len(b)) if b[x]=='#'])

f = open("input/day20.in")
numberMap = list(f.readline().strip())
f.readline()
image = []
for line in f:
    image.append(list(line.strip()))

currentBorder = '.'
addImageBorders(image,currentBorder)
for _ in range(2):
    addImageBorders(image,currentBorder)
    dims = getDims(image)
    if currentBorder=='.' and numberMap[0]=='#':
        currentBorder='#'
    elif currentBorder=='#' and numberMap[-1]=='.':
        currentBorder='.'
    newImage = [[currentBorder]*dims[1] for _ in range(dims[0])]
    for x in range(1,dims[0]-1):
        for y in range(1,dims[1]-1):
            subImage = [image[x-1+(z//3)][y-1+(z%3)] for z in range(9)]
            newImage[x][y] = numberMap[binToInt(subImage)]
    image = newImage

totalCount = sum([x.count('#') for x in image])
print(totalCount)

for _ in range(48):
    addImageBorders(image,currentBorder)
    dims = getDims(image)
    if currentBorder=='.' and numberMap[0]=='#':
        currentBorder='#'
    elif currentBorder=='#' and numberMap[-1]=='.':
        currentBorder='.'
    newImage = [[currentBorder]*dims[1] for _ in range(dims[0])]
    for x in range(1,dims[0]-1):
        for y in range(1,dims[1]-1):
            subImage = [image[x-1+(z//3)][y-1+(z%3)] for z in range(9)]
            newImage[x][y] = numberMap[binToInt(subImage)]
    image = newImage

totalCount = sum([x.count('#') for x in image])
print(totalCount)