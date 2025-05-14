# #Zadaca 1 
# #Да се напише програма што ќе генерриа оценки врз основа на освоените поени(Внесени од корисникот) од тестот,
# #  спорт следната табела
# # 0 - 60 poeni - 1
# # 61 - 70 poeni - 2
# # 71 - 80 poeni - 3
# # 81 - 90 poeni - 4
# # 91 - 100 poeni - 5

# def Grade(n):
    
#         if 0 <= n <= 60:
#                 return "Dobivte ocena 1"
#         elif 61 <= n <= 70:
#                 return "Dobivte ocena 2"
#         elif 71 <= n <= 80:
#                 return "Dobivte ocena 3"
#         elif 81 <= n <= 90:
#                 return "Dobivte ocena 4"
#         elif 91 <= n <= 100: 
#                 return "Dobivte ocena 5"
#         else:
#                 return "Imate greshka vo vnesuvanjeto na poenite"
   


# points = int(input("Vnesete gi dobienite poeni: "))
# print(Grade(points))

#------------------------------------------------------------------------------------------------------------

# # #ZADACA 2
# # #Programa kojshot kje prochita broj na mesec i kje ispechati kolku denovi ima toj mesec

# def NumDays (month):
    
#     if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#         return "31 days"
#     elif month == 2:
#         return "28 or 29 days"
#     elif month > 0 and month < 12:
#         return "30 days"
#     else:
#         return "Vnesivte nepostechki mesec"
    
# month = int(input("Vnesi mesec: "))
# print(NumDays(month))

#-----------------------------------------------------------------------------------------------------------------

# #ZADACA 3
# #da se napise programa koja prima string i da izbroi kolku bukvi i broevi se vneseni vo toj string

# a = input("Vnesete nekoj string: ")
# countNum = 0
# countChar = 0

# for char in a:
#     if char.isdigit():
#         countNum+=1
#     elif char.isalpha():
#         countChar+=1

# print(f"Vo stringot se izbroeni {countNum} broevi i {countChar} znaci")

#-----------------------------------------------------------------------------------------------------------------

# # ZADACA 4 
# # das enapisi kod go generirra sledniot pattern

# x = int(input("Vnesi eden broj: "))

# for i in range (1, x + 1):
#     for j in range (1, i + 1):
#         print(f"{j} ", end="")
#     print()

#-----------------------------------------------------------------------------------------------------------------

# # ZADACA 5
# # napisi programa vo koja kje se vnesi od tastatura ocenki po 3 predmeti
# # i kje presmeta vkupen zbir na prosek i kza kakov uchenik se raboit

# subject1 = int(input("Vnesi ocena za prviot predmet: "))
# subject2 = int(input("Vnesi ocena za vtoriot predmet: "))
# subject3 = int(input("Vnesi ocena za tretiot predmet: "))

# avg = (subject1 + subject2 + subject3) / 3

# print(f"Prosekot e {avg}")

# if 1 <= avg < 2:
#     print("Nedovolen")
# elif 2 <= avg < 3:
#     print("Dovolen")
# elif 3 <= avg < 4:
#     print("Dobar")
# elif 4 <= avg < 4.5:
#     print("Mn. Dobar")
# elif 4.5 <= avg <= 5:
#     print("Odlichen")
# else:
#     print ("Imate vneseno nepostoechka ocenka")

#-----------------------------------------------------------------------------------------------------------------

# ZADACA 6
# da se napisi kalkulator so  koja kje chita operator i dva broja

def Calculator(x, y, op):

    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    elif op == "%":
        return x % y
    elif op == "**":
        return x ** y
    else:
        return "Imate vneseno ne postechki operator"
    

n1 = int(input("Vnesi go prviot broj: "))
n2 = int(input("Vnesi go vtoriot broj: "))
op = input("Vnesi operator: ")

print(Calculator(n1, n2, op))
