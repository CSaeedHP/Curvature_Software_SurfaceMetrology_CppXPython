import math
import numpy as np


def find_quadratic(points):
    '''find a quadratic function that matches three points'''
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    a = np.array([
        [x1**2, x1, 1],
        [x2**2, x2, 1],
        [x3**2, x3, 1]
        ])
    b = np.array([z1, z2, z3])
    solution = np.linalg.solve(a, b)
    return list(solution)

find_quadratic()
#uses calculus method to find curvature after fitting the points to a parabola
def quad_curvature(points):
    x1 = points[0][0]; x2 = points[1][0]; x3 = points[2][0]; z1 = points[0][1]; z2 = points[1][1]; z3 = points[2][1]
    quadratic = find_quadratic(x1, z1, x2, z2, x3, z3)
    #print(quadratic)
    a = quadratic[0]
    b = quadratic[1]
    x = x2
    first_deriv = 2 * a * x + b
    second_deriv = 2 * a
    curvature = abs(second_deriv)/((1 + first_deriv**2)**1.5)
    return curvature