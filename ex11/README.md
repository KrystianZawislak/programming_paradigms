# Exercise 11 — Sums of Tuples

> Course: Programming Paradigms
> Date: 2026-10-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, która dla listy dwuelementowych krotek stworzy nową listę (z użyciem append) zawierającą sumy elementów tych krotek. Program ma wypisać stworzoną listę. Do sumowania proszę nie używać funkcji sum.

W programie posumuj krotki listy:
`[(1,2),(3,4),(5,6),(7,8)]` (ma 'wyjść' `[3,7,11,15]`)

### 🇬🇧 Task description (EN)

Write a program that, for a list of two-element tuples, creates a new list (using `append`) containing the sums of the elements of these tuples. The program should print the created list. Please do not use the `sum` function for summing.

In the program, sum the tuples of the list:
`[(1,2),(3,4),(5,6),(7,8)]` (the result should be `[3,7,11,15]`)

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - unpacks each tuple into `x, y` and builds the list of sums with a list comprehension. |

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
[3, 7, 11, 15]
```
