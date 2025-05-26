# Задача 4:
# File: "info.txt" содржи:
# “Hello world
# Python is great
# This is a test file”

# да се избројат колку редици се во филот.

import os
print(os.getcwd())

with open("info.txt", "r") as file:

    lines = file.readlines()
    print(lines)

