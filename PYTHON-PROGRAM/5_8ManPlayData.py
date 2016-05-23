# -*- coding: utf-8 -*-
"""
Created on Fri May 08 19:36:06 2015

@author: Administrator
"""

import numpy as np 
from xlrd import open_workbook
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D  



#a = [[0 for col in range(3)] for row in range(5)]
#a = np.zeros((5,3),np.float)
a = np.empty((515,6),np.float)
book = open_workbook("Book8.xlsx")
book.nsheets # 工作表的数目
print book.sheet_names()[0] #第一个工作表的名字
sheet = book.sheets()[0] # 获得第一个工作表
for i in xrange(515):
    for j in xrange(6):
#        print sheet.cell_value(i,j)
        a[i][j] = sheet.cell_value(i,j)


fig=plt.figure()     #准备好这张纸，并把句柄传给fig
ax = fig.add_subplot(111, projection='3d')  
plt.title('Kinect-3D-Point')   
ax.set_xlabel('X Label (m)')  
ax.set_ylabel('Y Label (m)')
ax.set_zlabel('Z Label (m)')   
'''
ax.scatter(a[89:97,3], a[89:97,4], a[89:97,5],c='r',marker = (3,0),alpha = 0.8,lw = 1) 
ax.hold('on')
'''
ax.scatter(a[139:148,3],a[139:148,4], a[139:148,5],c='b',marker = (6,0),alpha = 0.8,lw = 1)  
ax.hold('on')
ax.scatter(a[151:161,3],a[151:161,4], a[151:161,5],c='g',marker = (4,0),alpha = 0.8,lw = 1)  


ax.grid('on')    #以上语句不难理解
plt.show()  