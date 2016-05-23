# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:46:19 2015

@author: Administrator
"""

import numpy as np 
from xlrd import open_workbook
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D  



#a = [[0 for col in range(3)] for row in range(5)]
#a = np.zeros((5,3),np.float)
a = np.empty((45,3),np.float)
book = open_workbook("Book2.xlsx")
book.nsheets # 工作表的数目
print book.sheet_names()[0] #第一个工作表的名字
sheet = book.sheets()[0] # 获得第一个工作表
for i in xrange(45):
    for j in xrange(3):
#        print sheet.cell_value(i,j)
        a[i][j] = sheet.cell_value(i,j)

print a

fig=plt.figure()     #准备好这张纸，并把句柄传给fig
ax = fig.add_subplot(111, projection='3d')  
plt.title('Kinect-3D-Point')   
ax.set_xlabel('X Label (m)')  
ax.set_ylabel('Y Label (m)')  
ax.set_zlabel('Z Label (m)')   
ax.scatter(a[0:5,0], a[0:5,1], a[0:5,2],c='r',marker = (3,0),alpha = 0.8,lw = 1)
ax.hold('on')
ax.scatter(a[5:11,0], a[5:11,1], a[5:11,2],c='g',marker = (4,0),alpha = 0.8,lw = 1)  
ax.hold('on')
ax.scatter(a[11:24,0], a[11:24,1], a[11:24,2],c='b',marker = (3,3),alpha = 0.8,lw = 1)
ax.hold('on')
ax.scatter(a[24:32,0], a[24:32,1], a[24:32,2],c='r',marker = (4,2),alpha = 0.8,lw = 1) 
ax.grid('on')    #以上语句不难理解
plt.show()  
