# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print('解答1:')
s = '*'
for i in range(1, 8, 2):
    print((s*i).center(7))
for i in reversed(range(1, 6, 2)):
    print((s*i).center(7))
"""
程式執行結果
   *   
  ***  
 ***** 
*******
 ***** 
  ***  
   *   

"""

print('---------------------')








print('解答2:')
n=7
for i in range(1,n+1,2):
    string_1="*"*i
    print(string_1.center(n))
for i in range(n-2,0,-2):
    string_1="*"*i
    print(string_1.center(n))
    
"""
程式執行結果
   *   
  ***  
 ***** 
*******
 ***** 
  ***  
   *   
"""

