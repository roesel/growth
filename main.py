# -*- coding: utf-8 -*-
"""
@author: roesel@gmail.com
"""

import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from crystal import *

def plot_crystal(c):
    fig = plt.figure(1)
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
    c = Crystal(100,100)       
    #c.print_grid()
    c.grow(num_of_growths)
    c.print_grid()
    
    plot_crystal(c)

def profile():
    import cProfile
    cProfile.run('main(100)', 'pstats')
    
    from pstats import Stats
    p = Stats('pstats')
    
    p.strip_dirs().sort_stats('time').print_stats(10)

main(25)
#profile()















