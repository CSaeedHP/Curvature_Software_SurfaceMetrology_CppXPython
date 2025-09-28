import numba
import plotly.graph_objects as go
import pandas as pd
import tkinter
from tkinter import filedialog
tkinter.Tk().withdraw() 
window = tkinter.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()
import os

import plotly.express as px
#REMEMBER TO ADD HEADER!!!! DEFINE THE COLUMNS BY GIVING THEM NAMES


def filelabeling(): #used with select file button and filelabel
    '''mutates fileobject into data if valid file is inputted
    sets filelabel to path of file, fileobject is false if bad file'''
    file = filedialog.askopenfile(parent=window,
                                  initialdir="./",
                                  title="Select A File",
                                  filetypes = (("CSV files (Comma separated value)", "*.csv"),
                                               ("Text files", "*.txt"), 
                                               ("All files", "*")))
    print(type(file))
    if file:
        return(os.path.abspath(file.name))
    try:
        data = file.read().split()
    except UnicodeDecodeError:
        print("Unicode error: Data File Incompatible!") #handles incompatible files
        return
    for i in range(len(data)):
        point = data[i].split(',')
        try:
            x = float(point[0]); z = float(point[1])
        except ValueError:
            print("Field error: Data File Incompatible!") #handles incompatible files

            return
    return

filename = filelabeling()


df = pd.read_csv(rf"{filename}")
df.columns = ['X','S','C']
print(df)
if len(df) > 650000:
    df = df.sample(n=650000) #modify this number
zmax = df['C'].max()
zmin = df['C'].min()

print(df)

print(zmin,zmax)
fig = px.scatter_3d(df, x='X',y='S',z='C',range_z=[zmin,zmax])
fig.show()
# # Read data from a csv
# z_data = pd.read_csv(r"C:\Users\J\Downloads\export.csv")\]=

# fig = go.Figure(data=go.Scatter3d(z=z_data))
# fig.update_layout(
#     title='Mt Bruno Elevation',
#     width=400, height=400,
#     margin=dict(t=40, r=0, l=20, b=20)
# )

# name = 'default'
# # Default parameters which are used when `layout.scene.camera` is not provided
# camera = dict(
#     up=dict(x=0, y=0, z=1),
#     center=dict(x=0, y=0, z=0),
#     eye=dict(x=1.25, y=1.25, z=1.25)
# )

# fig.update_layout(scene_camera=camera, title=name)
# fig.show()