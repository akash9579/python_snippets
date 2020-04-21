# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:25:26 2020

@author: akash
"""
#    string class #


#print("hi bro")

mess = 'hi aza'
#print(mess)


print(type(mess))

print(len(mess))
print(mess[0:4])
print(mess[:4])

print(mess.lower())
print(mess.upper())

print(mess.count('hi'))
print(mess.find("az"))

new_m = mess.replace('hi', 'bhava')
print(new_m)


print(mess+','+new_m)

print(" {} , {} this is it".format(mess,new_m))
print(f" {mess} , {new_m} this is it")


print(dir())
print("-----------------------------------------------------------")
print(dir(mess))
print(help(str.lower))