# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:48:01 2016

@author: roese
"""


import numpy as np
import matplotlib.pyplot as plt

from crystal import *
from plot_init_tools import *

           
x=200
x, init = make_init("plain", x)
plain = Crystal(x, x, initial_grid=init.copy())
x, init = make_init("stairs", x)
stairs = Crystal(x, x, initial_grid=init.copy())
x, init = make_init("step", 100)
step = Crystal(x, x, initial_grid=init.copy())
x, init = make_init("screw", 100)
screw = Crystal(x, x, initial_grid=init.copy())

  
plt.figure(7)
plt.clf()

plt.subplot(141)  
plot_crystat(plain)

plt.tight_layout()
plt.savefig('C:\\BTSync\\Skola\\UW_2016_ST\\NANO701_MBE\\plots\\inits.png')

#def prob(x):
#    z=50
#    t=0.25
#    x = (x+0.04)/4
#    if x>t:
#        return 0.6*np.exp((x-0.25)/1.5)
#    else:
#        lower = np.exp(z*(x+(1-0.25)))/np.exp(z)
#        base = np.arctan(30*(x-0.25))/(np.pi/2)*0.5+0.5
#        return base * lower       
#    
#
#
#probabilities = [
#    0.001,  # no NN
#    0.6,  # 1 NN
#    0.7,
#    0.8,
#    1,   # 4 NN
#] 

#x = np.linspace(0, 4, 5) #[0,1,2,3,4]
#x2 = np.linspace(0, 4, 10000)
#y = np.zeros(x2.size)
#for i in range(x2.size):
#    y[i] = prob(x2[i])
#
#plt.figure(5)
#plt.clf()
#plt.scatter(x, probabilities)
#plt.plot(x2, y)













