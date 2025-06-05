class Patient:
    def __init__(self,name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
    def description_patient(self):
        print(f"{self.name} e {self.age} godini i ima {self.disease}")

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def description_doctor (self):
        print(f"{self.name} e lekar so specializacija {self.specialization} i negovi pacienti se: ")
        for patient in self.patients:
            patient.description_patient()
        
pat1 = Patient("Tamara", 30, "grip")
pat2 = Patient("Ivo", 40, "migrena")
pat3 = Patient("Adrijana", 25, "alergija")

doct1 = Doctor("Dr. Petrovski", "kardiolog")
doct2 = Doctor("Dr. Nikolovski", "dermatolog")

doct1.add_patient(pat1)
doct1.add_patient(pat2)
doct2.add_patient(pat3)

doct1.description_doctor()
doct2.description_doctor()

