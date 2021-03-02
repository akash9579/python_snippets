import sys
sys.stdin=open("C:/Users/91937/Documents/input.txt","r")
sys.stdout=open("C:/Users/91937/Documents/output.txt","w")


# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:47:39 2020

@author: CSE
"""

t=int(input())
for T in range(t):
    str=input()
    a=str
    length=len(a)
    #print(length)
    kickn=0
    ns=0
    for i in range (0,length-4):
        if ((a[i]=='K') and  (a[i+1]=='I') and (a[i+2]=='C') and (a[i+3]=='K')):
            ns+=1
        if ((a[i]=='S') and  (a[i+1]=='T') and (a[i+2]=='A') and (a[i+3]=='R') and (a[i+4]=='T')):
            kickn+=ns
    #print(kickn)
    print("Case #{}: {}".format(T+1,kickn))