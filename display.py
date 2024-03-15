import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from analysis import *
from tkinter import filedialog
import time

start_time = time.time()

fig, axs = plt.subplots(2)
ax = axs[0]
ax = plt.axes(projection='3d')
ax2 = axs[1]
ax.grid()

data = get_curvature(parse_data(format_data(filedialog.askopenfile())))

curvatures = data[0]
locations = data[1]
spacing = get_spacing()

x_pos = []; curvature_data = []; scales = []
for scale in range(len(locations)):
    for curvature_val in range(len(locations[scale])):
        scales.append((scale + 1) * spacing)
        x_pos.append(locations[scale][curvature_val])
        curvature_data.append(curvatures[scale][curvature_val])

print(np.array(x_pos))

ax.scatter3D(x_pos, scales, curvature_data)

ax.set_title('3D Parametric Plot')

# Set axes label
ax.set_xlabel('X Position', labelpad=20)
ax.set_ylabel('Scale', labelpad=20)
ax.set_zlabel('Curvature', labelpad=20)

true_data = get_actual()

x = []
y = []

for i in range(len(true_data)):
    x.append(true_data[i][0])
    y.append(true_data[i][1])

axs[1].plot(x, y)

plt.show()

print("process finished in %s", time.time()-start_time)