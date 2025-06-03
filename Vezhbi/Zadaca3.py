# Exercise 2 (and Solution)
# The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion.
#  Enjoy!

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#  Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Enter a number: "))

if number % 2 == 0:
    if number % 4 == 0:
        print("The number is even and 4 is his multiple")
    else:
        print("The number is even")
else:
    print("The number is odd")
        
num = int(input("Enter a number to check: "))
check = int(input("Enter a checker: "))

if num % check == 0:
    print("The numbers devide evenly")
else:
    print("They are not devisible")
    