# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""

from abc import ABCMeta, abstractmethod
import numpy as np

class Creature(metaclass=ABCMeta):
    def __init__(self, position, river):    #initializing the defined creature class
        self.position = position
        self.river = river

    @abstractmethod                         #integrating the abstract method which defines the move method for the bear and fish classes
    def move(self):
        pass
#creating the fish and bear subclasses which inherit from the creature class
class Bear(Creature):
    def move(self):
        empty_cell = [a for a, x in enumerate(self.river) if x is None]         #as requested from the task, defining the empty cells and adjacent cells for the moves of subclasses
        adjacent_cell = [a for a in [self.position-1, self.position+1] if a >= 0 and a < len(self.river)]
        moves_to = np.random.choice(empty_cell + adjacent_cell)
        if moves_to in empty_cell:
            self.river[self.position], self.river[moves_to] = None, self
            self.position = moves_to
        else:                                       #defining the interaction between the creatures as requested
            other = self.river[moves_to]
            if isinstance(other, Bear):             #same type of creature, create a new same type of creature
                self.river[self.position] = Bear(self.position, self.river)
            elif isinstance(other, Fish):           #when different type of creature, eat the fish
                self.river[self.position], self.river[moves_to] = None, self
                self.position = moves_to

class Fish(Creature):
    def move(self):
        empty_cell = [a for a, x in enumerate(self.river) if x is None]
        adjacent_cell = [a for a in [self.position-1, self.position+1] if a >= 0 and a < len(self.river)]
        moves_to = np.random.choice(empty_cell + adjacent_cell)
        if moves_to in empty_cell:                   #defining the moves of the fish, same as the bear
            self.river[self.position], self.river[moves_to] = None, self
            self.position = moves_to
        else:
            other = self.river[moves_to]
            if isinstance(other, Bear):
                self.river[moves_to] = Bear(moves_to, self.river)
            elif isinstance(other, Fish):            
                self.river[self.position] = Fish(self.position, self.river)


