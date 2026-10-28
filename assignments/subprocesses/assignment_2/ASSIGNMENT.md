# Zadanie: komunikacja między procesami przez potoki

## Cel zadania

Celem zadania jest praktyczne poznanie komunikacji między procesami z wykorzystaniem **potoków (pipes)**.

Program składa się z dwóch procesów:

- programu w języku **C**, który losuje liczbę i odpowiada na zgadywane wartości,
- programu w **Pythonie**, który uruchamia program C jako proces potomny i komunikuje się z nim przez `stdin` i `stdout`.

Otrzymujesz **niekompletny kod programu Python**. Należy uzupełnić brakujące fragmenty.

---

## Program C

Program C (`guess.c`) losuje liczbę całkowitą z zakresu **0–100**.

Po uruchomieniu wypisuje:

```text
READY
```

Następnie oczekuje na kolejne liczby podawane przez standardowe wejście.

Dla każdej otrzymanej liczby odpowiada:

- `TOO_LOW` — zgadywana liczba jest mniejsza od wylosowanej,
- `TOO_HIGH` — zgadywana liczba jest większa od wylosowanej,
- `CORRECT` — liczba została odgadnięta.

Po odpowiedzi `CORRECT` program C kończy działanie.


Program C jest już przygotowany. **Nie należy go modyfikować.**

---

## Zadanie

Uzupełnij dostarczony program Python tak, aby:

1. uruchamiał program `./guess` za pomocą `subprocess.Popen`,
2. tworzył potok do standardowego wejścia procesu C,
3. tworzył potok ze standardowego wyjścia procesu C,
4. oczekiwał na komunikat `READY`,
5. wysyłał do programu C kolejne liczby,
6. odczytywał odpowiedź programu C,
7. na podstawie odpowiedzi wybierał kolejną liczbę,
8. kończył działanie po otrzymaniu `CORRECT`,
9. poprawnie zamykał proces potomny.

Cała gra ma odbywać się z wykorzystaniem **jednego procesu C**.

Schemat komunikacji:

```text
Python                         C
   |                           |
   | -------- liczba --------> |
   |                           |
   | <------- odpowiedź ------ |
   |                           |
   | -------- liczba --------> |
   |                           |
   | <------- odpowiedź ------ |
   |                           |
```