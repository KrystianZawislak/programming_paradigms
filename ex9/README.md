# Exercise 9 — Making 100 zł from Coins

> Course: Programming Paradigms
> Date: 2026-10-14

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program znajdujący wszystkie możliwości złożenia 100zł z nominałów 2, 5 oraz 10 zł. Należy wypisać liczbę możliwych kombinacji.

### 🇬🇧 Task description (EN)

Write a program that finds all the ways of making 100 zł from the denominations 2, 5 and 10 zł. Print the number of possible combinations.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - reads the amount, loops over the number of 10 and 5 zł coins and counts the combinations where the rest is non-negative and even (can be filled with 2 zł coins). |

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
Input an amount of money you want to check:100
66
```

```
Input an amount of money you want to check:99
55
```
