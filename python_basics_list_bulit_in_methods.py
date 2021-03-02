# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:28:11 2021

@author: 91937
"""

# list is the collection of items having same data times
new1 = []
new2 = [1,2,3,4]
new3 = ['a','e','i','o','u']
new4 = list(i for i in range(10))

# adding item to list
new1.append(2)
new2.insert(4,4)
# index used to return the index of the element, we also add start,stop parameters 
check = new2.index(3)
# we can use extend with list,set,tuple
new1.extend(new2)

#remove
new1.remove(4)

#count
print(new1.count(1))

#pop index by default its -1
print(new1.pop())
print(new1.pop(0))



#reverse
new2.reverse()

# sort
new2.sort()
new2.sort(reverse=True)

# copy
c = new3.copy()

#clear
c.clear()