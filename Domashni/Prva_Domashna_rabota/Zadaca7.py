# Задача 7:
# Од листата:
# zborovi = ["ana", "level", "python", "radar", "code"]
# извлечи ги сите зборови кои се палиндроми и испечати ги во нова листа.

zborovi = ["ana", "level", "python", "radar", "code"]

palindromi = [ zbor for zbor in zborovi if zbor == zbor[::-1]]
print("Зборовите кои се палиндроми се:", palindromi)

# for zbor in zborovi:
#     if zbor == zbor[::-1]:
#         palindromi.append(zbor)

# print("Зборовите кои се палиндроми се:", palindromi)