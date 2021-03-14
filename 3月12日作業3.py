# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:46:04 2021

@author: TUF B360M-E
"""
print("執行結果")
import math
n = 0
count = 0
while True:
    first = n + 100
    second = n + 168
    first_sqrt = int(math.sqrt(first))
    second_sqrt = int(math.sqrt(second))
    if (first_sqrt*first_sqrt == first) and (second_sqrt*second_sqrt == second):
        print('ans:',n)
        break
    n = n + 1
'''
執行結果
ans: 156
'''

