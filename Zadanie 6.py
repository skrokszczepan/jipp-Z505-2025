# Prosty program kalkulatora

# Utwórz funkcję dodawania dwóch liczb
def add(a, b):
    return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    if b == 0:
        return "ERROR: you can't divide by zero"
    return a / b


# Wyświetl listę operacji
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

# Pozwól użytkownikowi wybrać żądane działanie
op = input("Please enter choice (a/ b/ c/ d): ")

# Przechwyć 2 liczby wprowadzone przez użytkownika i przekonwertuj je na format liczb całkowitych
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

# Logika do wykonywania określonej operacji
if op == "a":
    print("Result:", add(number1, number2))

elif op == "b":
    print("Result:", subtract(number1, number2))

elif op == "c":
    print("Result:", multiply(number1, number2))

elif op == "d":
    print("Result:", divide(number1, number2))

# Jeśli użytkownik wybierze operację, która nie jest dostępna
else:
    print("ERROR")
