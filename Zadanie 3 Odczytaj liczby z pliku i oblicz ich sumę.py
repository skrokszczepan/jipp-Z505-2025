suma = 0

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        suma += number

print("Suma liczb to: ", suma)

##Zadanie: Masz plik numbers.txt z jedną liczbą w każdej linii, na przykład:
##
##10 3 7 -2
##
##Napisz program, który:
##
##odczytuje liczby z pliku
##
##konwertuje je na int
##
##oblicza ich sumę
##
##wyświetla wynik
##
##Wskazówka: Użyj int(line.strip()) i przechowuj bieżącą sumę w zmiennej.
