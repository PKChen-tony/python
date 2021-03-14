# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:24:27 2021

@author: TUF B360M-E
"""
print("執行結果:")
import math;
def eratosthenes(n):
    P = [i for i in range(2, (int)(math.sqrt(n)+1))]
    p = 0
    while True:
        for i in P[p + 1:]:
            if i % P[p] == 0:
                P.remove(i)
        if P[p]**2 >= P[-1]:
            break
        p += 1
    return P

aNumber = (int)(input("Enter a number:"));
factors = eratosthenes(aNumber);

num = aNumber;

for divisor in factors:
        while( num % divisor == 0 ):
            num //= divisor
            print(divisor, ' ', end = '');
'''
執行結果:

Enter a number:720
2  2  2  2  3  3  5 
'''
print("="*30)  
print("執行結果:")
x = int(input("請輸入正整數： "))
result = []
n = x
for j in range(1,n//2+1):
    for i in range(2, n):
        if n % i == 0:
            result.append(i)
            n = n//i
            break
if len(result)!=0:
    result.append(n)
    print(x, '=', '*'.join(map(str, result)))
else:
    print("這是一個質數無法分解!")
'''
==============================
執行結果:

請輸入正整數： 5
這是一個質數無法分解!
==============================
執行結果:

請輸入正整數： 720
720 = 2*2*2*2*3*3*5
'''
