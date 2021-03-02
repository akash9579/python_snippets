# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 09:56:02 2021

@author: 91937
"""


string = "akash"
sub = []
for i in range(len(string)):
    for j in range (i,len(string)+1):
        sub.append(string[i:j])
        
print(len(sub))
se=set(sub)
nsub=list(se)
print(len(nsub))
    