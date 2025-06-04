class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Zdravo, jas sum {self.name} i imam {self.age} godini")

p1 = Person("Ivo",22)
p1.greet()
        