# Exercise 7 — Guess the Number 1-20 (while-else)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 7](../../class_exercises/ex7/) (Guess the Number (while-else)) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, który wylosuje liczbę całkowitą z zakresu 1-20 a następnie pozwoli na zgadnięcie tej liczby w 4 próbach. Program ma podawać po każdej nieudanej próbie, czy podana liczba jest większa czy mniejsza od wylosowanej. Po osiągnięciu zadanej liczby nieudanych prób program ma wypisać komunikat o porażce (razem z wylosowaną liczbą), a w wypadku zgadnięcia, komunikat o sukcesie. W programie należy wykorzystać konstrukcję while-else.

Przykład losowania liczb w Pythonie (do przerobienia i wykorzystania):

```python
import random

print(random.randint(1, 10))
```

### 🇬🇧 Task description (EN)

Write a program that draws a random integer from the range 1-20 and then lets the user guess it in 4 attempts. After each failed attempt the program should say whether the given number is greater or smaller than the drawn one. After the given number of failed attempts the program should print a failure message (together with the drawn number), and in case of a correct guess - a success message. Use the while-else construct in the program.

An example of drawing random numbers in Python (to be adapted and used):

```python
import random

print(random.randint(1, 10))
```

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
