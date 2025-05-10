x = 11
y = 5

if x <=10:
    print("Vrednosta e pomala ili ednkava od 10")
elif x>10:
    print("Vrednosta e pogolema od 10")

if x > 5 and y < 3:
    print("x e pogolemo od 5 i y e pomalo od 3")
elif not(x > 15 and y < 10):
    print("x e pogolem od 5 i y e pomal od 10")
else:
    print("Vrednosta na x e 10 i y e 5")

if x is y:
    print("true")
else:
    print("False")