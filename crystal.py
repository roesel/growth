# -*- coding: utf-8 -*-
''' The object representing one crystal as it evolves during the simulation. '''
import numpy as np

class Crystal:
    '''Class representing one growth chamber/surface/crystal.'''
   
    def __init__(self, m, n, initial_grid = 0, mode="step", hist_int=10, \
                 border_policy="loop", use_height=True):
        self.m = m
        self.n = n
        self.mode = mode
        self.num_of_growths = 0
        self.history = []
        self.history_growths = []
        self.history_interval = hist_int
        self.border_policy = border_policy
        self.use_height = use_height
        
        if not isinstance(initial_grid, np.ndarray):
            self.grid = np.zeros((m, n), dtype=np.int)
        elif initial_grid.shape == (m, n):
            self.grid = initial_grid
        else:
            raise ValueError('Wrong initial size of initial_grid.')
   
        self.max = np.amax(self.grid)
        self.min = np.amin(self.grid)

    def prob_spin(self, x):
        ''' Probability function for spiral growth. '''
        z=50
        t=0.25
        x = (x+0.04)/4        
        if x>t:
            lower = 1
        else:
            lower = np.exp(z*(x+(1-0.25)))/np.exp(z)                        
        base = np.arctan(30*(x-0.25))/(np.pi/2)*0.5+0.5
        return base * lower
        
    def prob_step(self, x):
        ''' Probability function for step growth. '''
        z=50
        t=0.25
        x = (x+0.04)/4
        if x>t:
            return 0.6*np.exp((x-0.25)/1.5)
        else:
            lower = np.exp(z*(x+(1-0.25)))/np.exp(z)
            base = np.arctan(30*(x-0.25))/(np.pi/2)*0.5+0.5
            return base * lower + 0.001   
    
    def prob(self, x):
        ''' Probability function filler for spiral/step growths. '''
        if self.mode == "spin":
            return self.prob_spin(x)
        elif self.mode == "step":
            return self.prob_step(x)
        
    def height_factor(self, coords):
        ''' Height factor function for spiral/step growths. '''
        if self.mode == "spin":
            height = self.get_value(coords)         
            return (height-self.min)/(self.max-self.min)        
        elif self.mode == "step":
            height = self.get_value(coords)  
            return self.height_prob[height-self.min]
        
    def probability_of_deposition(self, coords):
        ''' Probability of deposition semi-filler for any approach. '''
        # (!!!!!!!!!!)
        # This could be separated between "spin" and "step" even one layer 
        # earlier by making prob_of_deposition() mode dependent.
        # (!!!!!!!!!!)
        
        sites = self.get_number_of_sticky_NN(coords)
        factor=1
        
        if (sites==0):
            if not self.use_height:
                factor=0.001            
            else:        
                factor = self.height_factor(coords)
        
        return self.prob(sites) * factor   
        
    def get_number_of_sticky_NN(self, coords):
        ''' Returns the number of nearest neighbors of a specific site. 
            Can return float (area of contact in a**3)
        '''
        
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
                    
        return num_of_sticky_NN

    def get_value(self, coords): 
        ''' Gets values of specific coords, implements different border policies. '''
        if self.border_policy=="flex":
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
            
        elif self.border_policy=="loop":
            return int(self.grid[(coords[0]%self.m, coords[1]%self.n)])
            
    def random(self):
        ''' Returns random number from continuous uniform distribution. '''
        return np.random.random_sample()
        
    def get_random_tile(self):
        ''' Returns random coordinates from field. '''
        return (np.random.randint(self.m), np.random.randint(self.n))

    def grow_layer(self):
        ''' Attempts to land (m x n) atoms. '''
        self.height_prob = np.concatenate((np.linspace(0.001, 1, self.max-self.min), np.ones(10)))
        
        for i in range(self.m*self.n):
            index = self.get_random_tile()
            if self.random() < self.probability_of_deposition(index):
                self.grid[index] += 1
        
        self.num_of_growths += 1
        if self.num_of_growths%self.history_interval==0:
            self.history.append(self.grid.copy())
            self.history_growths.append(self.num_of_growths)
        
        self.max = np.amax(self.grid)
        self.min = np.amin(self.grid)
    
    def grow(self, layers):
        ''' Executes 'layers' of growths. '''
        for layers in range(layers):
            self.grow_layer()
                
    def print_grid(self):
        '''Prints current state of grid.'''
        print(self.grid)

            
            
            
            