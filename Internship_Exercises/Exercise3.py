#zapisi funkcija koja kje go presmetuva brojot na cifrite vo eden broj

def digit(num):
    counter = 0
    while num!=0:
        counter+=1
        num //= 10
    return counter
    
number = int(input("Vnesi broj: "))
print(number)
print(digit(number))