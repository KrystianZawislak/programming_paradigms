# Exercise 24 — Prime Numbers with a Timing Decorator

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-11-07

## Task

### 🇵🇱 Treść zadania (PL)

Napisz funkcję wyszukującą liczby pierwsze w przedziale [2,n] zwracającą listę znalezionych liczb. Można wykorzystać algorytm z zadania Liczby pierwsze z Tematu 2 lub zaimplementować Eratostenesa.

Napisz dekorator pozwalający na policzenie czasu wykonania 'dekorowanej' funkcji. Można wykorzystać poniższy schemat:

```python
from time import perf_counter

start = perf_counter()
# ...
end = perf_counter()
print(end - start)
```

'Udekoruj' funkcję szukającą liczb pierwszych.

Uruchom funkcję dla n=100000

Jako zadanie dodatkowe zaimplementuj drugą wersję algorytmu szukania licz pierwszych i również go udekoruj.

Uruchom obie  funkcje i zaobserwuj ich czasy wykonania.

### 🇬🇧 Task description (EN)

Write a function that finds the prime numbers in the interval [2,n] and returns a list of the numbers found. You can use the algorithm from the "Prime Numbers" exercise from Topic 2 ([ex10](../../2_control_statements/10_prime_numbers_for_else/)) or implement the Sieve of Eratosthenes.

Write a decorator that measures the execution time of the 'decorated' function. You can use the following scheme:

```python
from time import perf_counter

start = perf_counter()
# ...
end = perf_counter()
print(end - start)
```

'Decorate' the function that finds prime numbers.

Run the function for n=100000

As an additional task, implement a second version of the prime-finding algorithm and decorate it as well.

Run both functions and observe their execution times.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `count_time` decorator (a `wrapper` measuring the call with `perf_counter`, printing the time and returning the result); `sieve_eratosthenes` (Sieve of Eratosthenes) and `division_method` (trial division by odd numbers up to `isqrt`), both decorated with `@count_time`. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example output (execution times in seconds - sieve first, division method second; they differ between runs and machines):

```
0.01716704200953245
0.042646917048841715
```
