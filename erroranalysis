from tkinter import *
from tkinter import ttk
import matplotlib
from tkinter import filedialog
popup = Toplevel(root)
popup.wm_attributes('-topmost', 1)
popup.minsize(400,400)
popup.title("Error analysis")
popup.withdraw()
ErrorData = Variable()
theoreticaldataname = Variable()
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
            plt.figure("theoretical curvatures")
            plot2d(data)
            theoryfilenamesolo.set(os.path.basename(file.name))
            return
        
def performerroranalysis():
    if theoreticalfileobject.get() and XSC.get():
        ErrorData.set(analysis.GUI_percent_error(XSC.get(),theoreticalfileobject.get(),minimumcached.get()))
    else:
        nofileerror = messagebox.showerror("analysis not started", "Curvature data or measured data not detected")




def checkdata():
    theoreticalfile = theoreticalfileobject.get()
    if theoreticalfile:
        plot2d(theoreticalfile)
        return
    else:
        errorwindow = messagebox.showwarning("No file selected", "No curvature data has been loaded.")
def WriteCSV():
    '''writes input list of list to csv file at user specified location'''
    file = XSC.get()
    if file:
        new_file = filedialog.asksaveasfile(parent=popup,
                                            initialdir="",
                                            title="Save as",
                                            filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                                ("Text files", "*.txt"), 
                                                ("All files", "*")))
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
StartErrorAnalysisButton = Button(popup, text = "Start Error Analysis", command = performerroranalysis)

TheoreticalFileLabel.pack()
ErrorFileButton.pack()
StartErrorAnalysisButton.pack()
CheckButton.pack()

    





    

ErrorAnalysisButton = Button(root, text = "Error Analysis", command = open_popup_error_analysis)


ErrorAnalysisButton.pack()
