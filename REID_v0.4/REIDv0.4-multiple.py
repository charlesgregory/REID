#!/usr/bin/python

import tkinter
from tkinter import *
from Bio import SeqIO
import xlwt
import os
import shutil
from tkinter.filedialog import askdirectory

top = Tk()
top.title('Virtual Restriction Enzyme Digest')
top.geometry("800x350+250+100")



CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()
CheckVar10 = IntVar()
C1 = Checkbutton(top, text="EcoRI", variable=CheckVar1,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C2 = Checkbutton(top, text="BamHI", variable=CheckVar2,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C3 = Checkbutton(top, text="HindIII", variable=CheckVar3,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C4 = Checkbutton(top, text="SmaI", variable=CheckVar4,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C5 = Checkbutton(top, text="PvuII", variable=CheckVar5,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C6 = Checkbutton(top, text="EcoRV", variable=CheckVar6,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C7 = Checkbutton(top, text="XbaI", variable=CheckVar7,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C8 = Checkbutton(top, text="ClaI", variable=CheckVar8,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C9 = Checkbutton(top, text="Sites", variable=CheckVar9,
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C10 = Checkbutton(top, text="Fragments", variable=CheckVar10,
                  onvalue=1, offvalue=0, height=5,
                  width=20)
C1.grid(row=1, column=0)
C2.grid(row=1, column=1)
C3.grid(row=1, column=2)
C4.grid(row=1, column=3)
C5.grid(row=2, column=0)
C6.grid(row=2, column=1)
C7.grid(row=2, column=2)
C8.grid(row=2, column=3)
C9.grid(row=3, column=1)
C10.grid(row=3, column=2)
RElist = [["EcoRI", "gaattc", 1], ["BamHI", "ggatcc", 1], ["HindIII", "aagctt", 1], ["SmaI", "cccggg", 1],
          ["PvuII", "cagctg", 3], ["EcoRV", "gatatc", 3], ["XbaI", "tctaga", 1], ["ClaI", "atcgat", 2]]

def open_file():
    filename = askdirectory()
    entry.delete(0, END)
    entry.insert(0, os.path.normpath(filename))
    print(entry.get())

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
def close_program():
    top.destroy()

def process_file():
    dst = "C:\\Users\\musta_000\\Desktop\\REID\\REID_v0.4\\"
    src = os.path.normpath(entry.get())
    if os.path.isdir(dst):
        copytree(src, dst)

def collectfile():
    top = "."
    workbook = xlwt.Workbook()
    for files in os.walk(top, topdown=False):
        list = files[2]
        index5 = 0
        while index5 < len(list):
            string = list[index5]
            if not string.find(".fasta") > 0:
                list.remove(string)
                index5 += -1
            index5 += 1
    global list
    global workbook
def program():
    collectfile()
    index5 = 0
    while index5 < len(list):
        sheet = workbook.add_sheet(list[index5])
        REcurrentlist = []
        index1=0
        if CheckVar1.get() == 1:
            REcurrentlist.insert(index1, RElist[0])
            index1 += 1
        if CheckVar2.get() == 1:
            REcurrentlist.insert(index1, RElist[1])
            index1 += 1
        if CheckVar3.get() == 1:
            REcurrentlist.insert(index1, RElist[2])
            index1 += 1
        if CheckVar4.get() == 1:
            REcurrentlist.insert(index1, RElist[3])
            index1 += 1
        if CheckVar5.get() == 1:
            REcurrentlist.insert(index1, RElist[4])
            index1 += 1
        if CheckVar6.get() == 1:
            REcurrentlist.insert(index1, RElist[5])
            index1 += 1
        if CheckVar7.get() == 1:
            REcurrentlist.insert(index1, RElist[6])
            index1 += 1
        if CheckVar8.get() == 1:
            REcurrentlist.insert(index1, RElist[7])
            index1 += 1
        for usrseq in SeqIO.parse(list[index5], "fasta"):
            gtc =(usrseq.seq.lower())
            column = 0
            index3 = 0
            if CheckVar9.get() == 1:
                row = 0
                sheet.write(row, column, "Sites")
                column += 1
                for item in REcurrentlist:
                    index2 = 0
                    row = 0
                    sheet.write(row, column, REcurrentlist[index3][0])
                    row += 1
                    while index2 < len(gtc):
                        index2 = gtc.find(REcurrentlist[index3][1], index2)
                        if index2 == -1:
                            break
                        sheet.write(row, column, index2 + REcurrentlist[index3][2])
                        index2 += 6
                        row += 1
                    index3 +=1
                    column += 1
                index3 = 0
            if CheckVar10.get() == 1:
                row = 0
                sheet.write(row, column, "Fragments")
                column += 1
                for item in REcurrentlist:
                    index2 = 0
                    row = 0
                    sheet.write(row, column, REcurrentlist[index3][0])
                    row += 1
                    sheet.write(row, column, gtc.find(REcurrentlist[index3][1], index2)+REcurrentlist[index3][2])
                    row += 1
                    while index2 < len(gtc):
                        index2 = gtc.find(REcurrentlist[index3][1], index2)
                        index4 = index2+6
                        index4 = gtc.find(REcurrentlist[index3][1], index4)
                        if index2 == -1:
                            break
                        if index4 < 0:
                            break
                        sheet.write(row, column, index4-(index2 + REcurrentlist[index3][2]))
                        index2 += 6
                        row += 1
                    sheet.write(row, column, len(gtc)-gtc.rfind(REcurrentlist[index3][1]))
                    row += 1
                    index3 += 1
                    column += 1
                row = 0
                sheet.write(row, column, "length")
                row += 1
                sheet.write(row, column, len(gtc))
                row += 1
                index5 += 1
    workbook.save("Restriction Digest.xls")
    close_program()

entry = Entry(width=50)
entry.grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=2)
Button(text="Move File", width=32, command=process_file).grid(row=4, column=1, sticky='ew', padx=5, pady=5)
Button(text="Browse", command=open_file).grid(row=0, column=3, sticky='ew', padx=8, pady=4)
B = tkinter.Button(top, text="Analyze", command=program)
B.grid(row=4, column=1, columnspan=3)
top.mainloop()



