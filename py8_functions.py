# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:08:45 2020

@author: akash
"""

#############################################################



def hello ():
    pass        #this function doing nothing 

print(hello)    # gives us the location

                # for running that function u have to give()

hello()


def hello1 ():           # we are excuting basic function
    print("hi bro")      
hello1()



def hello2 ():           # here we are returnig something instead of running something
    return "hi bro"      
a=hello2()
print(a)
type(a)



def hello3 (variable):
    return "{} bro".format(variable)
hello3()                                   # giving error that 1 argument is required


hello3("ssup")
print(hello3("ssup"))

print(hello3("ssup").upper())    


def hello4 (name,name1='akash'):                              # name1 has default value is akash
    print("{}+{} this is my name".format(name,name1))
              
hello4(2)
hello4('akash')               # we are just passing just 1 argument but we dont getting anu error
                              # beacuse 2nd argument have deafult value

hello4('kamerkar','jaggu')



month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   # Number of days per month. First value placeholder for indexing purposes.


def is_leap(year):
    """Return True for leap years, False for non-leap years."""      # its always better to give function information

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

is_leap(2014)
is_leap(2020)

days_in_month(1997, 2)
days_in_month(1997, 3)
days_in_month(1996, 2)


