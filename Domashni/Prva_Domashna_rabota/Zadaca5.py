# Задача 5:
# Креирај нова листа од следната листа:
# lista = [23, 65, 12, 99, 34, 87, 3, 56, 78, 45]
# и испечати ги само броевите кои се поголеми од 50
# користејќи list comprehension.

lista = [23, 65, 12, 99, 34, 87, 3, 56, 78, 45]
new_list = []

for num in lista:
    if num > 50:
        new_list.append(num)
        
print("Броевите поголеми од 50 се:", new_list)

# new_List = [x for x in lista if x > 50]
# print (new_List)