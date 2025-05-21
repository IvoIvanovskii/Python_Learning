# Задача 1:
# Напиши програма која користи for loop
# за да ја испечати таблицата за множење 
# за број внесен од корисникот (до 10).

x = int(input("Vnesi broj koj kje se mnozhi: "))

for i in range (1, 11):
    print(f"{x} * {i} = {x*i} ")