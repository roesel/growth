# -*- coding: utf-8 -*-
"""
@author: roesel@gmail.com
"""

import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from crystal import *

def plot_crystal(c, num_figure=1):
    fig = plt.figure(num_figure)
    plt.clf()
    ax = fig.add_subplot(111)
    plt.imshow(c.grid, cmap=plt.get_cmap("YlOrBr"), interpolation='none')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #ax.patch.set_alpha(0)
    ax.set_title(str(c.grid.shape)+", "+str(c.num_of_growths)+" growths")
    ax.set_frame_on(False)
    plt.colorbar(orientation='vertical')            
        
        
def main(num_of_growths):
    
#    # stairs
#    k = np.repeat(np.arange(10), 5)
#    k = np.concatenate((k,k[::-1]))
#    j = np.tile(k, (100,1))    
    
    # step
    k = np.concatenate((np.zeros(60), np.ones(80), np.zeros(60)) )
    init = np.tile(k, (200,1))

    c = Crystal(200,200, initial_grid=init.copy())       
        
    #c.print_grid()
    c.grow(num_of_growths)
    #c.print_grid()
    
    plot_crystal(c)
    

    
    d = Crystal(200, 200, initial_grid=(c.grid-init))
    plot_crystal(d, 2)

def profile():
    import cProfile
    cProfile.run('main(50)', 'pstats')
    
    from pstats import Stats
    p = Stats('pstats')
    
    p.strip_dirs().sort_stats('time').print_stats(10)

main(40)
#profile()















