# -*- coding: utf-8 -*-

import numpy as np

class Crystal:
    '''Class representing one growth chamber/surface/crystal.'''
   
    def __init__(self, m, n, initial_grid = 0):
        self.m = m
        self.n = n
        self.num_of_growths = 0
        self.history = []
        self.history_interval = 10
        
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
        
        self.max = np.amax(self.grid)
        self.min = np.amin(self.grid)

    def p(self, x):
        return x**4
    
    def prob1(self, num_s_NN):
        return self.p(num_s_NN+1)/self.p(9)
        
    def prob2(self, num_s_NN):
        return np.exp(num_s_NN)/np.exp(4)

    def lower025(self, x):
        z=50
        t=0.25
        if x>t:
            return 1
        else:
            return np.exp(z*(x+(1-0.25)))/np.exp(z)        
        
    def prob(self, x):
        x = (x+0.04)/4
        base = np.arctan(30*(x-0.25))/(np.pi/2)*0.5+0.5
        return base * self.lower025(x)
    
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
        
    def height_factor(self, coords):
        height = self.get_value(coords)         
        return (height-self.min)/(self.max-self.min)        
    
    def probability_of_deposition(self, coords):
        
        sites = self.get_number_of_sticky_NN(coords)
        factor=1
        if sites==0:
            factor = self.height_factor(coords)
            #factor = 1
            #height = self.get_value(coords)  
            #factor = self.height_prob[height-self.min]
        # put dictionary outside of function for better performance        
        #return self.probabilities[sites] * factor       
        #if self.prob(sites) * factor > 0.02:
        #    print("probability: ", self.prob(sites) * factor)
        return self.prob(sites) * factor        
        #return 1
        
    def random(self):
        ''' Returns random number from continuous uniform distribution. '''
        return np.random.random_sample()
    
    def get_number_of_sticky_NN(self, coords):
        num_of_sticky_NN = 0
        main_val = self.get_value(coords)
        m1 = self.get_value((coords[0]-1, coords[1])) - main_val
        m2 = self.get_value((coords[0]+1, coords[1])) - main_val
        m3 = self.get_value((coords[0], coords[1]-1)) - main_val
        m4 = self.get_value((coords[0], coords[1]+1)) - main_val

        self.ms = [m1, m2, m3, m4]
        for m in self.ms:
            if m>0: 
                if m>1:          
                    num_of_sticky_NN += 1            
                else:
                    num_of_sticky_NN += m
        #if num_of_sticky_NN>1:
        #    print("returning: ", num_of_sticky_NN)
        return num_of_sticky_NN

    def get_value2(self, coords):
        return int(self.grid[(coords[0]%self.m, coords[1]%self.n)])
        
    def get_value(self, coords):        
        x, y = coords
        if coords[0]==self.m: 
            x=self.m-1
        if coords[0]<0:
            x=0
        if coords[1]==self.n: 
            y=self.n-1
        if coords[1]<0:
            y=0
            
        return self.grid[(x, y)]            
        
    def get_random_tile(self):
        return (np.random.randint(self.m), np.random.randint(self.n))

    def grow_layer1(self):
        order = self.get_deposition_order()  
        
        for index in order:
            if self.random() < self.probability_of_deposition(index):
                self.grid[index] += 1
        self.num_of_growths += 1
        
    def grow_layer(self):
        
        self.height_prob = np.concatenate((np.linspace(0.001, 1, self.max-self.min), np.ones(10)))
        
        for i in range(self.m*self.n):
            index = self.get_random_tile()
            if self.random() < self.probability_of_deposition(index):
                self.grid[index] += 1
        
        if self.num_of_growths%self.history_interval==0:
            self.history.append(self.grid.copy())
        self.num_of_growths += 1
        
        self.max = np.amax(self.grid)
        self.min = np.amin(self.grid)
        
    
    def grow(self, layers):
        for layers in range(layers):
            self.grow_layer()
            
            
            
            
            
            
            
            
            
            
            
            
            