from random import randint

class Side:
    """A class representing a single die"""
    
    def __init__(self, num_sides):
        self.num_sides = num_sides
        
    def roll(self):
        """Return a number from 1 to 6 (Which is the number of sides)"""
        return randint(1, self.num_sides)
    