# Exercise 7 — Guess the Number (while-else)

> Course: Programming Paradigms
> Date: 2026-10-14

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, który wylosuje liczbę całkowitą z zakresu 1-10 a następnie pozwoli na zgadnięcie tej liczby w 3 próbach. Program ma podawać po każdej nieudanej próbie, czy podana liczba jest większa czy mniejsza od wylosowanej. Po osiągnięciu zadanej liczby nieudanych prób program ma wypisać komunikat o porażce, a w wypadku zgadnięcia, komunikat o sukcesie. W programie należy wykorzystać konstrukcję while-else.

Przykład losowania liczb w Pythonie (do przerobienia i wykorzystania):

```python
import random

print(random.randint(1, 10))
```

### 🇬🇧 Task description (EN)

Write a program that draws a random integer from the range 1-10 and then lets the user guess it in 3 attempts. After each failed attempt the program should say whether the given number is greater or smaller than the drawn one. After reaching the given number of failed attempts the program should print a failure message, and when the number is guessed - a success message. The program must use the `while-else` construct.

Example of drawing random numbers in Python (to adapt and use):

```python
import random

print(random.randint(1, 10))
```

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `while` loop runs while the guess is wrong, `break` after 3 failed attempts, `else` branch prints the success message. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example input/output (drawn number: 7):

```
Guess the number: 3
Higer
Guess the number: 9
Lower
Guess the number: 7
You guessed right!
```

```
Guess the number: 3
Higer
Guess the number: 9
Lower
Guess the number: 1
End of trial
```
