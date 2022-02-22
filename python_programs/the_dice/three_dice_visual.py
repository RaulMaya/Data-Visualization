# Creating a histogram
from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Side

# Creating Two D6 Dices
die_1 = Side(6)
die_2 = Side(6)
die_3 = Side(6)
# Make some rolls, and store the results
results = []
for ind_roll in range(50000):
    result = die_1.roll() + die_2.roll() +die_3.roll()
    results.append(result)

# Reviewing the results
frec = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_results + 1):
    frecuency = results.count(value)
    frec.append(frecuency)
print(frec)

# Feeding the histogram
x_values = list(range(3, max_results+1))
data = [Bar(x=x_values, y=frec)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frecuency of Individual Value'}

my_hist = Layout(title='Output of Rolling Three 6-Sided Dice 51500 Times', xaxis = x_axis_config, yaxis = y_axis_config, colorway=['#E54066'])
offline.plot({'data':data, 'layout':my_hist}, filename = 'three_six_sided.html')