# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:29:01 2015

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np    #导入包

 

t1=np.arange(0.0,4.0,0.1)
t2=np.arange(0.0,4.0,0.05)     #准备一些数据

 

fig = plt.figure()    #准备好这张纸，并把句柄传给fig
ax1 = fig.add_subplot(211)    #使用句柄fig添加一个子图
line1, = plt.plot(t1,np.sin(2*np.pi*t1),'--*')   #绘图，将句柄返给line1 
plt.title('sine function demo')   
plt.xlabel('time(s)')
plt.ylabel('votage(mV)')   
plt.xlim([0.0,5.0])
plt.ylim([-1.2,1.2])   
plt.grid('on')    #以上语句不难理解

 

##这种方式的优势和不同在以下语句体现。因为句柄的引入，让我们更加的面向对象，思路也更加清晰。代码的

##可读性也更高了。

plt.setp(line1,lw=2,c='g')    #通过setp函数，设置句柄为line1的线的属性，c是color的简写
line1.set_antialiased(False)    #通过line1句柄的set_*属性设置line1的属性
plt.text(4,0,'$\mu=100,\\sigma=15$')    #添加text，注意，它能接受LaTeX哟！

 

ax2=fig.add_subplot(212)
plt.plot(t2,np.exp(-t2),':r')
plt.hold('on') 
plt.plot(t2,np.cos(2*np.pi*t2),'--b')

plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()