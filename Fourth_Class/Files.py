# try:
#     print(x)
# except:
#     print("There is an error")


# try:
#     print(x)
# except NameError:
#     print("X ne e definirana")
# except:
#     print("imate nekoj drug bug")


# try:
#     print("Hello")
# except NameError:
#     print("Nema output")
# else:
#     print("se e vo red")


# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("Hi")


# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Ne mozhete da delite so 0")

# Da se vnesi int, i toj int da se deli od 10
# da se hadnle sluchaite na vnesuvanje razlichni vrednosti od int ili 0

# try:
#     x = int(input("Vnesi eden broj: "))
#     res = 10 / x
#     print(res)
# except ValueError:
#     print("Nemate vneseno validen broj")
# except ZeroDivisionError:
#     print ("Vnesete broj pogolem od 0")
# else:
#     print("Operacijata e uspeshno zavrshena")
# finally: 
#     print()

# f = open("C:\\Users\\ivoiv\\OneDrive\\Desktop\\Python\\Fourth_Class\\test.txt")

# print(f.read(2))

# f = open("C:\\Users\\ivoiv\\OneDrive\\Desktop\\Python\\Fourth_Class\\test.txt", "r")
# print(f.read())

# f = open("C:\\Users\\ivoiv\\OneDrive\\Desktop\\Python\\Fourth_Class\\test.txt", "w")
# f.write("Vnesen e nov tekst")

with open("test.txt", "a") as f:
    f.write("Dodaden tekst so append preku with")
    f.write("123")