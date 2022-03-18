from fileinput import filename
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

path  = 'data/eq_data_30_day_m1.json'
with open(path) as j:
    earthquakes = json.load(j)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as j:
    json.dump(earthquakes, j, indent=4)

eq_features = earthquakes['features']
magnitudes  = []
longitudes  = []
latitudes  = []
hover_text = []

for feature in eq_features:
    magnitude = feature['properties']['mag']
    longitude = feature['geometry']['coordinates'][0]
    latitude = feature['geometry']['coordinates'][1]
    title = feature['properties']['title']

    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)
    hover_text.append(title)

data = [{
    'type':'scattergeo',
    'lon': longitudes, 
    'lat': latitudes,
    'text': hover_text,
    'marker':{
        'size': [3 * mag for mag in magnitudes],
        'color':magnitudes,
        'colorscale': 'rdylgn',
        'reversescale': True,
        'colorbar':{'title':'Magnitude'}
    }}]
        
my_layout = Layout(title = {
         'text': "Global Earthquakes",
         'y':0.9,
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top'
        })

fig ={'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')