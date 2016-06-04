# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:48:01 2016

@author: roese
"""


import numpy as np
import matplotlib.pyplot as plt

from crystal import *

e = Crystal(100, 100, mode="step")
f = Crystal(100, 100, mode="spin")


x = np.linspace(0, 4, 1000)
y = np.zeros(x.size)
y2 = np.zeros(x.size)
for i in range(x.size):
    y[i] = e.prob(x[i])
    y2[i] = f.prob(x[i])
  
plt.figure(6)
plt.clf()

plt.subplot(121)  
plt.plot(x, y, color=(72/255, 26/255, 108/255), lw=1.4)
plt.xlabel("$n_{NN}$", fontsize=20)
plt.ylabel("$p_d$", fontsize=20)
plt.title("a) step growth")

plt.subplot(122)
plt.plot(x, y2, color=(72/255, 26/255, 108/255), lw=1.4)
plt.xlabel("$n_{NN}$", fontsize=20)
plt.ylabel("$p_d$", fontsize=20)
plt.title("b) spiral growth")

plt.xlim(0,4)
plt.ylim(0,1)

plt.tight_layout()
plt.savefig('C:\\BTSync\\Skola\\UW_2016_ST\\NANO701_MBE\\plots\\p_step_and_spin.png')

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













