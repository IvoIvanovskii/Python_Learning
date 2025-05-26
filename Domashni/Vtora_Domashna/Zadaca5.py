# Задача 5:
# Од листата inputs = ["12.5", "7.0", "abc", "15.99", "20"], внеси ги во нова листа само броевите конвертирани во integer, отстрани ги стринговите.
# Користи try except методот.

inputs = ["12.5", "7.0", "abc", "15.99", "20"]

valid_inp = []

for i in inputs:
    try:
        num = float(i)
        valid_inp.append(round(num))
    except ValueError:
        continue

print(valid_inp)