# Converts ASCII to xls output
# Output should look like this:
# Designator MidX MidY Layer Rotation
# Assumptions:
# 1. no spaces in names
# 2. First is Designator not starts from space
import numpy as np
import xlsxwriter

lineNumber = 0
columnIterator = 0
i = 0
wordBegin = 0
wordEnd = 0

with open('PPinput.pos') as f:
    FileTextLines = f.readlines()

    print(FileTextLines[lineNumber])

DesignatorsTable = ['C', 'R', 'D', 'U', 'L', 'Q']
PPInputTitle = ["Ref", "Val", "Package", "PosX", "PosY", "Rot", "Side"]
PPOutputTitle = ["Designator", "Mid X", "Mid Y", "Layer", "Rotation"]
PPOutputTable = np.full((len(FileTextLines), len(PPInputTitle)), '#empty_cell')
Designator = []
Value = []
Package = []
Position_X = []
Position_Y = []
Rotation = []
Side = []

while lineNumber < (len(FileTextLines)):

    i = 0
    columnIterator = 0

    # checking if 1st letter contains designator type
    for designator in DesignatorsTable:
        if FileTextLines[lineNumber][0] == designator:
            while columnIterator < len(PPInputTitle):

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

                PPOutputTable[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]
                if PPInputTitle[columnIterator] in ['PosX', 'PosY']:
                    PPOutputTable[lineNumber][columnIterator] += "mm"

                columnIterator += 1
            break
    lineNumber += 1

#print(PPOutput)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('PickAndPlaceFile_generated.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Write title:
for i, val in enumerate(PPOutputTitle):
    worksheet.write(0, i, val)

# Write designators, PosX, PosY, Layer, Rotation:
for i, col in enumerate([0, 3, 4, 6, 5]):
    row = 1
    for d in range(len(FileTextLines)):
        if '#empty_cell' not in PPOutputTable[d][col]:
            worksheet.write(row, i, PPOutputTable[d][col])
            row += 1

#original:
'''
#Write title:
for firstRow in PPOutputTitle:
    worksheet.write(row, col, firstRow)
    col += 1

#Write designators:
row = 1
for d in range(len(FileTextLines)):
    if '#empty_cell' not in PPOutputTable[d][0]:
        worksheet.write(row, 0, PPOutputTable[d][0])
        row += 1

#Write PosX:
row = 1
for d in range(len(FileTextLines)):
    if '#empty_cell' not in PPOutputTable[d][3]:
        worksheet.write(row, 1, PPOutputTable[d][3])
        row += 1

#Write PosY:
row = 1
for d in range(len(FileTextLines)):
    if '#empty_cell' not in PPOutputTable[d][4]:
        worksheet.write(row, 2, PPOutputTable[d][4])
        row += 1

# Write Layer:
row = 1
for d in range(len(FileTextLines)):
    if '#empty_cell' not in PPOutputTable[d][6]:
        worksheet.write(row, 3, PPOutputTable[d][6])
        row += 1

# Write Rotation:
row = 1
for d in range(len(FileTextLines)):
    if '#empty_cell' not in PPOutputTable[d][5]:
        worksheet.write(row, 4, PPOutputTable[d][5])
        row += 1
'''

workbook.close()
