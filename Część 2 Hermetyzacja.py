#Ćwiczenie 2.1: Private Attributes
print("Ćwiczenie 2.1: Private Attributes")

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary if salary > 0 else 0

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print("Wynagrodzenie zostało zaktualizowane.")
        else:
            print("Błąd: wynagrodzenie musi być większe od 0.")

# Przetestuj swój kod:
emp = Employee("Alice", 50000)
print(f"Imię: {emp.get_name()}")
print(f"Pensja: ${emp.get_salary()}")

emp.set_salary(55000)
print(f"Nowa pensja: ${emp.get_salary()}")

emp.set_salary(-1000)  # Should show error

#Ćwiczenie 2.2: Dekorator Propertys
print("\nĆwiczenie 2.2: Dekorator Propertys")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # używa settera (walidacja)

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperatura nie może być niższa niż zero absolutne (-273.15°C)")

        self.__celsius = value
        

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32


#Test
temp = Temperature(25)
print(f"Temperatura w stopniach Celsjusza: {temp.celsius}°C")
print(f"Temperatura w stopniach Fahrenheita: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"Nowa temperatura w Celsjuszach: {temp.celsius}°C")
print(f"Nowa temperatura w Fahrenheicie: {temp.fahrenheit}°F")

try:
    temp.celsius = -300
except ValueError as e:
    print(f"Błąd: {e}")

