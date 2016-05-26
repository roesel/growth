# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:48:01 2016

@author: roese
"""
import numpy as np
coords = (3,3)
neighbours = [ tuple(map(sum, zip(x, coords))) for x in [(-1,0), (1,0), (0,-1), (0,1)] ]            
print(neighbours)