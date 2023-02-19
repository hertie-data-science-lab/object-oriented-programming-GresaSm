# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:41 2023

@author: Hannah
"""

from River import River

#defining the parameters for the river for a demonstration of the simulation
n_room = 5
bear = 2
fish = 3
steps = 10

#creating a river object and populating it with bears and fish to simulate the environment
river = River(n_room)
river.populate(bear, fish)
river.simulate(steps)
