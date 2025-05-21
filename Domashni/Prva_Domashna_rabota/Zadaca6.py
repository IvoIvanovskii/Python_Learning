# Задача 6:
# Побарај од корисникот 
# да внесе број од 1 до 7 и испечати 
# го соодветниот ден од неделата.

number = int(input("Внесете број од 1 до 7: "))
lista_Denovi = ["Ponedelnik" , "Vtornik", "Sreda", "Chetvrtok", "Petok", "Sabota", "Nedela"]

if 1 <= number <= 7:
    print(lista_Denovi[number-1])
else:
    print("Izbravte nepostechki broj")




