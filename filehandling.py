
import csv 
import tkinter
from tkinter import filedialog
tkinter.Tk().withdraw() 
def OpenCSV():
    '''Opens native file explorer. Opens CSV files only.'''
    fileToOpen =filedialog.askopenfile() #generate TextIOWrapper object

    
        # Return a reader object which will 
        # iterate over lines in the given csvfile 
    csv_reader = csv.reader(fileToOpen) #consumes TextIoWrapper object

    # convert string to list 
    list_of_csv = list(csv_reader) 

