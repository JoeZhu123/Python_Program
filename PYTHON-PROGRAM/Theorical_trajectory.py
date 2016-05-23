# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:15:15 2015

@author: Administrator
"""

#理论轨迹曲线_2D
import numpy as np 
import matplotlib.pyplot as plt 
import math

x0=0
y0=0
x=0
y=0
x1=0
y1=0
x2=0
y2=0
x3=0
y3=0

vt=6.606
g=9.8
lambda1=math.pi/6
lambda2=math.pi/3 #单位：弧度
v1=30
v2=60          #单位：m/s
vm=v1*np.cos(lambda1)
vn=v1*np.sin(lambda1)
vm1=v1*np.cos(lambda2)
vn1=v1*np.sin(lambda2)

vm2=v2*np.cos(lambda1)
vn2=v2*np.sin(lambda1)
vm3=v2*np.cos(lambda2)
vn3=v2*np.sin(lambda2)

'''
fig=plt.figure()     #准备好这张纸，并把句柄传给fig

'''
x=np.linspace(0,12,120)
y = y0+(vt**2/g)*np.log(np.abs((np.sin(vt*(np.exp(g*(x-x0)/vt**2)-1)/vm)+math.atan(vt/vn))/np.sin(math.atan(vt/vn))))
plt.plot(x,y,'-',c='r')
plt.hold('on')

x1=np.linspace(0,9.5,95)
y1 = y0+(vt**2/g)*np.log(np.abs((np.sin(vt*(np.exp(g*(x1-x0)/vt**2)-1)/vm1)+math.atan(vt/vn1))/np.sin(math.atan(vt/vn1))))
plt.plot(x1,y1,'-',c='g')
plt.hold('on')

x2=np.linspace(0,15,150)
y2= y0+(vt**2/g)*np.log(np.abs((np.sin(vt*(np.exp(g*(x2-x0)/vt**2)-1)/vm2)+math.atan(vt/vn2))/np.sin(math.atan(vt/vn2))))
plt.plot(x2,y2,'-',c='b')
plt.hold('on')

x3=np.linspace(0,12.2,122)
y3 = y0+(vt**2/g)*np.log(np.abs((np.sin(vt*(np.exp(g*(x3-x0)/vt**2)-1)/vm3)+math.atan(vt/vn3))/np.sin(math.atan(vt/vn3))))
plt.plot(x3,y3,'-',c='y')

plt.title('Badminton Theorical Trajectory  C=0.6') 
plt.xlabel('X-Label (m)')
plt.ylabel('Y-Label (m)')  
plt.xlim(0,16)
plt.ylim(0,10)
plt.grid('on')    #以上语句不难理解
plt.show()    