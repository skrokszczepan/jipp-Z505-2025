#Ćwiczenie 1.1: Utwórz Swoją Pierwszą Klasę
print("\nĆwiczenie 1.1: Utwórz Swoją Pierwszą Klasę")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages")

book1 = Book("1984", "George Orwell", 328)
book1.display_info()

book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2.display_info()

#Ćwiczenie 1.2: Praca z Wieloma Obiektami
print("\nĆwiczenie 1.2: Praca z Wieloma Obiektami")

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Dodano ocenę {grade} dla {self.name}")

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

student1 = Student("Alice", "S001")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(88)
print(f"{student1.name}'s average: {student1.calculate_average():.2f}")

#Ćwiczenie 1.3: Atrybuty Klasowe
print("\nĆwiczenie 1.3: Atrybuty Klasowe")

class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Kwota wpłaty musi być większa od 0")
            return
        self.balance += amount
        print(f"Wpłata {amount}. Stan rachunku: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Kwota wypłaty musi być większa od 0")
            return
        if amount > self.balance:
            print("Brak funduszy")
            return
        self.balance -= amount
        print(f"Wypłata {amount}. Stan rachunku: {self.balance}")

    def get_balance(self):
        return self.balance


# Test 
acc1 = BankAccount("ACC001", "Alice", 100)
acc2 = BankAccount("ACC002", "Bob", 50)

print("Nazwa banku #(class attribute):", BankAccount.bank_name)
print("Nazwa banku dla konta acc1:", acc1.bank_name)
print("Nazwa banku dla konta acc2:", acc2.bank_name)

acc1.deposit(50)
acc1.withdraw(30)
print("Stan konta acc1:", acc1.get_balance())

acc2.withdraw(100)
print("Stan konta acc2:", acc2.get_balance())

