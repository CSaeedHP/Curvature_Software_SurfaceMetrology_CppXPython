from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

root = Tk()

filevar = StringVar()

myLabel = Label(root, textvariable=filevar)
myLabel.pack()
filevar.set("select file")
myLabel.pack()

def updatelabel():
    file = filedialog.askopenfile(parent=root,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    if file:
        filevar.set(os.path.abspath(file.name))
        return
    filevar.set("No file selected")
    
mybutton = Button(root,text = "Select file",command = updatelabel)
mybutton.pack()



root.mainloop()