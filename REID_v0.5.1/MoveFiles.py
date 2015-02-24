
from tkinter import *
import os
import shutil
from tkinter.filedialog import askdirectory
content = ''
file_path = ''
#shows file in box
def open_file():
    global content
    global file_path
    filename = askdirectory()
    entry.delete(0, END)
    entry.insert(0, os.path.normpath(filename))
#copies files
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

#moves files to directory
def process_file():
    dst = "C:\\Users\\musta_000\\Desktop\\REID\\REID_v0.5.1\\"
    src = os.path.normpath(entry.get())
    if os.path.isdir(dst):
        copytree(src, dst)

#GUI setup
root = Tk()
root.title('Move Files')
root.geometry("598x120+250+100")

mf = Frame(root)
mf.pack()


f1 = Frame(mf, width=600, height=250)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=250)
f2.pack()



Label(f1, text="Select Your Directory").grid(row=0, column=0, sticky='e')
entry = Entry(f1, width=50, textvariable=file_path)
entry.grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=25)
Button(f1, text="Browse", command=open_file).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
Button(f2, text="Move Files", width=32, command=process_file).grid(sticky='ew', padx=10, pady=10)


root.mainloop()
