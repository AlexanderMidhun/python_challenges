class Vehicles:
    def specs(self):
        self.name = input("Enter vehicle name: ")
        self.color = input("Enter vehicle color: ")
        self.year = input("Enter vehicle year: ")

    def print_specs(self):
        print("Vehicle Name:", self.name)
        print("Vehicle Color:", self.color)
        print("Vehicle Year:", self.year)


class Car(Vehicles):
    def getspecs(self):
        super().specs()
        self.wheels = input("Enter number of wheels: ")

    def displayspecs(self):
        super().print_specs()
        print("Number of Wheels:", self.wheels)


class Bike(Vehicles):
    def specs(self):
        super().specs()
        self.gears = input("Enter number of gears: ")

    def print_specs(self):
        super().print_specs()
        print("Number of Gears:", self.gears)

car = Car()
car.specs()
print("--- Car Specifications ---")
car.print_specs()

print("___________________________________________________________")

bike = Bike()
bike.specs()
print("--- Bike Specifications ---")
bike.print_specs()
