name = input("Jak masz na imię: ")
age = input("Ile masz lat: ")
try:
    with open("user.txt", "w") as file:
        file.write(f"Imię: {name} Wiek: {age}")

    print("Dane zostały zapisane poprawnie.")

except Exception as e:
    print("ERROR")

# Test poprawności działania 
with open("user.txt", "r") as file:
        dane = file.read()

print("Dane zapisane")
print(f"Test pliku user.txt: {dane}")

##Zadanie: Napisz program, który:
##
##pyta użytkownika o jego imię i wiek
##
##zapisuje dane do user.txt w tym formacie:
##
##Imię: Jan Wiek: 12
##
##Wskazówka: Użyj input() aby odczytać dane od użytkownika, i write() aby formatować tekst za pomocą f-stringów.
