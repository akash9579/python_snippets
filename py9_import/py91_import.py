# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:39:13 2020

@author: akash
"""


######################################################################################


print('welcome Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''      #this stuff is important for ref stuff
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1