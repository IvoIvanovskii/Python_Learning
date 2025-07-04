# # Задача 1:
# # Од листата employees = [
# #     ("Tea", 87000),
# #     ("Ana", 12300),
# #     ("Marija", 56000),
# #     ("Aleksandar", 92000),
# #     ("Milan", 7800),
# #     ("Ivan", 34000),
# #     ("Ivana", 13450)
# # ]
# #  Фирмата одлучила да им се даде покачување на вработените за 6% од нивната моментална плата, изврши ја промената во листата.

# - Владата одлучува да се зголеми минималната плата на 18000, имплементирај ја промената во листата

# - Фирмата одлучува да ја отпушти Ана

# - Фирмата одлучува да им се намали платата за 10% на сите што земаат над 50000 поради економска криза

employees = [
    ("Tea", 87000),
    ("Ana", 12300),
    ("Marija", 56000),
    ("Aleksandar", 92000),
    ("Milan", 7800),
    ("Ivan", 34000),
    ("Ivana", 13450)
]

employees = [(name, salary * 1.06) for name, salary in employees]
print(employees)

print("-------------------------------------------------------------------------------------")

employees = [(name, 18000) if salary <= 18000 else (name, salary) for name, salary in employees]
print(employees)

print("-------------------------------------------------------------------------------------")

employees = [(name, salary) for name, salary in employees if name != "Ana"]
print(employees)

print("-------------------------------------------------------------------------------------")

employees = [(name, salary * 0.9) if salary >= 50000 else (name, salary) for name, salary in employees ] 
print (employees)

