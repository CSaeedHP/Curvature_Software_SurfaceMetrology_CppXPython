import matplotlib.pyplot as plt
import numpy as np

# t = np.arange(0.0, 2.0, 0.01)
# s1 = np.sin(2*np.pi*t)
# s2 = np.sin(4*np.pi*t)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t, s1)
# plt.subplot(212)
# plt.plot(t, 2*s1)

# plt.figure(2)
# plt.plot(t, s2)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t, s2, 's')
# ax = plt.gca()
# ax.set_xticklabels([])

# plt.show()

import pydeck
import pandas as pd

def pydeckplot(XSC):
    df = XSC
    print(df)
    target = XSC[0]

    point_cloud_layer = pydeck.Layer(
        "PointCloudLayer",
        data=df,
        get_position=["x", "y", "z"],
        get_normal=[0, 0, 15],
        color = [255,255,0],
        auto_highlight=True,
        pickable=True,
        point_size=3,
    )

    view_state = pydeck.ViewState(target=target, controller=True, rotation_x=15, rotation_orbit=30, zoom=5.3)
    view = pydeck.View(type="OrbitView", controller=True)

    r = pydeck.Deck(point_cloud_layer, initial_view_state=view_state, views=[view])
    r.to_html("point_cloud_layer.html", css_background_color="#add8e6")