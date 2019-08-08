#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GuessingGame.py
#  
#  www.practicepython.org Exercise 9 Guessing Game
import random
print("Welcome to Exercise 9: Guessing Game.")
print("A random number has been chosen between 1 and 10")
print("Type 'exit' if you want to quit")	
a = random.randint(1, 10)
b = 0 
c = 0
while int(b) != a and b != "exit" :
	b = input("Please guess the random number:")
	c += 1 
	if b == 'exit' :
		print("Better luck next time!")
		break
	elif int(b) < a :
		print("Too low, try again")
	elif int(b) > a :
		print("Too high, try again")
	else :
		print("You guessed correctly in", c, "tries.")
