with open("story.txt", "r") as file:
    text = file.read()

words = text.split()
print("Liczba słów: " + str(len(words)))
