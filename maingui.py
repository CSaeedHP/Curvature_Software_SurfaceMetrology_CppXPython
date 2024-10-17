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
import matplotlib as mplg
import numpy as np
import random
import X3Pconverter

root = Tk()
root.wm_attributes('-topmost', 0)
root.title("curvature project development")
try:
    root.iconbitmap("icon.ico")
    root.wm_iconbitmap("icon.ico")
except:
    print("icon not found")
root.minsize(400,600)
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
filename = StringVar() #path of file to be displayed at top of function
filename.set("select file") #default value


filenamesolo = StringVar() #name of file

fileobject = Variable() #initial x-z data points
fileobject.set(False) #returns false if no object set yet

standardmenu = StringVar()
standardmenu.set("Analysis method")

hybridmenu = StringVar()
hybridmenu.set("Hybrid mode not active")

minentrynumber = StringVar() #number for lower bound
minboundmessage = StringVar() #message for lower bound
minboundmessage.set("Please select a file first.") #default value before user input
minimumcached = DoubleVar()

maxentrynumber = StringVar() #number for upper bound
maxboundmessage = StringVar() #message for upper bound
maxboundmessage.set("Please select a file first.") #default value before user input

dpstring = StringVar() 
decimalmessage = StringVar()
decimalmessage.set("Round to number of decimal places")
dpstring.set("4")

decimalvalidity = BooleanVar()
decimalvalidity.set(1)
minboundvalidity = BooleanVar()
maxboundvalidity = BooleanVar()


automin = DoubleVar() #minimum possible 
automax = DoubleVar() #maximum possible

radiovalue = IntVar()
radiovalue.set("0")

hybrid = BooleanVar()

LogScaleOn = BooleanVar()

LogAbsCurvatureOn = BooleanVar()

WebBrowserGraphOn = BooleanVar()
ErrorWebBrowserGraphOn = BooleanVar()

analysisdetails = StringVar()
analysisdetails.set("No analysis stored")



XSC = Variable()



#DEFINE FUNCTIONS HERE
def filelabeling(): #used with select file button and filelabel
    '''mutates fileobject into data if valid file is inputted
    sets filelabel to path of file, fileobject is false if bad file'''
    file = filedialog.askopenfile(parent=root,
                                  initialdir="./",
                                  title="Select A File",
                                  filetypes = (("X3P (2D surface profile)","*.x3p"),
                                               ("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    if file:
        filename.set(os.path.abspath(file.name))
        extension = os.path.splitext(filename.get())[1]
        if extension == ".x3p": 
            print("x3p file found")
            #passes on the file path to the x3preader function
            data, hashvalue = X3Pconverter.readx3p(filename.get())
        else:
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
        minboundmessage.set("Please input a minimum scale bound.")
        maxboundmessage.set("Please input a maximum scale bound.")
        maxboundvalidity.set(1)
        minboundvalidity.set(1)
        enablebounds()
        plot2d(data,"input profile")
        filenamesolo.set(os.path.basename(file.name))
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
    '''debugging purposes only'''
    if fileobject.get():
        print(fileobject.get())
        plot2d(fileobject.get(),"input profile")
    else:
        nofile = messagebox.showwarning("No file", "No file selected")





#start post working1 modifications, dropdown function options


def radioclick():
    '''toggles betweeen hybrid on and hybrrid off'''
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
    '''currently unused'''
    print(FunctionCombo.get())





# working 2


def checkValidDoubleEntry(entry): #helper function to check if valid double input in minbound and maxbound
    '''check valid double.'''
    try:
        float_number = float(entry)
        return True
    except ValueError:
        return False
    


def mincheckbound(a,b,c): #used with minbound and maxbound
    '''checks the entry field of the minimum entry box. changes the corresponding messagebox accordingly.'''
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
    '''checks validity of the bound upon editing of the entry field for maximum. changes message box accordingly'''
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
    '''used to automatically set the bounds based on valid minimum and maximum of the input data'''
    maxentrynumber.set(automax.get())
    minentrynumber.set(automin.get())
    minboundmessage.set(f"Automatically set to minimum of {automin.get()}")
    maxboundmessage.set(f"Automatically set to maximum of {automax.get()}")

#enable and disable bound ui elements
def enablebounds():
    '''used to enable the bound entry fields'''
    minimumentry["state"]=NORMAL
    maximumentry["state"]=NORMAL
    resetboundbutton["state"]=NORMAL
def disablebounds():
    '''used to disable the bound entry fields'''
    minimumentry["state"]=DISABLED
    maximumentry["state"]=DISABLED
    resetboundbutton["state"]=DISABLED

def startanalysis():
    ''' checks for validity of the input paramaters, and then performs either standard or hybrid analysis'''
    if not fileobject.get():
        fileerror = messagebox.showwarning(title = "Analysis not started", message = "Data file missing or invalid. Please select another data file.")
        return #check to see if file exists for analysis
    if not minboundvalidity.get() or  not maxboundvalidity.get():
        bounderror = messagebox.showwarning(title = "Analysis not started", message = "Please check your bounds before continuing, or use the autoset button.")
        return #checks bound validity
    if not decimalvalidity.get():
        decimalerror = messagebox.showwarning(title = "decimal field invalid", message = "invalid decimal places")
        return
    scale_user_lower = math.floor(float(minimumentry.get())/automin.get())
    scale_user_upper = math.ceil(float(maximumentry.get())/automin.get())
    dec_places = int(dpstring.get())
    minimumcached.set(scale_user_lower)
    print(scale_user_lower)
    print(scale_user_upper)
    if radiovalue.get():
        xsc1 = analysis.GUI_parse_hybrid_data(fileobject.get(),FunctionCombo.get(),FunctionHybrid.get(),scale_user_lower,scale_user_upper,dec_places)
        analysisdetails.set(f"{filenamesolo.get()}_Hybrid_{FunctionCombo.get()}_{FunctionHybrid.get()}_{minentrynumber.get()}_to_{maxentrynumber.get()}")
        
    else:
        xsc1 = analysis.GUIparse_data(fileobject.get(),FunctionCombo.get(),scale_user_lower,scale_user_upper,dec_places)
        analysisdetails.set(f"{filenamesolo.get()}_Standard_{FunctionCombo.get()}_{minentrynumber.get()}_to_{maxentrynumber.get()}")
    
    XSC.set(xsc1)



def plot3d(XSC,LogScale,LogABSCurvature,title,xlabel,ylabel,zlabel):
    #initial declaration of the figure
    ThreeDplot = plt.figure(title)
    '''plot a set of points for curvature. Options are for Log of the scale and log of absolute value of curvature'''
    print(len(XSC))
    #i have no idea what these do
    labelpadsize = 10
    plt.rcParams['font.size'] = 10

    #X positions
    X = [row[0] for row in XSC]


    if LogScale: #applies logarithmic scale
        S = [math.log10(row[1]) for row in XSC]
    else:
        S = [row[1] for row in XSC]
    if LogABSCurvature: #applies log abs curvature
        C = [math.log10(abs(row[2])) for row in XSC]
    else:
        C = [row[2] for row in XSC]
    # Xarr = np.asarray(X)
    # Sarr = np.asarray(S)
    # Carr = np.asarray(C)

    theplot = plt.axes(projection='3d')
    colors = plt.cm.turbo(C)
    colors2 = plt.get_cmap('turbo')
    scatter = theplot.scatter3D(X,S,C,c = C, cmap = colors2)
    # scatter = theplot.plot_trisurf(Xarr,Sarr,Carr, cmap = colors2)
    theplot.set_xlabel('X Position', labelpad=labelpadsize)
    if LogScale:
        theplot.set_ylabel('log(Scale)', labelpad=labelpadsize)
    else:
        theplot.set_ylabel('Scale', labelpad=labelpadsize)
    if title == "Position, Scale, Percent Error":
        theplot.set_zlabel('Percent Error', labelpad = labelpadsize)
    else:
        theplot.set_zlabel('Curvature', labelpad=labelpadsize)
    plt.colorbar(scatter, ax = theplot, label = "Curvature", ticklocation = 'auto')
    theplot.locator_params(nbins = 5)
    #colorbar = plt.colorbar(mpl.cm.ScalarMappable(cmap='turbo'), ax=theplot, orientation='vertical', label='Curvature')
    # ThreeDplot.canvas.manager.window.attributes('-topmost', 0)
    plt.show(block = False)
    return theplot

def plot2d(input_array,fignumber):
    '''plots a 2d array of the inputted data.'''
    # fig, axs = plt.subplots(2)
# ax = axs[0]
# ax = plt.axes(projection='3d')
# ax2 = axs[1]
# ax.grid()
    plt.figure(fignumber)
    plt.rcParams['font.size'] = 20
    X = [row[0] for row in input_array]
    Y = [row[1] for row in input_array]
    ax = plt.axes()
    ax.grid()
    ax.scatter(X,Y)
    ax.set_xlabel('X position', labelpad = 20)
    ax.set_ylabel('Height', labelpad = 20)
    plt.show(block = False)
    return ax
    

def graphdata():
    data = XSC.get()
    if data and WebBrowserGraphOn.get():
        display.plotly3d(data,LogScaleOn.get(),LogAbsCurvatureOn.get())
        return
    if data:
        plot3d(data,LogScaleOn.get(),LogAbsCurvatureOn.get(),"Position, Scale, Curvature","Position","Scale","Curvature")
        return
    else:
        grapherror = messagebox.showerror(title = "Graphing failed", message = "Please perform an analysis before graphing.")



#defines quit logic
def quit_me():
    print('quit')
    root.quit()
    root.destroy()


#save file
def WriteCSV():
    '''writes input list of list to csv file at user specified location'''
    file = XSC.get()
    if file:
        new_file = filedialog.asksaveasfile(parent=root,
                                            initialdir="./",
                                            title="Save as",
                                            filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                                ("Text files", "*.txt"), 
                                                ("All files", "*")),defaultextension="*.*")
        if new_file:
            writer = csv.writer(new_file)
            writer.writerows(file)
            
    else:
        warning =messagebox.showwarning("No file stored","No file available to save")

def decimalcheck(a,b,c):
    string_number = dpstring.get()
    if string_number == "":
        decimalmessage.set("Please input number of decimal places.")
        decimalvalidity.set(0)
        return
    try:
        int_number = int(string_number)

        if int_number < 0:
            decimalmessage.set(f"Number of decimal places must be positive")
            decimalvalidity.set(0)
            return

        decimalmessage.set("Valid decimal place count!")
        decimalvalidity.set(1)
        
        
    except ValueError:
        decimalmessage.set(f"Cannot convert '{string_number}' to a integer.")
  

   



#DEFINING STATES



#UI ELEMENTS GO HERE
    
filelabel = Label(root, textvariable=filename)
    
filebutton = Button(root,text = "Select file",command = filelabeling)


#debugging button
checkfilebutton = Button(root,text = "check file", command = checkfile)

#standard/hybrid analysis
standardbutton = Radiobutton(root, text="Standard Analysis",variable=radiovalue, value = 0, command = radioclick)
hybridbutton = Radiobutton(root, text="Hybrid Analysis",variable=radiovalue, value = 1, command = radioclick)

#standard/obtuse box
StandardObtuseLabel = Label(root, textvariable = standardmenu)
FunctionCombo = ttk.Combobox(root, value = listofkey, state="readonly")
FunctionCombo.current(0)
#hybridacute box
HybridAcuteLabel = Label(root, textvariable = hybridmenu)
FunctionHybrid = ttk.Combobox(root, value = listofkey,state="readonly")
FunctionHybrid.current(0)

#bounds
minimumbound = Label(root, textvariable = minboundmessage)
minimumentry = Entry(root, textvariable = minentrynumber, width = 50, borderwidth = 1)
maximumbound = Label(root, textvariable = maxboundmessage)
maximumentry = Entry(root, textvariable = maxentrynumber, width = 50, borderwidth = 1)
resetboundbutton = Button(root, text = "automatically set bounds", command = autosetbounds)





#decimal limiting
decimaltext = Label(root, textvariable = decimalmessage)
decimalplaces = Entry(root, textvariable = dpstring)







#analysis
analysisLabel = Label(root, textvariable = analysisdetails)
analysisbutton = Button(root,text = "start curvature analysis", command = startanalysis)


#graphing
graphbutton = Button(root, text = "Graph curvature data", command = graphdata)
Graphoptions = Label(root, text = "Graphing options")
LogBox = Checkbutton(root, text = "Logarithmic Scale", variable = LogScaleOn, onvalue = 1, offvalue = 0)
LogAbsCurvature = Checkbutton(root, text = "Log|curvature|", variable = LogAbsCurvatureOn, onvalue = 1, offvalue = 0)
Plotlygraph = Checkbutton(root, text = "Graph in web browser?", variable = WebBrowserGraphOn, onvalue = 1, offvalue =  0)

#savefile
savebutton = Button(root, text = "save analysis", command = WriteCSV)





#CALL FUNCTIONS BASED ON USER INTERACTION
minentrynumber.trace_add("write",mincheckbound)
maxentrynumber.trace_add("write",maxcheckbound)
FunctionCombo.bind("<<ComboboxSelected>>", FunctionKeySelect)

dpstring.trace_add("write",decimalcheck)
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


decimaltext.pack()
decimalplaces.pack()

analysisbutton.pack()
analysisLabel.pack()



Graphoptions.pack()
LogBox.pack()
LogAbsCurvature.pack()
Plotlygraph.pack()
graphbutton.pack()
savebutton.pack()

#STATE
#sets default state of ui elements upon initialization

root.protocol("WM_DELETE_WINDOW", quit_me) #defines what happens on closing


FunctionHybrid["state"] = DISABLED
minimumentry["state"] = DISABLED
maximumentry["state"] = DISABLED


# e = Entry(root, width = 50,borderwidth = 100)
# e.pack()
# e.insert(0,"default value")


#popup window for error analysis


popup = Toplevel(root)
popup.wm_attributes('-topmost', 0)
popup.minsize(400,400)
popup.title("Error analysis")
popup.withdraw()
ErrorData = Variable()
theoreticaldataname = Variable()
analysistype = IntVar()
analysistype.set(0)
theoreticallabel = StringVar()
theoreticalfileobject = Variable()
theoryfilenamesolo = StringVar()




def errorselectfile():
        file = filedialog.askopenfile(parent=popup,
                                    initialdir="",
                                    title="Select A File",
                                    filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                                ("Text files", "*.txt"), 
                                                ("All files", "*")))
        if file:
            theoreticaldataname.set(os.path.abspath(file.name))
            try:
                data = file.read().split()
            except UnicodeDecodeError:
                theoreticaldataname.set("Unicode error: Data File Incompatible!") #handles incompatible files
                theoreticalfileobject.set(False) 
                return
            for i in range(len(data)):
                point = data[i].split(',')
                try:
                    x = float(point[0]); z = float(point[1])
                except ValueError:
                    theoreticallabel.set("Field error: Data File Incompatible!") #handles incompatible files
                    theoreticalfileobject.set(False)
                    return
                data[i] = [x, z]
            theoreticalfileobject.set(data)
            plot2d(data,"theoretical curvatures")
            theoryfilenamesolo.set(os.path.basename(file.name))
            return
        
def performerroranalysis():
    if theoreticalfileobject.get() and XSC.get():
        if analysistype.get() == 0:
            ErrorData.set(analysis.GUI_percent_error2(XSC.get(),theoreticalfileobject.get(),minimumcached.get()))
        else:
            ErrorData.set(analysis.GUI_absolute_error2(XSC.get(),theoreticalfileobject.get(),minimumcached.get()))
    else:
        nofileerror = messagebox.showerror("analysis not started", "Curvature data or measured data not detected")




def checkdata():
    theoreticalfile = theoreticalfileobject.get()
    if theoreticalfile:
        plot2d(theoreticalfile,"theoretical curvatures")
        return
    else:
        errorwindow = messagebox.showwarning("No file selected", "No curvature data has been loaded.")

def graph_theoretical_comparison():
    xlabel = "Position"
    ylabel = "Scale"
    if analysistype.get() == 0:
        title = "Position, Scale, Percent Error"
        zlabel = "Percent Error"
    else:
        title = "Position, Scale, Error difference" 
        zlabel = "Error difference"
        
    data = ErrorData.get()
    if data and ErrorWebBrowserGraphOn.get():
        display.plotly3d(data,LogScaleOn.get(),LogAbsCurvatureOn.get())
        return
    if data:
        plot3d(data,LogScaleOn.get(),LogAbsCurvatureOn.get(),title,xlabel,ylabel,zlabel)
        return
    else:
        grapherror = messagebox.showerror(title = "Graphing failed", message = "Please perform a comparison before graphing.")
def WriteCSVError():
    '''writes input list of list to csv file at user specified location'''
    file = ErrorData.get()
    if file:
        new_file = filedialog.asksaveasfile(parent=root,
                                            initialdir="./",
                                            title="Save as",
                                            filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                                ("Text files", "*.txt"), 
                                                ("All files", "*")),defaultextension="*.*")
        if new_file:
            writer = csv.writer(new_file)
            writer.writerows(file)
            
    else:
        warning =messagebox.showwarning("No file stored","No file available to save")


def quit_popup():
    print('quit')
    popup.withdraw()

popup.protocol("WM_DELETE_WINDOW", quit_popup)
def open_popup_error_analysis():
    popup.deiconify()

    


CheckButton = Button(popup, text = "check theoretical data", command = checkdata)
SaveDataButton = Button(popup, text = "Save file", command = WriteCSV)


TheoreticalFileLabel = Label(popup, textvariable= theoreticaldataname)
ErrorFileButton = Button(popup, text = "select error analysis file", command = errorselectfile)


percenterrorbutton = Radiobutton(popup, text="Percent error",variable=analysistype, value = 0)
differencebutton = Radiobutton(popup, text="Absolute error",variable=analysistype, value = 1)

StartErrorAnalysisButton = Button(popup, text = "Start Error Analysis", command = performerroranalysis)
GraphErrorAnalysisButton = Button(popup, text = "graph comparison data", command = graph_theoretical_comparison)
ErrorWebGraph = Checkbutton(popup, text = "Graph in web browser?",variable = ErrorWebBrowserGraphOn)
SaveErrorAnalysisButton = Button(popup, text = "Save Error Analysis", command = WriteCSVError)
TheoreticalFileLabel.pack()
ErrorFileButton.pack()
CheckButton.pack()
percenterrorbutton.pack()
differencebutton.pack()
ErrorWebGraph.pack()
StartErrorAnalysisButton.pack()
GraphErrorAnalysisButton.pack()
SaveErrorAnalysisButton.pack()






    

ErrorAnalysisButton = Button(root, text = "Error Analysis", command = open_popup_error_analysis)


ErrorAnalysisButton.pack()

root.mainloop()