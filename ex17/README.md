# Exercise 17 — Words to Number (20-59)

> Course: Programming Paradigms
> Date: 2026-10-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz funkcję, która otrzymuje napis zawierający słownie opisaną liczbę z zakresu 20-59 (np. 'dwadzieścia jeden') i zamienia ją na 'prawdziwą' liczbę całkowitą (21). Wykorzystaj słownik. Może być przydatna metoda split (`napis.split()`) dzieląca napis na wyrazy.

### 🇬🇧 Task description (EN)

Write a function that receives a string containing a number from the range 20-59 written in words (e.g. 'twenty one') and converts it into a 'real' integer (21). Use a dictionary. The `split` method (`string.split()`), which splits a string into words, may be useful.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `convert_writing_to_int` splits a two-word input into the tens word and the units word and adds their values from the dictionary; a single word (e.g. `twenty`) is looked up directly. |

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
twenty one
21
```

```
fifty nine
59
```

```
twenty
20
```
