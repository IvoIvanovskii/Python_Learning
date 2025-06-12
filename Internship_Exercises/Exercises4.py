#programa koja kje gi isprinta site borevi od 1 - n 
# i se delivi so 3
def deliviSoTri(num):
    for i in range(3, num+1, 3):
        if i % 3 == 0:
            print(i)
        
n = int(input("Vnesi Broj: "))


deliviSoTri(n)
