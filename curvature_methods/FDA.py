import numpy as np

def fin_dif_slope(points):
    x1 = points[0][0]
    x2 = points[1][0]
    x3 = points[0][2]
    z1 = points[0][1]
    z2 = points[1][1]
    z3 = points[2][0]

    ZPrime = (z3-z1)/(x3-x1)

    ZDoublePrime = (((z3-z2)/(x3-x2))-((z2-z1)/(x2-x1)))/((x3-x2)*(x2-x1))
    
    return  ZDoublePrime/((1+ZPrime^2)**1.5)