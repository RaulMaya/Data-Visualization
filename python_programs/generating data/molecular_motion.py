# Importing Modules
#%matplotlib inline
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
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plotting points in the walk
    plt.style.use('classic')
    # fig, ax = plt.subplots(figsize=(20,12))
    fig, ax = plt.subplots(figsize=(5,3))
    ax.set_facecolor('lightskyblue')
    point_num = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c='gold', linewidth = 1.5)
    
    
    # Removing axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax.set_title('Pollen Grain on the Surface of a Drop of Water', fontsize = 10)
    plt.show()
    fig.savefig('../../outputs/generating data/random_walks/rw_output5.png')
    
    continue_running = input('Make another run? (yes/no):')
    if continue_running == 'no':
        break