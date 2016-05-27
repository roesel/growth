# -*- coding: utf-8 -*-

import numpy as np

class Crystal:
    '''Class representing one growth chamber/surface/crystal.'''
   
    def __init__(self, m, n, initial_grid = 0):
        self.m = m
        self.n = n
        self.num_of_growths = 0
        
        self.probabilities = [
            0.001,  # no NN
            0.6,  # 1 NN
            0.7,
            0.8,
            1,   # 4 NN
        ]        
        
        if not isinstance(initial_grid, np.ndarray):
            self.grid = np.zeros((m, n), dtype=np.int)
        elif initial_grid.shape == (m, n):
            self.grid = initial_grid
        else:
            raise ValueError('Wrong initial size of initial_grid.')
   
        #Get a list of indices for an array of this shape        
        self.deposition_order = list(np.ndindex(self.grid.shape))    

    def p(self, x):
        return x**4
    
    def prob(self, num_s_NN):
        return self.p(num_s_NN+1)/self.p(9)
    
    def print_grid(self):
        '''Prints current state of grid.'''
        print(self.grid)

    def get_deposition_order(self):
        '''
        Get a random permutation of all indices on grid.
        src: http://stackoverflow.com/questions/3891180/select-cells-randomly-from-numpy-array-without-replacement
        '''
        #Shuffle the indices in-place
        np.random.shuffle(self.deposition_order)
        return self.deposition_order
    
    def probability_of_deposition(self, coords):
        
        sites = self.get_number_of_sticky_NN(coords)
        # put dictionary outside of function for better performance        
        return self.probabilities[sites]        
        #return self.prob(sites)        
        #return 1
        
    def random(self):
        ''' Returns random number from continuous uniform distribution. '''
        return np.random.random_sample()
    
    def get_number_of_sticky_NN(self, coords):
        num_of_sticky_NN = 0
        main_val = self.get_value(coords)
        if self.get_value((coords[0]-1, coords[1]))>main_val: num_of_sticky_NN += 1            
        if self.get_value((coords[0]+1, coords[1]))>main_val: num_of_sticky_NN += 1            
        if self.get_value((coords[0], coords[1]-1))>main_val: num_of_sticky_NN += 1            
        if self.get_value((coords[0], coords[1]+1))>main_val: num_of_sticky_NN += 1            
#        if self.get_value((coords[0]-1, coords[1]-1))>main_val: num_of_sticky_NN += 1            
#        if self.get_value((coords[0]-1, coords[1]+1))>main_val: num_of_sticky_NN += 1            
#        if self.get_value((coords[0]+1, coords[1]-1))>main_val: num_of_sticky_NN += 1            
#        if self.get_value((coords[0]+1, coords[1]+1))>main_val: num_of_sticky_NN += 1            
        return num_of_sticky_NN

    def get_value(self, coords):
        return self.grid[(coords[0]%self.m, coords[1]%self.n)]
        
    def get_random_tile(self):
        return (np.random.randint(self.m), np.random.randint(self.n))

    def grow_layer1(self):
        order = self.get_deposition_order()  
        
        for index in order:
            if self.random() < self.probability_of_deposition(index):
                self.grid[index] += 1
        self.num_of_growths += 1
        
    def grow_layer(self):
        for i in range(self.m*self.n):
            index = self.get_random_tile()
            if self.random() < self.probability_of_deposition(index):
                self.grid[index] += 1
        self.num_of_growths += 1
    
    def grow(self, layers):
        for layers in range(layers):
            self.grow_layer()