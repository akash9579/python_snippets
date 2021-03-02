# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:36:37 2020

@author: 91937
"""


t=int(input())
for T in range(t):
    l=[int(i) for i in input().split()]
    n=l[0]
    k=l[1]
    s=l[2]
    #calculate m1
    def m1(n,k,s):
        total=(k-1)+1+n
        return total
    
    def m2(n,k,s):
        total1=(k-1)+(k-s)+(n-s+1)
        return total1
    
    a1=m1(n,k,s)
    a2=m2(n,k,s)
    final=min(a1,a2)
    print("Case #{}: {}".format(T+1,final))