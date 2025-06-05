class Patient:
    def __init__(self,name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
    def description(self):
        print(f"{self.name} e {self.age} godini i ima {self.disease}")

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def description(self):
        print(f"{self.name} e lekar so specializacija {self.specialization}")
        
