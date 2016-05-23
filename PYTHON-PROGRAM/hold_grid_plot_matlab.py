# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:33:50 2015

@author: Administrator
"""

from pylab import *    #引入兼容MATLAB包：pylab


t1=arange(0.0,4.0,0.1)
t2=arange(0.0,4.0,0.05)    #准备一些数据，注意和MATLAB的不同

 

figure()   
subplot(211)   
plot(t1,sin(2*pi*t1),'--g*')

title('sine function demo')   
xlabel('time(s)')
ylabel('votage(mV)')   

xlim([0.0,5.0])
ylim([-1.2,1.2])   
grid('on')    #控制网格显示和grid(True)效果一样。不带参数的grid()起到toggle的作用。

 

subplot(212)
plot(t2,exp(-t2),':r')
hold('on')    #前一条线保持。用法和grid类似。
plot(t2,cos(2*pi*t2),'--b')

xlabel('time')
ylabel('amplitude')
show()    #这是和MATLAB很大的不同，这个命令用完，图形才会出来。