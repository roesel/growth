# -*- coding: utf-8 -*-
"""
@author: roesel@gmail.com
"""

import numpy as np

class Crystal:
    '''Class representing one growth chamber/surface/crystal.'''
   
    def __init__(self, m, n, initial_grid = 0):
        self.m = m
        self.n = n
        self.probabilities = [
            0.001,  # no NN
            0.2,  # 1 NN
            0.3,
            0.4,
            0.5,   # 4 NN
        ]        
        
        if not isinstance(initial_grid, np.ndarray):
            self.grid = np.zeros((m, n), dtype=np.int)
        elif initial_grid.shape == (m, n):
            self.grid = initial_grid
        else:
            raise ValueError('Wrong initial size of initial_grid.')
   
    def print_grid(self):
        '''Prints current state of grid.'''
        
        print(self.grid)

    def get_deposition_order(self):
        '''
        Get a random permutation of all indices on grid.
        src: http://stackoverflow.com/questions/3891180/select-cells-randomly-from-numpy-array-without-replacement
        '''
        #Get a list of indices for an array of this shape        
        indices = list(np.ndindex(self.grid.shape))    
        
        #Shuffle the indices in-place
        np.random.shuffle(indices)
        
        return indices
    
    def probability_of_deposition(self, coords):
        
        sites = self.get_number_of_sticky_NN(coords)
        # put dictionary outside of function for better performance        
        return self.probabilities[sites]        
        #return 1
        
    def random(self):
        ''' Returns random number from continuous uniform distribution. '''
        return np.random.random_sample()
    
    def get_number_of_sticky_NN(self, coords):
        if (coords[0]<self.m and coords[1]<self.n):
            num_of_sticky_NN = 0
            main_val = self.get_value(coords)
            NN = [ tuple(map(sum, zip(x, coords))) for x in [(-1,0), (1,0), (0,-1), (0,1)] ]            
            for neighbor in NN:
                if self.get_value(neighbor)>main_val:
                    num_of_sticky_NN += 1
            return num_of_sticky_NN
        else:
            raise ValueError("Out of bounds of grid!")

    def get_value(self, coords):
        if (0<=coords[0]<self.m and 0<=coords[1]<self.n):
            return self.grid[coords]
        else:
            x, y = 0, 0
            if coords[0]<0: x = coords[0]+self.m
            elif coords[0]>=self.m: x = coords[0]-self.m
            if coords[1]<0: y = coords[1]+self.n
            elif coords[1]>=self.n: y = coords[1]-self.n
            return self.grid[(x, y)]

    def grow_layer(self):
        order = self.get_deposition_order()  
        
        for index in order:
            if self.random() < self.probability_of_deposition(index):
                self.grid[index] += 1
    
    def get_grid(self):
        return self.grid
        
#init = np.zeros((5,5))
c = Crystal(50,50)
num_of_growths = 50


c.print_grid()
for g in range(num_of_growths):
    c.grow_layer()
c.print_grid()


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

plt.imshow(c.get_grid(), cmap=plt.get_cmap("YlOrBr"))



















