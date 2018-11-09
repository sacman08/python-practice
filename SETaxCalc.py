#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SETaxCalc.py
#  
#  
#  

print ("""\
Welcome to self employed tax rate calculator!
Please have your miles driven, wages earned,
and miscellanous cost totals ready for 2018!
""")

FedSETax = .153
FedIncTax1 = .1
FedIncTax2 = .12
FedMileRate = .545
GAIncTax = .06

#Input requests
WageEarned = float(input("What are the wages you earned?"))
# Add a goto or jump to end operator if WageEarned is zero.
MileEarned = float(input("How many miles were driven?"))
MiscEarned = float(input("Please enter any other costs:"))

# Compute routine
# Add a if statement to findout if earns are over $9525 then use FedIncTax2
TotalTax =  (WageEarned * FedSETax) + (WageEarned * FedIncTax1) + (WageEarned * GAIncTax)
TotalMile = MileEarned * FedMileRate
TotalDisc = TotalMile + MiscEarned

print("For $",WageEarned," your total tax is $",format(TotalTax, '.2f'), ".")
print('For ',MileEarned,' miles and $',MiscEarned,' your total writoff is $',TotalDisc,'.')
