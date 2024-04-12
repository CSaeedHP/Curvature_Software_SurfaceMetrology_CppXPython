import plotly.graph_objects as go
import pandas as pd

import plotly.express as px
#REMEMBER TO ADD HEADER!!!! DEFINE THE COLUMNS BY GIVING THEM NAMES
df = pd.read_csv(r"C:\Users\J\Downloads\circletest2.csv")
fig = px.scatter_3d(df, x='X', y='S', z='C')
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