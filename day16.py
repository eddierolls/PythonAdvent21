# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:49:03 2021

@author: edwar
"""

binMap = {'0' : '0000',
          '1' : '0001',
          '2' : '0010',
          '3' : '0011',
          '4' : '0100',
          '5' : '0101',
          '6' : '0110',
          '7' : '0111',
          '8' : '1000',
          '9' : '1001',
          'A' : '1010',
          'B' : '1011',
          'C' : '1100',
          'D' : '1101',
          'E' : '1110',
          'F' : '1111'}

def toNumber(binIn):
    return sum([2**x for x in range(len(binIn)) if binIn[-x-1]=='1'])

def unpackLiteral(p):
    literalDigits = p[1:5]
    p = p[5:]
    return literalDigits,p
    
def parsePacket(p):
    version = toNumber(p[0:3])
    p = p[3:]
    literalValue = -9999
    typeId = toNumber(p[:3])
    p = p[3:]
    if typeId==4: # Literal packet
        literalDigits = ''
        while p[0]=='1':
            thisLiteral,p = unpackLiteral(p)
            literalDigits+=thisLiteral
        thisLiteral,p = unpackLiteral(p)
        literalDigits+=thisLiteral
        literalValue = toNumber(literalDigits)
    else:
        lengthType = p[0]
        p = p[1:]
        literalValues = []
        if lengthType=='0':
            totalLength = toNumber(p[:15])
            p = p[15:]
            pToParse = p[:totalLength]
            p = p[totalLength:]
            while len(pToParse)>0:
                thisVersion,thisLiteral,pToParse = parsePacket(pToParse)
                version+=thisVersion
                literalValues.append(thisLiteral)
        else:
            totalPackets = toNumber(p[:11])
            p = p[11:]
            for _ in range(totalPackets):
                thisVersion,thisLiteral,p = parsePacket(p)
                version+=thisVersion
                literalValues.append(thisLiteral)
        if typeId==0:
            literalValue = sum(literalValues)
        elif typeId==1:
            literalValue = 1
            for v in literalValues:
                literalValue*=v
        elif typeId==2:
            literalValue=min(literalValues)
        elif typeId==3:
            literalValue=max(literalValues)
        elif typeId==5:
            literalValue = int(literalValues[0]>literalValues[1])
        elif typeId==6:
            literalValue = int(literalValues[0]<literalValues[1])
        elif typeId==7:
            literalValue = int(literalValues[0]==literalValues[1])
    return version,literalValue,p
        
    
f = open("input/day16.in")
puzzle = f.readline().strip()
# puzzle = '9C0141080250320F1802104A08'
puzzle = ''.join([binMap[s] for s in puzzle])
print(parsePacket(puzzle)[:2])

