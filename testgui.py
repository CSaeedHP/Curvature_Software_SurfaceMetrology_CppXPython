from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

root = Tk()

filename = StringVar()

filelabel = Label(root, textvariable=filename)
filelabel.pack()
filename.set("select file")
filelabel.pack()


fileobject = Variable()
fileobject.set(False)

def filelabeling():
    file = filedialog.askopenfile(parent=root,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    if file:
        filename.set(os.path.abspath(file.name))
        fileobject.set(file)
        return
    filename.set("No file selected")
    fileobject.set(False)
    
filebutton = Button(root,text = "Select file",command = filelabeling)
filebutton.pack()


def checkfile():
    print(fileobject.get())
checkfilebutton = Button(root,text = "check file", command = checkfile)
checkfilebutton.pack()

root.mainloop()