# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 02:47:18 2021

@author: TUF B360M-E
"""
print("解一執行結果:")
from itertools import permutations
abc=['A','B','C']
for item in permutations(abc,3):
    print(item)
print("="*40)  
print("解二執行結果:")  
from itertools import permutations  
a = "ABC"  
p = permutations(a)   
for j in list(p):  
    print(j) 
"""
解一執行結果:
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
========================================
解二執行結果:
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
"""   


