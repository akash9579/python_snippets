# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:17:51 2021

@author: 91937
"""

from fractions import Fraction 
def countStrings(n): 
  
    a=[0 for i in range(n)] 
    b=[0 for i in range(n)] 
    a[0] = b[0] = 1
    for i in range(1,n): 
        a[i] = a[i-1] + b[i-1] 
        b[i] = a[i-1] 
        
    #print(a[n-1] + b[n-1]) 
    #print(a[n-3] + b[n-3])
    result=[]
    result.append(a[n-1] + b[n-1])
    a=Fraction(a[n-3] + b[n-3], a[n-1] + b[n-1])
    result.append(a)
    return result
  
# Driver program to test 
# above functions 
  
print(countStrings(3)) 