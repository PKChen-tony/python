# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 00:24:05 2021

@author: TUF B360M-E
"""
# 題目：將一個列表的數據複製到另一個列表中

a = [1,2,3]
b = a[:] 
print(a) 
print(b)
b.reverse() 
print(b) 
print(a)
'''
[1, 2, 3]
[1, 2, 3]
[3, 2, 1]
[1, 2, 3]
'''


