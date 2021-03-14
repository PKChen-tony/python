# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:46:04 2021

@author: TUF B360M-E
"""
print("執行結果:")
data=[90,2,7]
data.sort(reverse=False)
print(data)
print("="*30)
l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)
'''
執行結果:
[2, 7, 90]
==============================

integer:
2

integer:
7

integer:
90
[2, 7, 90]
'''