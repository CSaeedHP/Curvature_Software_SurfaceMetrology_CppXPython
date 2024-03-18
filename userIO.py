from tkinter import filedialog
import tkinter
tkinter.Tk().withdraw()
def fileselect():
    fileToOpen =filedialog.askopenfile()
    return fileToOpen

function_keys = {
    "herons" : "herons_curvature",
    "diffslope" : "diff_slope",
    "calculus" : "quad_curvature",
    "3lag" : "oriented_lagrangian",
    "fda" : "fin_diff_slope"
}


def askkey(function_keys):
    listofkey = function_keys.keys()
    functionkey = input('Please select function analysis, or type "help" for help \n')
    
    while not functionkey in listofkey:
        if functionkey == "help":
            print("To select function analysis, choose one of the following functions:")
            print(listofkey)
            functionkey = input('Please select function analysis, or type "help" for help \n')
        else:
            functionkey = input('Your function key is invalid. Please enter a valid function key, or type "help" for more info \n')
