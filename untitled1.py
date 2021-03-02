# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:10:18 2021

@author: 91937
"""


def SimplePassword(strParam):
    valid = 1
    flag = 0
    digit = 0
    present = 0
    #print(len(strParam))
    length = len(strParam)
    if length < 8 or length > 30:
        valid = 0
    #print(valid)
    
    strParam1 = strParam.lower()
    if strParam1.find("password") != -1:
        valid = 0
    #print(valid)
        
    for ele in strParam:
        if (ele.isupper()):
            flag=1
        
    #print(flag)
    
    for ele in strParam:
        if (ele.isdigit()):
            digit = 1
    #print(digit)
    
    for ele in strParam:
        if ele in ['!','=','-','*','=','%','/']:
            present = 1
            
    if (present == 1 and digit == 1 and flag == 1 and valid == 1):
        strParam = 'true'
    else:
        strParam = 'false'

  # code goes here
    return strParam

# keep this function call here 
print(SimplePassword(input()))