# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:00:46 2020

@author: akash
"""


""" list concept """

courses = ['ak','jk','lm']
print(courses)

print(type(courses))
print(courses[0])
print(courses[-1])

print(courses[0:2]) #0 to 2 means include 0th and exclude 2th so only 0,1


print(len(courses))

courses.append('jkjk')
print(courses)

courses.insert(0, 'new_inserted')
print(courses)

c = ["new list created"]
courses.insert(0,c)
print(courses)  # but new element in sep list form so use extend 

courses.extend(c)

#for removing items

val = courses.pop()
print(val)

courses.remove('lm')
courses.reverse()
print(courses)


courses1 = ['2','3','3']
sorted_ver = sorted(courses1)
print(sorted_ver)

# extra

print('ak' in courses)

for item in courses:
        print(item)
        
        
for index,item in enumerate(courses):
        print(index,'------>',item)
        print('a'+'b')
        
cou = ['ak','kk','kj','lk']
new_c = ' , '.join(cou)           # used to convert list into string
print(new_c)                

print(type(new_c))

new_c1 = ' --- '.split(new_c)     #convert the string into list
print(new_c1)   



""" tupple is immutable  here we dont modify the stuff rest of application same as the list"""

t1 = ( " aksh" ,"kamerkar")
t2 = t1

print(type(t1))




""" sets dont care about order , dont have duplicate , optimize for check item in set"""

# we can use set oprator

c1 = {"2","3","4","5"}

c2 = {"2","3","4","6"}

print(c1.intersection(c2))

print(c1.difference(c2))

print(c1.union(c2))



# empty list

e1 = []
e2 = list()

#empty tuples

t11 = ()
t12 = tuple()

#empty sets

s1 = {}  ########################## its dictonary not a set
s2 = set()



