# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 13:19:54 2021

@author: 91937
"""


# implementation of queue
# based on first in first out
# enqueue opration means insertion 
# dequeue opration means deletion


# implementation using list
class queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self,item):
        self.q.insert(0,item)
        
    def dequeue(self):
        self.q.pop()        
# we can define seek and length function also
# we are inserting 1 then 2 then 3
# so in queue -----> 3--2--1    
a = queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
print(a.q)
# perform dequeue operation on the queue so output will be ---->   3--2    
a.dequeue()
print(a.q)


-
# implementing using collection module
from collections import deque
q1 = deque()
q1.appendleft('akash') 
q1.appendleft('ashok') 
q1.appendleft('kamerkar')
print(q1) 
q1.pop()
print(q1)
