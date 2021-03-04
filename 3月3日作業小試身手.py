# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 01:50:54 2021

@author: TUF B360M-E
"""
print("***程式執行結果***")
import random
count=0
min = 0
max = 100
ans=random.randint(1, 100)
print("random值",ans)
guess=0
print("請輸入1-100之間的整數")
while ans != guess :
     guess = int(input("請輸入數字:"))
     if guess > ans:
         max = guess
         print("Try again between {0} and {1}".format(min, max))         
     else:
         min = guess
         print("Try again between {0} and {1}.".format(min, max))         
     count+=1
print ("Congratulations, the munber is ",ans)
print("恭喜你答對了,共猜:",count,"次")
print("***程式執行完畢***")

"""
***程式執行結果***
random值 88
請輸入1-100之間的整數

請輸入數字:70
Try again between 70 and 100.

請輸入數字:80
Try again between 80 and 100.

請輸入數字:85
Try again between 85 and 100.

請輸入數字:90
Try again between 85 and 90

請輸入數字:87
Try again between 87 and 90.

請輸入數字:89
Try again between 87 and 89

請輸入數字:88
Try again between 88 and 89.
Congratulations, the munber is  88
恭喜你答對了,共猜: 7 次
***程式執行完畢***
"""

