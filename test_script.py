# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:48:01 2016

@author: roese
"""


import numpy as np
import matplotlib.pyplot as plt

from crystal_spi import *
e = Crystal(100, 100)
plt.figure(5)
plt.clf()
x = np.linspace(0, 4, 100)
y = np.zeros(x.size)
for i in range(x.size):
    y[i] = e.prob(x[i])
plt.plot(x, y)
plt.xlim(0,4)
plt.ylim(0,1)
