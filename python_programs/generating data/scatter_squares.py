# Importing Modules
%matplotlib inline
import matplotlib.pyplot as plt

# Graph Rev 7
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# Using Colormap
# Colormap references: 
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.plasma, s = 10)

# Setting titles and axes names
ax.set_title('Square Numbers', fontsize = 20)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of Values', fontsize = 14)

# Set size of the ticks labels
ax.tick_params(axis='both', which='major', labelsize = 14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
fig.savefig('../outputs/scatter_output7.png', bbox_inches = 'tight')