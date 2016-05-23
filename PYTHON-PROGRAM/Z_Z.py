# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:46:22 2015

@author: Administrator
"""

import re


f=open('rudy_badminton02data.txt','r')
s=f.read()

'''
A=re.findall('A: (\d+)',s)
B=re.findall('B: (\d+)',s)
C=re.findall('C: (\d+)',s)
print A
print B
print C
'''
point = re.findall('badminton point is  (\d+)',s)
print point