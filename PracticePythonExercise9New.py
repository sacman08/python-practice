# Practice Python Exercise 9
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# Generate random number
import random
ranNum = random.randint(1,9)
asNum = 0
cntNum = 0
#Ask for user input
usNum = input("Would like to play a guessing game? [y\\n]")
if usNum == 'y':
    while asNum != ranNum and asNum != 'exit':
        print("A random number between 1 and 9 has been chosen.")
        print("Type ""exit"" to quit the game.")
        asNum = input("Please enter your guess of the number:")
        cntNum += 1
        if asNum.lower() == 'exit':
            print("Bye, quitter!")
            break
        asNum = int(asNum)
        if asNum > ranNum:
            print("Too high! Guess again.")
        elif asNum < ranNum:
            print("Too low! Guess again.")
        elif asNum == ranNum:
            print("That's it exactly!")
            print ("It only took", cntNum, "tries.")
elif usNum =='n':
    print("Maybe next time!")
