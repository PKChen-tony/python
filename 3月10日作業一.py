# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 02:29:03 2021

@author: TUF B360M-E
"""
"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出這個數列的前20项之和。
"""
print("解一執行結果:")
a = 2
b = 1
sum = 0
for i in range(20):
    sum = a / b + sum
    a, b = (a + b), a
print('總和=',sum)

print("="*40) 
print("解二執行結果:")
n = int(input('Please enter the number of items:'))
fenzi = 2# molecule
fenmu = 1#denominator
l = []
s = 0
 
for i in range(1,n+1):
    a = fenzi
    b = fenmu
    
    s += (a/b)
    l.append('%s/%s'%(a,b))
    
    fenzi = a+b
    fenmu = a
    
print('+'.join(str(i) for i in l),end = '')
print('=%.2f'%s)
'''
解一執行結果:
總和= 32.66026079864164
========================================
解二執行結果:

Please enter the number of items:20
2/1+3/2+5/3+8/5+13/8+21/13+34/21+55/34+89/55+144/89+233/144+377/233+610/377+987/610+1597/987+2584/1597+4181/2584+6765/4181+10946/6765+17711/10946=32.66
'''

