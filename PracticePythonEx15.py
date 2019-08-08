# Practice Python Exercise 15
# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

# Functions area below
def procStrInput(strB):
    print("\nProcessing list...")
    print("The original words typed are now reversed.\n")
    strC = strB.split()
    return " ".join(reversed(strC))

# setup up our string variable
strA = []  # type list
# Ask user for string input
if not strA:  # if the string is still empty, please type words.
    strA = input("Please enter a line of words:\n")
# Call function to reverse string
print(procStrInput(strA))

# Future add: Request to run program again or exit.
