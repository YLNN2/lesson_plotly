import plotly.graph_objs as go
import numpy as np
import pandas as pd

dices = pd.DataFrame(np.random.randint(low=1, high=7, size=(100, 2)), columns=('Кость 1', 'Кость 2'))
dices['Сумма'] = dices['Кость 1'] + dices['Кость 2']
dices2 = pd.DataFrame(np.random.randint(low=1, high=7, size=(100, 2)), columns=('Кость 1', 'Кость 2'))
dices2['Сумма'] = dices2['Кость 1'] + dices2['Кость 2']
dices3 = pd.DataFrame(np.random.randint(low=1, high=7, size=(1000, 2)), columns=('Кость 1', 'Кость 2'))
dices3['Сумма'] = dices3['Кость 1'] + dices3['Кость 2']

fig = go.Figure()
fig.add_trace(go.Histogram(x=dices['Сумма'], histnorm='probability density'))
fig.add_trace(go.Histogram(x=dices2['Сумма'], histnorm='probability density'))
fig.add_trace(go.Histogram(x=dices3['Сумма'], histnorm='probability density'))
fig.show()
