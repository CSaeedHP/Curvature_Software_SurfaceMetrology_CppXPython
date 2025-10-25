import fastplotlib as fpl
import numpy as np

xs = np.linspace (-10, 10, 100)
ys = np.sin(xs)
data = np.dstack([xs, ys])[0]

figure = fpl.Figure()
line_graphic = figure[0,0].add_line(data=data,thickness=5,color='cyan')
figure.show90
fpl.loop.run()