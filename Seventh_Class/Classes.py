# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Zdravo, jas sum {self.name} i imam {self.age} godini")

#     def prezentier(self):
#         print(f"Jas sum {self.name} i imam {self.name}")

# p1 = Person("Ivo",22)
# p1.greet()


# class Student(Person):
#     def __init__(self, name, age, fakultet):
#         super().__init__(name,age)
#         self.fakultet = fakultet
    
#     def prezentier(self):
#         return super().prezentier()
        
class Employeee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"{self.name} zema {self.salary}")
    
e1 = Employeee("Marko", 50000)
e1.info()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def info(self):
        print(f"{self.owner} sostojbata na vasata smetka e {self._balance}")

o1 = BankAccount("Marko", 600000)
o1.info()
        