# Zadanie

Uzupełnij szablon programu tak, aby wygenerować pięć syntetycznych zbiorów
danych do klasyfikacji z użyciem wątków (`threading.Thread`). Każdy wątek
powinien:

* wykorzystać funkcję `make_classification` z przygotowanymi parametrami;
* użyć własnej wartości `random_state`;
* utworzyć ramkę danych zawierającą cechy oraz kolumnę `target`;
* zapisać wynik do przypisanego pliku CSV.

W funkcji `main` utwórz katalog wyjściowy, przygotuj i uruchom pięć wątków,
a następnie wywołaj `join()` dla każdego z nich, aby program zakończył się
dopiero po zapisaniu wszystkich plików. Nie zmieniaj nazw plików ani
parametrów generowania danych.