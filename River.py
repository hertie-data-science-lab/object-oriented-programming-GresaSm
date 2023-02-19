# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
from Creatures import Bear, Fish
import numpy as np

class River:                                                            #defining the river class
    def __init__(self, n_room, bear, fish):
        self.n_room = n_room
        self.river = [None] * self.n_room                               #creating empty cells or rooms in the river
        self.populate(bear, fish)                                       #populating the river with the creatures                  
    
    def populate(self, bear, fish):                                    #defining the population of the river and the random positions of the creatures
        placement = np.random.choice(self.n_room, bear+fish, replace=False)
        for y, place in enumerate(placement):
            if y < bear:
                self.river[place] = Bear(place, self.river)
            else:
                self.river[place] = Fish(place, self.river)

    def simulate(self, steps):                                   #simulating the river and the moves of the creatures   
        for y in range(steps):
            for creature in self.river:
                if creature:
                    creature.move()
            print(self) 
    def __str__(self):                                           #defining the string method for the river
        return ''.join(['B' if isinstance(creature, Bear) else 'F' if isinstance(creature, Fish) else '-' for creature in self.river])