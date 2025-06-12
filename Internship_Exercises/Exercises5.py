#od dadenata lista 
# kreiraj lista so kvadrati na parnite borevi

list = [1,3,5,12,24,20,32]
list1 = [i**2 for i in list if i%2==0]
print(list1)