# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:16:00 2015

@author: Administrator
"""

import numpy as np
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
#from enthought.mayavi import mlab
#X = np.array([])

x,y = np.mgrid[-2:2:20j,-2:2:20j]
z = x*np.exp(-x**2-y**2)

from xlrd import open_workbook


book = open_workbook("Book2.xlsx")
book.nsheets    #工作表的数目
print book.sheet_names()[0]     #第四个工作表的名字
sheet = book.sheet_by_name(u'Sheet1')#通过名称获取
#nrows = book.nrows 
#ncols = book.ncols
for i in range(5):
    print sheet.row_values(i)
   
   
#for i in range(3):
#      print sheet.col_values(i) 
mlab.point3d(sheet.col_values(0),sheet.col_values(1),sheet.col_values(2))
mlab.show()     

ax = plt.subplot(111,projection='3d')
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap = plt.cm.Blues_r)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.figtext(1,1,u"Figure 1",color = "red")
plt.show()


