# -*- coding: utf-8 -*-
''' The main script to run, enables profiling. '''
import numpy as np
import math

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from crystal import *
from plot_init_tools import *


def main(num_of_growths):
    ''' Main method to start simulation. Uncomment specific simulation or write a new one. '''
    
    # Main simulation crystal, x is dimensions (m=n=x)
    
    # Stairs    
    x, init = make_init("stairs", 200)
    c = Crystal(x, x, initial_grid=init.copy(), mode="step", hist_int=int(num_of_growths/4), \
                border_policy="loop", use_height=False)       

    c.grow(num_of_growths)

    plot_crystal(c)
    
#    # Step    
#    x, init = make_init("step", 200)
#    c = Crystal(x, x, initial_grid=init.copy(), mode="step", hist_int=int(num_of_growths/4), \
#                border_policy="loop")       
#    #c.print_grid()
#    c.grow(num_of_growths)
#    #c.print_grid()
#    plot_crystal(c)
#    
#    # Screw
#    x, init = make_init("screw", 200)
#    c = Crystal(x, x, initial_grid=init.copy(), mode="spin", hist_int=int(num_of_growths/8), \
#                border_policy="flex")       
#    #c.print_grid()
#    c.grow(num_of_growths)
#    #c.print_grid()
#    plot_crystal(c)
    
#    # A crystal object serving to visualize only "what grew" without init state   
#    d = Crystal(x, x, initial_grid=(c.grid-init))
#    plot_crystal(d, 2)
    
    # Show history of simulation
    plot_history(c)
    
#    # Generate a publishable plot
#    plot_out(c)

def profile():
    ''' Function used to profile code for speedups. '''    
    
    import cProfile
    cProfile.run('main(50)', 'pstats')
    from pstats import Stats
    p = Stats('pstats')
    p.strip_dirs().sort_stats('time').print_stats(10)

    
main(50)    
#profile()















