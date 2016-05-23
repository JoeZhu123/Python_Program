# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:30:05 2015

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


#计算一个txt文件中共有多少行
#文件比较小
line_number = len(open(r'D:/PYTHON-PROGRAM/rudy_badminton02data.txt','rU').readlines())
print line_number
a = np.empty((line_number,3),np.float)  #   定义一个line_number行3列的数组内存空间
for line in open(r'D:/PYTHON-PROGRAM/rudy_badminton02data.txt'):
    print line
        




