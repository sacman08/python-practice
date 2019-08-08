#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ListOverlapEx10.py
#  
import random
print ("www.praticepython.org Excerise 10 List Overlap")
a = random.sample(range(100), 12)
b = random.sample(range(100), 15)


x = [i for i in a if i in b] 


print ("Here is the first list: ",a)
print ("Here is the second list: ",b)
print ("Here are the matches: ", x)
