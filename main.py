# -*- coding: utf-8 -*-
import numpy as np
import math

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from crystal import *
from plot_init_tools import *


def main(num_of_growths):
    ''' Main method to start simulation. '''
    
    # Main simulation crystal, x is dimensions (m=n=x)
    
#    # Stairs    
#    x, init = make_init("stairs", 200)
#    c = Crystal(x, x, initial_grid=init.copy(), mode="step", hist_int=int(num_of_growths/4), \
#                border_policy="loop", use_height=False)       
#
#    c.grow(num_of_growths)
#
#    plot_crystal(c)
    
#    # Averaging
#    print("Finished one")
#    return c
    
#    # Step    
#    x, init = make_init("step", 200)
#    c = Crystal(x, x, initial_grid=init.copy(), mode="step", hist_int=int(num_of_growths/4), \
#                border_policy="loop")       
#    #c.print_grid()
#    c.grow(num_of_growths)
#    #c.print_grid()
#    plot_crystal(c)
#    
    # Screw
    x, init = make_init("screw", 200)
    c = Crystal(x, x, initial_grid=init.copy(), mode="spin", hist_int=int(num_of_growths/8), \
                border_policy="flex")       
    #c.print_grid()
    c.grow(num_of_growths)
    #c.print_grid()
    plot_crystal(c)
    
#    # A crystal object serving to visualize only "what grew" without init state   
#    d = Crystal(x, x, initial_grid=(c.grid-init))
#    plot_crystal(d, 2)
    
#    # Show history of simulation
#    plot_history(c)
    
    plot_out(c)

def profile():
    ''' Function used to profile code for speedups. '''    
    
    import cProfile
    cProfile.run('main(50)', 'pstats')
    from pstats import Stats
    p = Stats('pstats')
    p.strip_dirs().sort_stats('time').print_stats(10)

# averaging
#maximum = 10
#g = []
#for i in range(maximum):
#    out = main(40)
#    g.append(out.grid)
#    
#suma = g[0]+g[1]+g[2]+g[3]+g[4]+g[5]+g[6]+g[7]+g[8]+g[9]
#prumer = suma/maximum
#    
#rr = Crystal(100, 100, initial_grid=prumer)
#plot_crystal(rr, 2)
    
main(200)    
#profile()















