# www.practicepython.org Exercise 4
import math
print("Welcome to Divisors program! Entering a number will show all the divisors")
EtrNum = int(input("Please enter a random number:"))
MtNum = list(range(1, EtrNum+1))
y = []
for number in MtNum:
	if EtrNum % number == 0:	
		y.append(number)
print(" Your divisors for ", EtrNum, " are ", y, ".")
