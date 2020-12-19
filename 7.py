import plotly.graph_objs as go
import numpy as np

x = np.arange(0, 5, 0.1)


def f(x):
    return x ** 2


fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=f(x), name='f(x)=x<sup>2</sup>'))
fig.add_trace(go.Scatter(x=x, y=x, name='g(x)=x'))
fig.add_trace(go.Scatter(x=x, y=np.sin(x), name='h(x)=sin(x)'))
fig.update_layout(
    title="Графики",
    xaxis_title="x",
    yaxis_title="y")
fig.show()
