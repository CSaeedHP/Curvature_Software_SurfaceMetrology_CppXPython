import numpy as np

def diff_slope (points):

    ABX = (points[0][0]-points[1][0])
    ABZ = (points[0][1]-points[1][1])
    if(ABX == 0):
        print('Slope = undifiend')

    SlopeAB = (ABZ/ABX)

    BCX = (points[1][0]-points[2][0])
    BCZ = (points[1][1]-points[2][1])

    if(BCX == 0):
        disp('Slope = undifiend')

    SlopeBC = (BCZ/BCX)

    if(SlopeBC == SlopeAB):
        print('Straight line')
        return 0
    else:
        return (SlopeAB - SlopeBC)/(points[2][0]-points[0][0])
