# Utwórz słownik filmów. Klucz: nazwa filmu, wartości: [kryterium wiekowe, liczba biletów]
movies = {"Finding Nemo":[5,2], "Moana":[6,3], "Batman":[18,5], "The Lion King":[10,4]}

# Utwórz pętlę, która będzie działać w nieskończoność
# Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca, a następnie zamień frazę na format tytułowy (pierwsza litera każdego słowa jest wielka)
# Stwórz instrukcję warunkową if. Jeśli wybrany film jest dostępny w słowniku, kontynuuj
# Zapytaj użytkownika o wiek
# Sprawdź użytkownika pod kątem kwalifikowalności
# Jeśli użytkownik znajduje się w grupie docelowej, sprawdź dostępność miejsc
# Jeśli liczba dostępnych miejsc jest wartością dodatnią, zmniejsz pulę dostępnych miejsc o 1

while True:    
    movie = input("Available movies: Finding Nemo, Moana, Batman, The Lion King.\n"
                  "Which movie would you like to watch?  ").strip().title()    
    if movie in movies:        
        age = int(input("How old are you? ").strip())        
        if age >= movies[movie][0]:          
            if movies[movie][1] > 0:               
                movies[movie][1] -= 1
                print(f"You bought a ticket for {movie}. Tickets left: {movies[movie][1]}")
            
            else:
                print("Sorry we have no more tickets available for this movie.")
        
        else:
            print(f"You are too young for '{movie}'. Required age: {movies[movie][0]}")
    
    else:
        print("Movie not found. Available movies:", ", ".join(movies.keys()))
