class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def description(self):
        print(f"{self.name} raboti")
