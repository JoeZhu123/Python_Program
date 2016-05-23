# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:05:41 2015

@author: Administrator
"""

print 'Badminton_Points_Number'
#计算一个txt文件中共有多少行

#文件比较小
count = len(open(r'D:/PYTHON-PROGRAM/rudy_badminton02data.txt','rU').readlines())
print count

#文件比较大
count = -1
for count,line in enumerate(open(r'D:/PYTHON-PROGRAM/rudy_badminton02data.txt','rU')):
    pass
count += 1
print count

#更好的方法
count = 0
thefile = open(r'D:/PYTHON-PROGRAM/rudy_badminton02data.txt','rb')
while True:
    buffer = thefile.read(1024*8192)
    if not buffer:
        break
    count += buffer.count('\n')
thefile.close()
print count
    