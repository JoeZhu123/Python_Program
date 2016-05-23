# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:50:29 2015

@author: Administrator
""" 
import matplotlib.pyplot as plt 
import numpy as np  
#data is an ndarray with the necessary data and colors is an ndarray with #'b', 'g' and 'r' to paint each point according to its class ...  
P = np.array([[2.95086,1.52456,5.246],
[-0.58745,-0.676676,2.164],
[0.503054,0.904206,5.088],
[2.43112,1.54562,5.059],
[2.34022,1.54496,5.015],
[2.14507,1.56086,4.855],
[2.33137,1.56595,4.82],
[1.60653,1.56492,4.837],
[1.27128,1.52,5.127],
[0.805727,1.10298,3.788],
[0.549473,1.01175,4.362],
[0.620268,1.04212,4.2],
[0.609366,1.06048,4.053]])

P1 = np.array([[0.495076,1.21073,4.115],
[-0.0656897,1.5338,4.981],
[-0.582407,1.54101,4.879],
[-0.785486,0.942489,3.179],
[-1.9457,1.44242,5.47],
[-1.74608,1.45453,5.404],
[-1.77667,1.47521,5.32],
[0.465363,0.912133,5.132]])

P2 = np.array([[0.494376,1.24909,4.407],
[-0.222981,	1.54922,4.861],
[-0.833488,1.53573,4.517],
[-0.882908,	0.979745,2.93],
[-1.92763,1.53318,4.858],
[-1.86628,1.55906,4.735]])

fig=plt.figure()     #准备好这张纸，并把句柄传给fig
plt.title('Kinect-3D-Point-XY_Axis')   
plt.xlabel('X(m)')
plt.ylabel('Y(m)')   
plt.xlim(-3.0,5.0)
plt.ylim(-2.0,3.0)
plt.scatter(P[:,0], P[:,1],c='r',marker = (3,0),alpha = 0.6,lw = 1)
plt.hold('on')
plt.scatter(P1[:,0], P1[:,1],c='g',marker = (4,0),alpha = 0.6,lw = 1)  
plt.hold('on')
plt.scatter(P2[:,0], P2[:,1],c='b',marker = (5,3),alpha = 0.6,lw = 1)
  
plt.grid('on')    #以上语句不难理解
plt.show()  