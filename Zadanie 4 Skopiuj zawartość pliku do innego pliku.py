with open("numbers.txt", "r") as file:
    dane = file.read()

with open("copy.txt", "w") as file2:
    file2.write(dane)

print("Plik został skopiowany")

# Sprawdzenie czy działa
with open("numbers.txt", "r") as file:
    dane = file.read()
print("Zawartość pliku numbers.txt: \n" + dane)


with open("copy.txt", "r") as file:
    dane = file.read()
print("Zawartość pliku copy.txt: \n" + dane)

##Zadanie:
##Napisz program, który:
##
##odczytuje zawartość numbers.txt
##
##kopiuje wszystko do nowego pliku o nazwie copy.txt
##
##Wskazówka:
##Użyj read() aby pobrać całą zawartość na raz, lub kopiuj linię po linii.
