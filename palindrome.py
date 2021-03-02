# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 10:34:54 2021

@author: 91937
"""


st="malylam"
j=len(st)
for i in range (len(st)//2 + 1):
    j=j-1
    if st[i] != st[j]:
        print("not a palindrome")
        break

        