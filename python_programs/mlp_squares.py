%matplotlib inline
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth = 3)

# Setting the title and the label names
ax.set_title('Square Numbers', fontsize = 20)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of Values', fontsize = 14)

# Setting the size of the ticks
ax.tick_params(axis='both', labelsize = 14)

plt.show()
fig.savefig('../outputs/mlp_output_main.png')