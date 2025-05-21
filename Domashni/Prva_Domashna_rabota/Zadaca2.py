# Задача 2:
# Напиши функција која ќе генерира и испечати n први броеви од Фибоначи низата.
# (Првите елементи на Фибоначи се 1, 1, 2, 3, 5, 8, ..., секој нареден се добива 
#  како сума од претходните две броеви).

# def Fibonachi(n):
#     x, y = 0, 1
#     for i in range(n):
#         print(x, end=" ")
#         x, y = y, y+x
        

# num = int(input("Vnesete broj: "))
# Fibonachi(num)

def Fibonachi(n):
    
    if n <= 1:
        return n
    else:
        return Fibonachi(n-1) + Fibonachi(n-2)

num = int(input("Vnesete broj: "))

for i in range(num+1):
    print(Fibonachi(i), end=" ")

    
    
        