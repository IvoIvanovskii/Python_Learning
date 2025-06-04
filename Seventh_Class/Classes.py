class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Zdravo, jas sum {self.name} i imam {self.age} godini")

    def prezentier(self):
        print(f"Jas sum {self.name} i imam {self.name}")

p1 = Person("Ivo",22)
p1.greet()


class Student(Person):
    def __init__(self, name, age, fakultet):
        super().__init__(name,age)
        self.fakultet = fakultet
    
    def prezentier(self):
        return super().prezentier()
        

        