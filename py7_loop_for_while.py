# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:27:01 2020

@author: akash
"""


###############  loops and iteration ###################

###################   FOR LOOP  #########################

num = ['1','2','3']
print(type(num))

for inte in num:
    print(inte)
    print(type(inte))
    
    
num = [1,2,3]
for inte in num:
    if inte == 3:
        print("we fount it")
        break                          # we can use break for stopping the loop
    print(inte)
      
    
num = [1,2,3,4,5,6]
for inte in num:
    if inte == 3:
        print("we fount it")
        continue                    # we can use break for stopping the loop
    print(inte)
    


num = [1,2,3,4,5,6]                # for loop in for loop     NESTED LOOP
for inte in num:
    for letter in 'abc':
        print(inte,letter)
        
        
for i in range(1,10):
    print(i)
    
    
        
    
####################  = is assignmet operator and == is checking operator #######################
    
#############  list = ['a'] its list of str   and   list = [1] list of integer  #############
    
    
#############################      WHILE LOOP   ###################################   
    
    
x = 5                       #  basic while loop      if condition is true upto that while loop excute
while x < 10:
    print(x)
    x = x + 1
    
x = 5                      #  this loop goes infinite for getting out og that loop press clt + c
while x < 10:
    print(x)
       
    
    
x = 5                      #  this loop goes infinite for getting out og that loop press clt + c
while x < 10:
    x=x+1
    if x == 8:
        print(x)           # using of break
        break
          
    
    
    
    
    
    
    
    
    
    
    
    