import plotly.express as px
import numpy as np

x = np.arange(0, 5, 0.1)


def f(x):
    return x ** 2


fig = px.scatter(x=x, y=f(x))
fig.show()
