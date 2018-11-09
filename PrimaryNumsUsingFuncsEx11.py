#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PrimaryNumsUsingFuncsEx11.py
#  
# 
#  www.practicepython.org Excercise 11

print("Welcome to Exercise 11!")
def get_integer(help_text="Please enter a random integer: "):
	return int(input(help_text))
	
x = get_integer()
y = list(range(1, x+1))
z=[]
for number in y :
	if x % number == 0:
		z.append(number)
	
print("Your random number was", x, ". The divisor's are", z)
