words = ["jabłko", "banan", "wiśnia"]

with open("fruits.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

#Sprawdzenie czy sie udało
with open("fruits.txt", "r") as file:
    lista = file.read()

print("W pliku znajduje się lista: \n" + lista)

