# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:42:02 2020

@author: akash
"""


##################################################


import py91_import as p      #beacuse its in same directory
#from py91_import import *
import sys
courses = ['History', 'Math', 'Physics', 'CompSci']

index = p.find_index(courses,'Math')
print(index)

# import py91_import 
# from py91_import import find_index , test
#from py91_import import *


#print(test)

print(sys.path)   # gives the list of directory where we check the import files
                  # we can add our external directory loaction to list by using append but its bad practice
                  # sys.path.append('')


########### know we check some function from standard library#################

import random
courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)
print(random_course)



import math
rad = math.radians(1)
print(math.sin(rad))

import datetime
today = datetime.date.today()
print(today)

import os
print(os.getcwd())

print(os.__file__)   # print location of file in file system

import antigravity    # went to website