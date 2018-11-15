#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Ex14ListRemoveDuplicates.py
#  

print("""
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.
Write two different functions to do this - one using a loop and 
constructing a list, and another using sets.
""")

def num_list(x):
	y = set(x)
	print (y)

x = [1,2,3,12,3,5,34,1,4,4,7,8,9]
print("Here is the list:", x)
print("Here is the list without duplicates:")
num_list(x)
