import numpy as np

#returns the area of a triangle given side lengths (herons)
def area_heron(a, b, c):
    s = (a + b + c)/2
    return (s * (s-a) * (s-b) * (s-c)) ** 0.5
# 10


def area_shoelace(points):
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    product1 = x1 * z2 + x2 * z3 + x3 * z1
    product2 = x1 * z3 + x2 * z1 + x3 * z2
    return 0.5 * abs(product1 - product2)
# 13


#returns distance between two points
def pythag(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return (x**2 + y**2) ** 0.5
# 6


#returns curvature of 3 points using shoelace
def los_curvature(points):
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    a = pythag(x1, z1, x2, z2)
    b = pythag(x1, z1, x3, z3)
    c = pythag(x2, z2, x3, z3)
    trianglearea = area_shoelace(x1, z1, x2, z2, x3, z3)
    return 4 * trianglearea / a / b / c
# 


#returns curvature of 3 points using shoelace
def herons_curvature(points):
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    a = pythag(x1, z1, x2, z2)
    b = pythag(x1, z1, x3, z3)
    c = pythag(x2, z2, x3, z3)
    trianglearea = area_heron(a, b, c)
    return 4 * trianglearea / a / b / c

#returns curvature of 3 points using law of sines
def los_curvature(points):
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    sinA = (z2 - z1)/(pythag(x1, z1, x2, z2))
    cosA = (1- sinA**2) ** 0.5
    sinB = (z3 - z1)/(pythag(z1, z1, x3, z3))
    cosB = (1 - sinB**2) ** 0.5
    sin = sinA * cosB + sinB * cosA
    return (2 * sin)/pythag(x2, z2, x3, z3)

def herons_calc(points):
    return herons_curvature(points)