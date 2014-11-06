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
C1.pack()
C2.pack()
C3.pack()
C4.pack()

from tkinter import messagebox
def runprogram():
   messagebox.showinfo(E1.get())

B = tkinter.Button(top, text ="Go", command = runprogram)
B.pack()

top.mainloop()

