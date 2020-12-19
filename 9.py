import plotly.graph_objs as go
import numpy as np
import pandas as pd

dices = pd.DataFrame(np.random.randint(low=1, high=7, size=(100, 2)), columns=('Кость 1', 'Кость 2'))
dices['Сумма'] = dices['Кость 1'] + dices['Кость 2']
sum_counts = dices['Сумма'].value_counts().sort_index()

fig = go.Figure()
fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, sort=False, pull=0.2))
fig.show()
