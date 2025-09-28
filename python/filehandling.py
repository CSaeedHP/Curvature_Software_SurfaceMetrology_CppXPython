import os
import csv 
import tkinter
from tkinter import filedialog
tkinter.Tk().withdraw() 
window = tkinter.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()
# def OpenCSV():
#     '''Opens native file explorer. Opens CSV files only.'''
#     fileToOpen = filedialog.askopenfile() #generate TextIOWrapper object

    
#         # Return a reader object which will 
#         # iterate over lines in the given csvfile 
#     csv_reader = csv.reader(fileToOpen) #consumes TextIoWrapper object

#     # convert string to list 
#     list_of_csv = list(csv_reader)
#     return list_of_csv

def ReadCSV(CSVtoRead):
    csv_reader = csv.reader(CSVtoRead)
    list_of_csv = list(csv_reader)
    return list_of_csv


def OpenCSV():
    my_file = filedialog.askopenfile(parent=window,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    data = my_file.read().split()
    for i in range(len(data)):
        point = data[i].split(',')
        x = float(point[0]); y = float(point[1])
        data[i] = [x, y]
    for x in data:
        return data
    


def OpenCSVexceptionhandler():
    my_file = filedialog.askopenfile(parent=window,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    data = my_file.read().split()
    for i in range(len(data)):
        point = data[i].split(',')
        try:
            x = float(point[0]); y = float(point[1])
        except ValueError:
            print("Value error")
            return
        data[i] = [x, y]
    for x in data:
        return data


def DataReader(my_file):
    data = my_file.read().split()
    for i in range(len(data)):
        point = data[i].split(',')
        x = float(point[0]); y = float(point[1])
        data[i] = [x, y]
    for x in data:
        return data


def WriteCSV(XSC):
    '''writes input list of list to csv file at user specified location'''
    new_file = filedialog.asksaveasfile(parent=window,
                                        initialdir="",
                                        title="Select A File",
                                        filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    writer = csv.writer(new_file)
    writer.writerows(XSC)
def TestWrite():
    filedialog.asksaveasfile()



def OpenFile():
    my_file = filedialog.askopenfile(parent=window,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    return os.path.abspath(my_file.name)