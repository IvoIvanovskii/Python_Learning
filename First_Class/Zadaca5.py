# Count Vowels in a String
# Write a Python function that accepts a string and counts the number of vowels ('a', 'e', 'i', 'o', 'u') in it.
x = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0
for char in x:
    if char in vowels:
        count += 1
        print(f"Count so far {char}")
print(count)