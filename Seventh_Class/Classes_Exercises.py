class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Employee:
    def __init__(self, name, position, company):
        self.name = name
        self.position = position
        self.company = company

    def description(self):
        print(f"{self.name} raboti")

    def description1(self):
        print(f"{self.name} raboti kako {self.position} vo kompanijata {self.company}")



emp1 = Employee("Tamara", "Front-end developer", "ITQuarks")
emp2 = Employee("Ivo", "Full Stack developer", "Valtech")
emp3 = Employee("Adrijana", "Data Scientis", "Technoperia")

employees = [emp1, emp2, emp3]

for e in employees:
    e.description1()

