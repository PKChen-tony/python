# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 01:35:41 2021

@author: TUF B360M-E
"""

number=int(input("請輸入次數:"))
for i in range(1,number+1):
    if i%2== 0 :
        print(i)
        print("上面數字是偶數")
        print("=============")
    elif i%2== 1 :
        print(i)
        print("上面數字是奇數")
        print("=============")
print("全部分類:")
for i in range(1,number+1):
    if i%2== 0 :
        print(i)
print("=================")
print("上面數字是偶數")
for i in range(1,number+1):
    if i%2== 1 :
        print(i)
print("=================")
print("上面數字是奇數")