
from tkinter import *
import subprocess

#Enables the button commands
def open1():
    subprocess.call(" REIDv0.5.2.py 1", shell=True)
def open2():
    subprocess.call(" REIDv0.5.2-multiple.py 1", shell=True)
def open3():
    subprocess.call(" MoveFiles.py 1", shell=True)
def open4():
    subprocess.call("Analyze.py", shell=True)
def open5():
    subprocess.call("Restriction Digest.xls", shell=True)
readme = open("Readme.txt", "r")
text = readme.read()

    
root = Tk()
root.title("REID")
root.geometry("700x700")

#Closes the window with the Exit button
def close_program():
    root.destroy()

mb1 = Menubutton(root, text="Programs", relief=RAISED)
mb1.grid()
mb1.menu = Menu(mb1, tearoff=0)
mb1["menu"] = mb1.menu

mb2 = Menubutton(root, text="Options", relief=RAISED)
mb2.grid(row=0, column=2)
mb2.menu = Menu(mb2, tearoff=0)
mb2["menu"] = mb2.menu

mb3 = Menubutton(root, text="Analyze", relief=RAISED)
mb3.grid(row=0, column=1)
mb3.menu = Menu(mb3, tearoff=0)
mb3["menu"] = mb3.menu

labelframe = LabelFrame(root, text="Instructions")
labelframe.grid(row=2, column=3, columnspan=3)
left = Label(labelframe, text=text)
left.grid(row=2, column=3, columnspan=3)

mb1.menu.add_command(label=" Single fasta file", command=open1)
mb1.menu.add_command(label=" Multiple fasta files", command=open2)
mb2.menu.add_command(label=" Move files", command=open3)
mb2.menu.add_command(label=" View Restriction Digest ", command=open5)
mb2.menu.add_command(label=" Exit ", command=close_program)
mb3.menu.add_command(label=" Simulate", command=open4)
root.mainloop()
