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

for i, col in enumerate([PPInputTitle.index("Ref"), PPInputTitle.index("PosX"), PPInputTitle.index("PosY"), PPInputTitle.index("Side"), PPInputTitle.index("Rot")]):
    row = 1
    for d in range(len(FileTextLines)):
        if '#empty_cell' not in PPOutputTable[d][col]:
            worksheet.write(row, i, PPOutputTable[d][col])
            row += 1

workbook.close()