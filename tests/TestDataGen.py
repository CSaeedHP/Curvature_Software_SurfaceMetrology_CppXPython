import math
import sympy as sp
import numpy as np

x = sp.symbols('x')
f = math.sqrt(2-x^2)

range = 2
minscale = 0.1

#Define derivative and second derivative of function for curvature calculation
df = sp.diff(f, x)
d2f = sp.diff(df, x)


for i in range(0,maxx-minx):
    z = []
    c = []

    pos = i+minx
    inst_curvature = d2f(pos)/((1+(df(pos))^2)^(3/2))
    
    z[i][0] = pos
    z[i][1] = f(pos)
    c[i][0] = pos
    c[i][1] = inst_curvature

    print("position:", z[i][0], " z value", z[i][1])

    