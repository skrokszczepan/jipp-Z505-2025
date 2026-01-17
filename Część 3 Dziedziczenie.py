#Ćwiczenie 3.1: Basic Dziedziczenie
print("Ćwiczenie 3.1: Basic Dziedziczenie")
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Engine starting .. ")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def start_engine(self):
        print(f"{self.brand} {self.model} is ready")

# Przetestuj swój kod:
vehicle = Vehicle("Generic", "Vehicle", 2020)
vehicle.start_engine()

car = Car("Toyota", "Camry", 2023, 4)
car.start_engine()
print(f"This car has {car.num_doors} doors")

#Ćwiczenie 3.2: Multi-level Dziedziczenie
print("\nĆwiczenie 3.2: Multi-level Dziedziczenie")
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

class Dog(Mammal):
    def __init__(self, name, species, fur_color, breed):
        super().__init__(name, species, fur_color)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Hau Hau")

# Przetestuj swój kod:
dog = Dog("Buddy", "Canis familiaris", "Golden", "Golden Retriever")
print(f"Name: {dog.name}")
print(f"Species: {dog.species}")
print(f"Fur: {dog.fur_color}")
print(f"Breed: {dog.breed}")
dog.bark()


#Ćwiczenie 3.3: Multiple Dziedziczenie
print("\nĆwiczenie 3.3: Multiple Dziedziczenie")
class Flyable:
    def fly(self):
        print(f"{self.name} fly")

class Swimmable:
    def swim(self):
        print(f"{self.name} swim")

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

# Przetestuj swój kod:
duck = Duck("Donald")
duck.fly()
duck.swim()
