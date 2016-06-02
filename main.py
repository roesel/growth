# -*- coding: utf-8 -*-
"""
@author: roesel@gmail.com
"""

import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from crystal_spi import *

def plot_crystal(c, num_figure=1):
    fig = plt.figure(num_figure)
    plt.clf()
    ax = fig.add_subplot(111)
    plt.imshow(c.grid, cmap=plt.get_cmap("viridis"), interpolation='none', vmin=0)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #ax.patch.set_alpha(0)
    ax.set_title(str(c.grid.shape)+", "+str(c.num_of_growths)+" growths")
    ax.set_frame_on(False)
    cbar = plt.colorbar(orientation='vertical')  
    cbar.set_ticks(np.arange(3+1))

def plot_history(c, num_figure=4):
    fig = plt.figure(num_figure)          
    plt.clf()
    i=1
    for grid in c.history:    
        ax = fig.add_subplot(2,5,i)
        plt.imshow(grid, cmap=plt.get_cmap("viridis"), interpolation='none', vmin=0)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)  
        ax.set_frame_on(False)
        ax.set_title(str(i*c.history_interval)+" growths")
        i+=1
    plt.suptitle("History of growth: "+str(c.grid.shape)+", "+str(c.num_of_growths)+" growths")    
    
        
def plot_crystal_3d(c, num_figure=3):
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
    elif kind=="plain":
        k = np.zeros((x, x), dtype=np.int)
        return x, k
    elif kind=="screw":
        k = np.linspace(1, 0, int(x/2))
        j = np.zeros(x-int(x/2))
        l = np.concatenate((k, j))
        m = np.tile(l, (int(x/2), 1))
        n = np.zeros((x-int(x/2), x))
        o = np.vstack((m, n))
        return x, o
           
            
def main(num_of_growths):
    
    x, init = make_init("screw", 100)

    c = Crystal(x, x, initial_grid=init.copy())       
        
    #c.print_grid()
    c.grow(num_of_growths)
    #c.print_grid()
    
    plot_crystal(c)
    

    
    d = Crystal(x, x, initial_grid=(c.grid-init))
    plot_crystal(d, 2)
    
    plot_history(c)

def profile():
    import cProfile
    cProfile.run('main(50)', 'pstats')
    
    from pstats import Stats
    p = Stats('pstats')
    
    p.strip_dirs().sort_stats('time').print_stats(10)

main(100)
#profile()















