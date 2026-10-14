# Exercise 8 — Days of the Week (match)

> Course: Programming Paradigms
> Date: 2026-10-14

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program pobierający z klawiatury liczbę (od 1 do 7) i wypisujący na ekran odpowiedni dzień tygodnia. Przy czym dla 1 wypisujemy poniedziałek, 2 - wtorek itd. natomiast dla 6 i 7 ma być wypisane WEEKEND! Dla innych wartości ma być wypisywany komunikat, że to nie jest poprawna wartość

Należy użyć instrukcji match. To ma być jedyna instrukcja wyboru (nie wolno stosować if-else). Nie wolno też stosować pętli.

W programie ma być tylko jedna instrukcja ze słowem WEEKEND

### 🇬🇧 Task description (EN)

Write a program that reads a number (from 1 to 7) from the keyboard and prints the corresponding day of the week. For 1 we print Monday, for 2 - Tuesday, etc., while for 6 and 7 it should print WEEKEND! For any other value it should print a message saying that it is not a valid value.

You must use the `match` statement. It must be the only selection statement (`if-else` is not allowed). Loops are not allowed either.

There may be only one statement containing the word WEEKEND in the program.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - a single `match` on the input string with one `case` per weekday, `case "6" \| "7"` for the weekend and `case _` for invalid values (including non-numeric input). |

## How to run

Requires Python 3.10+ (`match` statement).

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
Provide the day of the week: 1
Monday
```

```
Provide the day of the week: 7
WEEKEND!
```

```
Provide the day of the week: abc
Invalid data!
```
