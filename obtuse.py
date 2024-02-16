import math

#finds angle between a and b given three side lengths of a triangle
def find_angle(a, b, c):
    return math.acos((c**2 - a**2 - b**2)/(-2 * a * b)) * 180 / math.pi

#returns distance between two points
def pythag(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return (x**2 + y**2) ** 0.5

#checks if a triangle is obtuse or not using pythag inequalities
#point A is the left most, point B is the middle, point C is the right most
def isObtuse(points):
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    slope1 = (z2 - z1)/(x2 - x1)
    slope2 = (z3 - z2)/(x3 - x2)
    return slope1 * slope2 >= -1