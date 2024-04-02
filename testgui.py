from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import csv
import userIO
import analysis
import display
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
root = Tk()
root.title("curvature project development")


#structure of code:
#code is divided into various sections, in a specifc order to ensure functionality of code.
#constants --> defined at the beginning
#variables --> defined, and some have default values set at the beginning
#functions --> defined using the variables and constants above
#ui elements --> defined, some of which call functions and rely upon the previously defined variables

#CONSTANTS

function_keys = {
    "herons" : "herons_curvature",
    "diffslope" : "diff_slope",
    "calculus" : "quad_curvature",
    "3lag" : "oriented_lagrangian",
    "fda" : "fin_diff_slope",
    "AcuteTest" : "isObtuse"
}
listofkey = list(function_keys.keys()) #used in reference for dropdown menu


#VARIABLES SECTION
filename = StringVar() #name of file to be displayed at top of function
filename.set("select file") #default value

fileobject = Variable() #initial x-z data points
fileobject.set(False) #returns false if no object set yet

standardmenu = StringVar()
standardmenu.set("Analysis method")

hybridmenu = StringVar()
hybridmenu.set("Hybrid mode not active")

minentrynumber = StringVar() #number for lower bound
minboundmessage = StringVar() #message for lower bound
minboundmessage.set("Please select a file first.") #default value before user input

maxentrynumber = StringVar() #number for upper bound
maxboundmessage = StringVar() #message for upper bound
maxboundmessage.set("Please select a file first.") #default value before user input

minboundvalidity = BooleanVar()
maxboundvalidity = BooleanVar()


automin = DoubleVar() #minimum possible 
automax = DoubleVar() #maximum possible

radiovalue = IntVar()
radiovalue.set("0")

hybrid = BooleanVar()


XSC = Variable()



#DEFINE FUNCTIONS HERE
def filelabeling(): #used with select file button and filelabel
    '''mutates fileobject into data if valid file is inputted
    sets filelabel to path of file, fileobject is false if bad file'''
    file = filedialog.askopenfile(parent=root,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    if file:
        filename.set(os.path.abspath(file.name))
        try:
            data = file.read().split()
        except UnicodeDecodeError:
            filename.set("Unicode error: Data File Incompatible!") #handles incompatible files
            fileobject.set(False) 
            minentrynumber.set("")
            maxentrynumber.set("")
            minboundmessage.set("Please select a file.")
            maxboundmessage.set("Please select a file.")
            disablebounds()
            return
        for i in range(len(data)):
            point = data[i].split(',')
            try:
                x = float(point[0]); z = float(point[1])
            except ValueError:
                filename.set("Field error: Data File Incompatible!") #handles incompatible files
                minentrynumber.set("")
                maxentrynumber.set("")
                minboundmessage.set("Please select a file.")
                maxboundmessage.set("Please select a file.")
                fileobject.set(False)
                disablebounds()
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
        maxboundvalidity.set(1)
        minboundvalidity.set(1)
        enablebounds()
        return
    
    minentrynumber.set("")
    maxentrynumber.set("")
    minboundmessage.set("Please select a file.")
    maxboundmessage.set("Please select a file.")
    filename.set("No file selected")
    fileobject.set(False)
    disablebounds() 
    

# for debugging purposes
def checkfile(): #check file button
    print(fileobject.get())





#start post working1 modifications, dropdown function options


def radioclick():
    value = radiovalue.get()
    if value:
        standardmenu.set("Hybrid Obtuse analysis method")
        hybridmenu.set("Hybrid Acute analysis method")
        FunctionHybrid["state"] = "readonly"
    else:
        standardmenu.set("Analysis method")
        hybridmenu.set("Hybrid mode not active")
        FunctionHybrid["state"] = DISABLED





def FunctionKeySelect(event): #may not have a use, for functioncombo
    print(FunctionCombo.get())





# working 2

def DataReader(my_file): #unused
    data = my_file.read().split()
    for i in range(len(data)):
        point = data[i].split(',')
        x = float(point[0]); y = float(point[1])
        data[i] = [x, y]
    for x in data:
        return data

def checkValidDoubleEntry(entry): #helper function to check if valid double input in minbound and maxbound
    try:
        float_number = float(entry)
        return True
    except ValueError:
        return False
    


def mincheckbound(a,b,c): #used with minbound and maxbound
    global minboundmessage
    string_number = minimumentry.get()
    if a:
        maxcheckbound(0,0,0) # runs maxcheckbound without running mincheckbound again (prevent infininte loop)
    if string_number == "":
        minboundmessage.set("Please input a minimum bound.")
        minboundvalidity.set(0)
        return
    try:
        float_number = float(string_number)
        if checkValidDoubleEntry(maximumentry.get()) and float_number >= float(maximumentry.get()):
            if float_number == automin.get():
                maxboundmessage.set("Please increase your maximum bound.")
                minboundmessage.set("Minimum bound cannot be decreased further.")
                minboundvalidity.set(0)
                return
            minboundmessage.set(f"Your minimum bound must be less than your maximum bound.")
            minboundvalidity.set(0)
            return
        if float_number < automin.get():
            minboundmessage.set(f"Your minimum bound cannot be less than {automin.get()}")
            minboundvalidity.set(0)
            return
        if float_number > automax.get():
            minboundmessage.set(f"Your minimum bound cannot be greater than {automax.get()}")
            minboundvalidity.set(0)
            return
        

        minboundmessage.set("Valid minimum bound!")
        minboundvalidity.set(1)

    except ValueError:
        minboundmessage.set(f"Cannot convert '{string_number}' to a number.")
    






#maximum bound logic

def maxcheckbound(a,b,c): #used with maxbound, minbound
    global maxboundmessage
    if a:
        print("run mincheckbound")
        mincheckbound(0,0,0) # runs mincheckbound without running maxcheckbound again (prevent infinite loop)
    string_number = maximumentry.get()
    if string_number == "":
        maxboundmessage.set("Please input a maximum bound.")
        maxboundvalidity.set(0)
        return
    try:
        float_number = float(string_number)
        if checkValidDoubleEntry(minimumentry.get()) and float_number <= float(minimumentry.get()):
            if float_number == automax.get():
                minboundmessage.set("Please decrease your minimum bound.")
                maxboundmessage.set("Maximum bound cannot be increased further.")
                maxboundvalidity.set(0)
                return
            maxboundmessage.set(f"Your maximum bound must be greater than your minimum bound.")
            maxboundvalidity.set(0)
            return
        if float_number < automin.get():
            maxboundmessage.set(f"Your maximum bound cannot be less than {automin.get()}")
            maxboundvalidity.set(0)
            return
        if float_number > automax.get():
            maxboundmessage.set(f"Your maximum bound cannot be greater than {automax.get()}")
            maxboundvalidity.set(0)
            return
        maxboundmessage.set("Valid maximum bound!")
        maxboundvalidity.set(1)
        
        
    except ValueError:
        maxboundmessage.set(f"Cannot convert '{string_number}' to a number.")
  





#end bounding logic

#begin autoset
def autosetbounds(): #used with automatically reset button
    maxentrynumber.set(automax.get())
    minentrynumber.set(automin.get())
    minboundmessage.set(f"Automatically set to minimum of {automin.get()}")
    maxboundmessage.set(f"Automatically set to maximum of {automax.get()}")

#enable and disable bound ui elements
def enablebounds():
    minimumentry["state"]=NORMAL
    maximumentry["state"]=NORMAL
    resetboundbutton["state"]=NORMAL
def disablebounds():
    minimumentry["state"]=DISABLED
    maximumentry["state"]=DISABLED
    resetboundbutton["state"]=DISABLED


def startanalysis():
    if not fileobject.get():
        fileerror = messagebox.showwarning(title = "Analysis not started", message = "Data file missing or invalid. Please select another data file.")
        return
    if not minboundvalidity.get() or  not maxboundvalidity.get():
        bounderror = messagebox.showwarning(title = "Analysis not started", message = "Please check your bounds before continuing, or use the autoset button.")
        return
    scale_user_lower = math.floor(float(minimumentry.get())/automin.get())
    scale_user_upper = math.ceil(float(maximumentry.get())/automin.get())
    print(scale_user_lower)
    print(scale_user_upper)
    xsc1 = analysis.GUIparse_data(fileobject.get(),FunctionCombo.get(),scale_user_lower,scale_user_upper)
    XSC.set(xsc1)



    
def plot3d(XSC):
    
    '''plot a set of points for curvature'''
    userlog = False
    labelpadsize = 40
    axes_font = 40
    plt.rcParams['font.size'] = 20
    X = [row[0] for row in XSC]
    S = [row[1] for row in XSC]
    C = [row[2] for row in XSC]
    ax = plt.axes(projection='3d')
    
    colors = plt.cm.turbo(C)
    ax.scatter3D(X,S,C,c=colors)
    ax.set_xlabel('X Position', labelpad=labelpadsize)
    if userlog:
        ax.set_ylabel('log(Scale)', labelpad=labelpadsize)
    else:
        ax.set_ylabel('Scale', labelpad=labelpadsize)
    ax.set_zlabel('Curvature', labelpad=labelpadsize)
    plt.colorbar(mpl.cm.ScalarMappable(cmap='turbo'), ax=ax, orientation='vertical', label='Curvature')
    return ax



def graphdata():
    data = XSC.get()
    if data:
        plot3d(data)
        plt.show(block = False)
        return
    else:
        grapherror = messagebox.showerror(title = "Graphing failed", message = "Please perform an analysis before graphing.")


#DEFINING STATES



#UI ELEMENTS GO HERE
    
filelabel = Label(root, textvariable=filename)
    
filebutton = Button(root,text = "Select file",command = filelabeling)



checkfilebutton = Button(root,text = "check file", command = checkfile)


standardbutton = Radiobutton(root, text="Standard Analysis",variable=radiovalue, value = 0, command = radioclick)
hybridbutton = Radiobutton(root, text="Hybrid Analysis",variable=radiovalue, value = 1, command = radioclick)



minimumbound = Label(root, textvariable = minboundmessage)
minimumentry = Entry(root, textvariable = minentrynumber, width = 50, borderwidth = 1)



maximumbound = Label(root, textvariable = maxboundmessage)
maximumentry = Entry(root, textvariable = maxentrynumber, width = 50, borderwidth = 1)



StandardObtuseLabel = Label(root, textvariable = standardmenu)

FunctionCombo = ttk.Combobox(root, value = listofkey, state="readonly")
FunctionCombo.current(0)

HybridAcuteLabel = Label(root, textvariable = hybridmenu)

FunctionHybrid = ttk.Combobox(root, value = listofkey,state="readonly")
FunctionHybrid.current(0)


resetboundbutton = Button(root, text = "automatically set bounds", command = autosetbounds)

analysisbutton = Button(root,text = "start curvature analysis", command = startanalysis)

graphbutton = Button(root, text = "Graph curvature data", command = graphdata)

#CALL FUNCTIONS BASED ON USER INTERACTION
minentrynumber.trace_add("write",mincheckbound)
maxentrynumber.trace_add("write",maxcheckbound)
FunctionCombo.bind("<<ComboboxSelected>>", FunctionKeySelect)

#PACKING ELEMENTS, determines packing order
filelabel.pack()
filebutton.pack()
checkfilebutton.pack()


standardbutton.pack()
hybridbutton.pack()


StandardObtuseLabel.pack()
FunctionCombo.pack()
HybridAcuteLabel.pack()
FunctionHybrid.pack()


minimumbound.pack()
minimumentry.pack()
maximumbound.pack()
maximumentry.pack()

resetboundbutton.pack()

analysisbutton.pack()
graphbutton.pack()


#STATE
FunctionHybrid["state"] = DISABLED
minimumentry["state"] = DISABLED
maximumentry["state"] = DISABLED

# e = Entry(root, width = 50,borderwidth = 100)
# e.pack()
# e.insert(0,"default value")
root.mainloop()