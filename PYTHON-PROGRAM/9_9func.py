# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:11:11 2015

@author: Administrator
"""

import numpy as np

def func2(i,j):
    return (i+1)*(j+1)
a = np.fromfunction(func2,(9,9))
print a    
    