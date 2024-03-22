
from tests import *
import numpy as np
import functions_class
from alive_progress import alive_bar;
#pip install alive-progress

#putting all the functions inside a dictionary
function_keys = {
    "herons" : "herons_curvature",
    "diffslope" : "diff_slope",
    "calculus" : "quad_curvature",
    "3lag" : "oriented_lagrangian",
    "fda" : "fin_diff_slope"
}

#this processes all the curvatures

#returns the curvature of a given 2d array of 3 points
#functionally hybrid, work is needed




#data is a two dimensional list of points
#points_org is a 4-d list (1st level: scales; 2nd level: set of 3 points (this will later be converted into curvatures); 3rd level: x,y coordinates of a single point)
def parse_data(data,functionkey,min,max):
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
                XSC.append([X, S, C])
            scale += 1
            bar()
    return XSC

def parse_hybrid_data(data,obtusekey,acutekey,min,max):
    '''takes in points data, and a function key. Returns n by 3 array, columns are X values, Scales, and Curvatures'''
    #pass in function key here
    #dictionary reference goes here

    #define curvature function to be used here
    
    obtusefunction = getattr(functions_class,function_keys[obtusekey])
    acutefunction = getattr(functions_class,function_keys[acutefunction])
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
'''
def percent_rror(xsc, curv_theoretical):
    x_positions = xsc[0][:] #array of x positions
    curv_calculated = xsc[1][:] #array of calculated curvature values
    scales = xsc[2][0]   #array of scales


    curv_theoretical = curv_theoretical[2:len(curv_theoretical)-1][:] #
    [rows, columns] = len(x_positions)

    PE = []
    search = 1
    indexlimits = []

    while search < columns:
        if scales[search] == scales[search+1]:
            indexlimits = [indexlimits, search]
        search = search + 1
    
    iteration = 1
    act_curv_val_index = 1
    ili = 1

    [row1, column1] = len(indexlimits)
    
    while iteration < columns:
        #Actualcurvature rows change, not columns (column 1 = x_pos position, column 2 = curvature) 
        if((ili < search) and (ili <= column1) and iteration == indexlimits(ili)))
            act_curv_val_index = find(curv_theoretical(:, 1) == x_pos(iteration))
            ili = ili + 1

        PE[iteration] = (abs((curv_theoretical(act_curv_val_index, 2) - curv_calculated(iteration))/(curv_theoretical(act_curv_val_index, 2)))*100);

        act_curv_val_index =+ 1
        iteration =+ 1
        
    act_curv_val_index = find(curv_theoretical(:, 1) == x_pos(columns));
    PE[iteration] = (abs((curv_theoretical(act_curv_val_index, 2) - C(iteration))/(curv_theoretical(act_curv_val_index, 2)))*100);

    return PE

'''

