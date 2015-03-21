import xlrd
import subprocess
import math

file = open("Data.txt", "w")

#Finds the resolution distance in bps based off the position
#in pixels
time = 45
voltage = 100
agarose = 0.8
def reverse(pos, time, voltage, agarose):
    time = float(time)
    voltage = float(voltage)
    agarose = float(agarose)
    maxDist = 0.25 * time * voltage
    optimumLength = 2000/agarose ** 3
    def reverseEquation(c, t):
        b = 1.0 / t
        c = float(pos)
        x = 0.0
        x += (math.log(c/maxDist) * 20)/-b
        return x
    g = reverseEquation(pos, optimumLength/20)
    length = int(g)
    return length


#Finds position of fragments (in pixels) of a simulated gel digest
#the resolution distance is 4 pixels
def analyze(length, time, voltage, agarose):
    length = float(length)
    time = float(time)
    voltage = float(voltage)
    agarose = float(agarose)
    def equation(x, t, k=1):
        b = 1.0 / t
        x = x * k
        c = 0.0
        c += math.exp(-b * x)
        return c
    optimumLength = 2000/agarose ** 3
    g = equation(length/20, optimumLength/20)
    maxDist = 0.25 * time * voltage
    pos = maxDist * g
    return pos


#Groups fragments within resolution distance
workbook = xlrd.open_workbook("Restriction Digest.xls")
sheets = workbook.sheet_names()

for sheet in sheets:
    file.write("%s\n\n" % sheet)
    column = 0
    index = 0
    sheet = workbook.sheet_by_name(sheet)
    columnLengths = []
    while index < sheet.ncols:
        if sheet.cell_value(1, column) != "":
            columnLengths.append(sheet.cell_value(1, column))
        column += 1
        index += 1
    repLen = min(columnLengths)
    repLen = int(repLen)
    repCol = columnLengths.index(repLen)+1
    repLen2 = max(columnLengths)
    repLen2 = int(repLen2)
    repCol2 = columnLengths.index(repLen2)+1
    index2 = 2
    index6 = 0
    while index2 < repLen+2:
        repCell = sheet.cell_value(index2, repCol)
        repCell2 = int(sheet.cell_value(1, repCol2))
        repCell = float(repCell)
        bpPos = analyze(repCell,time,voltage,agarose)
        if bpPos - 4 <= 0:
                bpPos = 4.00000001
        bpRange = [reverse(bpPos+4.0, time, voltage, agarose), reverse(bpPos-4.0,time,voltage,agarose)]
        if bpRange[0] < 0:
            bpRange[0] = 0.0
        column2 = 1
        index4 = 0
        print(bpRange)
        while column2 <= sheet.ncols - 1:
            length = sheet.cell_value(1, column2)
            length = int(length)
            index5 = 0
            row = (length//2)+1
            while 2 < 3:
                if row > length + 1:
                    column2 +=1
                    break
                cell = sheet.cell_value(row, column2)
                if isinstance(cell,str) == True:
                    column2 += 1
                    break
                if column2 == repCol:
                    column2 += 1
                    break
                if cell == 0:
                    column2 +=1
                    break
                if row <= 1:
                    column2 += 1
                    break
                if bpRange[0] <= cell <= bpRange[1]:
                    column2 += 1
                    index4 += 1
                    break
                if index5 > (repCell2 // 2) + 2:
                    column2 += 1
                    break

                elif cell < bpRange[0]:
                    row += 1
                    index5 += 1

                elif cell > bpRange[1]:
                    row -= 1
                    index5 += 1


        if index4 == sheet.ncols - 2:
            file.write(str(bpRange))
            file.write("\n")
            index6 += 1
        index2 += 1
    if index6 == 0:
        file.write("No ranges found\n")
    file.write("\n")







file.close()
subprocess.call("Data.txt", shell=True)
