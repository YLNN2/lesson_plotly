import plotly.graph_objs as go
import numpy as np
import pandas as pd

cities = pd.read_csv('https://raw.githubusercontent.com/hflabs/city/master/city.csv')

fig = go.Figure(go.Scattermapbox(lat=cities['geo_lat'], lon=cities['geo_lon']))

capital = cities[cities['region'] == 'Москва']
map_center = go.layout.mapbox.Center(lat=capital['geo_lat'].values[0], lon=capital['geo_lon'].values[0])

fig.update_layout(mapbox_style="open-street-map", mapbox=dict(center=map_center))
fig.show()
