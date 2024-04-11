from math import atan
import numpy as np

#---------------------------------------------------------------------------------------------------------------------
#Herons

#returns the area of a triangle given side lengths (herons)
def area_heron(a, b, c):
    s = (a + b + c)/2

    return (s * (s-a) * (s-b) * (s-c)) ** 0.5
# 10


#returns distance between two points
def pythag(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return (x**2 + y**2) ** 0.5
# 6


def herons_curvature(x1,z1,x2,z2,x3,z3):
    # x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    a = pythag(x1, z1, x2, z2)
    b = pythag(x1, z1, x3, z3)
    c = pythag(x2, z2, x3, z3)


    

    trianglearea = area_heron(a, b, c)
    if (z3 + z1) / 2 < z2:
        return -4 * trianglearea / a / b / c
    elif (z3 + z1) / 2 ==z2:
        return 0
    return 4 * trianglearea / a / b / c


#matlab translation
def CurveHeron(x1,z1,x2,z2,x3,z3):

    ABX = x1-x2
    ABZ = z1-z2
    if(ABX == 0):
        print('Slope = undifiend')

    SlopeAB = (ABZ/ABX)

    BCX = x2-x3
    BCZ = z2-z3
    if(BCX == 0):
        print('Slope = undifiend')

    SlopeBC = (BCZ/BCX)

    yfor = (SlopeAB * x3) + (z1 - (SlopeAB*x1))

    if(SlopeBC == SlopeAB):
        # print('Straight line')
        return 0
    elif(SlopeAB != SlopeBC):
        sideA =((x1-x2)**2+(z1-z2)**2)**0.5
        sideB =((x3-x2)**2+(z3-z2)**2)**0.5
        sideC =((x1-x3)**2+(z1-z3)**2)**0.5
    SP = ((sideA + sideB + sideC)/2)#Semi Perimeter 
    CurveHeron = 4*(SP * (SP - sideA)**2 * (SP - sideB) * (SP - sideC))/(sideA * sideB * sideC)
    if(z3 < yfor):
        CurveHeron = (CurveHeron * -1)
    return CurveHeron




#---------------------------------------------------------------------------------------------------------------------
#Calculus (parabola in matlab)

#finds a quadratic function that matches three points
def find_quadratic(x1,z1,x2,z2,x3,z3):
    # x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    a = np.array([
        [x1**2, x1, 1],
        [x2**2, x2, 1],
        [x3**2, x3, 1]
        ])
    b = np.array([z1, z2, z3])
    solution = np.linalg.solve(a, b)
    return list(solution)

#uses calculus method to find curvature after fitting the points to a parabola
def quad_curvature(x1,z1,x2,z2,x3,z3):
    # x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    quadratic = find_quadratic(x1, z1, x2, z2, x3, z3)
    #print(quadratic)
    a = quadratic[0]
    b = quadratic[1]
    x = x2
    first_deriv = 2 * a * x + b
    second_deriv = 2 * a
    curvature = abs(second_deriv)/((1 + first_deriv**2)**1.5)
    if (z3 + z1) / 2 < z2:
        return -4 * curvature
    elif (z3 + z1) / 2 ==z2:
        return 0
    return 4 * curvature

#---------------------------------------------------------------------------------------------------------------------
# Difference of slopes

def diff_slope (x1,z1,x2,z2,x3,z3):

    # ABX = (points[0][0]-points[1][0])
    # ABZ = (points[0][1]-points[1][1])
    ABX = (x1-x2)
    ABZ = (z1-z2)
    if(ABX == 0):
        print('Slope = undifiend')

    SlopeAB = (ABZ/ABX)

    # BCX = (points[1][0]-points[2][0])
    # BCZ = (points[1][1]-points[2][1])
    BCX = (x2-x3)
    BCZ = (z2-z3)

    if(BCX == 0):
        print('Slope = undifiend')

    SlopeBC = (BCZ/BCX)

    if(SlopeBC == SlopeAB):
        print('Straight line')
        return 0
    else:
        # return (SlopeAB - SlopeBC)/(points[2][0]-points[0][0])
        return (SlopeAB - SlopeBC)/(x3-x1)

#---------------------------------------------------------------------------------------------------------------------
#Langrangian
def oriented_lagrangian(x1,z1,x2,z2,x3,z3):
    return  (2*(z1)-(z2)-(z3))/((((x3) - (x1))/2)**2)

#---------------------------------------------------------------------------------------------------------------------
#fda
def fin_dif_slope(x1,z1,x2,z2,x3,z3):
    # x1 = points[0][0]
    # x2 = points[1][0]
    # x3 = points[0][2]
    # z1 = points[0][1]
    # z2 = points[1][1]
    # z3 = points[2][0]

    ZPrime = (z3-z1)/(x3-x1)

    ZDoublePrime = (((z3-z2)/(x3-x2))-((z2-z1)/(x2-x1)))/((x3-x2)*(x2-x1))
    
    return  ZDoublePrime/((1+ZPrime^2)**1.5)


#---------------------------------------------------------------------------------------------------------------------
def isObtuse(x1,z1,x2,z2,x3,z3):
    slope1 = (z2 - z1)/(x2 - x1)
    slope2 = (z3 - z2)/(x3 - x2)
    return slope1 * slope2 >= -1




#---------------------------------------------------------------------------------------------------------------------
#for defining new functions:
# make sure your function follows the following format:
# def function(x1,z1,x2,z2,z3,z3):
#     ...
#     ...
#     ...
#     return curvature
#---------------------------------------------------------------------------------------------------------------------
def herons(x1,z1,x2,z2,x3,z3):
    if isObtuse(x1,z1,x2,z2,x3,z3):
        return herons_curvature(x1,z1,x2,z2,x3,z3) * (2 * sign_calc(x1,z1,x2,z2,x3,z3) - 1)
    else:
        return quad_curvature(x1,z1,x2,z2,x3,z3) * (2 * sign_calc(x1,z1,x2,z2,x3,z3) - 1)
    

def sign_calc(points):
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    slope1 = (z2 - z1)/(x2 - x1)
    slope2 = (z3 - z2)/(x3 - x2)
    if atan(slope2) >= atan(slope1):
        return True
    else:
        return False