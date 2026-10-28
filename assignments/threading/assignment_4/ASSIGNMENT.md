# Zadanie

Grupa magów próbuje uruchomić starożytną magiczną statuę. Aby rytuał się udał, **wszyscy magowie muszą jednocześnie uczestniczyć w rytuale**.

Każdy mag działa jako osobny wątek. Rytuał trwa przez ustaloną liczbę tur.

W każdej turze magowie przygotowują się do rytuału, a następnie próbują dotknąć magicznej statuy. Statua zapamiętuje, którzy magowie dotknęli jej w danej turze.

Samo dotknięcie statuy nie wystarcza jednak do zakończenia rytuału. Mag musi poczekać na pozostałych uczestników.

## Zasady rytuału

Na końcu każdej tury wszyscy magowie muszą spotkać się przy statui.

Rytuał może zostać dopełniony tylko wtedy, gdy:

* każdy mag dotknął statuy,

Jeżeli choć jeden mag nie dotknął statuy w danej turze, magia wymyka się spod kontroli:

> **Statua eksploduje, wszyscy magowie giną, a gra się kończy.**

Jeżeli magowie pomyślnie przejdą przez wszystkie tury, rytuał zostaje dopełniony i statua zostaje aktywowana.

## Zadanie

Zaimplementuj symulację pracy magów wykorzystując **wątki (`threading.Thread`)** oraz **barierę synchronizacyjną (`threading.Barrier`)**.

Każdy mag powinien działać w osobnym wątku.

W każdej turze mag:

1. wykonuje swoje działania przygotowawcze,
2. próbuje dotknąć statuy,
3. oczekuje na pozostałych magów,
4. po zakończeniu synchronizacji przechodzi do następnej tury.
