# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:59:24 2015

@author: Administrator
"""

import pylab as p  
import mpl_toolkits.mplot3d.axes3d as p3  
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
fig=p.figure()  
#point_num=100  
#data=np.random.random((point_num,3))  
#colors=[['b','g','r'][int(i*2.999)] for i in np.random.random((point_num,1))]  
#ax = p3.Axes3D(fig)  
ax = p3.Axes3D(fig) 
#ax.scatter(data[:,0], data[:,1], data[:,2],c = colors) 
ax.scatter(P[:,0], P[:,1], P[:,2])  
#ax.scatter(P1[:,0], P1[:,1], P1[:,2])  
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_zlabel('Z')  
fig.add_axes(ax)  
#fig.add_axes(bx)
p.show()  
