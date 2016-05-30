# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:48:01 2016

@author: roese
"""


import numpy as np

x=8
k = np.linspace(0, 1, int(x/2))
k2 = np.concatenate((k,k[::-1]))
j = np.tile(k2, (int(x/2), 1))
j2 = np.zeros((int(x/4),x))
o = np.vstack((j2, j, j2))
print(o)


#l = np.concatenate((k, j))
#m = np.tile(l, (int(x/2), 1))
#n = np.zeros((x-int(x/2), x))
#o = np.vstack((m, n))
#print(o)
