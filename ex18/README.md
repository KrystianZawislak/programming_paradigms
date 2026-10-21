# Exercise 18 — 2D Array from Lists

> Course: Programming Paradigms
> Date: 2026-10-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, który stworzy tablicę dwuwymiarową przy użyciu list - tak aby można się było odwołać do elementu takiej tablicy jak np. w C (pierwszy element - `tab[0][0]`). Niech "tablica" ma rozmiar 3x5 i niech zostanie utworzona jednym poleceniem wypełniającym ją jednocześnie zerami. Następnie należy wypełnić tablicę kwadratami kolejnych liczb całkowitych począwszy od 1 i wypisać.

### 🇬🇧 Task description (EN)

Write a program that creates a two-dimensional array using lists - so that an element of the array can be accessed like e.g. in C (the first element - `tab[0][0]`). Let the "array" be 3x5 in size and let it be created with a single statement that also fills it with zeros. Then fill the array with the squares of consecutive integers starting from 1 and print it.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - creates a 3x5 list of lists filled with zeros using a nested list comprehension, then fills it row by row with the squares of 1, 2, 3, ... and prints it. |

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
[[1, 4, 9, 16, 25], [36, 49, 64, 81, 100], [121, 144, 169, 196, 225]]
```
