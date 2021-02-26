# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 00:56:43 2021

@author: TUF B360M-E
"""

number=int(input("請輸入次數:"))
sum=0
for i in range(1,number+1):
    if i%2== 0 :
        print(i)        
        sum+=i      
print("==================")        
print("上面數字是偶數")
print("總和==",sum)



    