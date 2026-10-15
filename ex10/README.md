# Exercise 10 — Prime Numbers (for-else)

> Course: Programming Paradigms
> Date: 2026-10-15

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program znajdujący (i wypisujący) wszystkie liczby pierwsze z zakresu 1-100. Wykorzystaj dwie pętle for z czego jedna ma być typu for-else.

### 🇬🇧 Task description (EN)

Write a program that finds (and prints) all prime numbers in the range 1-100. Use two `for` loops, one of which must be a `for-else` loop.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - prints 2, then checks only odd numbers, dividing only by odd divisors up to `isqrt(n)`; the `else` of the inner loop prints the number when no divisor was found. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example output:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```
