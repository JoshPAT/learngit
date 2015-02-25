#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import math

def LatticePath(down, right):
    
    if(down == 0 or right == 0):
        return 1
    
    else:
        return LatticePath(down -1, right) + LatticePath(down, right -1)
    	
    
def LatticePath_v2(down, right):
	numPaths = 0
    #define in the math formula
	return math.factorial(2*right) / (math.factorial(right)**2)
    #  _n+m_      _(n+m)!_
	#    n         n!*m!

print LatticePath(3,3)

print LatticePath_v2(20,20)


