#Zadaca 1 
#Exercise 1 (and Solution)
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
# If you want to do this in a generic way, see exercise 39.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
#  (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
age = int(input("Plese enter your age: "))
birthYear = 2025 - age
copyNum = int(input("Enter a number for copies: "))
for i  in range(0,copyNum):
    print(f"Hello {name} {surname} you will be 100 years old in the year {birthYear + 100}")


