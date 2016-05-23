# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:45:32 2015

@author: Administrator
"""

from numpy import *
import matplotlib.pyplot as plt
from random import *
def loadData():
    x = arange(-1,1,0.02)
    y = ((x*x-1)**3+1)*(cos(x*2)+0.6*sin(x*1.3))
    #生成的曲线上的各个点偏移一下，并放入到xa,ya中去
    xr=[];yr=[];i = 0
    for xx in x:
        yy=y
        d=float(randint(80,120))/100
        i+=1
        xr.append(xx*d)
        yr.append(yy*d)
    return x,y,xr,yr
def XY(x,y,order):
    X=[]
    for i in range(order+1):
        X.append(x**i)
    X=mat(X).T
    Y=array(y).reshape((len(y),1))
    return X,Y
def figPlot(x1,y1,x2,y2):
    plt.plot(x1,y1,color='g',linestyle='-',marker='')
    plt.plot(x2,y2,color='m',linestyle='',marker='.')
    plt.show()
def Main():
    x,y,xr,yr = loadData()
    X,Y = XY(x,y,9)
    XT=X.transpose()#X的转置
    B=dot(dot(linalg.inv(dot(XT,X)),XT),Y)#套用最小二乘法公式
    myY=dot(X,B)
    figPlot(x,myY,xr,yr)
    
Main()








