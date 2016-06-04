# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:05:45 2016

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
x, init = make_init("step", x)
step = Crystal(x, x, initial_grid=init.copy())
x, init = make_init("screw", x)
screw = Crystal(x, x, initial_grid=init.copy())

cs = [
    [plain, 1, "i) plain"],
    [stairs, 2, "ii) stairs"],
    [step, 3, "iii) step"],
    [screw, 4, "iv) screw"],
]
  
fig = plt.figure(7)
plt.clf()

for cg in cs:
    c = cg[0]    
    
    # Determining top range of colorbar
    max_int = math.ceil(c.max)    
    
    # Plotting
    ax = fig.add_subplot(1,4,cg[1])
    plt.imshow(c.grid, cmap=plt.get_cmap("viridis"), interpolation='none', vmin=0, vmax=max_int)
    
    # Cosmetics    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_title(cg[2])
    ax.set_frame_on(False)
    cbar = plt.colorbar(orientation='vertical')  
    cbar.set_ticks(np.arange(max_int+1))

plt.tight_layout()
plt.savefig('C:\\BTSync\\Skola\\UW_2016_ST\\NANO701_MBE\\plots\\inits.png')