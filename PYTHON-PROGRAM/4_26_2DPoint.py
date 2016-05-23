# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:39:21 2015

@author: Administrator
"""

import matplotlib.pyplot as plt 
import numpy as np
from xlrd import open_workbook

P = np.empty((54,2),np.float)
book = open_workbook("Book6.xlsx")
book.nsheets # 工作表的数目
print book.sheet_names()[0] #第一个工作表的名字
sheet = book.sheets()[0] # 获得第一个工作表
for i in xrange(54):
    for j in xrange(2):
#        print sheet.cell_value(i,j)
        P[i][j] = sheet.cell_value(i,j)
        
#   

    
fig=plt.figure()     #准备好这张纸，并把句柄传给fig
plt.title('Camera-YZ_Axis-Trajectory-Point')   
plt.xlabel('Y-Label')
plt.ylabel('Z-Label')   
#plt.xlim(-3.0,5.0)
#plt.ylim(-2.0,3.0)
'''
plt.scatter(10**(-2)*P[0:6,0], 10**(-2)*(500-P[0:6,1]),c='r',marker = (3,0),alpha = 0.6,lw = 1)
plt.hold('on')
plt.scatter(10**(-2)*P[6:12,0], 10**(-2)*(500-P[6:12,1]),c='g',marker = (4,0),alpha = 0.6,lw = 1)  
plt.hold('on')
plt.scatter(10**(-2)*P[12:18,0], 10**(-2)*(500-P[12:18,1]),c='b',marker = (5,3),alpha = 0.6,lw = 1)
plt.hold('on')
plt.scatter(10**(-2)*P[18:24,0], 10**(-2)*(500-P[18:24,1]),c='c',marker = (5,0),alpha = 0.6,lw = 1)
plt.hold('on')
plt.scatter(10**(-2)*P[24:30,0], 10**(-2)*(500-P[24:30,1]),c='m',marker = (6,0),alpha = 0.6,lw = 1)  
plt.hold('on')
'''
plt.scatter(10**(-2)*P[30:36,0], 10**(-2)*(500-P[30:36,1]),c='y',marker = (8,0),alpha = 0.6,lw = 1)
plt.hold('on')
plt.scatter(10**(-2)*P[36:42,0], 10**(-2)*(500-P[36:42,1]),c='k',marker = (6,1),alpha = 0.6,lw = 1)  
plt.hold('on')
plt.scatter(10**(-2)*P[42:48,0], 10**(-2)*(500-P[42:48,1]),c='w',marker = (4,0),alpha = 0.6,lw = 1)
plt.hold('on')
plt.scatter(10**(-2)*P[48:54,0], 10**(-2)*(500-P[48:54,1]),c='r',marker = (3,0),alpha = 0.6,lw = 1)

plt.grid('on')    #以上语句不难理解
plt.show()  