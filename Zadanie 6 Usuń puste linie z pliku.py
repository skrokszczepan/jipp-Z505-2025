try:
    with open("raw.txt", "r",encoding="utf-8") as file1:
        dane = file1.read()

    with open("clean.txt", "w",encoding="utf-8") as file2:
        for line in dane.splitlines():
            if line.strip() != "":
                file2.write(line+ " ")

    print("Puste linie zostały usunięte i zapisane do clean.txt")

except FileNotFoundError:
    print("ERROR")

# Test 
print("Zawartość pliku raw.txt: " + dane)

print("Zawartość pliku clean.txt:")
with open("clean.txt", "r", encoding="utf-8") as file:
        print(file.read())

##Zadanie: Masz plik raw.txt, który zawiera puste i niepuste linie.
##
##Napisz program, który:
##
##odczytuje wszystkie linie z raw.txt
##
##usuwa puste linie (linie, które są puste lub zawierają tylko białe znaki)
##
##zapisuje tylko niepuste linie do nowego pliku o nazwie clean.txt
##
##Wskazówka: Użyj .strip() aby sprawdzić czy linia jest pusta; if line.strip() != "", zachowaj ją.
