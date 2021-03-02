# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:03:02 2021

@author: 91937
"""

def solve (N, A):
    # Write your code here
    new=[]
    for ele in A:
        if ele == 1:
            new.append(ele)
        if ele == 2:
            new.append(ele)
        else:
            for i in range(2,ele):
                if(ele%i)==0:
                    break
                else:
                    new.append(ele)
                    break
    ulist=set(new)
    new1=list(ulist)
    if len(new1)>1:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print (out_)




