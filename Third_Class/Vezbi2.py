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

#ZADACA 2
#Programa kojshot kje prochita broj na mesec i kje ispechati kolku denovi ima toj mesec

def NumDays (month):
    
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return "31 days"
    elif month == 2:
        return "28 or 29 days"
    elif month > 0 and month < 12:
        return "30 days"
    else:
        return "Vnesivte nepostechki mesec"
    
month = int(input("Vnesi mesec: "))
print(NumDays(month))
