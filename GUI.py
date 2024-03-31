from tkinter import * # import tkinter library
from tkinter import filedialog
from tkinter import ttk
import csv
import os
import analysis
import userIO
import display
import filehandling
def quit_me():
    print('quit')
    root.quit()
    root.destroy()

root = Tk() 
root.protocol("WM_DELETE_WINDOW", quit_me)
root.title('Curvature Analysis Program')
data = 0




function_keys = {
    "herons" : "herons_curvature",
    "diffslope" : "diff_slope",
    "calculus" : "quad_curvature",
    "3lag" : "oriented_lagrangian",
    "fda" : "fin_diff_slope",
    "hybrid": "parse_hybrid_data"
}
listofkey = list(function_keys.keys())


var = StringVar()

myLabel = Label(root, textvariable=var)
myLabel.pack()
var.set("select file")


def GUIopenFile():
    
    file = filedialog.askopenfile(parent=root,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    if file:
        data = file.read().split()
        print(data)
        for i in range(len(data)):
            point = data[i].split(',')
            x = float(point[0]); y = float(point[1])
            data[i] = [x, y]
        for x in data:
            var.set(os.path.abspath(file.name))
            print(os.path.abspath(file.name))
            return data
    var.set("No file selected")
        

# event for what happens when option from dropdown menu selected
def FunctionKeySelect(event):
    print(FunctionCombo.get())




#functionkey selection dropdown
FunctionCombo = ttk.Combobox(root, value = listofkey)
FunctionCombo.current(0)
FunctionCombo.bind("<<ComboboxSelected>>", FunctionKeySelect)
FunctionCombo.pack()

#open filedialog window
fileButton = Button(root, text = "Open Curvature Data File",command = GUIopenFile)
fileButton.pack()



# def StartAnalysis():
#     var.get()

    
#initialize curvature analysis
# AnalysisButton = Button(root, text = "Start Curvature Analysis",command = StartAnalysis)
# AnalysisButton.pack()


#root.iconbitmap("")
#grid.forget()
e = Entry(root, width = 50,borderwidth = 100)
e.pack()
e.insert(0,"default value")
def myClick():
    hello = e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

clicked = StringVar()
clicked.set("default value")

drop = OptionMenu(root,clicked,"herons","parabola","three ordinate lagrangian","difference of slopes","finite difference analysis")
drop.pack()
myButton = Button(root, text = "click me", command = myClick, fg="purple",bg="green",padx=20,pady=40)
myButton.pack()
root.mainloop() #initializes root
#command = root.quit() 
