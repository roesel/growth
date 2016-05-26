# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:48:01 2016

@author: roese
"""
import numpy as np
ray = np.arange(25).reshape((5,5))
print(ray)
print(ray[-1%5,6%5])