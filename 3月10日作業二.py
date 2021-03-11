# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 02:18:05 2021

@author: TUF B360M-E
"""
print("執行結果:")
def combi(r, n):
    return 1 if n == 0 else combi(r, n - 1) * (r - n + 1) // n
	
height = 5
c = [[combi(r, n) for n in range(r + 1)] for r in range(height)]
 
for r in range(len(c)):
    print(("%" + str((len(c) - r) * 3) + "s") % "", end = "")
    for n in range(len(c[r])):
	    print("%6d" % c[r][n], end = "");
    print()
"""
執行結果:
                    1
                 1     1
              1     2     1
           1     3     3     1
        1     4     6     4     1
"""
  