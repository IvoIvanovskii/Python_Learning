# Задача 4:
# File: "info.txt" содржи:
# “Hello world
# Python is great
# This is a test file”




with open(r"C:\\Users\\ivoiv\\OneDrive\\Desktop\\Python\Domashni\\Vtora_Domashna", "r") as file:

    lines = file.readlines()
    print(lines)

