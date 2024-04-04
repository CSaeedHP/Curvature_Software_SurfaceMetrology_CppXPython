from tests import *
import numpy as np
import functions_class
from alive_progress import alive_bar;
from tkinter import ttk
import tkinter as tk
#pip install alive-progress

#putting all the functions inside a dictionary
function_keys = {
    "herons" : "herons_curvature",
    "diffslope" : "diff_slope",
    "calculus" : "quad_curvature",
    "3lag" : "oriented_lagrangian",
    "fda" : "fin_diff_slope",
    "AcuteTest" : "isObtuse"
}

#this processes all the curvatures

#returns the curvature of a given 2d array of 3 points
#functionally hybrid, work is needed

def trunkate_float(value, places):
    multiplier = 10 ** int(places)
    return int(multiplier*value)/multiplier


#data is a two dimensional list of points
#points_org is a 4-d list (1st level: scales; 2nd level: set of 3 points (this will later be converted into curvatures); 3rd level: x,y coordinates of a single point)
def parse_data(data,functionkey,min,max, dec_places):
    '''takes in points data, and a function key. Returns n by 3 array, columns are X values, Scales, and Curvatures'''
    #pass in function key here
    #dictionary reference goes here

    #define curvature function to be used here
    
    choicefunction = getattr(functions_class,function_keys[functionkey])
    # points_org = []
    XSC = [] #X is X positions, S is scales, C is curvatures
    min_length_interval = (data[1][0] - data[0][0])
    datamax = len(data)
    scale = min
    with alive_bar(max - min + 1) as bar:
        while scale <= max:
            # if 2*scale + 1 > n: # make conditon, while co ndition?
            #     break
            # points_org.append([]) deprecated
            S = scale * min_length_interval
            for i in range(0, datamax - 2*scale):
                #points is what gets passed into the curvature function
                # points = [[data[i][0], data[i][1]], [data[i + scale][0], data[i + scale][1]], [data[i + 2 * scale][0], data[i + 2 * scale][1]]]
                
                X = data[i + scale][0] #points[1][0]
                
                C = choicefunction(data[i][0], data[i][1], X, data[i + scale][1], data[i + 2 * scale][0], data[i + 2 * scale][1])

                C = trunkate_float(C, dec_places)

                XSC.append([X, S, C])
            scale += 1
            bar()
    return XSC

def GUIparse_data(data,functionkey,min,max):
    '''takes in points data, and a function key. Returns n by 3 array, columns are X values, Scales, and Curvatures'''
    #pass in function key here
    #dictionary reference goes here

    #define curvature function to be used here
    maxprog = max - min + 1
    progress = 0
    messagevar = tk.StringVar()
    popup = tk.Toplevel()
    tk.Label(popup, textvariable = messagevar).pack()
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable = progress_var, maximum = maxprog)
    progress_bar.pack()
    


    choicefunction = getattr(functions_class,function_keys[functionkey])
    # points_org = []
    XSC = [] #X is X positions, S is scales, C is curvatures
    min_length_interval = (data[1][0] - data[0][0])
    datamax = len(data)
    scale = min

    while scale <= max:
        # if 2*scale + 1 > n: # make conditon, while co ndition?
        #     break
        # points_org.append([]) deprecated
        S = scale * min_length_interval
        for i in range(0, datamax - 2*scale):
            #points is what gets passed into the curvature function
            # points = [[data[i][0], data[i][1]], [data[i + scale][0], data[i + scale][1]], [data[i + 2 * scale][0], data[i + 2 * scale][1]]]
            
            X = data[i + scale][0] #points[1][0]
            
            C = choicefunction(data[i][0], data[i][1], X, data[i + scale][1], data[i + 2 * scale][0], data[i + 2 * scale][1])
            XSC.append([X, S, C])
        scale += 1
        popup.update()
        progress += 1
        progress_var.set(progress)
        messagevar.set(f"Standard analysis in progress...\n{progress} of {maxprog}")
    popup.destroy()
    return XSC

def parse_hybrid_data(data,obtusekey,acutekey,min,max):
    '''takes in points data, and a function key. Returns n by 3 array, columns are X values, Scales, and Curvatures'''
    #pass in function key here
    #dictionary reference goes here

    #define curvature function to be used here
    
    obtusefunction = getattr(functions_class,function_keys[obtusekey])
    acutefunction = getattr(functions_class,function_keys[acutekey])
    # points_org = []
    XSC = [] #X is X positions, S is scales, C is curvatures
    min_length_interval = (data[1][0] - data[0][0])
    datamax = len(data)
    scale = min
    with alive_bar(max - min + 1) as bar:
        while scale <= max:
            # if 2*scale + 1 > n: # make conditon, while co ndition?
            #     break
            # points_org.append([]) deprecated
            S = scale * min_length_interval
            for i in range(0, datamax - 2*scale):
                #points is what gets passed into the curvature function
                # points = [[data[i][0], data[i][1]], [data[i + scale][0], data[i + scale][1]], [data[i + 2 * scale][0], data[i + 2 * scale][1]]]
                x1  = data[i][0]
                x2 = data[i + scale][0] #points[1][0]
                x3 = data[i + 2 * scale][0]
                z1 = data[i][1]
                z2 = data[i + scale][1]
                z3 = data[i + 2 * scale][1]
                if functions_class.isObtuse(x1,z1,x2,z2,x3,z3):
                    C = obtusefunction(x1,z1,x2,z2,x3,z3)
                else:
                    C = acutefunction(x1,z1,x2,z2,x3,z3)
                XSC.append([x2, S, C])
            scale += 1
            bar()
    return XSC



def GUI_parse_hybrid_data(data,obtusekey,acutekey,min,max):
    '''takes in points data, and a function key. Returns n by 3 array, columns are X values, Scales, and Curvatures'''
    #pass in function key here
    #dictionary reference goes here
    maxprog = max - min + 1
    progress = 0
    messagevar = tk.StringVar()
    popup = tk.Toplevel()
    tk.Label(popup, textvariable = messagevar).pack()
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable = progress_var, maximum = maxprog)
    progress_bar.pack()
    #define curvature function to be used here
    
    obtusefunction = getattr(functions_class,function_keys[obtusekey])
    acutefunction = getattr(functions_class,function_keys[acutekey])
    # points_org = []
    XSC = [] #X is X positions, S is scales, C is curvatures
    min_length_interval = (data[1][0] - data[0][0])
    datamax = len(data)
    scale = min
    while scale <= max:
        # if 2*scale + 1 > n: # make conditon, while co ndition?
        #     break
        # points_org.append([]) deprecated
        S = scale * min_length_interval
        for i in range(0, datamax - 2*scale):
            #points is what gets passed into the curvature function
            # points = [[data[i][0], data[i][1]], [data[i + scale][0], data[i + scale][1]], [data[i + 2 * scale][0], data[i + 2 * scale][1]]]
            x1  = data[i][0]
            x2 = data[i + scale][0] #points[1][0]
            x3 = data[i + 2 * scale][0]
            z1 = data[i][1]
            z2 = data[i + scale][1]
            z3 = data[i + 2 * scale][1]
            if functions_class.isObtuse(x1,z1,x2,z2,x3,z3):
                C = obtusefunction(x1,z1,x2,z2,x3,z3)
            else:
                C = acutefunction(x1,z1,x2,z2,x3,z3)
            XSC.append([x2, S, C])
        scale += 1
        popup.update()
        progress += 1
        progress_var.set(progress)
        messagevar.set(f"Hybrid analysis in progress...\n{progress} of {maxprog}")
    popup.destroy()
    return XSC

def get_curvature(data):
    #positions is a list of lists, which each sublist represent a scale and each individual element is the central x-value for that point 
    positions = []
    #print(positions)
    for scale in range(len(data)):
        positions.append([])
        for set in range(len(data[scale])):
            positions[-1].append(data[scale][set][1][0])
            data[scale][set] = curvature(data[scale][set])
    #print(positions)
    return [data, positions]




#returns the average of the magnitude in % error
def compare(data, real):
    sum = 0
    for i in range(len(data)):
        sum += abs(real[i+1][1] - data[i])/real[i][1]
    return 100 * sum/len(real)




#gets the 'pixel length' of the data
def get_spacing():
    data = format_data("sineP.txt")
    return data[1][0] - data[0][0]


#returns the actual curvature data for the test sample
def get_actual():
    return format_data("sineC.txt")


#returns percent error (0-100) between two given values
def error_calculation(calculated, theoretical):
    perc_error  = abs(calculated-theoretical)/theoretical
    return perc_error


def percent_error(xsc, curv_theoretical, listshrink):
    #inputs: XSC (x, scale, curv), Theoretical curvature (x, Curv)
    #return: XSPE (x, scale, percent_error)
    XSPE = []
    i = 0
    while i < listshrink:
        curv_theoretical = curv_theoretical[1:-1]
        i += 1
    #Iterate through positons
    i = 0
    CT_index = 0
    with alive_bar(len(xsc))as bar:
        while i < len(xsc):
                if (CT_index == len(curv_theoretical)):
                    curv_theoretical = curv_theoretical[1:-1]
                    CT_index = 0
                position = xsc[i][0]
                expected_curvature = curv_theoretical[CT_index][1]
                calculated_curvature = xsc[i][2]
                perc_error = error_calculation(calculated_curvature, expected_curvature)
                XSPE.append([position, xsc[i][1], perc_error])
                i += 1
                CT_index += 1
                bar()
        return XSPE
