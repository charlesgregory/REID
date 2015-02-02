import xlrd
import subprocess
bins = [100, 150, 200, 300, 400, 500, 600, 700, 800]
bins2 = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
bins3 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
bins4 = [1000, 5000, 8000, 10000, 12000, 15000, 18000, 20000]
workbook = xlrd.open_workbook("Restriction Digest.xls")
sheets = workbook.sheet_names()
index = 0
file = open("Data.txt", "w")
for sheet in sheets:
    file.write("%s\n\n" % sheet)
    worksheet = workbook.sheet_by_name(sheets[index])
    index2 = 0
    while index2 < worksheet.ncols:
        index3 = 0
        column = worksheet.col(index2)
        bin100 = []
        bin150 = []
        bin200 = []
        bin300 = []
        bin400 = []
        bin500 = []
        bin600 = []
        bin700 = []
        bin800 = []
        binsid = [bin100, bin150, bin200, bin300, bin400, bin500, bin600, bin700, bin800]
        while index3 < len(column):
            cell = worksheet.cell_value(index3, index2)
            if isinstance(cell,str) == False:
                index4 = 0
                while index4 < len(bins):
                    if cell < bins[index4]:
                        write = binsid[index4]
                        write.append(cell)
                        index3 += 1
                        index4 = 100
                    else:
                        index4 += 1
                index3 += 1
                    
            else:
                index3 += 1
                if cell != '':
                    file.write("%s\n" % cell)
        binsid = str(binsid)
        binsid = binsid.replace('[]','0')
        file.write("%s\n" % binsid)
        index2 += 1
    index += 1
file.close()
subprocess.call("Data.txt", shell=True)
