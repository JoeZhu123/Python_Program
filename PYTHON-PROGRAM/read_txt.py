# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 08:46:44 2015

@author: Administrator
"""

f = open(r'D:/PYTHON-PROGRAM/4_24.txt','r')
line = f.readline()
print line
while line:
    print line
    line = f.readline()

for line in open(r'D:/PYTHON-PROGRAM/4_24.txt'):
    print line

f = open(r'D:/PYTHON-PROGRAM/4_24.txt','r')
print f.readlines(5)
