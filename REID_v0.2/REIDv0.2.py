#!/usr/bin/python

import tkinter
from tkinter import *

top = Tk()
top.title('Virtual Restriction Enzyme Digest')
top.geometry("700x300+250+100")
L1 = Label(top, text="File Name")
E1 = Entry(top, bd =5,textvariable = StringVar())
L1.grid(row=0,column=1)
E1.grid(row=0,column=2)


CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
C1 = Checkbutton(top, text = "EcoRI", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(top, text = "BamHI", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(top, text = "HindIII", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C4 = Checkbutton(top, text = "SmaI", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C5 = Checkbutton(top, text = "PvuII", variable = CheckVar5, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C6 = Checkbutton(top, text = "EcoRV", variable = CheckVar6, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C7 = Checkbutton(top, text = "XbaI", variable = CheckVar7, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C8 = Checkbutton(top, text = "ClaI", variable = CheckVar8, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.grid(row=1,column=0)
C2.grid(row=1,column=1)
C3.grid(row=1,column=2)
C4.grid(row=1,column=3)
C5.grid(row=2,column=0)
C6.grid(row=2,column=1)
C7.grid(row=2,column=2)
C8.grid(row=2,column=3)

from tkinter import messagebox
from Bio import SeqIO
import xlwt
def runprogram():
   for usrseq in SeqIO.parse(E1.get(), "fasta"):
      gtc =(usrseq.seq.lower())
      workbook = xlwt.Workbook()
      sheet = workbook.add_sheet("Digest",)
      column=0
      if CheckVar1.get() == 1:
         index=0
         row=0
         sheet.write(row,column,"EcoRI")
         row +=1
         while index < len(gtc):
            index = gtc.find("gaattc", index)#EcoRI
            if index ==-1:
               break
            sheet.write(row,column,index + 1)
            index += 6
            row+=1
         column +=1
      if CheckVar2.get() == 1:
         index=0
         row=0
         sheet.write(row,column,"BamHI")
         row +=1
         while index < len(gtc):
            index = gtc.find("ggatcc", index)#BamHI
            if index ==-1:
               break
            sheet.write(row,column,index + 1)
            index += 6
            row+=1
         column+=1
         pass
      if CheckVar3.get() == 1:
         index=0
         row=0
         sheet.write(row,column,"HindIII")
         row +=1
         while index < len(gtc):
            index = gtc.find("aagctt", index)#HindIII
            if index ==-1:
               break
            sheet.write(row,column,index + 1)
            index += 6
            row+=1
         column +=1
         pass
      if CheckVar4.get() == 1:
         index=0
         row=0
         sheet.write(row,column,"SmaI")
         row +=1
         while index < len(gtc):
            index = gtc.find("cccggg", index)#SmaI
            if index ==-1:
               break
            sheet.write(row,column,index + 1)
            index += 6
            row+=1
         column +=1
         pass
      if CheckVar5.get() == 1:
         index=0
         row=0
         sheet.write(row,column,"PvuII")
         row +=1
         while index < len(gtc):
            index = gtc.find("cagctg", index)#PvuII
            if index ==-1:
               break
            sheet.write(row,column,index + 3)
            index += 6
            row+=1
         column+=1
         pass
      if CheckVar6.get() == 1:
         index=0
         row=0
         sheet.write(row,column,"EcoRV")
         row +=1
         while index < len(gtc):
            index = gtc.find("gatatc", index)#EcoRV
            if index ==-1:
               break
            sheet.write(row,column,index + 3)
            index += 6
            row+=1
         column+=1
         pass
      if CheckVar7.get() == 1:
         index=0
         row=0
         sheet.write(row,column,"XbaI")
         row +=1
         while index < len(gtc):
            index = gtc.find("tctaga", index)#XbaI
            if index ==-1:
               break
            sheet.write(row,column,index + 1)
            index += 6
            row+=1
         column+=1
         pass
      if CheckVar8.get() == 1:
         index=0
         row=0
         sheet.write(row,column,"ClaI")
         row +=1
         while index < len(gtc):
            index = gtc.find("atcgat", index)#ClaI
            if index ==-1:
               break
            sheet.write(row,column,index + 2)
            index += 6
            row+=1
         column+=1
         
      row=0
      sheet.write(row,column,"length")
      row+=1
      sheet.write(row,column,len(gtc))
      row +=1
      workbook.save("Restriction Digest "+ E1.get()+".xls")

B = tkinter.Button(top, text ="Go", command = runprogram)
B.grid(row=3,column=1,columnspan=2)
top.mainloop()


