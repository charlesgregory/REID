#!/usr/bin/python

import tkinter
from tkinter import *
from Bio import SeqIO
import xlwt
import os
import shutil
from tkinter.filedialog import askdirectory
import csv

#GUI Settings
top = Tk()
top.title('Virtual Restriction Enzyme Digest')
top.geometry("800x350+250+100")


#Sets checkbox variables
CheckVar9 = IntVar()
CheckVar10 = IntVar()

#Sets each Checkbox
C9 = Checkbutton(top, text="Sites", variable=CheckVar9,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C10 = Checkbutton(top, text="Fragments", variable=CheckVar10,
                  onvalue=1, offvalue=0, height=5,
                  width=20)


C9.grid(row=3, column=1)
C10.grid(row=3, column=2)

RElist = []
with open("RElist.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        RElist.append(line)
    print(RElist)

#shows file in box
def open_file():
    filename = askdirectory()
    entry.delete(0, END)
    entry.insert(0, os.path.normpath(filename))
    print(entry.get())

#copies files
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

#closes program
def close_program():
    top.destroy()

#moves files to directory
def process_file():
    dst = "C:\\Users\\musta_000\\Desktop\\REID\\REID_v0.5.2\\phages\\"
    src = os.path.normpath(entry.get())
    if os.path.isdir(dst):
        copytree(src, dst)

#reads files in directory
def collectfile():
    top = "."
    workbook = xlwt.Workbook()
    for files in os.walk("phages\\", topdown=False):
        list1 = files[2]
        index5 = 0
        while index5 < len(list1):
            string = list1[index5]
            if not string.find(".fasta") > 0:
                list1.remove(string)
                index5 += -1
            index5 += 1
    global list1
    global workbook

#Checks the checkboxes and creates a list of the used restriction enzymes
def program():
    collectfile()
    index5 = 0
    index3 = 0
    while index3 < len(RElist)-1:
        sheet = workbook.add_sheet(RElist[index3][0])
        #Parses each fasta file
        column = 0
        if CheckVar9.get() == 1:
            row = 0
            sheet.write(row, column, "Sites")
            column += 1
            for item in list1:
                for usrseq in SeqIO.parse("phages\\"+item, "fasta"):
                    gtc = (usrseq.seq.lower())
                    index2 = 0
                    row = 0
                    sheet.write(row, column, item)
                    row += 1
                    while index2 < len(gtc):
                        index2 = gtc.find(RElist[index3][1], index2)
                        if index2 == -1:
                            break
                        sheet.write(row, column, index2 + RElist[index3][2])
                        index2 += len(RElist[index3][1])
                        row += 1
                    column += 1
        if CheckVar10.get() == 1:
            row = 0
            sheet.write(row, column, "Fragments")
            column += 1
            for item in list1:
                print(item)
                for usrseq in SeqIO.parse("phages\\"+item, "fasta"):
                    writelist1 = []
                    gtc =(usrseq.seq.upper())
                    index2 = 0
                    row = 0
                    sheet.write(row, column, item)
                    row += 1
                    writelist1.append(gtc.find(RElist[index3][1], index2)+int(RElist[index3][2]))

                    while index2 < len(gtc):
                        index2 = gtc.find(RElist[index3][1], index2)
                        index4 = index2+6
                        index4 = gtc.find(RElist[index3][1], index4)
                        if index2 == -1:
                            break
                        if index4 < 0:
                            break
                        writelist1.append((index4 + int(RElist[index3][2]))-(index2 + int(RElist[index3][2])))
                        index2 += 6
                    writelist1.append(len(gtc)-(gtc.rfind(RElist[index3][1]) + int(RElist[index3][2])))
                    sheet.write(row, column, len(writelist1))
                    row += 1
                    writelist1.sort()
                    for item in writelist1:
                        sheet.write(row, column, item)
                        row += 1
                    column += 1
            index3 += 1
    workbook.save("Restriction Digest.xls")
    close_program()

#GUI setup
entry = Entry(width=50)
entry.grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=2)
Button(text="Move File", width=32, command=process_file).grid(row=4, column=1, sticky='ew', padx=5, pady=5)
Button(text="Browse", command=open_file).grid(row=0, column=3, sticky='ew', padx=8, pady=4)
B = tkinter.Button(top, text="Analyze", command=program)
B.grid(row=4, column=1, columnspan=3)
top.mainloop()



