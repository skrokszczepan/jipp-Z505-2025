# Zapytaj użytkownika o nazwisko
name = input("What is your name?: ")

# Zapytaj użytkownika o wiek
age = input("What is your age?: ")

# Zapytaj użytkownika o miasto
city = input("What is your city?: ")

# Zapytaj użytkownika o jego zainteresowania
hobby = input("What is your hobby?: ")

# Utwórz tekst wyjściowy za pomocą formatowania ciągów
string = "Hi {}, you are {} years old. You live in {} and you love {}!"
output = string.format(name, age, city, hobby)

# Wydrukuj tekst wyjściowy
print(output)
