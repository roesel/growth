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
        
        
def plot_crystal_3d(c, num_figure=3):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(num_figure)        
    ax = fig.add_subplot(111, projection='3d')
    x = range(c.m)
    y = range(c.n)
    X, Y = np.meshgrid(x,y)
    plt.xlim(0, c.m)
    plt.ylim(0, c.n)
    ax.plot_surface(X, Y, c.grid, rstride=1, cstride=1, antialiased=False)
        
def make_init(kind, x):
    if kind=="step":
        k = np.concatenate((np.zeros(int(0.4*x)), np.ones(int(0.2*x)), np.zeros(x-(int(0.4*x)+int(0.2*x)))) )
        init = np.tile(k, (x,1))        
        return x, init
    elif kind=="stairs":
        k = np.repeat(np.arange(10), (x/10/2))
        k = np.concatenate((k,k[::-1]))
        j = np.tile(k, (x,1))
        return x, j
           
            
def main(num_of_growths):
    
    x, init = make_init("step", 200)

    c = Crystal(x, x, initial_grid=init.copy())       
        
    #c.print_grid()
    c.grow(num_of_growths)
    #c.print_grid()
    
    plot_crystal(c)
    

    
    d = Crystal(x, x, initial_grid=(c.grid-init))
    plot_crystal(d, 2)

def profile():
    import cProfile
    cProfile.run('main(50)', 'pstats')
    
    from pstats import Stats
    p = Stats('pstats')
    
    p.strip_dirs().sort_stats('time').print_stats(10)

main(50)
#profile()















