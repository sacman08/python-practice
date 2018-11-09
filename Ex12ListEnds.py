#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Ex12ListEnds.py
#  
#  www.praticepython.org Excerise 12 List Ends
#  
print("""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
""")
import random

a = random.randint(1,15)
b = random.sample(range(100), a)

print ("This list of numbers is ", b)	
print ("The start number is ", b[0], "and the end number is ", b[-1])
