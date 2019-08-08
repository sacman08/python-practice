# Practice Python Example 10 Exercise
# Take two lists and write a program that returns a list
# that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Extra: Randomly generate two lists to test this
import random
#Ask the user for a random sample range
print("Welcome to excercise 10!")
ranA = int(input("Please select a random number from 5 to 20:"))
if ranA < 5 or ranA > 20:
    ranA = int(input("Please only use a number from 5 to 20:"))
    ranB = random.randint(ranA, 30)
else:
    ranB = random.randint(ranA, 30)

#Generate lists
print("\nYour random number -",ranA,"- will be used to generate a list.")
print ("Another random number -", ranB, "- will be used to generate a second list.")
print("Processing...\n")
lisA = random.sample(range(100), ranA)
lisB = random.sample(range(100), ranB)


#Compare lists with random numbers and sort
print("The two lists have been created.")
print("Now the lists will be compared for duplicates.")
print("Processing...\n")
lisX = [lisX for lisX in lisA if lisX in lisB]
lisA.sort()
lisB.sort()
lisX.sort()

#Show results to our user
print("The two lists are show below.")
print(lisA)
print(lisB)
print("\nThe duplicates in the lists are shown below.")
print(lisX)

#Ask for repeat
inpY = input("\nWould you like to run the program again? [y\\n] ")
if inpY == "y":
    print("Please re-run the file. *wink*")
else:
    print("Until next time!")
