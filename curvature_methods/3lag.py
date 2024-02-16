import numpy as np

def oriented_lagrangian(points):
    return  (2*(points[1][0])-(points[1][1])-(points[1][2]))/((((points[0][2]) - (points[0][0]))/2)^2)