# Importing Modules
%matplotlib inline
import matplotlib.pyplot as plt
from random import choice

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plotting points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(20,12))
    point_num = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_num, cmap=plt.cm.cool, edgecolors='none', s=2)
    
    # Start and end point
    ax.scatter(0,0, c = 'lightgreen', edgecolors = 'black', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='black', s=100)
    
    # Removing axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    fig.savefig('../outputs/random_walks/rw_output4.png')
    
    continue_running = input('Make another run? (yes/no):')
    if continue_running == 'no':
        break