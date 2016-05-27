# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:48:01 2016

@author: roese
"""
import numpy as np
## stairs
#k = np.repeat(np.arange(5), 5)
#k = np.concatenate((k,k[::-1]))
#j = np.tile(k, (50,1))
#print(j)

#
## step
#k = np.concatenate((np.zeros(35), np.ones(30), np.zeros(35)) )
#j = np.tile(k, (100,1))
#print(j)

k = np.concatenate((np.zeros(60), np.ones(80), np.zeros(60)) )
mooster = np.tile(k, (200,1))

grown = c.grid - mooster
