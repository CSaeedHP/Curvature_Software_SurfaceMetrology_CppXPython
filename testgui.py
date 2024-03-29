from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import csv

root = Tk()
root.title("curvature project development")

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

# for debugging purposes
def checkfile():
    print(fileobject.get())
checkfilebutton = Button(root,text = "check file", command = checkfile)
checkfilebutton.pack()




#start post working1 modifications, dropdown function options

function_keys = {
    "herons" : "herons_curvature",
    "diffslope" : "diff_slope",
    "calculus" : "quad_curvature",
    "3lag" : "oriented_lagrangian",
    "fda" : "fin_diff_slope",
    "hybrid": "parse_hybrid_data"
}
listofkey = list(function_keys.keys())


def FunctionKeySelect(event):
    print(FunctionCombo.get())


FunctionCombo = ttk.Combobox(root, value = listofkey)
FunctionCombo.current(0)
FunctionCombo.bind("<<ComboboxSelected>>", FunctionKeySelect)
FunctionCombo.pack()


# working 2

def DataReader(my_file):
    data = my_file.read().split()
    for i in range(len(data)):
        point = data[i].split(',')
        x = float(point[0]); y = float(point[1])
        data[i] = [x, y]
    for x in data:
        return data

entrynumber = StringVar()
minimumbound = Label(root, text = "insert minimum bound below")
minimumentry = Entry(root, textvariable = entrynumber, width = 50, borderwidth = 1)
entrynumber.trace_add("write", )


minimumbound.pack()
minimumentry.pack()


sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)
e.pack()

def checkbound():
    print(type(minimumentry.get()))

boundbutton = Button(root, text = "check bound type", command = checkbound)
boundbutton.pack()
# e = Entry(root, width = 50,borderwidth = 100)
# e.pack()
# e.insert(0,"default value")
root.mainloop()