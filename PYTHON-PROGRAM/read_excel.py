# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:18:18 2015

@author: Administrator
"""

from xlrd import open_workbook
book = open_workbook("temp.xls")
book.nsheets # 工作表的数目
print book.sheet_names()[0] #第一个工作表的名字
sheet = book.sheets()[0] # 获得第一个工作表
sheet.cell(0,0) # 读取A1的内容
sheet.row(0) #读取第一行的内容
#读取第二列的内容，从第二行开始，并对其求和
sum(x.value for x in sheet.col(1,start_rowx=1))
sum(sheet.col_values(1,start_rowx=1)) # 同上
sheet.cell(1,3) # 读取公式单元格的值
for i in xrange(4):
    for j in xrange(3):
        print sheet.cell_value(i+1,j)