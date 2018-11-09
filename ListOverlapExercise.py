#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ListOverlapExercise.py
#  
#  www.practicepython.org Exercise 5

print("Welcome to the list overlap exercise!")
 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = []
if a > b :
	for a in b:
		y.append(a)
		print("List a was larger, here are the matches:", y)
elif b > a:
	for b in a:
		y.append(b)
		print("List b was larger, here are the matches:", y)
else:
	for a in b:
		y.append(a)
		print("The lists were equal length, here are the matches:", y)
