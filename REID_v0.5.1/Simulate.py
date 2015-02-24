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
index = 0
for sheet in sheets:
    file.write("%s\n\n" % sheet)
    worksheet = workbook.sheet_by_name(sheets[index])
    index2 = 0
    while index2 < worksheet.ncols:
        index3 = 0
        column = worksheet.col(index2)
        list1 = []
        while index3 < len(column):
            cell = worksheet.cell_value(index3, index2)
            if isinstance(cell,str) == False:
                index4 = 0
                list1.append(cell)
                index3 += 1
                    
            else:
                index3 += 1
                if cell != '':
                    file.write("%s\n" % cell)
        listPos = []
        listLength = []
        listRange = []
        listFinal = []
        list1.sort()
        for item in list1:
            a = analyze(item, time, voltage, agarose)
            listPos.append(a)
            print(listPos)
        for item in listPos:
            if item - 4 <= 0:
                item = 4.00000001
            b = reverse(item - 4.0, time, voltage, agarose)
            c = reverse(item + 4.0, time, voltage, agarose)
            if c < 0:
                c = 0
            listLength.append([c, b])
            print(listLength)
        index5 = 0
        while index5 + 1 <= len(listLength)- 1:
            d = listLength[index5]
            e = listLength[index5 + 1]
            print(1)
            if e[0] >= d[0] and e[0] <= d[1]:
                index6 = index5 - 1
                if index6 < 0:
                    listFinal.append([[d[0], e[1]], int(listPos[index5]), int(listPos[index5 + 1])])
                    index5 += 1
                    print(2)
                if index6 >= 0:
                    f = listLength[index6]
                    if d[0] >= f[0] and d[0] <= f[1]:
                        listFinal.append([[f[0], e[1]], int(listPos[index6]), int(listPos[index5]), int(listPos[index5 + 1])])
                        index5 += 1
                        print(3)
                    else:
                        listFinal.append([[d[0], e[1]], int(listPos[index5]), int(listPos[index5 + 1])])
                        index5 += 1
                        print(4)


            else:
                index6 = index5 - 1
                if index6 < 0:
                    listFinal.append([list1[index5], int(listPos[index5])])
                    index5 += 1
                    print(5)
                if index6 >= 0:
                    f = listLength[index6]
                    if d[0] >= f[0] and d[0] <= f[1]:
                        listFinal.append([[f[0], d[1]], int(listPos[index6]), int(listPos[index5])])
                        index5 += 1
                        print(6)
                    else:
                        listFinal.append([list1[index5], int(listPos[index5])])
                        index5 += 1
                        print(7)
            print(index5)
            print(listFinal)
            print(len(listLength))

        index2 += 1
        listFinal = str(listFinal)
        file.write(listFinal)
        file.write("\n")
    index += 1
file.close()
subprocess.call("Data.txt", shell=True)
