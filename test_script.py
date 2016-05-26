# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:48:01 2016

@author: roese
"""
import numpy as np
# stairs
k = np.repeat(np.arange(5), 5)
k = np.concatenate((k,k[::-1]))
j = np.tile(k, (50,1))
print(j)