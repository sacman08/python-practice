#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Ex15TextReverseOrder.py
#  
print("""
Write a program (using functions!) that asks the user for a long
 string containing multiple words. Print back to the user the 
 same string, except with the words in backwards order.
 """)
def name_result(g):
	h = g.split()
	result = ""
	for i in range(len(h), 0 -1):
		result += h[i-1]
	print(result)
	
g = input("Please enter a string of words:")
name_result(g)
