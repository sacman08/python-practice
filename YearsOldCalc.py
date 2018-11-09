#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  YearsOldCalc.py
#  
#  www.practicepython.org Exercise 1
print("Welcome to Excerise 1!")
PersonName = input("What is your name:")
PersonAge = int(input("What is your age:"))

print("Calculating years...")

YearsOld = str((2018 - PersonAge)+100)

print("Hello, " + PersonName + ". You will be 100 years old in " + YearsOld)
