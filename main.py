DesignatorsTable = ['C', 'R', 'D', 'U', 'L', 'Q']
PPtable = [["Designator"]]

i = 5


with open('Wibra_2023_PCB_ana_compact-top.pos') as f:
    FileTextLines = f.readlines()

    print(FileTextLines[i])

    print(("PosX" in FileTextLines[i]) & ("PosX" in FileTextLines[i]))



