# Exercise 24 — Prime Numbers with a Timing Decorator

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 24](../../class_exercises/ex24/) (Prime Numbers with a Timing Decorator) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz funkcję wyszukującą liczby pierwsze w przedziale [2,n] zwracającą listę znalezionych liczb. Można wykorzystać algorytm z zadania 10 lub zaimplementować sito Eratostenesa.

Napisz dekorator pozwalający na policzenie czasu wykonania 'dekorowanej' funkcji. Można wykorzystać poniższy schemat:

```python
from time import perf_counter

start = perf_counter()
# ...
end = perf_counter()
print(end - start)
```

'Udekoruj' funkcję szukającą liczb pierwszych.

Uruchom funkcję dla n=200000 i wypisz, ile liczb pierwszych znalazła.

Jako zadanie dodatkowe zaimplementuj drugą wersję algorytmu szukania liczb pierwszych i również go udekoruj.

Uruchom obie funkcje i zaobserwuj ich czasy wykonania.

### 🇬🇧 Task description (EN)

Write a function that finds the prime numbers in the interval [2,n] and returns a list of the numbers found. You can use the algorithm from [exercise 10](../ex10/) or implement the Sieve of Eratosthenes.

Write a decorator that measures the execution time of the 'decorated' function. You can use the following scheme:

```python
from time import perf_counter

start = perf_counter()
# ...
end = perf_counter()
print(end - start)
```

'Decorate' the function that finds prime numbers.

Run the function for n=200000 and print how many prime numbers it found.

As an additional task, implement a second version of the prime-finding algorithm and decorate it as well.

Run both functions and observe their execution times.

## Files

| File | Description |
| ---- | ----------- |
| `main.py` | Solution - not written yet. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```
