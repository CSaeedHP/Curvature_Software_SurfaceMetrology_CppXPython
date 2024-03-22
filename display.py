import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib as mpl
from analysis import *
from tkinter import filedialog
import time
import plotly.graph_objects as go
import math
import userIO

# start_time = time.time()

# fig, axs = plt.subplots(2)
# ax = axs[0]
# ax = plt.axes(projection='3d')
# ax2 = axs[1]
# ax.grid()

# data = get_curvature(parse_data(format_data(filedialog.askopenfile())))

# curvatures = data[0]
# locations = data[1]
# spacing = get_spacing()

# x_pos = []; curvature_data = []; scales = []
# for scale in range(len(locations)):
#     for curvature_val in range(len(locations[scale])):
#         scales.append((scale + 1) * spacing)
#         x_pos.append(locations[scale][curvature_val])
#         curvature_data.append(curvatures[scale][curvature_val])

# print(np.array(x_pos))

# ax.scatter3D(x_pos, scales, curvature_data)

# ax.set_title('3D Parametric Plot')

# # Set axes label

# ax.set_xlabel('X Position', labelpad=20)
# ax.set_ylabel('Scale', labelpad=20)
# ax.set_zlabel('Curvature', labelpad=20)

# true_data = get_actual()

# x = []
# y = []

# for i in range(len(true_data)):
#     x.append(true_data[i][0])
#     y.append(true_data[i][1])

# axs[1].plot(x, y)

# plt.show()

# print("process finished in %s", time.time()-start_time)




def plot3d(XSC):
    '''plot a set of points for curvature'''
    userlog = False
    X = [row[0] for row in XSC]
    if userIO.YesNo("Logarithmic scale?"):
        S = [math.log(row[1],10) for row in XSC]
        userlog = True
    else:
        S = [row[1] for row in XSC]
    C = [row[2] for row in XSC]
    ax = plt.axes(projection='3d')
    colors = plt.cm.turbo(C)
    ax.scatter3D(X,S,C,c=colors)
    ax.set_xlabel('X Position', labelpad=20)
    if userlog:
        ax.set_ylabel('log(Scale)', labelpad=20)
    else:
        ax.set_ylabel('Scale', labelpad=20)
    ax.set_zlabel('Curvature', labelpad=20)
    # plt.colorbar(mpl.cm.ScalarMappable(cmap='turbo'), orientation='vertical', label='Curvature',)
    return ax
    plt.show(block = False)
    
def plot2d(input_array):
    # fig, axs = plt.subplots(2)
# ax = axs[0]
# ax = plt.axes(projection='3d')
# ax2 = axs[1]
# ax.grid()
    plt.figure(1)
    X = [row[0] for row in input_array]
    Y = [row[1] for row in input_array]
    ax = plt.axes()
    ax.grid()
    ax.scatter(X,Y)
    ax.set_xlabel('X position', labelpad = 20)
    ax.set_ylabel('Height', labelpad = 20)
    return ax
    plt.show(block = False)

def plotly3d(XSC):
    marker_data = go.Scatter3d(x=[row[0] for row in XSC],
                               y=[row[1] for row in XSC],
                               z=[row[2] for row in XSC],
                               marker=go.scatter3d.Marker(size=3),
                               opacity=1,
                               mode='markers')
    fig=go.Figure(data=marker_data)
    fig.show()