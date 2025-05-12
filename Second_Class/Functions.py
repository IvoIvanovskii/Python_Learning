#Lambda function
x = lambda a,b : a*b

print(x(5,6))

y=int(input("Vnesete broj: "))

#Za vnesen broj proveri dalie edno ili dvocifren broj

x = int(input("Vnesi broj od 1 do 99: "))
if x < 10 and x > 0:
    print("Ednocifren")
elif x >= 10 and x <= 99:
    print("dvocifren")
else:
    print("Brojot ne e validen")