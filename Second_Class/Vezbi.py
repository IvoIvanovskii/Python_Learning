# ZADACA 1: 
# def OddOrEven(a):

#     if a % 2 == 0:
#         return "Paren"
#     elif a % 2 == 1:
#         return "Neparen"
#     else:
#         return "Brojot e Nevaliden"

# x = int(input("vnesi broj za proverka"))
# print(OddOrEven(x))

#---------------------------------------------------------

#ZADACA 2: 
# Faktoriel na daden broj

# def Faktoriel(n):
#     sum = 1
#     for i in range (1, n+1):
#         sum = sum * i
#     return sum
# n = 6
# print(f"Vrendosta na faktorelot od {n} e : {Faktoriel(n)}")

#------------------------------------------------------------

#ZADACA 3: 
# a,b,c kolku ima deletteli vo opsegot od a do b koi se delat so c

# count = 0
# a = int(input("Vnesete broj za a: "))
# b = int(input("Vnesete broj za b: "))
# c = int(input("Vnesete broj za c: "))

# for i in range(a,b+1):
#     if i % c == 0:
#         count+=1
    
# print(count)

#--------------------------------------------------------------

#ZADACA 4:
# Да се напише програма која што ќе ги испринта
# сите броеви од 1 до n (n е број внесен од тастатура).
# доколку бројот се дели со 3 да се испечати "#tri"
# Доколку се дели со 5 да се испечати "#pet"
# Доколку се дели со 3 и 5 да се испечати "#TriPet"

# n = int(input("Vnesi broj"))
# for i in range (1,n+1):
#     print(i)

# for i in range (1,n+1):
    
#     if i % 3 == 0 and i % 5 == 0:
#         print("#TriPet")
#         print("-----------------------")
#     elif i % 3 == 0:
#         print("#Tri")
#         print("------------------------")
#     elif i % 5 == 0:
#         print ("#Pet")
#         print("------------------------")
