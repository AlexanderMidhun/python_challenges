class Hospital:
    def __init__(self, admin_name, doctor_name, sister_name, department_name):
        self.admin_name = admin_name
        self.doctor_name = doctor_name
        self.sister_name = sister_name
        self.department_name = department_name


class HospitalDetails(Hospital):
    def __init__(self, admin_name, doctor_name, sister_name, department_name):
        super().__init__(admin_name, doctor_name, sister_name, department_name)

    def print_details(self):
        print("Admin Name:", self.admin_name)
        print("Doctor Name:", self.doctor_name)
        print("Sister Name:", self.sister_name)
        print("Department Name:", self.department_name)

admin_name = input("Admin Name: ")
doctor_name = input("Doctor Name: ")
sister_name = input("Sister Name: ")
department_name = input("Department Name: ")

class PatientWard:
    def __init__(self, patient_name, age, number, disease):
        self.patient_name = patient_name
        self.age = age
        self.number = number
        self.disease = disease

    def print_details(self):
        print("Patient Name:", self.patient_name)
        print("Age:", self.age)
        print("Number:", self.number)
        print("Disease:", self.disease)
print("_________________________________________________________________________")
patient_name = input("Patient Name: ")
age = input("Age: ")
number = input("Number: ")
disease = input("Disease: ")

print("___________________________________________________________________________")

hospital = HospitalDetails(admin_name, doctor_name, sister_name, department_name)
hospital.print_details()

print("___________________________________________________________________________")

patient = PatientWard(patient_name, age, number, disease)
patient.print_details()
