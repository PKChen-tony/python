# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 00:49:17 2021

@author: TUF B360M-E
"""
print("執行結果")
i=int(input('請輸入利潤:'))
earn=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
bonus=0
for m in range(len(earn)):
    if i>earn[m]:
        bonus+=(i-earn[m]*rat[m])
        i=earn[m]
print("奬金:",bonus)
'''
執行結果

請輸入利潤:150000
奬金: 242500.0

'''
    

