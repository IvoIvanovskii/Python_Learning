#Lambda function
x = lambda a,b : a*b

print(x(5,6))

y=int(input("Vnesete broj: "))

#Za vnesen broj proveri dalie edno ili dvocifren broj

x = int(input("Vnesi broj od 1 do 99: "))
# if x < 10 and x > 0:
#     print("Ednocifren")
# elif x >= 10 and x <= 99:
#     print("dvocifren")
# else:
#     print("Brojot ne e validen")
if 1 <= x < 10:
    print("Ednocifren")
elif 10 <= x <= 99:
    print("Dvocifren")
else:
    print("Nevaliden broj")

#Primer Funkcii

def suma(a,b):
    return a+b

print(suma(10,12))

