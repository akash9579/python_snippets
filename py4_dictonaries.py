# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:03:11 2020

@author: akash
"""


""" dictonaries are the pair of key and value """


student = {"akash" : "kamerkar","pranita" : "a" }

print(student)

print(student['akash'])  # if we pass value which is in not a list then we get error

print(student.get(12))

print(student.get('akash'))

print(student.get(12 , 'not found'))

# update value

student['akash']='michel'

student.update({'akash' :'professor', ' pranita' :'stud'})# for multiple update

del student.['pranita']

age = student.pop('pranita')

print(student.values())

print(student.items())

print(student['akash'])

 