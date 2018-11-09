#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  OddOrEvenCheck.py
#  
#  www.practicepython.org Exercise 2

print("Welcome to Excerise 2!")
AskNumber = int(input("Please enter a random number:"))

ModChck = AskNumber % 2
Mod2Chck = AskNumber % 4

if ModChck == 0 :
	print("Your number was even.")
else:
	print("Your number was odd.")
	
if Mod2Chck == 0 :
	print("Your number was divisable by 4.")
else:
	print("Your number was not divisable by 4.")
	
print("Thanks have a great day!")
