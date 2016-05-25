# -*- coding: utf-8 -*-
"""
@author: roesel@gmail.com
"""

import numpy as np

class Crystal:
    '''Class representing one growth chamber/surface/crystal...'''
   
    def __init__(self, m, n, initial_grid = 0):
        self.m = m
        self.n = n
        if not isinstance(initial_grid, np.ndarray):
            self.grid = np.zeros((m, n))
        elif initial_grid.shape == (m, n):
            self.grid = initial_grid
        else:
            raise ValueError('Wrong initial size of initial_grid.')
   
    def print_grid(self):
        print(self.grid)

    def get_deposition_order(self):
        
init = np.ones((5,5))
c = Crystal(5,5, initial_grid=init)
c.print_grid()