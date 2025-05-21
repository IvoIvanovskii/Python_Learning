# Задача 8: Побарај од корисникот да внесе неколку 
# броеви (внесот завршува кога ќе внесе -1)
# и пресметај го нивниот просек.
# (Користи while loop)

sum = 0
count = 0

while True:
    num = int(input("Внесете број (-1 за крај): "))
    if num == -1:
        break
    count += 1
    sum += num
    
print(count)
print (sum)
print(sum / count)