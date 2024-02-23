from curvature_methods import calculus, herons, obtuse, sign
from tests import *

#this processes all the curvatures

#returns the curvature of a given 2d array of 3 points
def curvature(points):
    if obtuse.isObtuse(points):
        return herons.herons_calc(points) * (2 * sign.sign_calc(points) - 1)
    else:
        return calculus.quad_curvature(points) * (2 * sign.sign_calc(points) - 1)
    
#data is a two dimensional list of points
#points_org is a 4-d list (1st level: scales; 2nd level: set of 3 points (this will later be converted into curvatures); 3rd level: x,y coordinates of a single point)
def organize_data(data):
    points_org = []
    n = len(data)
    scale = 1
    while True:
        if 2*scale + 1 > n: # make conditon, while condition?
            break
        points_org.append([])
        for i in range(0, n - 2*scale):
            points = [[data[i][0], data[i][1]], [data[i + scale][0], data[i + scale][1]], [data[i + 2 * scale][0], data[i + 2 * scale][1]]]
            points_org[-1].append(points)
        scale += 1
    return points_org

#collects the data from sineP.txt and returns a list of points (2d list)
def format_data(file):
    my_file = open(file, "r") 
    data = my_file.read().split()
    for i in range(len(data)):
        point = data[i].split(',')
        x = float(point[0]); y = float(point[1])
        data[i] = [x, y]
    for x in data:
        return data


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
