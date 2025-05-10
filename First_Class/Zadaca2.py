# Find the Largest Number
# Write a Python function that accepts three numbers as input and returns the largest one.
x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
z = int(input("Enter a number for z: "))

if x == y == z:
    print(f"The numbers are equal: {x}")
elif x > y and x > z:
    print(f"The highest number is: {x}")
elif y > x and y > z:
    print(f"The highest number is: {y}")
else:
    print(f"The highest number is {z} ")

    