# Tworzymy symulator ciekawskiego dziecka za pomocą pętli

# Program Symulujący Ciekawskiego Malucha

# Użyj modułu random
import random

# Stwórz listę "questions" składającą się z 3 pytań, które często zadają dzieci
questions = [
    "Tato, a czemu niebo jest niebieskie?",
    "Tato, a czemu słońce nie spada z nieba?",
    "Tato, a czemu psy nie chodzą do szkoły?",
    "Tato, a czemu woda jest mokra?",
    "Tato, a czemu dorośli piją kawę, a dzieci nie?"
]
answer = ""

while answer != "to wszystko":
    
# Wybierz losowe pytanie z danej listy
    question = random.choice(questions)
    
# Zadaj wybrane pytanie za pomocą funkcji input()
# Pytania muszą zachować jednolite formatowanie
# Aby to uzyskać, przekonwertuje wszystkie odpowiedzi na małe litery i usuń wszelkie nadmiarowe spacje
    answer = input(question + "\n").strip().lower()


# Wyświetl wiadomość
print("Weź się tato")

