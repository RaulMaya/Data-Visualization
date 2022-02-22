# Creating a histogram
from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Side

# Creating Two D6 Dices
die_1 = Side(6)
die_2 = Side(6)

# Make some rolls, and store the results
results = []
for ind_roll in range(51500):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Reviewing the results
frec = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(1, max_results + 1):
    frecuency = results.count(value)
    frec.append(frecuency)
print(frec)

# Feeding the histogram
x_values = list(range(2, max_results+1))
data = [Bar(x=x_values, y=frec)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frecuency of Individual Value'}

my_hist = Layout(title='Output of Rolling Two 6-Sided Dice 51500 Times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout':my_hist}, filename = '../outputs/dice_simulation/two_six_sided.html')