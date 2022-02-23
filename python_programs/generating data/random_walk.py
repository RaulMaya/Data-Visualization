# Importing Modules
%matplotlib inline
import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    # Class to generate random walks
    
    def __init__(self, num_points = 7000):
        self.num_points = num_points
        
        # Starting walks at 0, 0
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        # Calculating points in the walk
        # Specifying the desired length
        
        while len(self.x_values) < self.num_points:
            # Deciding the direction and the distance
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            # Reject no moves
            if x_step == 0 and y_step == 0:
                continue
                
            # Calculating the new position
            x =  self.x_values[-1] + x_step
            y =  self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
                        

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