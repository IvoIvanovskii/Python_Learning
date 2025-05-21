# Задача 6:
# Побарај од корисникот 
# да внесе број од 1 до 7 и испечати 
# го соодветниот ден од неделата.

number = int(input("Внесете број од 1 до 7: "))
if number == 1:
    print("Понеделник")
elif number == 2:
    print("Вторник")
elif number == 3:
    print("Среда")
elif number == 4:
    print("Четврток")
elif number == 5:
    print("Петок")
elif number == 6:
    print("Сабота")
elif number == 7:
    print("Недела")
else:
    print("Внесете број помеѓу 1 и 7")