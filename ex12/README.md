# Exercise 12 — Leap Years (list comprehension)

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-10-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program tworzący listę lat przestępnych z przedziału podanego z klawiatury (wczytujemy dwie wartości: rok początkowy i końcowy).

Przypominam, że rok jest przestępny, jeżeli jest podzielny przez 4, ale nie jest podzielny przez 100, chyba, że jest podzielny przez 400.

Listę proszę stworzyć z użyciem list comprehension.

Poprawność proszę sprawdzić podając przedział 1900-2000 - rok 1900 nie ma się pojawić (nie był przestępny), a 2000 już tak (był).

### 🇬🇧 Task description (EN)

Write a program that creates a list of leap years in a range given from the keyboard (we read two values: the start year and the end year).

As a reminder, a year is a leap year if it is divisible by 4 but not divisible by 100, unless it is divisible by 400.

Please create the list using a list comprehension.

Please check correctness with the range 1900-2000 - the year 1900 must not appear (it was not a leap year), but 2000 must (it was).

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - reads the start and end year, builds the list of leap years with a list comprehension. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example input/output:

```
1900
2000
[1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000]
```
