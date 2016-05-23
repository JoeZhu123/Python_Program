# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 07:43:03 2015

@author: Administrator
"""

#Single Panel Badminton Trajectory Experiment
import matplotlib.pyplot as plt 
import numpy as np
import math
from xlrd import open_workbook


f_i=12*40e-3;    #sampling interval 采样时间间隔，单位：s
vt=0;
rope=1.23;          #空气密度，单位：kg/m**3
g=9.8;             #重力加速度，单位：m/s**2
S=3.116e-3;   #羽毛球迎风面面积，单位：m**2
m=5.12e-3;    #一般羽毛球的质量，单位：kg
C=0.60;            #空气阻力系数
vm=0;vn=0;
basic_h=30e-2;#标定柱的基本高 单位：m
 
vt=np.sqrt(2*m*g/(C*rope*S)); 

print vt

P = np.empty((47,2),np.float)
book = open_workbook("Book5.xlsx")
book.nsheets # 工作表的数目
print book.sheet_names()[0] #第一个工作表的名字
sheet = book.sheets()[0] # 获得第一个工作表
for i in xrange(47):
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

plt.scatter(10**(-2)*P[0:6,0], 10**(-2)*(500-P[0:6,1]),c='r',marker = (3,0),alpha = 0.6,lw = 1)
plt.hold('on')
plt.scatter(10**(-2)*P[6:13,0], 10**(-2)*(500-P[6:13,1]),c='g',marker = (4,0),alpha = 0.6,lw = 1)  
plt.hold('on')
plt.scatter(10**(-2)*P[13:21,0], 10**(-2)*(500-P[13:21,1]),c='b',marker = (5,3),alpha = 0.6,lw = 1)

plt.hold('on')
x0=P[0,0]*10**(-2);#初始采样点横坐标
y0=(500-P[0,1])*10**(-2);#初始采样点纵坐标 
vn=vt*(g*(500-P[1,1])*10**(-2)/(vt**2)-np.cos(g*f_i*1/vt))/np.sin(g*f_i*1/vt);
vm=(vt**2)*(np.exp(g*P[1,0]*10**(-2)/vt**2)-1)/(g*f_i*1); 
print vn
print vm
x = np.linspace(x0,0,100)
def f(x):
    return (y0+(vt**2/g)*np.log(np.abs((np.sin(vt*(np.exp(g*(-x+x0)/vt**2)-1)/vm)+math.atan(vt/vn))/np.sin(math.atan(vt/vn)))))
plt.plot(x,f(x),'-',c='r',label='line 1',linewidth=2) 

plt.hold('on')
x1=P[6,0]*10**(-2);#初始采样点横坐标
y1=(500-P[6,1])*10**(-2);#初始采样点纵坐标 
vn1=vt*(g*(500-P[6,1])*10**(-2)/(vt**2)-np.cos(g*f_i*1/vt))/np.sin(g*f_i*1/vt);
vm1=(vt**2)*(np.exp(g*P[6,0]*10**(-2)/vt**2)-1)/(g*f_i*1); 
print vn1
print vm1
x = np.linspace(x1,0,100)
def f1(x):
    return (y1+(vt**2/g)*np.log(np.abs((np.sin(vt*(np.exp(g*(-x+x1)/vt**2)-1)/vm1)+math.atan(vt/vn1))/np.sin(math.atan(vt/vn1)))))
plt.plot(x,f1(x),'-',c='g',label='line 2',linewidth=2) 

plt.hold('on')
x2=P[13,0]*10**(-2);#初始采样点横坐标
y2=(500-P[13,1])*10**(-2);#初始采样点纵坐标 
vn2=vt*(g*(500-P[13,1])*10**(-2)/(vt**2)-np.cos(g*f_i*1/vt))/np.sin(g*f_i*1/vt);
vm2=(vt**2)*(np.exp(g*P[13,0]*10**(-2)/vt**2)-1)/(g*f_i*1); 
print vn2
print vm2
x = np.linspace(x2,0,100)
def f2(x):
    return (y2+(vt**2/g)*np.log(np.abs((np.sin(vt*(np.exp(g*(-x+x2)/vt**2)-1)/vm2)+math.atan(vt/vn2))/np.sin(math.atan(vt/vn2)))))
plt.plot(x,f2(x),'-',c='b',label='line 3',linewidth=2) 
 
plt.grid('on')    #以上语句不难理解
plt.legend()
plt.show()    