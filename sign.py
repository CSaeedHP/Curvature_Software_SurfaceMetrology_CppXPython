from math import atan

#finds the sign of the curvature
def sign_calc(points):
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    slope1 = (z2 - z1)/(x2 - x1)
    slope2 = (z3 - z2)/(x3 - x2)
    if atan(slope2) >= atan(slope1):
        return True
    else:
        return False