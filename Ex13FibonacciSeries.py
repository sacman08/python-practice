#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Ex13FibonacciSeries.py
#  
#  

print("""
Write a program that asks the user how many Fibonnaci numbers 
to generate and then generates them. Take this opportunity 
to think about how you can use functions.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …
""")
def Fibonacci(num_list):
	results = [1]
	fibnum = 1
	for number in range(1,num_list):
		results.append(fibnum)
		fibnum = ((results[-1])+(results[number-1]))
	print(results)
		
num_list = int(input("How many Fibonacci numbers to show?\n"))

Fibonacci(num_list)
