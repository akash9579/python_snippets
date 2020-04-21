# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:22:28 2020

@author: akash
"""

##################################################################################################

if True:
    print('akash')
    
s1='ak'

if s1 == 'ak':
    print("yes")
else:
    print("no")
    
    

if s1 != 'ak':
    print("yes")
else:
    print("no")
    
value=True                  ###### combine if condition with and,or
if s1 == 'ak' and value:
    print('jai hind')
else:
    print('jaja')
    
    
value=True                   ########### python dont have switch case #####################
if s1 == 'ak' and value:
    print('jai hind')
elif:
    print("switch case")
else:
    print('jaja')
    
    
    
a = ['1','2','3']
b = ['1','2','3']

print(a == b)  # true

print(a is b)       # false bcae they have different id
print(id(a))
print(id(b))


#  false
    #False ,    None  , 0 , any empty seqence "",'',(),{},[] 

cond = 0
if cond:
    print("true")
else:
    print("evalute to false")