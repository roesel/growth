# -*- coding: utf-8 -*-
''' Plots used probabilities for step and spiral growth. '''
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

#plt.tight_layout()
#plt.savefig('')
