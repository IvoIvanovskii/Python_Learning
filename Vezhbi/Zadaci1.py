# # 1. Create a list of 5 integers. Print the list.
# list = [1, 6, 2, 15, 10]
# print(list)
# for i in range(len(list)):
#     print(list[i], end=" ")
# print(" ")
# print(*list)


# # Append a new number to the list.
# list.append(15)
# print(*list)


# # Remove the first element of the list.
# list.pop(0)
# print(*list)

# # Sort the list in ascending order.
# list.sort()
# print(*list)

# # Reverse the list.
# list.sort(reverse=True)
# print(*list)



#-------------------------------------------------------------------------------------------



numbers = [12, 45, 23, 89, 45, 66, 12, 33, 78, 90]
# list = [1, 6, 2, 15, 10]
# # Find the maximum and minimum elements in a list.
# highest = 0
# for x in numbers:
#     if x > highest:
#         highest = x

# print(highest)

# # Count the number of even numbers in a list.
# evenNums = 0;
# for x in numbers:
#     if x % 2 == 0:
#         evenNums+=1

# print(evenNums)
# # Remove duplicates from a list.
# uniqueItems = []
# for i in numbers:
#     if i not in uniqueItems:
#         uniqueItems.append(i)

# print(uniqueItems)
# # Merge two lists and sort the result.
# numbers.extend(list)
# numbers.sort()
# print(numbers)
# Get the second-largest number from a list.
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
print(unique_numbers[1])
    