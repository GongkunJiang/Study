from scipy.optimize import fsolve
from math import sin, cos
from sympy import *

[x0, x1, x2] = symbols('x0 x1 x2')
x_list = [x0, x1, x2]
n = 3
F = [
    x0*cos(x1)*sin(x2),    # y0
    x0*cos(x2)*sin(x1),    # y1
    x0*cos(x2)            # y2
]
J_f = []
for i in range(len(F)):
    line = []
    for j in range(n):
        line.append(diff(F[i], x_list[j]))
    print(line)
    J_f.append(line)












