# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:44:52 2016

@author: roese
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

def plot_crystal(c, num_figure=1):
    ''' Plots crystal on a colored 2D plot. '''
    
    # Determining top range of colorbar
    max_int = math.ceil(c.max)    
    
    # Plotting
    fig = plt.figure(num_figure)
    plt.clf()
    ax = fig.add_subplot(111)
    plt.imshow(c.grid, cmap=plt.get_cmap("viridis"), interpolation='none', vmin=0, vmax=max_int)
    
    # Cosmetics    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_title(str(c.grid.shape)+", "+str(c.num_of_growths)+" growths")
    ax.set_frame_on(False)
    cbar = plt.colorbar(orientation='vertical')  
    cbar.set_ticks(np.arange(max_int+1))

def plot_history(c, num_figure=4):    
    ''' Plots evolution of crystal growth history based on settings in the 
        'Crystal' object. '''
        
    # Determining top range of colorbar
    max_int = math.ceil(c.max)    
    
    # Plotting
    fig = plt.figure(num_figure)          
    plt.clf()
    i=1
    for grid in c.history:    
        ax = fig.add_subplot(2,5,i)
        plt.imshow(grid, cmap=plt.get_cmap("viridis"), interpolation='none', vmin=0, vmax=max_int)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)  
        ax.set_frame_on(False)
        ax.set_title(str(c.history_growths[i-1])+" growths")
        i+=1
    plt.suptitle("History of growth: "+str(c.grid.shape)+", "+str(c.num_of_growths)+" growths")    
    
        
def plot_crystal_3d(c, num_figure=3):
    ''' Plotting 3D plot of crystal. '''    
    
    fig = plt.figure(num_figure)        
    ax = fig.add_subplot(111, projection='3d')
    x = range(c.m)
    y = range(c.n)
    X, Y = np.meshgrid(x,y)
    plt.xlim(0, c.m)
    plt.ylim(0, c.n)
    ax.plot_surface(X, Y, c.grid, rstride=1, cstride=1, antialiased=False)
        
def make_init(kind, x):
    ''' Create different initial states of crystal surface. '''
    
    if kind=="step":
        # A column of value 1 surrounded by values 0 from both sides
        k = np.concatenate((np.zeros(int(0.4*x)), np.ones(int(0.2*x)), np.zeros(x-(int(0.4*x)+int(0.2*x)))) )
        init = np.tile(k, (x,1))        
        return x, init
    elif kind=="stairs":
        # Stairs stepping up one atomic level at a time
        num_of_stairs = 5
        k = np.repeat(np.arange(num_of_stairs), (x/num_of_stairs/2))
        k = np.concatenate((k,k[::-1]))
        j = np.tile(k, (x,1))
        return x, j
    elif kind=="plain":
        # A plain plane start (all zeros)
        k = np.zeros((x, x), dtype=np.int)
        return x, k
    elif kind=="screw":
        # An attempted screw dislocation
        k = np.linspace(1, 0, int(x/2))
        j = np.zeros(x-int(x/2))
        l = np.concatenate((k, j))
        m = np.tile(l, (int(x/2), 1))
        n = np.zeros((x-int(x/2), x))
        o = np.vstack((m, n))
        return x, o