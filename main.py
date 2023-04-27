# Output should look like this:
# Designator MidX MidY Layer Rotation
# Assumptions:
# 1. no spaces in names
# 2. First is Designator not starts from space
import numpy as np

lineNumber = 0
columnIterator = 0
i = 0
wordBegin = 0
wordEnd = 0

with open('Wibra_2023_PCB_ana_compact-top.pos') as f:
    FileTextLines = f.readlines()

    print(FileTextLines[lineNumber])

DesignatorsTable = ['C', 'R', 'D', 'U', 'L', 'Q']
PPtable = ["Ref", "Val", "Package", "PosX", "PosY", "Rot", "Side"]
PPOutput = np.full((len(FileTextLines), len(PPtable)), '#empty')
Designator = []
Value = []
Package = []
Position_X = []
Position_Y = []
Rotation = []
Side = []



for designator in DesignatorsTable:
    if FileTextLines[lineNumber][i] == designator:
        break

while lineNumber < (len(FileTextLines)):

    i = 0
    columnIterator = 0

    while columnIterator < len(PPtable):

        while i < len(FileTextLines[lineNumber]):
            if FileTextLines[lineNumber][i] != ' ':
                wordBegin = i
                break
            i = i + 1

        while i < len(FileTextLines[lineNumber]):
            wordEnd = i
            if FileTextLines[lineNumber][i] == ' ':
                break
            i = i + 1

        if columnIterator == 0:
            PPOutput[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]
        if columnIterator == 1:
            PPOutput[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]
        if columnIterator == 2:
            PPOutput[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]
        if columnIterator == 3:
            PPOutput[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]
        if columnIterator == 4:
            PPOutput[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]
        if columnIterator == 5:
            PPOutput[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]
        if columnIterator == 6:
            PPOutput[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]

        columnIterator += 1
    lineNumber += 1
print(Designator)
print(Value)
print(Package)
print(Position_X)
print(Position_Y)
print(Rotation)
print(Side)
