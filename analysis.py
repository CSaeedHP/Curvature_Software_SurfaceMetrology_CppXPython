
from tests import *
import numpy as np
import functions_class
from alive_progress import alive_bar;

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
def curvature(points):
    if obtuse.isObtuse(points):
        return herons.herons_calc(points) * (2 * sign.sign_calc(points) - 1)
    else:
        return calculus.quad_curvature(points) * (2 * sign.sign_calc(points) - 1)



def ops(number,data):
    if data%2 == 1:
        operations = number^2
    else:
        operations = number * (number + 1)
    return operations
#data is a two dimensional list of points
#points_org is a 4-d list (1st level: scales; 2nd level: set of 3 points (this will later be converted into curvatures); 3rd level: x,y coordinates of a single point)
def parse_data(data,functionkey,min,max):
    '''takes in points data, and a function key. Returns n by 3 array, columns are X values, Scales, and Curvatures'''
    #pass in function key here
    #dictionary reference goes here

    #define curvature function to be used here
    

    choicefunction = getattr(functions_class,function_keys[functionkey])
    points_org = []
    XSC = [] #X is X positions, S is scales, C is curvatures
    min_length_interval = (data[1][0] - data[0][0])
    datamax = len(data)
    scale = min
    with alive_bar(max - min + 1) as bar:
        while scale <= max:
            # if 2*scale + 1 > n: # make conditon, while co ndition?
            #     break
            points_org.append([])
            for i in range(0, datamax - 2*scale):
                #points is what gets passed into the curvature function
                points = [[data[i][0], data[i][1]], [data[i + scale][0], data[i + scale][1]], [data[i + 2 * scale][0], data[i + 2 * scale][1]]]
                X = points[1][0]
                S = scale * min_length_interval
                C = choicefunction(points)
                XSC.append([X, S, C])
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
