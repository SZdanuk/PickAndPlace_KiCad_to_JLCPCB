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

with open('Wibra_2023_PCB_ana_compact-top.pos') as f:
    FileTextLines = f.readlines()

    print(FileTextLines[lineNumber])

DesignatorsTable = ['C', 'R', 'D', 'U', 'L', 'Q']
PPtable = ["Ref", "Val", "Package", "PosX", "PosY", "Rot", "Side"]
PPOutputTable = ["Designator", "Mid X", "Mid Y", "Layer", "Rotation"]
PPOutput = np.full((len(FileTextLines), len(PPtable)), '#empty_cell')
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

                PPOutput[lineNumber][columnIterator] = FileTextLines[lineNumber][wordBegin:wordEnd]
                if PPtable[columnIterator] == 'PosX' or PPtable[columnIterator] == 'PosY':
                    PPOutput[lineNumber][columnIterator] += "mm"

                columnIterator += 1
            break
    lineNumber += 1

print(PPOutput)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('PickAndPlaceFile_generated.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

#Write title:
for firstRow in PPOutputTable:
    worksheet.write(row, col, firstRow)
    col += 1
col = 0

#Write first column:
#for designator in PPOutputTable:
#    if PPtable == "Designator":
#while col < len(PPOutputTable):
#    row = 0
#    while row < len(FileTextLines):
#        worksheet.write(row, col, PPOutput[row][col])
#        row += 1
#    col += 1


# Write a total using a formula.
#worksheet.write(row, 0, 'Total')
#worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()