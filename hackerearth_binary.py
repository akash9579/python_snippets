# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:25:50 2021

@author: 91937
"""

from fractions import Fraction 
t=int(input())
def append(st,l):
    return [st + element for element in l]

def main(t):
    if t == 0:
        return [ ]
    if t == 1:
        return ["0","1"]
    return (append("0",main(t-1)) +
    append("1",main(t-1)))
p=main(t)
subs = "11"
res = [i for i in p if subs not in i] 
ab=[]
for ele in res:
    if(ele[t-1]=='1'):
        ab.append(ele)
print(len(res))
print (Fraction(len(ab), len(res)))
