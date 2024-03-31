from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

root = Tk()
root.title("Curvature Analysis Program")
filevar = StringVar()

myLabel = Label(root, textvariable=filevar)
myLabel.pack()
filevar.set("select file")
myLabel.pack()
filevar = Variable()
filevar.set(False) #default value to check for no file selected
def updatelabel():
    file = filedialog.askopenfile(parent=root,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    if file:
        filevar.set(os.path.abspath(file.name))
        filevar.set(file)
        return
    filevar.set("No file selected")
    filevar.set(False)
    
filebutton = Button(root,text = "Select file",command = updatelabel)
filebutton.pack()


def checkfile():
    print(filevar.get()) 

testbutton = Button(root,text = "check file",command = checkfile)
testbutton.pack()

root.mainloop()