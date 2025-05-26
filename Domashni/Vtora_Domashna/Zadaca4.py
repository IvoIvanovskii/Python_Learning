# Задача 4:
# File: "info.txt" содржи:
# “Hello world
# Python is great
# This is a test file”




with open(r"c:\Users\ivoiv\OneDrive\Desktop\Python\Domashni\Vtora_Domashna\info.txt", "r", encoding="utf-8") as file:

    lines = file.readlines()
    print(lines)

