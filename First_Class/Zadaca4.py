# Check for Even or Odd Numbers
# Write a Python program that asks the user for a number and prints whether the number is even or odd.
x = int(input("Enter a number: "))
if x == 0:
    print("The number is zero")
elif x % 2 == 0:
    print("The nubmer is even")
else:
    print("The number is odd")