from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import csv
import userIO
root = Tk()
root.title("curvature project development")

#CONSTANTS

function_keys = {
    "herons" : "herons_curvature",
    "diffslope" : "diff_slope",
    "calculus" : "quad_curvature",
    "3lag" : "oriented_lagrangian",
    "fda" : "fin_diff_slope",
    "hybrid": "parse_hybrid_data"
}
listofkey = list(function_keys.keys()) #used in reference for dropdown menu


#VARIABLES SECTION
filename = StringVar() #name of file to be displayed at top of function
filename.set("select file") #default value

fileobject = Variable() #initial x-z data points
fileobject.set(False) #returns false if no object set yet

minentrynumber = StringVar() #number for lower bound
minboundmessage = StringVar() #message for lower bound
minboundmessage.set("Insert minimum bound below.") #default value before user input

maxentrynumber = StringVar() #number for upper bound
maxboundmessage = StringVar() #message for upper bound
maxboundmessage.set("Insert maximum bound below.") #default value before user input


automin = DoubleVar() #minimum possible 
automax = DoubleVar() #maximum possible





#DEFINE FUNCTIONS HERE
def filelabeling():
    file = filedialog.askopenfile(parent=root,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    if file:
        filename.set(os.path.abspath(file.name))
        data = file.read().split()
        for i in range(len(data)):
            point = data[i].split(',')
            try:
                x = float(point[0]); z = float(point[1])
            except ValueError:
                filename.set("Data File Incompatible!") #handles incompatible files
                return
            data[i] = [x, z]
        fileobject.set(data)
        [datamin,datamax,odd] = userIO.get_range(data) #determining minimum and maximum possible bounds based on data
        minentrynumber.set(datamin)
        maxentrynumber.set(datamax)
        automin.set(datamin)
        automax.set(datamax)
        minboundmessage.set("Please input a minimum bound.")
        maxboundmessage.set("Please input a maximum bound.")

        return
    filename.set("No file selected")
    fileobject.set(False)
    

# for debugging purposes
def checkfile():
    print(fileobject.get())





#start post working1 modifications, dropdown function options




def FunctionKeySelect(event):
    print(FunctionCombo.get())





# working 2

def DataReader(my_file):
    data = my_file.read().split()
    for i in range(len(data)):
        point = data[i].split(',')
        x = float(point[0]); y = float(point[1])
        data[i] = [x, y]
    for x in data:
        return data

def checkValidDoubleEntry(entry): #helper function to check if valid double input
    try:
        float_number = float(entry)
        return True
    except ValueError:
        return False
    


def mincheckbound(a,b,c):
    global minboundmessage
    string_number = minimumentry.get()
    if a:
        maxcheckbound(0,0,0) # runs maxcheckbound without running mincheckbound again (prevent infininte loop)
    if string_number == "":
        minboundmessage.set("Please input a minimum bound.")
        return
    try:
        float_number = float(string_number)
        if checkValidDoubleEntry(maximumentry.get()) and float_number >= float(maximumentry.get()):
            if float_number == automin.get():
                maxboundmessage.set("Please increase your maximum bound.")
                minboundmessage.set("Minimum bound cannot be decreased further.")
                return
            minboundmessage.set(f"Your minimum bound must be less than your maximum bound.")
            return
        if float_number < automin.get():
            minboundmessage.set(f"Your minimum bound cannot be less than {automin.get()}")
            return
        if float_number > automax.get():
            minboundmessage.set(f"Your minimum bound cannot be greater than {automax.get()}")
            return
        

        minboundmessage.set("Valid minimum bound!")

    except ValueError:
        minboundmessage.set(f"Cannot convert '{string_number}' to a number.")
    






#maximum bound logic

def maxcheckbound(a,b,c):
    global maxboundmessage
    if a:
        print("run mincheckbound")
        mincheckbound(0,0,0) # runs mincheckbound without running maxcheckbound again (prevent infinite loop)
    string_number = maximumentry.get()
    if string_number == "":
        maxboundmessage.set("Please input a maximum bound.")
        return
    try:
        float_number = float(string_number)
        if checkValidDoubleEntry(minimumentry.get()) and float_number <= float(minimumentry.get()):
            if float_number == automax.get():
                minboundmessage.set("Please decrease your minimum bound.")
                maxboundmessage.set("Maximum bound cannot be increased further.")
                return
            maxboundmessage.set(f"Your maximum bound must be greater than your minimum bound.")
            return
        if float_number < automin.get():
            maxboundmessage.set(f"Your maximum bound cannot be less than {automin.get()}")
            return
        if float_number > automax.get():
            maxboundmessage.set(f"Your maximum bound cannot be greater than {automax.get()}")
            return
        maxboundmessage.set("Valid maximum bound!")
        
        
    except ValueError:
        maxboundmessage.set(f"Cannot convert '{string_number}' to a number.")
  





#end bounding logic

#begin autoset
def autosetbounds():
    maxentrynumber.set(automax.get())
    minentrynumber.set(automin.get())
    minboundmessage.set(f"Automatically set to minimum of {automin.get()}")
    maxboundmessage.set(f"Automatically set to maximum of {automax.get()}")





#UI ELEMENTS GO HERE
    
filebutton = Button(root,text = "Select file",command = filelabeling)


filelabel = Label(root, textvariable=filename)

checkfilebutton = Button(root,text = "check file", command = checkfile)


minimumbound = Label(root, textvariable = minboundmessage)
minimumentry = Entry(root, textvariable = minentrynumber, width = 50, borderwidth = 1)
minentrynumber.trace_add("write",mincheckbound)

maximumbound = Label(root, textvariable = maxboundmessage)
maximumentry = Entry(root, textvariable = maxentrynumber, width = 50, borderwidth = 1)
maxentrynumber.trace_add("write",maxcheckbound)





FunctionCombo = ttk.Combobox(root, value = listofkey)
FunctionCombo.current(0)
FunctionCombo.bind("<<ComboboxSelected>>", FunctionKeySelect)



resetboundbutton = Button(root, text = "automatically set bounds", command = autosetbounds)

#CALL FUNCTIONS BASED ON USER INTERACTION




#PACKING ELEMENTS
filelabel.pack()
filebutton.pack()
checkfilebutton.pack()

FunctionCombo.pack()


minimumbound.pack()
minimumentry.pack()
maximumbound.pack()
maximumentry.pack()

resetboundbutton.pack()

# e = Entry(root, width = 50,borderwidth = 100)
# e.pack()
# e.insert(0,"default value")
root.mainloop()