# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:25:03 2021

@author: 91937
"""


# stack follow the last in first out
# example web brawsing application
# push,pop operation

"""
Write a function in python that can reverse a string using stack data structure.
"""
string = "we will play football"

x = string.split(" ")
from collections import deque
stack = deque()

for ele in x:
    stack.append(ele[::-1])
    
print(stack)

# for reverse string 
# txt = "Hello World" [::-1]
# print(txt) 