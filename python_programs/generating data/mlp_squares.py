#%matplotlib inline
import matplotlib.pyplot as plt

# Graph Rev 4
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('ggplot')
# fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(input_values,squares, linewidth = 3)

# Setting the title and the label names
ax.set_title('Square Numbers', fontsize = 15)
ax.set_xlabel('Value', fontsize = 10)
ax.set_ylabel('Square of Values', fontsize = 10)

# Setting the size of the ticks
ax.tick_params(axis='both', labelsize = 10)

plt.show()
fig.savefig('../../outputs/generating data/mlp_squares/mlp_output4.png', bbox_inches = 'tight')