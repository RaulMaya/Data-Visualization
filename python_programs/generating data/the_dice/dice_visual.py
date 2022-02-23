# Creating a histogram
from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Side

# Creating a D6
die = Side(6)

# Make some rolls, and store the results
results = []
for ind_roll in range(1500):
    result = die.roll()
    results.append(result)

# Reviewing the results
frec = []
for value in range(1, die.num_sides + 1):
    frecuency = results.count(value)
    frec.append(frecuency)
print(frec)

# Feeding the histogram
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frec)]

x_axis_config = {'title':'Dice Individual Value'}
y_axis_config = {'title':'Frecuency of Individual Value'}

my_hist = Layout(title='Output of Rolling One 6-Sided Dice 1500 Times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout':my_hist}, filename = 'six_sided.html')