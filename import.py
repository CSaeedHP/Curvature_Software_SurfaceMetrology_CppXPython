 
import csv 
import tkinter
from tkinter import filedialog
tkinter.Tk().withdraw() 
fileToOpen = str(filedialog.askopenfile())
print(fileToOpen)
with open(fileToOpen, 'r') as read_obj: 
  
    # Return a reader object which will 
    # iterate over lines in the given csvfile 
    csv_reader = csv.reader(read_obj) 
  
    # convert string to list 
    list_of_csv = list(csv_reader) 
  
    print(list_of_csv)
