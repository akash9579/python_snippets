# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:09:24 2020

@author: 91937
"""


t=int(input())
for T in range(t):
    a=[]
    l=[int(i) for i in input().split()]
    start=l[0]
    end=l[1]
    count= 0
    for i in range (start,end+1):
        #print(i)
        st=str(i)
        length=len(st)
        flag=1
        for i in range(0,length):
            p=i+1
            if((p % 2) !=0):                   
                if int(st[i]) % 2 != 0:
                    pass
                else:
                    flag=0
            elif((p % 2) ==0):
                if int(st[i]) % 2 == 0:
                    pass
                else:
                    flag=0
        if flag==1:
            a.append(int(st))
        final=len(a)
    print("Case #{}: {}".format(T+1,final))