# Importing Modules

import matplotlib.pyplot as plt
#%matplotlib inline

# Graph Rev 7
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(5,3))

# Using Colormap
# Colormap references: 
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.plasma, s = 10)

# Setting titles and axes names
ax.set_title('Square Numbers', fontsize = 15)
ax.set_xlabel('Value', fontsize = 10)
ax.set_ylabel('Square of Values', fontsize = 10)

# Set size of the ticks labels
ax.tick_params(axis='both', which='major', labelsize = 10)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
fig.savefig('../../outputs/generating data/scatter_squares/scatter_output7.png', bbox_inches = 'tight')