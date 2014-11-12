#!/usr/bin/python

import tkinter
from tkinter import *

top = Tk()
L1 = Label(top, text="File Name")
E1 = Entry(top, bd =5,textvariable = StringVar())
L1.pack( side = LEFT)
E1.pack(side = RIGHT)

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
C1.pack()
C2.pack()
C3.pack()
C4.pack()
C5.pack()
C6.pack()
C7.pack()
C8.pack()

from tkinter import messagebox
from Bio import SeqIO
def runprogram():
   for usrseq in SeqIO.parse(E1.get(), "fasta"):
      gtc =(usrseq.seq.lower())
      if CheckVar1.get() == 1:
         index=0
         while index < len(gtc):
            index = gtc.find("gaattc", index)
            if index ==-1:
               break
            print( index + 1)
            index += 6
         messagebox.showinfo(E1.get(),"Check the Shell")#EcoRI
      elif CheckVar2.get() == 1:
         index=0
         while index < len(gtc):
            index = gtc.find("ggatcc", index)
            if index ==-1:
               break
            print( index + 1)
            index += 6
         messagebox.showinfo(E1.get(),"Check the Shell")#BamHI
      elif CheckVar3.get() == 1:
         index=0
         while index < len(gtc):
            index = gtc.find("aagctt", index)
            if index ==-1:
               break
            print( index + 1)
            index += 6
         messagebox.showinfo(E1.get(),"Check the Shell")#HindIII
      elif CheckVar4.get() == 1:
         index=0
         while index < len(gtc):
            index = gtc.find("cccggg", index)
            if index ==-1:
               break
            print( index + 3)
            index += 6
         messagebox.showinfo(E1.get(),"Check the Shell")#SmaI
      elif CheckVar5.get() == 1:
         index=0
         while index < len(gtc):
            index = gtc.find("cagctg", index)
            if index ==-1:
               break
            print( index + 3)
            index += 6
         messagebox.showinfo(E1.get(),"Check the Shell")#PvuII
      elif CheckVar6.get() == 1:
         index=0
         while index < len(gtc):
            index = gtc.find("gatatc", index)
            if index ==-1:
               break
            print( index + 3)
            index += 6
         messagebox.showinfo(E1.get(),"Check the Shell")#EcoRV
      elif CheckVar7.get() == 1:
         index=0
         while index < len(gtc):
            index = gtc.find("tctaga", index)
            if index ==-1:
               break
            print( index + 1)
            index += 6
         messagebox.showinfo(E1.get(),"Check the Shell")#XbaI
      elif CheckVar8.get() == 1:
         index=0
         while index < len(gtc):
            index = gtc.find("atcgat", index)
            if index ==-1:
               break
            print( index + 2)
            index += 6
         messagebox.showinfo(E1.get(),"Check the Shell")#ClaI
      else:
         messagebox.showinfo(E1.get(),"Please choose a restriction enzyme")
         print (len(gtc))

B = tkinter.Button(top, text ="Go", command = runprogram)
B.pack()

top.mainloop()


