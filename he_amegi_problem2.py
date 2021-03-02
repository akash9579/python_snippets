# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:59:24 2021

@author: 91937
"""


from itertools import combinations      
test_str = "abcdabc"  
res = [test_str[x:y] for x, y in combinations( 
            range(len(test_str) + 1), r = 2)] 
pre=[]
for i in range (len(test_str)):
    pre.append(test_str[0:i])
pre.append()   

count1=0
for ele in res:
    if ele in pre:
        print(ele)
        count1=count1+1